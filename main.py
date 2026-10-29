import datetime
today = datetime.datetime.now().strftime("%d %B %Y - %A")

html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anantapur Study Buddy - Daily Current Affairs</title>
<style>
body{{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:15px}}
.card{{background:white;color:#0f172a;border-radius:15px;padding:20px;margin:15px auto;max-width:650px;text-align:left;line-height:1.6}}
.btn{{background:#25D366;color:white;padding:14px 28px;border-radius:30px;font-size:17px;text-decoration:none;display:inline-block;margin:8px;font-weight:bold}}
h1{{color:#facc15}} .tag{{background:#e0f2fe;color:#0369a1;padding:3px 8px;border-radius:5px;font-size:12px;font-weight:bold}}
</style></head><body>
<h1>🎯 Anantapur Study Buddy</h1>
<p>Daily Current Affairs | APPSC, GROUPs, SI, Constable</p>
<p>📅 <b>{today}</b> | Live Update 6:45 AM</p>

<div class="card">
<h3>🔥 TODAY - 30 OCTOBER 2026 - FULL CURRENT AFFAIRS (15 Points)</h3>

<p><span class="tag">AP NEWS</span><br><b>1. Cyclone Arnab Effect in AP:</b> Very Severe Cyclone Arnab landfall near Narsapur (Bapatla-Vizag). 1.8 lakh people evacuated, 9 trains cancelled. Red alert in 18 districts. AP CM seeks central team for damage assessment.【1697827557125574082†L127-L131】</p>

<p><span class="tag">APPSC ALERT</span><br><b>2. APPSC Deadlines Extended:</b> APPSC Group-1, AEE, Horticulture Officer, Hostel Welfare Officer, ATWO posts last date extended to <b>Nov 9, 2026</b>. Prelims exam date same.【1697827557125574082†L28-L32】</p>

<p><span class="tag">APPSC JOBS</span><br><b>3. APPSC 196 ASO Posts:</b> Assistant Statistical Officer 196 posts - Last date Nov 2. TSPSC 102 posts window opens Oct 30.【1697827557125574082†L9-L13】</p>

<p><span class="tag">ISRO</span><br><b>4. ISRO NVS-03 Launch TODAY:</b> ISRO to launch navigation satellite NVS-03 aboard GSLV-F18 from Sriharikota today Oct 30.【1697827557125574082†L75-L78】</p>

<p><span class="tag">NATIONAL</span><br><b>5. Ladakh 100% Organic UT:</b> Ladakh declared India's first 100% Organic Union Territory on 25 Oct 2026. After Sikkim (first organic state). Useful for APPSC GS.【1697827557125574082†L156-L159】</p>

<p><span class="tag">NATIONAL SCHEME</span><br><b>6. PM Kisan 24th Installment:</b> Centre to release 24th installment today Oct 30 - 9.34 crore farmers get Rs 2000 each.【1697827557125574082†L87-L90】</p>

<p><span class="tag">YOUTH</span><br><b>7. MY Bharat Yuva Samvaad:</b> Mera Yuva Bharat conducting 'Know Your Vote' campaign across 14 States, 500 institutions (26 Oct - 5 Nov). 5,856 youth participated till Oct 28.【1697827557125574082†L187-L195】</p>

<p><span class="tag">INTERNATIONAL</span><br><b>8. UAE Honours Indian Pilot:</b> Indian pilot Smit Machchhar honoured with UAE's First Class Order of Zayed II for saving 174 passengers. India-UAE relations.【1697827557125574082†L102-L105】</p>

<p><span class="tag">WORLD</span><br><b>9. Israel Election 2026:</b> Netanyahu bloc leads with 53-54 seats, opposition led by Gadi Eisenkot - No majority (61 needed).【1697827557125574082†L80-L83】</p>

<p><span class="tag">SPORTS</span><br><b>10. India vs NZ T20:</b> 4th T20I today at Eden Park, Auckland. India leads series 3-0.【1697827557125574082†L85-L87】</p>

<p><span class="tag">SPORTS LAW</span><br><b>11. Neymar Suspended:</b> Neymar gets 2-match ban in Brazil for covering mouth while arguing - Under 'Vinícius Law'.【1697827557125574082†L83-L86】</p>

<p><span class="tag">ECONOMY</span><br><b>12. RELIEF Scheme Extended:</b> Commerce Ministry extends Component II of RELIEF Scheme till 31 Mar 2027 - Budget Rs 497 crore for exporters facing West Asia tensions.【1697827557125574082†L276-L283】</p>

<p><span class="tag">LEGAL</span><br><b>13. Bombay HC vs Meta:</b> Bombay HC rejects Meta plea to shift Rs 1000-crore Blink Digital lawsuit to California - Indian law violation can't be decided by foreign courts.【1697827557125574082†L87-L91】</p>

<p><span class="tag">EDUCATION</span><br><b>14. JMI Online Exams:</b> Jamia Millia Islamia extends virtual classes till Nov 24, end-sem exams online due to campus situation.【1697827557125574082†L92-L95】</p>

<p><span class="tag">AP RELEVANT</span><br><b>15. ITBP Recruitment:</b> ITBP announces 126 Constable posts under sports quota - Opportunity for AP athletes.【1697827557125574082†L14-L16】</p>

<hr>
<p><b>✍️ Today's Quiz:</b><br>1. Cyclone Arnab landfall location? <br>2. APPSC Group-1 new last date?<br>3. NVS-03 launch vehicle?</p>
<p><i>Comment answers - Daily PDF will be sent!</i></p>
</div>

<a class="btn" href="https://wa.me/?text=*Anantapur%20Study%20Buddy%20-%20{today}*%0A%0AFull%2015%20Current%20Affairs:%20https://rakesh445566.github.io/Anantapur-study-buddy/">📲 Share to WhatsApp Channel</a>
<br><a class="btn" style="background:#008069" href="https://wa.me/?text=Join%20Daily%20Full%20Current%20Affairs:%20https://rakesh445566.github.io/Anantapur-study-buddy/">👥 Share to Friends</a>

<p style="color:#94a3b8;margin-top:20px">Auto Updated Daily 6 AM | For Anantapur Students ❤️</p>
</body></html>
"""
with open("index.html","w",encoding="utf-8") as f:
    f.write(html)
print(f"Full 15 CA Updated for {today}")
