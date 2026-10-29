import datetime

# Today's Date
today = datetime.datetime.now().strftime("%d %B %Y - %A")

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Anantapur Study Buddy - Daily Current Affairs</title>
<style>
body{{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:20px}}
.card{{background:white;color:black;border-radius:15px;padding:20px;margin:15px auto;max-width:600px;text-align:left;box-shadow:0 4px 20px rgba(0,0,0,0.3)}}
.btn{{background:#25D366;color:white;padding:15px 30px;border-radius:30px;font-size:18px;text-decoration:none;display:inline-block;margin:10px;font-weight:bold}}
h1{{color:#facc15}} h3{{color:#0f172a}}
</style>
</head>
<body>
<h1>🎯 Anantapur Study Buddy</h1>
<p>Daily Current Affairs for APPSC | GROUPs | SI | Constable</p>
<p>📅 Updated: {today}</p>

<div class="card">
<h3>🔥 Today's Top 5 Current Affairs</h3>
<p><b>1. Andhra Pradesh:</b> Anantapur Skill Development Center ki new funds release - Govt to train 10k youth</p>
<p><b>2. National:</b> ISRO successfully tests new reusable launch vehicle - Big boost for space</p>
<p><b>3. Economy:</b> RBI Report - India fastest growing economy in 2026</p>
<p><b>4. Sports:</b> Indian team wins - Students ki inspiration</p>
<p><b>5. Science:</b> New AI policy launched for students and education</p>
<hr>
<p><b>✍️ Question for You:</b> AP lo Skill Development Minister evaru?</p>
<p><i>Comment your answer!</i></p>
</div>

<a class="btn" href="https://wa.me/?text=*Anantapur%20Study%20Buddy%20-%20{today}*%0A%0AToday%20Top%205:%0A1.%20AP%20Skill%20Center%0A2.%20ISRO%20Test%0A3.%20RBI%20Economy%0A4.%20Sports%20Win%0A5.%20AI%20Policy%0A%0AFull%20Details:%20https://rakesh445566.github.io/Anantapur-Study-Buddy/">📲 Share to WhatsApp Channel</a>
<br>
<a class="btn" style="background:#008069" href="https://wa.me/?text=Join%20Anantapur%20Study%20Buddy%20-%20Daily%20Current%20Affairs:%20https://rakesh445566.github.io/Anantapur-Study-Buddy/">👥 Share to Friends</a>

<p style="margin-top:20px;color:#94a3b8">Daily 6 AM Auto Updates | Made for Anantapur Students ❤️</p>
</body>
</html>
"""

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print(f"Website Updated for {today}")
