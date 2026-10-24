"""The Brenham scene: water tower, courthouse, Main Street, trees, bluebonnet dots and fall pumpkins."""
def scene(pumpkins=False):
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
    parts.append('</svg>')
    return "".join(parts)
