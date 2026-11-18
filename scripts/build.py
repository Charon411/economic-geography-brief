from pathlib import Path
import re,html,shutil,datetime
root=Path(__file__).resolve().parents[1]
rows=[]
for p in (root/'briefs').glob('*.html'):
 m=re.fullmatch(r'(\d{4}-\d{2}-\d{2})-(\d+)\.html',p.name)
 if not m: raise ValueError('文件名须为 YYYY-MM-DD-期号.html: '+p.name)
 date,issue=m.groups(); datetime.date.fromisoformat(date)
 s=p.read_text(); title=re.search(r'<title>(.*?)</title>',s,re.S)
 subtitle=re.search(r'<div class="subtitle">(.*?)</div>',s,re.S)
 desc=html.unescape(re.sub('<[^>]+>','',subtitle.group(1))) if subtitle else ''
 rows.append((date,int(issue),p.name,desc))
rows.sort(reverse=True)
cards=[]
for i,(date,issue,name,desc) in enumerate(rows):
 cards.append(f'<article data-month="{date[:7]}" data-search="{html.escape(f"{date} 第{issue}期 {desc}",quote=True)}"><div class="meta">{date} <span>{"最新一期 · " if i==0 else ""}第{issue}期</span></div><h2><a href="briefs/{name}">经济地理每日重点简报 <b>↗</b></a></h2><p>{html.escape(desc)}</p><a class="read" href="briefs/{name}">阅读本期 →</a></article>')
page=(root/'template.html').read_text().replace('{{CARDS}}','\n'.join(cards)).replace('{{COUNT}}',str(len(rows))).replace('{{MONTHS}}',''.join(f'<option>{m}</option>' for m in sorted({r[0][:7] for r in rows},reverse=True)))
(root/'index.html').write_text(page)
dist=root/'_site'
if dist.exists(): shutil.rmtree(dist)
dist.mkdir(); (dist/'index.html').write_text(page); shutil.copytree(root/'briefs',dist/'briefs'); (dist/'.nojekyll').touch()
print(f'Built {len(rows)} real issues: '+', '.join(str(r[1]) for r in rows))
