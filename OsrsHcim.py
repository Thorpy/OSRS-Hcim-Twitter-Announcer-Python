import requests
import json
import schedule
import time
from twython import Twython
from deepdiff import DeepDiff

APP_KEY = 'REMOVED'  # Customer Key here
APP_SECRET = 'REMOVED'  # Customer secret here
OAUTH_TOKEN = 'REMOVED'  # Access Token here
OAUTH_TOKEN_SECRET = 'REMOVED'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

bossname = ""
number = 0

urlStart = "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/ranking.json?table="
urlBoss = ["12","13","14","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58"]
urlFinish = "&category=1&size=10"
messagelist = []

def GrabList(boss):
    global number
    global messagelist
    global bossname
    print("Grabbing " + bossname + " hcim hiscores")
    file = (str(boss) + ".json")
    previousinfo = json.loads(open(file).read())
    url = (urlStart + str(boss) + urlFinish)
    info = requests.get(url).json()
    with open(file, "w") as myfile:
        myfile.write(json.dumps(info, indent=4,))
    changes = DeepDiff(previousinfo, info, ignore_order=True, view='tree')
    set_of_values_changed = changes['values_changed']
    number = 0
    for i in set_of_values_changed:
        try:
            changed=list(set_of_values_changed)[number]
            #oldscore = changed.t1
            #newscore = changed.t2
            #newscore = newscore.replace(',', '')
            #oldscore = oldscore.replace(',', '')
            name = changed.up.t1
            newrank = changed.up.t2["rank"]
            newname = (name['name'])
            oldrank = (name['rank'])
            #scorediff = (int(newscore) - int(oldscore))
            time.sleep(5)
            if (int(oldrank) > int(newrank)):
                time.sleep(2)
                message = ("Congrats to " + str(newname) + " who was promoted from Rank: " + str(oldrank) + " to Rank: " + str(newrank) + " at " + bossname)
                if message not in messagelist:
                    messagelist.append(message)
                    message = ""
                    number = (number + 1)
        except Exception as e:
            print(e)
            message = ""
            number = 0


def Takeinfo():
    print("Connecting to hcim hiscores\n")
    global bossname
    global messagelist
    for boss1 in urlBoss:
        if boss1 == "12":
            bossname = "Abyssal Sire"
        if boss1 == "13":
            bossname = "Alchemical Hydra"
        if boss1 == "14":
            bossname = "Barrows Chests"
        if boss1 == "15":
            bossname = "Bryophyta"
        if boss1 == "16":
            bossname = "Callisto"
        if boss1 == "17":
            bossname = "Cerberus"
        if boss1 == "18":
            bossname = "Chambers of Xeric"
        if boss1 == "19":
            bossname = "Chambers of Xeric: Challenge Mode"
        if boss1 == "20":
            bossname = "Chaos Elemental"
        if boss1 == "21":
            bossname = "Chaos Fanatic"
        if boss1 == "22":
            bossname = "Commander Zilyana"
        if boss1 == "23":
            bossname = "Corporeal Beast"
        if boss1 == "24":
            bossname = "Crazy Archaeologist"
        if boss1 == "25":
            bossname = "Dagannoth Prime"
        if boss1 == "26":
            bossname = "Dagannoth Rex"
        if boss1 == "27":
            bossname = "Dagannoth Supreme"
        if boss1 == "28":
            bossname = "Deranged Archaeologist"
        if boss1 == "29":
            bossname = "General Graardor"
        if boss1 == "30":
            bossname = "Giant Mole"
        if boss1 == "31":
            bossname = "Grotesque Guardians"
        if boss1 == "32":
            bossname = "Hespori"
        if boss1 == "33":
            bossname = "Kalphite Queen"
        if boss1 == "34":
            bossname = "King Black Dragon"
        if boss1 == "35":
            bossname = "Kraken"
        if boss1 == "36":
            bossname = "Kree'Arra"
        if boss1 == "37":
            bossname = "K'ril Tsutsaroth"
        if boss1 == "38":
            bossname = "Mimic"
        if boss1 == "39":
            bossname = "Nightmare"
        if boss1 == "40":
            bossname = "Phosani's Nightmare"
        if boss1 == "41":
            bossname = "Obor"
        if boss1 == "42":
            bossname = "Sarachnis"
        if boss1 == "43":
            bossname = "Scorpia"
        if boss1 == "44":
            bossname = "Skotizo"
        if boss1 == "45":
            bossname = "Tempoross"
        if boss1 == "46":
            bossname = "The Gauntlet"
        if boss1 == "47":
            bossname = "The Corrupted Gauntlet"
        if boss1 == "48":
            bossname = "Theatre of Blood"
        if boss1 == "49":
            bossname = "Theatre of Blood: Hard Mode"
        if boss1 == "50":
            bossname = "Thermonuclear Smoke Devil"
        if boss1 == "51":
            bossname = "TzKal-Zuk"
        if boss1 == "52":
            bossname = "TzTok-Jad"
        if boss1 == "53":
            bossname = "Venenatis"
        if boss1 == "54":
            bossname = "Vet'ion"
        if boss1 == "55":
            bossname = "Vorkath"
        if boss1 == "56":
            bossname = "Wintertodt"
        if boss1 == "57":
            bossname = "Zalcano"
        if boss1 == "58":
            bossname = "Zulrah"
        try:
            GrabList(int(boss1))
        except Exception as e:
            print(e)
            print(bossname + " has not changed info")
            print()
    twittermessage = "\n\n".join(messagelist)
    try:
        if twittermessage != "":
            if messagelist != "":
                if len(messagelist) < 3:
                    time.sleep(5)
                    twitter.update_status(status=twittermessage)
                    messagelist = []
                    twittermessage = ""
                else:
                    time.sleep(5)
                    twittermessage = "\n\n".join(messagelist[:3])
                    twitter.update_status(status=twittermessage)
                    time.sleep(5)
                    twittermessage = "\n\n".join(messagelist[3:])
                    if twittermessage != "":
                        twitter.update_status(status=twittermessage)
                    messagelist = []
                    twittermessage = ""
    except Exception as e:
        print(e)
        messagelist = []
        twittermessage = ""

Takeinfo()
schedule.every(10).minutes.do(Takeinfo) # Start the whole process again every minute

while 1:
    schedule.run_pending()  # Keep things looping
    time.sleep(3)
