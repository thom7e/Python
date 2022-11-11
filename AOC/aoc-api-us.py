import requests
import json
from datetime import datetime
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import schedule
import time


## Create a .txt file with pw for your SMTP, your Cookie from AOC and your Mail and change the path
with open("PATHTOTHETXTFILE") as f:
    dates = f.read().splitlines()

pw = dates[0]
cooky = dates[1]
mail = dates[2]

print("logging in")
#cookies
cookie = {"session":f"{cooky}"}

## HERE YOU HAVE TO CHANGE THE URL TO YOUR JSON DATA
url = "https://adventofcode.com/2021/leaderboard/private/view/blablabla.json"
r = requests.get(url,cookies=cookie)

def data_converting(url, cookie):
    content = r.content
    table = json.loads(content)


    return table

table = data_converting(url,cookie)

## PARSING
todays_date = int(datetime.today().strftime("%d"))
start = datetime(2021, 12, int(f"{todays_date}"), 6, 0, 0)
results=[]
print("get members")
for member in table["members"]:
    name = table["members"][f"{member}"]["name"]
    stars = table["members"][f"{member}"]["local_score"]

    ## Check if only Part I, both Parts or no Parts
    try:
        try:
            part1_time = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["1"]["get_star_ts"]).strftime('%H:%M')
            part2_time = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["2"]["get_star_ts"]).strftime('%H:%M')
            part1 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["1"]["get_star_ts"])
            part2 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["2"]["get_star_ts"])
            part1_and_2 = str(f"{name} took until PART I {part1_time} for PART I today, so {part1 - start} [hh:mm:ss]. For PART II took until {part2_time}, so {part2 - part1} [hh:mm:ss]. New Score: {stars} Stars")
            results.append(part1_and_2)
        except KeyError:
            try:
                part1_time = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["1"]["get_star_ts"]).strftime('%H:%M')
                part1 = datetime.fromtimestamp(table["members"][f"{member}"]["completion_day_level"][f"{todays_date}"]["1"]["get_star_ts"])
                only_part1 = str(f"{name} got only PART I and took until {part1_time}, so {part1 - start} [hh:mm:ss]. New Score: {stars} Stars")
                results.append(only_part1)
            except KeyError:
                no_part = str(f"{name} didn't get any Part last day. Old Score: {stars} Sterne")
                results.append(no_part)


    except KeyError:
        continue

print("sending mails to subscribers")

def send_mail():
    ## Create a .txt file with pw for your Subscribers with YOUR SMTP MAIL in the first line and change the path
    with open("PATH TO SUBSCRIBERS") as subs:
        subscriberz = subs.read().splitlines()

### CHANGE THE LINK TO YOUR OWN SCOREBOARD
    html = """\
    <html>
      <body>
        <p><b>Python Mail Test</b><br>
           Peace !<br><br>
           What's up?<br><br>
           Yesterday's Scores: <br><br>
           $code <br><br>
           The total Overview and Scoreboard u can find here: <br>
           <a href="YOUR SCOREBOARDLINK">Leaderbord</a> 
           <br><br>
           Greetings
        </p>
      </body>
    </html>
    """

    result = "<br><br>".join(results)

    s = Template(html).safe_substitute(code=f"{result}")
    part = MIMEText(s, "html")
    port = 465  # For SSL
    login = str(f"{subscriberz[0]}")
    password = str(pw)
    context = ssl.create_default_context()
    heute = datetime.today().strftime("%d.%m.%y")
    msg = MIMEMultipart()
    msg['From'] = f"{mail}"
    msg['Subject'] = f"Results Advent of Code from  {heute}"
    msg.attach(part)

    for sub in subscriberz:
        with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
            server.login(login,password)
            server.sendmail(f"{subscriberz[0]}",f"{sub}",msg.as_string())
            server.quit()

send_mail()
print("mails have been sent")

schedule.every().day.at("23:58").do(lambda: send_mail())
# planunterlage(source,destination)

while True:
    schedule.run_pending()
    time.sleep(1)