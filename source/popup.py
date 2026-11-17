"""Once-per-visitor signup nudge (approved by Caroline 2026-11-17).
Phones: small bar slides up after 50% scroll. Computers: exit intent.
Skipped while a signup box is on screen; 30-day snooze once shown (localStorage in try/catch)."""

JS = """<script>(function () {
  var KEY = "bed_nudge", DAYS = 30, el = document.getElementById("nudge"), done = false;
  if (!el) return;
  function snoozed() { try { var t = +localStorage.getItem(KEY); return t && (Date.now() - t) < DAYS * 864e5; } catch (e) { return false; } }
  function snooze() { try { localStorage.setItem(KEY, String(Date.now())); } catch (e) {} }
  function boxOnScreen() {
    var boxes = document.querySelectorAll(".signup, .subpage");
    for (var i = 0; i < boxes.length; i++) { var r = boxes[i].getBoundingClientRect(); if (r.bottom > 0 && r.top < innerHeight) return true; }
    return false;
  }
  function show() {
    if (done || snoozed() || boxOnScreen()) return;
    done = true; snooze(); el.hidden = false;
    requestAnimationFrame(function () { requestAnimationFrame(function () { el.classList.add("on"); }); });
  }
  function hide() { el.classList.remove("on"); setTimeout(function () { el.hidden = true; }, 300); }
  el.querySelector(".nudge-x").addEventListener("click", hide);
  el.querySelector(".nudge-btn").addEventListener("click", function () { setTimeout(hide, 400); });
  if (snoozed()) return;
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
    head = "Get the free Brenham Holiday Guide" if gift else "Get the weekend guide every Wednesday"
    sub = ("Every deadline and date for Thanksgiving through New Year&rsquo;s, in your inbox right away."
           if gift else "The best family things to do in and around Brenham. One email a week.")
    btn = "Send it to me" if gift else "Sign me up"
    return ('<div class="nudge" id="nudge" role="dialog" aria-label="' + head + '" hidden>'
            '<button class="nudge-x" type="button" aria-label="Close">&times;</button>'
            '<p class="nudge-h">' + head + '</p><p class="nudge-s">' + sub + '</p>'
            '<a class="btn nudge-btn" href="https://brenhameveryday.beehiiv.com/subscribe?utm_source=popup" '
            'target="_blank" rel="noopener">' + btn + '</a></div>' + JS)
