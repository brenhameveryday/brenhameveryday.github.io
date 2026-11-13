def deer(x, y, nose='#6b4a2f'):
    return (f'<g transform="translate({x} {y})">'
            '<rect x="-26" y="-14" width="52" height="20" rx="10" fill="#8a5a3b"/>'  # body
            '<path d="M-20 4 l-10 16 M-12 4 l-4 18 M14 4 l8 16 M20 4 l12 14" stroke="#6b4a2f" stroke-width="5" stroke-linecap="round"/>'  # legs, galloping
            '<path d="M18 -10 l10 -16" stroke="#8a5a3b" stroke-width="10" stroke-linecap="round"/>'  # neck
            '<ellipse cx="34" cy="-28" rx="12" ry="8" fill="#8a5a3b"/>'  # head
            f'<circle cx="46" cy="-27" r="4.5" fill="{nose}"/><circle cx="34" cy="-31" r="2" fill="#1f2d4d"/>'
            '<path d="M28 -34 l-6 -12 m3 6 l-7 -2 M36 -35 l2 -13 m-1 6 l6 -3" stroke="#f2d07e" stroke-width="3.5" stroke-linecap="round" fill="none"/>'  # antlers
            '<path d="M-26 -8 l-8 -6" stroke="#8a5a3b" stroke-width="5" stroke-linecap="round"/></g>')
def sleigh_svg():
    g = ['<svg class="sleigh" viewBox="0 0 330 120" aria-hidden="true">']
    # sparkle trail
    g.append('<g fill="#f2d07e"><circle cx="8" cy="96" r="3"/><circle cx="24" cy="86" r="4"/><circle cx="16" cy="70" r="2.5"/><circle cx="40" cy="98" r="2.5"/></g>')
    # reins
    g.append('<path d="M118 62 Q170 52 196 60 Q236 50 262 56" stroke="#f4ecdf" stroke-width="2.5" fill="none"/>')
    # Santa (behind sleigh front)
    g.append('<rect x="74" y="44" width="34" height="34" rx="10" fill="#d4483b"/><rect x="74" y="64" width="34" height="6" fill="#1f2d4d"/>'
             '<circle cx="92" cy="38" r="12" fill="#f3c9a8"/><path d="M80 40 Q92 62 104 40Z" fill="#f4ecdf"/>'
             '<path d="M79 33 Q92 12 106 30 L112 24" stroke="#d4483b" stroke-width="10" fill="none" stroke-linecap="round"/><circle cx="114" cy="22" r="5" fill="#f4ecdf"/>'
             '<rect x="78" y="28" width="28" height="6" rx="3" fill="#f4ecdf"/>'
             '<path d="M106 54 L120 60" stroke="#d4483b" stroke-width="8" stroke-linecap="round"/><circle cx="121" cy="61" r="4.5" fill="#1f2d4d"/>')
    # gift sack
    g.append('<path d="M50 70 Q46 40 62 40 Q78 40 72 70Z" fill="#8a5a3b"/><rect x="56" y="38" width="12" height="5" rx="2" fill="#f2d07e"/>')
    # sleigh body + runner
    g.append('<path d="M44 66 L124 66 Q132 66 130 80 Q126 92 108 92 L56 92 Q44 92 44 80Z" fill="#d4483b"/>'
             '<path d="M44 66 Q34 62 36 54 Q40 48 48 54" stroke="#d4483b" stroke-width="8" fill="none" stroke-linecap="round"/>'
             '<rect x="52" y="74" width="66" height="5" rx="2.5" fill="#f2d07e"/>'
             '<path d="M40 104 L120 104 Q138 104 140 92" stroke="#f2d07e" stroke-width="5" fill="none" stroke-linecap="round"/>'
             '<path d="M64 92 v12 M104 92 v12" stroke="#f2d07e" stroke-width="4"/>')
    g.append(deer(212, 70) + deer(286, 60, '#d4483b'))
    g.append('</svg>')
    return ''.join(g)
