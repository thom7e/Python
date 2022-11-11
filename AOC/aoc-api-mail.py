import requests
import json
from datetime import datetime
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template


with open("C:\\Users\\thoma\\OneDrive\\Python\\daten.txt") as f:
    dates = f.read().splitlines()
pw = dates[0]
cooky = dates[1]
mail = dates[2]


#cookies
cookie = {"session":f"{cooky}"}
url = "https://adventofcode.com/2021/leaderboard/private/view/1061043.json"
r = requests.get(url,cookies=cookie)
def data_converting(url, cookie):
    content = r.content
    table = json.loads(content)


    return table

table = data_converting(url,cookie)

## PARSING
heutiger_tag = int(datetime.today().strftime("%d"))
start = datetime(2021, 12, int(f"{heutiger_tag}"), 6, 0, 0)
results=[]
for member in table["members"]:
    name = table["members"][f"{member}"]["name"]
    stars = table["members"][f"{member}"]["local_score"]

    ## Check if only Part I, both Parts or no Parts
    try:
        try:
            part1_uhr = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["1"]["get_star_ts"]).strftime('%H:%M')
            part2_uhr = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["2"]["get_star_ts"]).strftime('%H:%M')
            part1 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["1"]["get_star_ts"])
            part2 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["2"]["get_star_ts"])
            print(f"{name} hat heute für PART I bis {part1_uhr} Uhr gebraucht, also {part1 - start} [hh:mm:ss] , und für PART II bis {part2_uhr} Uhr, also {part2 - part1} [hh:mm:ss]. Neue Punktzahl: {stars} Sterne")
            part1_und_2 = str(f"{name} hat heute für PART I bis {part1_uhr} Uhr gebraucht, also {part1 - start} [hh:mm:ss] , und für PART II bis {part2_uhr} Uhr, also {part2 - part1} [hh:mm:ss]. Neue Punktzahl: {stars} Sterne")
            results.append(part1_und_2)
        except KeyError:
            try:
                part1_uhr = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["1"]["get_star_ts"]).strftime('%H:%M')
                part1 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{heutiger_tag}"]["1"]["get_star_ts"])
                print(f"{name} hat heute nur PART I geschafft und bis {part1_uhr} Uhr gebraucht, also {part1 - start} [hh:mm:ss]Neue Punktzahl: {stars} Sterne")
                only_part1 = str(f"{name} hat heute nur PART I geschafft und bis {part1_uhr} Uhr gebraucht, also {part1 - start} [hh:mm:ss]Neue Punktzahl: {stars} Sterne")
                results.append(only_part1)
            except KeyError:
                print(f"{name} hat heute keinen Part geschafft und hat jetzt somit insgesamt {stars} Sterne")
                no_part = str(f"{name} hat heute keinen Part geschafft und hat jetzt somit insgesamt {stars} Sterne")
                results.append(no_part)


    except KeyError:
        print(f"{name} hat heute keinen Part gschafft")

html = """\
<html>
  <body>
    <p><b>Python Mail Test</b><br>
       Servus Codler!<br><br>
       was macht die Kunst?<br>
       Folgendes gibt es heute zu berichten: <br>
       $code <br><br>
       Die Übersicht über das Tableu findet ihr hier: <br>
       <a href="https://adventofcode.com/2021/leaderboard/private/view/1061043">Leaderbord</a> 
       <br><br>
       Liebe Grüße thom7e
    </p>
  </body>
</html>
"""

result = "<br><br>".join(results)

s = Template(html).safe_substitute(code=f"{result}")
part = MIMEText(s, "html")
print(s)

port = 465  # For SSL
login = "thomas.kurfiss@gmail.com"
password = str(pw)
context = ssl.create_default_context()
heute = datetime.today().strftime("%d.%m.%y")
msg = MIMEMultipart()
msg['From'] = "thomas.kurfiss@gmail.com"
msg['To'] = "thomas.kurfiss@gmail.com"
msg['Subject'] = f"Ergebnisse Advent of Code vom {heute}"
msg.attach(part)
with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(login,password)
    server.sendmail("thomas.kurfiss@gmail.com","thomas.kurfiss@gmail.com",msg.as_string())
    server.quit()


