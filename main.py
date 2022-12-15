import os
import time
import requests
import re

Username = "ipaddy" # Discourse Username Here
IGN = "ip" # Swordbattle in game name Here
bio = "Test bio #%place%" # user %place% as a placeholder

def isReplit():
    try:
        os.environ["REPLIT_DB_URL"]
        return True
    except KeyError:
        return False

if isReplit():
    # import server W.I.P.
    os.getenv("apiKey") # Discourse Userapikey here
else:
    from dotenv import load_dotenv
    load_dotenv()
    os.getenv("apiKey")



#while True:
if True:
    req = requests.get(f"https://swordbattle.io/{IGN}")
    place= re.findall('#.*all', req.text)[0].split(" ")[0].replace("#", '')
    fullBio = bio.replace('%place%', place)
    print(f"setting @{Username}'s bio to \n```\n{fullBio}\n```")
    # time.sleep(60*5)
    # exit()
