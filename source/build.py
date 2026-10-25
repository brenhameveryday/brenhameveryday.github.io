"""Build brenhameveryday.com from issue fragments.

Each file in issues/ is named YYYY-MM-DD.html (the weekend's first day) and starts with
<!--meta {...} --> holding: start, end, label, range, sent, title, picks, publish_on,
and optionally special (a nav button, e.g. "Halloween") and scene_pumpkins.

Usage: python3 build.py [--drafts] [--today YYYY-MM-DD]
  --drafts  also include issues whose publish_on is after today (marked as previews)
Output goes to public/: index.html (newest published issue), one folder per issue,
about/index.html, style.css, CNAME.
"""
import datetime, html, json, os, re, shutil, sys

from scene import scene

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
DOMAIN = "brenhameveryday.com"

FOOT_SYMBOL = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="foot" viewBox="0 0 40 50"><ellipse cx="21" cy="33" rx="11" ry="15"/><ellipse cx="10.5" cy="12" rx="4.2" ry="5.2"/><ellipse cx="18.5" cy="8" rx="3.4" ry="4.2"/><ellipse cx="25.5" cy="8.5" rx="3" ry="3.7"/><ellipse cx="31" cy="11.5" rx="2.6" ry="3.2"/><ellipse cx="35" cy="16" rx="2.2" ry="2.7"/></symbol>
</svg>"""

FB_URL = 'https://www.facebook.com/share/19rUeAqB4Z/'
FB_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><path d="M15 8h-1.5A1.5 1.5 0 0 0 12 9.5V21M9.5 13H15" stroke-linecap="round"/></svg>'
IG_ICON = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'


def load_issues():
    issues = []
    for name in sorted(os.listdir(os.path.join(ROOT, "issues"))):
        if not name.endswith(".html"):
            continue
        text = open(os.path.join(ROOT, "issues", name), encoding="utf-8").read()
        m = re.match(r"<!--meta (\{.*?\}) -->\n", text, re.S)
        meta = json.loads(m.group(1))
        meta["slug"] = name[:-5]
        meta["body"] = text[m.end():]
        issues.append(meta)
    return issues


def page(title, description, prefix, body, issues, current=None, preview=False, pumpkins=False):
    """prefix is the relative path back to the site root ("" or "../")."""
    opts = []
    for i in reversed(issues):
        label = i["label"].rsplit(", ", 1)[0] + (" (newest)" if i is issues_published(issues)[-1] else "") + (" (preview)" if i.get("draft") else "")
        sel = " selected" if current is i else ""
        opts.append(f'<option value="{prefix}{i["slug"]}/index.html"{sel}>{html.escape(label)}</option>')
    specials = "".join(
        f'<a class="special" href="{prefix}{i["slug"]}/index.html">{html.escape(i["special"])}</a>'
        for i in issues if i.get("special") and not i.get("past"))
    data = json.dumps([{"slug": i["slug"], "start": i["start"], "end": i["end"], "label": i["label"], "draft": bool(i.get("draft"))} for i in issues])
    cur = current["slug"] if current else ""
    if current:
        status = f'<span class="status" id="status">This weekend</span><strong>{html.escape(current["range"])}</strong>'
        issue_line = f'<div class="issue"><span class="chip-dark">{html.escape(current["title"])}</span><span>Sent {html.escape(current["sent"])}</span><span>·</span><span>{current["picks"]} picks</span></div>'
    else:
        status = '<strong>About Brenham Every Day</strong>'
        issue_line = ""
    banner = '<div class="preview">Preview. This issue isn\'t published yet.</div>' if preview else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;800;900&family=Sacramento&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap">
<link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
{FOOT_SYMBOL}
{banner}
<div class="band">
  <div class="wrap">
    <div class="topbar">
      <div class="when">{status}</div>
      <nav>
        <label class="sr" for="issuepick">Pick an issue</label>
        <select id="issuepick" onchange="location.href=this.value">{''.join(opts)}</select>
        {specials}
        <a href="{prefix}about/index.html">About</a>
        <a href="https://www.instagram.com/brenhameveryday/" target="_blank" rel="noopener" aria-label="Instagram">{IG_ICON}</a>
        <a href="{FB_URL}" target="_blank" rel="noopener" aria-label="Facebook">{FB_ICON}</a>
      </nav>
      <p class="over" id="over" hidden></p>
    </div>
    <header class="mast">
      <a class="logo" href="{prefix}index.html" aria-label="Brenham Every Day home"><span class="s top">every</span><span class="b">BRENHAM</span><span class="s bot">day</span></a>
      <p class="sub">The best of what's happening this weekend in and around Brenham</p>
      {issue_line}
    </header>
  </div>
  <div class="scene">{scene(pumpkins=pumpkins)}</div>
</div>
<main class="wrap">
  <div class="signup">
    <h3>Get it in your inbox every Wednesday</h3>
    <a class="btn" href="https://brenhameveryday.beehiiv.com/subscribe" target="_blank" rel="noopener">Sign me up</a>
    <small id="signupmsg">Free. One email a week. Unsubscribe anytime.</small>
  </div>
{body}
  <footer>
    <h2>Never miss <span class="s">a weekend</span></h2>
    <div class="signup">
      <h3>Want next weekend's guide in your inbox?</h3>
      <a class="btn" href="https://brenhameveryday.beehiiv.com/subscribe" target="_blank" rel="noopener">Sign me up</a>
      <small>Free. One email a week. Unsubscribe anytime.</small>
    </div>
    <p>We check every pick against the venue or event page before it goes out, but plans change, especially with Texas weather. Double-check before you load up the truck.</p>
    <p>Covering Brenham and towns within about 30 miles, including Chappell Hill, Burton, Independence, Washington, Round Top, Bellville, Somerville, Hempstead and Navasota. Follow along on <a href="https://www.instagram.com/brenhameveryday/" target="_blank" rel="noopener">Instagram</a> and <a href="{FB_URL}" target="_blank" rel="noopener">Facebook</a>.</p>
    <p class="love">I love Brenham, yes I do. I love Brenham, how 'bout you?</p>
  </footer>
</main>
<script>
(function () {{
  var issues = {data}, cur = "{cur}", prefix = "{prefix}";
  if (!cur) return;
  var today = new Intl.DateTimeFormat("en-CA", {{ timeZone: "America/Chicago" }}).format(new Date());
  var me = issues.filter(function (i) {{ return i.slug === cur; }})[0];
  var live = issues.filter(function (i) {{ return !i.draft; }});
  var newest = live[live.length - 1];
  var status = document.getElementById("status"), over = document.getElementById("over");
  if (today > me.end) {{
    status.textContent = "Past issue";
    var next = issues.filter(function (i) {{ return i.end >= today && !i.draft; }})[0] || newest;
    if (next && next.slug !== cur) {{
      over.innerHTML = 'This weekend is over. <a href="' + prefix + next.slug + '/index.html">Newest issue: ' + next.label.replace(/, \\d{{4}}$/, "") + "</a>";
    }} else {{
      over.textContent = "This weekend is over. A new issue is on the way.";
    }}
    over.hidden = false;
  }} else if (today < me.start) {{
    status.textContent = "Coming up";
  }}
}})();
</script>
<script data-goatcounter="https://brenhameveryday.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
</body>
</html>
"""


def issues_published(issues):
    return [i for i in issues if not i.get("draft")] or issues


def main():
    args = sys.argv[1:]
    drafts = "--drafts" in args
    today = datetime.date.today().isoformat()
    if "--today" in args:
        today = args[args.index("--today") + 1]
    issues = [i for i in load_issues() if i["publish_on"] <= today or drafts]
    for i in issues:
        i["draft"] = i["publish_on"] > today
        i["past"] = i["end"] < today
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copy(os.path.join(ROOT, "style.css"), OUT)
    if os.path.isdir(os.path.join(ROOT, "img")):
        shutil.copytree(os.path.join(ROOT, "img"), os.path.join(OUT, "img"))
    open(os.path.join(OUT, "CNAME"), "w").write(DOMAIN + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    for i in issues:
        title = f"Brenham Every Day: {i['label']}"
        desc = f"The best of what's happening in and around Brenham, TX, {i['range']}."
        d = os.path.join(OUT, i["slug"])
        os.makedirs(d)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
            page(title, desc, "../", i["body"], issues, i, preview=i["draft"], pumpkins=i.get("scene_pumpkins", False)))
    newest = issues_published(issues)[-1]
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        page("Brenham Every Day", "Something to do in Brenham, TX and nearby towns, every weekend.", "", newest["body"],
             issues, newest, preview=newest["draft"], pumpkins=newest.get("scene_pumpkins", False)))
    about = open(os.path.join(ROOT, "about.html"), encoding="utf-8").read()
    os.makedirs(os.path.join(OUT, "about"))
    open(os.path.join(OUT, "about", "index.html"), "w", encoding="utf-8").write(
        page("About Brenham Every Day", "Who we are and why we do this.", "../", about, issues))
    print("built", [i["slug"] + (" (draft)" if i["draft"] else "") for i in issues], "newest:", newest["slug"])


if __name__ == "__main__":
    main()
