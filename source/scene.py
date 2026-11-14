"""The Brenham scene: water tower, courthouse, Main Street, trees, bluebonnet dots and fall pumpkins."""
def scene(pumpkins=False, spooky=False, christmas=False, thanks=False):
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
     # trees (round; hidden at Christmas)
     '' if christmas or thanks else '<g fill="#4f8a5b"><circle cx="330" cy="300" r="40"/><circle cx="370" cy="315" r="30"/><circle cx="60" cy="320" r="38"/><circle cx="720" cy="320" r="30"/></g>',
     '' if christmas else '<g fill="#6b4a2f"><rect x="326" y="320" width="8" height="30"/><rect x="56" y="340" width="8" height="20"/></g>',
    ]
    # bluebonnets, drawn as simple dots
    if not christmas: parts.append('<g fill="#3d5a94"><circle cx="100" cy="420" r="9"/><circle cx="120" cy="430" r="8"/><circle cx="260" cy="440" r="9"/><circle cx="420" cy="425" r="8"/><circle cx="440" cy="438" r="9"/><circle cx="620" cy="430" r="9"/><circle cx="800" cy="420" r="8"/><circle cx="820" cy="436" r="9"/><circle cx="980" cy="428" r="9"/></g>')
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
    if thanks:
        # fall trees in orange, red and gold
        parts.append('<g fill="#6b4a2f"><rect x="366" y="330" width="8" height="22"/><rect x="716" y="335" width="8" height="20"/><rect x="326" y="320" width="8" height="30"/><rect x="56" y="340" width="8" height="20"/></g>')
        parts.append('<circle cx="330" cy="300" r="40" fill="#d9822b"/><circle cx="370" cy="315" r="30" fill="#c0492f"/><circle cx="60" cy="320" r="38" fill="#e3a832"/><circle cx="720" cy="320" r="30" fill="#c0492f"/>')
        # harvest bunting across the courthouse and shops
        def bunting(x1, x2, y):
            cols = ['#b85a26', '#e3a832', '#c0492f', '#f4ecdf']
            n = max(3, int((x2 - x1) / 24)); w = (x2 - x1) / n
            out = [f'<path d="M{x1} {y} L{x2} {y}" stroke="#6b4a2f" stroke-width="2"/>']
            for i in range(n):
                x = x1 + i * w
                out.append(f'<path d="M{x + 2:.0f} {y} L{x + w - 2:.0f} {y} L{x + w / 2:.0f} {y + 18}Z" fill="{cols[i % 4]}"/>')
            return ''.join(out)
        parts.append(bunting(400, 700, 172) + bunting(740, 1060, 212))
        # hay bales and pumpkins
        parts.append('<g fill="#e3c06a"><rect x="470" y="372" width="70" height="36" rx="6"/><rect x="840" y="378" width="60" height="32" rx="6"/></g>'
                     '<g stroke="#c9a24f" stroke-width="2"><path d="M478 384 h54 M478 396 h54 M848 390 h44 M848 400 h44"/></g>'
                     '<g fill="#e98a3a"><ellipse cx="505" cy="360" rx="20" ry="15"/><ellipse cx="575" cy="392" rx="22" ry="17"/><ellipse cx="930" cy="395" rx="20" ry="15"/></g>'
                     '<g fill="#4f8a5b"><rect x="502" y="342" width="6" height="8" rx="2"/><rect x="572" y="372" width="6" height="8" rx="2"/><rect x="927" y="377" width="6" height="8" rx="2"/></g>')
        # a friendly turkey on the hill
        parts.append('<g transform="translate(250 390)">'
                     '<g><ellipse cx="0" cy="-28" rx="13" ry="34" fill="#c0492f" transform="rotate(-50)"/><ellipse cx="0" cy="-30" rx="13" ry="36" fill="#e3a832" transform="rotate(-25)"/>'
                     '<ellipse cx="0" cy="-32" rx="13" ry="38" fill="#b85a26"/><ellipse cx="0" cy="-30" rx="13" ry="36" fill="#e3a832" transform="rotate(25)"/><ellipse cx="0" cy="-28" rx="13" ry="34" fill="#c0492f" transform="rotate(50)"/></g>'
                     '<ellipse cx="0" cy="0" rx="24" ry="22" fill="#6b4a2f"/><circle cx="0" cy="-26" r="13" fill="#7a5638"/>'
                     '<circle cx="-4" cy="-29" r="2.5" fill="#1f2d4d"/><circle cx="4" cy="-29" r="2.5" fill="#1f2d4d"/><path d="M-4 -24 L4 -24 L0 -17Z" fill="#e3a832"/>'
                     '<path d="M2 -21 q5 6 0 12 q-3 -5 0 -12Z" fill="#d9473b"/><path d="M-8 20 v10 M8 20 v10" stroke="#e3a832" stroke-width="3"/></g>')
        # falling leaves
        leaf = '<ellipse cx="{x}" cy="{y}" rx="7" ry="4" fill="{c}" transform="rotate({r} {x} {y})"/>'
        parts.insert(1, ''.join(leaf.format(x=x, y=y, c=c, r=r) for x, y, c, r in
                     [(300, 80, '#e3a832', 30), (440, 50, '#c0492f', -20), (700, 70, '#d9822b', 45), (860, 120, '#e3a832', -35), (990, 60, '#c0492f', 15), (120, 90, '#d9822b', -10)]))
    if christmas:
        def bulbs(x1, x2, y, sag):
            cols = ['#d9473b', '#5ee3b1', '#f2d07e', '#e5b6bd', '#4a68a3']
            out = [f'<path d="M{x1} {y} Q{(x1+x2)/2} {y+sag*2} {x2} {y}" stroke="#1f2d4d" stroke-width="2" fill="none"/>']
            n = max(4, int((x2 - x1) / 26))
            for i in range(1, n):
                t = i / n; bx = x1 + (x2 - x1) * t; by = y + sag * 4 * t * (1 - t)
                out.append(f'<circle cx="{bx:.0f}" cy="{by + 4:.0f}" r="5" fill="{cols[i % 5]}"/>')
            return ''.join(out)
        # string lights on the courthouse and storefronts
        parts.append(bulbs(400, 700, 172, 14) + bulbs(470, 630, 112, 10) + bulbs(740, 850, 212, 10) + bulbs(850, 950, 232, 10) + bulbs(950, 1060, 202, 10))
        # wreaths on the courthouse door and shop doors
        wreath = '<circle cx="{x}" cy="{y}" r="12" fill="none" stroke="#4f8a5b" stroke-width="7"/><circle cx="{x}" cy="{yb}" r="3.5" fill="#d9473b"/>'
        parts.append(''.join(wreath.format(x=x, y=y, yb=y + 11) for x, y in [(550, 245), (797, 285), (899, 290), (1005, 285)]))
        # decorated Christmas trees with stars
        def xtree(x, y, sc):
            return (f'<g transform="translate({x} {y}) scale({sc})"><rect x="-6" y="0" width="12" height="18" fill="#6b4a2f"/>'
                    '<path d="M0 -110 L-48 0 L48 0Z" fill="#4f8a5b"/><path d="M0 -118 l6 12 l13 1 l-10 9 l3 13 l-12 -7 l-12 7 l3 -13 l-10 -9 l13 -1Z" fill="#f2d07e"/>'
                    '<circle cx="-14" cy="-30" r="6" fill="#d9473b"/><circle cx="16" cy="-50" r="6" fill="#5ee3b1"/><circle cx="-6" cy="-70" r="5" fill="#e5b6bd"/><circle cx="22" cy="-14" r="6" fill="#f2d07e"/><circle cx="-26" cy="-8" r="5" fill="#4a68a3"/></g>')
        parts.append(xtree(330, 345, 1.0) + xtree(60, 360, .8) + xtree(720, 345, .7))
        # presents
        gift = '<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/><rect x="{rx}" y="{y}" width="6" height="{h}" fill="#f4ecdf"/><rect x="{x}" y="{ry}" width="{w}" height="6" fill="#f4ecdf"/>'
        parts.append(''.join(gift.format(x=x, y=y, w=w, h=h, c=c, rx=x + w / 2 - 3, ry=y + h / 2 - 3) for x, y, w, h, c in
                             [(380, 355, 40, 32, '#d9473b'), (425, 365, 30, 22, '#5ee3b1'), (600, 380, 44, 34, '#e5b6bd'), (860, 385, 36, 28, '#d9473b'), (150, 395, 34, 26, '#f2d07e')]))
        # a few twinkly stars in the sky
        parts.insert(1, '<g fill="#f2d07e"><circle cx="320" cy="60" r="4"/><circle cx="700" cy="40" r="3"/><circle cx="860" cy="110" r="4"/><circle cx="1000" cy="60" r="3"/><circle cx="440" cy="40" r="3"/></g>')
    parts.append('</svg>')
    return "".join(parts)
