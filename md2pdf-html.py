import re,sys,html

def esc(s): return html.escape(s,quote=False)

def inline(t):
    t=esc(t)
    codes=[]
    def keep(m):
        codes.append(m.group(1)); return "\x00%d\x00"%(len(codes)-1)
    t=re.sub(r'`([^`]+)`',keep,t)
    t=re.sub(r'\[([^\]]+)\]\(#([A-Za-z0-9\-_]+)\)',r'<a href="#\2">\1</a>',t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])',r'<em>\1</em>',t)
    t=re.sub(r'\x00(\d+)\x00',lambda m:"<code>%s</code>"%codes[int(m.group(1))],t)
    return t

SEEN={}
def convert(md):
    lines=md.split("\n"); out=[]; i=0; n=len(lines)
    listbuf=None
    def closelist():
        nonlocal listbuf
        if listbuf: out.append("</%s>"%listbuf); listbuf=None
    while i<n:
        L=lines[i]
        if L.startswith("```"):
            closelist(); i+=1; buf=[]
            while i<n and not lines[i].startswith("```"): buf.append(esc(lines[i])); i+=1
            i+=1; out.append("<pre><code>%s</code></pre>"%"\n".join(buf)); continue
        if re.match(r'^<a name="[^"]+"></a>\s*$',L): i+=1; continue
        m=re.match(r'^(#{1,6}) (.+?)\s*$',L)
        if m:
            closelist(); lvl=len(m.group(1)); txt=m.group(2)
            slug=txt if re.fullmatch(r'[a-z0-9\-]+',txt) else re.sub(r'[^a-z0-9]+','-',txt.lower()).strip('-')
            SEEN[slug]=SEEN.get(slug,0)+1
            if SEEN[slug]>1: slug="%s--%d"%(slug,SEEN[slug])
            out.append('<h%d id="%s">%s</h%d>'%(lvl,slug,inline(txt),lvl)); i+=1; continue
        if re.match(r'^---+\s*$',L):
            closelist(); out.append("<hr/>"); i+=1; continue
        if L.startswith(">"):
            closelist(); buf=[]
            while i<n and lines[i].startswith(">"):
                buf.append(lines[i][1:].lstrip() if lines[i][1:2]==" " else lines[i][1:]); i+=1
            out.append("<blockquote>%s</blockquote>"%convert("\n".join(buf))); continue
        if L.lstrip().startswith("|") and i+1<n and re.match(r'^\s*\|[\s\-:|]+\|\s*$',lines[i+1]):
            closelist()
            def cells(r): return [c.strip() for c in r.strip().strip("|").split("|")]
            hdr=cells(L); i+=2; rows=[]
            while i<n and lines[i].lstrip().startswith("|"): rows.append(cells(lines[i])); i+=1
            # A header row whose first cell is filled and whose remaining cells are all
            # empty is a caption spanning the table: "| Title | | | |".
            spanning = len(hdr)>1 and bool(hdr[0]) and not any(hdr[1:])
            if spanning:
                head='<tr><th class="span" colspan="%d">%s</th></tr>'%(len(hdr),inline(hdr[0]))
            else:
                head="<tr>"+"".join("<th>%s</th>"%inline(c) for c in hdr)+"</tr>"
            t=["<table><thead>",head,"</thead><tbody>"]
            # Inside a table that opted into the spanning caption above, an empty cell
            # means "merge upward" and becomes a rowspan on the cell it continues.
            span=[[1]*len(r) for r in rows]; skip=[[False]*len(r) for r in rows]
            if spanning and rows:
                for c in range(max(len(r) for r in rows)):
                    anchor=None
                    for ri,r in enumerate(rows):
                        if c>=len(r): anchor=None; continue
                        if r[c]=="" and anchor is not None:
                            span[anchor][c]+=1; skip[ri][c]=True
                        else: anchor=ri
            for ri,r in enumerate(rows):
                cs=[]
                for c,val in enumerate(r):
                    if skip[ri][c]: continue
                    a=' rowspan="%d"'%span[ri][c] if span[ri][c]>1 else ''
                    cs.append("<td%s>%s</td>"%(a,inline(val)))
                t.append("<tr>"+"".join(cs)+"</tr>")
            t.append("</tbody></table>"); out.append("".join(t)); continue
        m=re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$',L)
        if m:
            kind="ol" if re.match(r'\d+\.',m.group(2)) else "ul"
            if listbuf!=kind: closelist(); out.append("<%s>"%kind); listbuf=kind
            item=m.group(3); i+=1
            while i<n and lines[i].strip() and not re.match(r'^(\s*)([-*]|\d+\.)\s+',lines[i]) \
                  and not lines[i].startswith(("#","```",">","|","---")):
                item+=" "+lines[i].strip(); i+=1
            out.append("<li>%s</li>"%inline(item)); continue
        if not L.strip(): closelist(); i+=1; continue
        buf=[L]; i+=1
        while i<n and lines[i].strip() and not re.match(r'^(#{1,6} |```|>|\||---+\s*$|\s*([-*]|\d+\.)\s)',lines[i]):
            buf.append(lines[i]); i+=1
        closelist(); out.append("<p>%s</p>"%inline(" ".join(buf)))
    closelist()
    return "\n".join(out)

CSS="""
@page { size: A4; margin: 14mm 12mm; }
body { font: 10.2pt/1.5 "DejaVu Serif","Liberation Serif",Georgia,serif; color:#111; }
h1 { font-size: 19pt; border-bottom:2px solid #333; padding-bottom:4px; margin:22pt 0 10pt; page-break-before: always; }
h1:first-of-type { page-break-before: avoid; }
h2 { font-size: 14pt; margin:16pt 0 6pt; color:#1a1a1a; border-bottom:1px solid #bbb; }
h3 { font-size: 11.6pt; margin:12pt 0 4pt; }
h4 { font-size: 10.6pt; margin:10pt 0 3pt; }
h1,h2,h3,h4 { page-break-after: avoid; font-family:"DejaVu Sans","Liberation Sans",Helvetica,sans-serif; }
p { margin: 0 0 6pt; text-align: justify; }
a { color:#0b4fa8; text-decoration:none; }
code { font-family:"DejaVu Sans Mono","Liberation Mono",monospace; font-size:8.6pt; background:#f2f2f2; padding:0 2px; }
pre { background:#f6f6f6; border:1px solid #ddd; padding:6pt; overflow:hidden; page-break-inside:avoid; }
pre code { font-size:7.6pt; background:none; white-space:pre; }
table { border-collapse:collapse; width:100%; margin:6pt 0; font-size:8.8pt; page-break-inside:avoid; }
th.span { text-align:left; font-size:9.6pt; padding:4pt 5pt; }
td[rowspan] { vertical-align:middle; text-align:center; }
th,td { border:1px solid #bbb; padding:3pt 5pt; text-align:left; vertical-align:top; }
th { background:#ececec; }
blockquote { margin:6pt 0; padding:4pt 10pt; border-left:3px solid #888; background:#fafafa; page-break-inside:avoid; }
ul,ol { margin:0 0 6pt 16pt; padding:0; }
li { margin-bottom:2pt; }
hr { border:none; border-top:1px solid #ccc; margin:10pt 0; }
"""
md=open(sys.argv[1],encoding='utf8').read()
title=md.split("\n",1)[0].lstrip("# ").strip()
body=convert(md)
open(sys.argv[2],"w",encoding='utf8').write(
 "<!doctype html><html><head><meta charset='utf-8'><title>%s</title><style>%s</style></head><body>%s</body></html>"
 %(esc(title),CSS,body))
print("html written:",sys.argv[2])
