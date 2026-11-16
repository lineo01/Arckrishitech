#!/usr/bin/env python3
"""Refresh the weekly Kalimati reference snapshot from Ramro Patro. Fails closed on layout changes."""
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from datetime import datetime, timezone
from pathlib import Path
import json, re
ROOT=Path(__file__).resolve().parents[1]
URL="https://www.ramropatro.com/vegetable"
class Tables(HTMLParser):
    def __init__(self): super().__init__(); self.tables=[]; self.table=None; self.row=None; self.cell=None
    def handle_starttag(self,tag,attrs):
        if tag=="table": self.table=[]
        elif tag=="tr" and self.table is not None: self.row=[]
        elif tag in ("td","th") and self.row is not None: self.cell=[]
    def handle_data(self,data):
        if self.cell is not None: self.cell.append(data)
    def handle_endtag(self,tag):
        if tag in ("td","th") and self.cell is not None:
            self.row.append(" ".join(" ".join(self.cell).split())); self.cell=None
        elif tag=="tr" and self.row is not None:
            if self.row: self.table.append(self.row)
            self.row=None
        elif tag=="table" and self.table is not None:
            self.tables.append(self.table); self.table=None
req=Request(URL,headers={"User-Agent":"Arkrishitech weekly market snapshot bot/1.0"})
with urlopen(req,timeout=30) as resp: html=resp.read().decode("utf-8","replace")
p=Tables(); p.feed(html)
rows=[]
for table in p.tables:
    for row in table:
        low=" ".join(row).lower()
        if "commodity" in low and "minimum" in low and "maximum" in low and "average" in low: rows=table[table.index(row)+1:]; break
    if rows: break
if not rows: raise SystemExit("Expected Ramro Patro price table not found; refusing to publish an empty/guessed snapshot")
# Keep a curated list used in the interface; match exact commodity labels from source.
keep={"Tomato Big(Nepali)":"Tomato, big (Nepali)","Tomato Small(Local)":"Tomato, small (local)","Potato Red(Long)":"Potato, red (long)","Potato White":"Potato, white","Carrot(Local)":"Carrot (local)","Cabbage(Local)":"Cabbage (local)","Cauli Local":"Cauliflower (local)","Raddish Red":"Radish, red","Green Peas":"Green peas","French Bean(Local)":"French bean (local)","Bitter Gourd":"Bitter gourd","Bottle Gourd":"Bottle gourd","Okra":"Okra","Spinach Leaf":"Spinach leaf","Gundruk":"Gundruk"}
ne={"Tomato, big (Nepali)":"गोलभेडा ठूलो (नेपाली)","Tomato, small (local)":"गोलभेडा सानो (लोकल)","Potato, red (long)":"आलु रातो (लाम्चो)","Potato, white":"सेतो आलु","Carrot (local)":"गाजर (लोकल)","Cabbage (local)":"बन्दा (लोकल)","Cauliflower (local)":"काउली (लोकल)","Radish, red":"मूला रातो","Green peas":"हरियो केराउ","French bean (local)":"सिमी (लोकल)","Bitter gourd":"करेला","Bottle gourd":"लौका","Okra":"भिण्डी","Spinach leaf":"पालुङ्गो","Gundruk":"गुन्द्रुक"}
out=[]
for row in rows:
    if len(row)<5: continue
    name=row[0].strip();
    if name not in keep: continue
    nums=[]
    for x in row[2:5]:
        m=re.search(r"\d+(?:\.\d+)?",x.replace(",","")); nums.append(float(m.group()) if m else None)
    if any(x is None for x in nums): continue
    out.append({"name":keep[name],"name_ne":ne[keep[name]],"min":round(nums[0]),"max":round(nums[1]),"avg":round(nums[2])})
if len(out)<10: raise SystemExit(f"Only {len(out)} expected commodities parsed; refusing to replace last known-good snapshot")
# Source page title includes its publication date; use capture date if date extraction changes.
date_match=re.search(r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),\s+(\d{4})",html,re.I)
captured=datetime.now(timezone.utc).astimezone().date().isoformat()
if date_match:
    from datetime import datetime as _dt
    captured=_dt.strptime(" ".join(date_match.groups()),"%B %d %Y").date().isoformat()
payload={"market":"Kalimati wholesale market, Kathmandu, Nepal","source":"Ramro Patro","source_url":URL,"source_publisher":"Kalimati daily wholesale rates as displayed by Ramro Patro","captured_on":captured,"currency":"NPR","unit":"kg","refresh_policy":"Weekly snapshot; not a live feed","prices":out}
for folder in (ROOT/"public",ROOT/"frontend"):
    (folder/"market_snapshot.json").write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(f"Updated {len(out)} Kalimati commodity rates for {captured}")
