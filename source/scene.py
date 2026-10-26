"""The Brenham scene: water tower, courthouse, Main Street, trees, bluebonnet dots and fall pumpkins."""
def scene(pumpkins=False, spooky=False):
    parts = ['<svg viewBox="0 0 1080 480" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">',
     '<path d="M0 330 C200 270 380 300 540 320 C720 340 880 280 1080 300 L1080 480 L0 480Z" fill="#8fbf8a"/>',
     # water tower
     '<g fill="#cfd8ea"><rect x="150" y="150" width="8" height="190"/><rect x="232" y="150" width="8" height="190"/><rect x="190" y="150" width="8" height="190"/><ellipse cx="195" cy="140" rx="70" ry="50"/><path d="M125 130 L195 70 L265 130Z"/></g>',
     '<text x="195" y="150" text-anchor="middle" font-family="Montserrat, sans-serif" font-weight="900" font-size="24" fill="#4a68a3">BRENHAM</text>',
     # courthouse
     '<rect x="400" y="170" width="300" height="170" fill="#e8d9c4"/><rect x="470" y="110" width="160" height="70" fill="#efe3d1"/><rect x="510" y="70" width="80" height="45" fill="#f4ecdf"/><rect x="545" y="40" width="10" height="32" fill="#f4ecdf"/>',
     '<g fill="#4a68a3"><rect x="420" y="200" width="22" height="40"/><rect x="460" y="200" width="22" height="40"/><rect x="500" y="200" width="22" height="40"/><rect x="578" y="200" width="22" height="40"/><rect x="618" y="200" width="22" height="40"/><rect x="658" y="200" width="22" height="40"/><rect x="420" y="265" width="22" height="40"/><rect x="460" y="265" width="22" height="40"/><rect x="618" y="265" width="22" height="40"/><rect x="658" y="265" width="22" height="40"/><rect x="525" y="260" width="50" height="80" rx="4"/><rect x="490" y="130" width="18" height="34"/><rect x="525" y="130" width="18" height="34"/><rect x="560" y="130" width="18" height="34"/><rect x="595" y="130" width="18" height="34"/></g>',
     # storefronts
     '<rect x="740" y="210" width="110" height="130" fill="#e5b6bd"/><rect x="850" y="230" width="100" height="110" fill="#f2d07e"/><rect x="950" y="200" width="110" height="140" fill="#9db6e0"/>',
     '<g fill="#fff" opacity=".85"><rect x="760" y="240" width="28" height="36"/><rect x="805" y="240" width="28" height="36"/><rect x="870" y="255" width="26" height="32"/><rect x="910" y="255" width="26" height="32"/><rect x="968" y="230" width="28" height="36"/><rect x="1012" y="230" width="28" height="36"/></g>',
     '<g fill="#1f2d4d"><rect x="780" y="295" width="34" height="45"/><rect x="882" y="300" width="34" height="40"/><rect x="988" y="295" width="34" height="45"/></g>',
     # trees
     '<g fill="#4f8a5b"><circle cx="330" cy="300" r="40"/><circle cx="370" cy="315" r="30"/><circle cx="60" cy="320" r="38"/><circle cx="720" cy="320" r="30"/></g>',
     '<g fill="#6b4a2f"><rect x="326" y="320" width="8" height="30"/><rect x="56" y="340" width="8" height="20"/></g>',
    ]
    # bluebonnets, drawn as simple dots
    parts.append('<g fill="#3d5a94"><circle cx="100" cy="420" r="9"/><circle cx="120" cy="430" r="8"/><circle cx="260" cy="440" r="9"/><circle cx="420" cy="425" r="8"/><circle cx="440" cy="438" r="9"/><circle cx="620" cy="430" r="9"/><circle cx="800" cy="420" r="8"/><circle cx="820" cy="436" r="9"/><circle cx="980" cy="428" r="9"/></g>')
    if pumpkins:
        parts.append('<g fill="#e98a3a"><ellipse cx="560" cy="380" rx="26" ry="20"/><ellipse cx="610" cy="388" rx="20" ry="15"/><ellipse cx="900" cy="385" rx="24" ry="18"/></g>')
    if spooky:
        # moon and bats in the sky
        parts.insert(1, '<circle cx="880" cy="90" r="48" fill="#f4ecdf" opacity=".95"/><circle cx="860" cy="78" r="8" fill="#e8d9c4"/><circle cx="895" cy="108" r="6" fill="#e8d9c4"/>')
        bat = '<path transform="translate({x} {y}) scale({s})" d="M0 0 C6 -10 14 -10 18 -2 C20 -8 24 -8 26 -2 C30 -10 38 -10 44 0 C36 -3 30 2 26 6 L22 2 L18 6 C14 2 8 -3 0 0Z" fill="#1f2d4d"/>'
        parts.append(''.join(bat.format(x=x, y=y, s=sc) for x, y, sc in [(300, 70, 1.1), (360, 40, .8), (720, 120, .9), (980, 160, .7), (60, 90, .8)]))
        # glowing windows
        parts.append('<g fill="#f2d07e" opacity=".9"><rect x="760" y="240" width="28" height="36"/><rect x="910" y="255" width="26" height="32"/><rect x="1012" y="230" width="28" height="36"/><rect x="460" y="200" width="22" height="40"/><rect x="618" y="265" width="22" height="40"/></g>')
        # ghost peeking from behind the water tower
        parts.append('<path d="M262 250 C262 215 300 215 300 250 L300 290 L293 283 L287 290 L281 283 L275 290 L269 283 L262 290Z" fill="#fff"/><circle cx="275" cy="248" r="3.5" fill="#1f2d4d"/><circle cx="288" cy="248" r="3.5" fill="#1f2d4d"/>')
        # jack-o'-lanterns
        jack = ('<g transform="translate({x} {y}) scale({s})"><rect x="-4" y="-30" width="8" height="12" rx="2" fill="#4f8a5b"/>'
                '<ellipse cx="0" cy="0" rx="34" ry="26" fill="#e98a3a"/><path d="M-18 -8 l7 -10 l7 10Z M4 -8 l7 -10 l7 10Z" fill="#1f2d4d"/>'
                '<path d="M-20 6 Q0 24 20 6 L14 8 L10 13 L5 9 L0 14 L-5 9 L-10 13 L-14 8Z" fill="#1f2d4d"/></g>')
        parts.append(''.join(jack.format(x=x, y=y, s=sc) for x, y, sc in [(500, 395, 1.1), (570, 405, .8), (860, 400, 1), (180, 405, .85)]))
    parts.append('</svg>')
    return "".join(parts)
