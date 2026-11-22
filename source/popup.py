"""Once-per-visitor signup nudge (approved by Caroline 2026-11-17).
Phones: small bar slides up after 50% scroll. Computers: exit intent.
Skipped while a signup box is on screen. Shows once per browser session; closing it snoozes 30 days.
?popup=test forces it to show (for checking)."""

POPUP_FORM_ID = "9db22e13-0393-4787-a946-6d2b13077c43"   # beehiiv "Website pop-up (Holiday Guide)", button "Send it to me"
WEEKLY_FORM_ID = "9bd79a0c-a3ea-40ff-a7f8-a820b5fc88b1"  # main site form, used after New Year's

JS = """<script>(function () {
  var KEY = "bed_nudge", DAYS = 30, el = document.getElementById("nudge"), done = false;
  if (!el) return;
  var test = /[?&]popup=test/.test(location.search);
  function snoozed() {
    if (test) return false;
    try { if (sessionStorage.getItem(KEY)) return true; } catch (e) {}
    try { var t = +localStorage.getItem(KEY); return t && (Date.now() - t) < DAYS * 864e5; } catch (e) { return false; }
  }
  function snooze() { try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {} }
  function boxOnScreen() {
    var boxes = document.querySelectorAll(".signup, .subpage");
    for (var i = 0; i < boxes.length; i++) { var r = boxes[i].getBoundingClientRect(); if (r.bottom > 0 && r.top < innerHeight) return true; }
    return false;
  }
  function show() {
    if (done || snoozed() || boxOnScreen()) return;
    done = true; el.classList.add("on");
    try { sessionStorage.setItem(KEY, "1"); } catch (e) {}
  }
  function hide() { el.classList.remove("on"); snooze(); }
  el.querySelector(".nudge-x").addEventListener("click", hide);
  el.querySelector(".nudge-btn").addEventListener("click", function () { setTimeout(hide, 400); });
  if (test) { setTimeout(show, 600); return; }
  if (snoozed()) return;
  setTimeout(show, 10000);  // ~10s in, or the triggers below, whichever comes first
  if (matchMedia("(pointer: coarse)").matches) {
    addEventListener("scroll", function () {
      var h = document.documentElement.scrollHeight - innerHeight;
      if (h > 0 && scrollY / h >= 0.5) show();
    }, { passive: true });
  } else {
    document.addEventListener("mouseout", function (e) { if (!e.relatedTarget && e.clientY <= 0) show(); });
  }
})();</script>"""


def popup_html(today):
    gift = today <= "2027-01-01"
    head = "Get our weekly Brenham email (+ a free Holiday Guide)" if gift else "Get our weekly Brenham email"
    sub = "The best family things to do in and around Brenham, every Tuesday night."
    btn = "Sign me up"
    return ('<div class="nudge" id="nudge" role="dialog" aria-label="' + head + '">'
            '<button class="nudge-x" type="button" aria-label="Close">&times;</button>'
            '<p class="nudge-h">' + head + '</p><p class="nudge-s">' + sub + '</p>'
            '<div class="bhform"><script async src="https://subscribe-forms.beehiiv.com/v3/loader.js" '
            'data-beehiiv-form="' + (POPUP_FORM_ID if gift else WEEKLY_FORM_ID) + '"></script>'
            '<a class="btn bhfallback nudge-btn" href="https://brenhameveryday.beehiiv.com/subscribe?utm_source=popup" '
            'target="_blank" rel="noopener">' + btn + '</a></div></div>' + JS)
