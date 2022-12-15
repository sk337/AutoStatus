import os
import time
import requests
import re


Username = "" # Discourse Username Here
IGN = "" # Swordbattle in game name Here
bio = "Basic bio #%place%" # user %place% as a placeholder


def isReplit():
    try:
        os.environ["REPLIT_DB_URL"]
        return True
    except KeyError:
        return False

if isReplit():
    apiKey = os.getenv("apiKey") # Discourse Userapikey here
else:
    from dotenv import load_dotenv
    load_dotenv()
    apiKey = os.getenv("apiKey")

while True:
    req = requests.get(f"https://swordbattle.io/{IGN}")
    place = re.findall('#.*all', req.text)[0].split(" ")[0].replace("#", '')
    fullBio = bio.replace('%place%', place)
    print(f"setting @{Username}'s bio to \n```\n{fullBio}\n```")
    req2 = requests.put(f"https://forum.codergautam.dev/users/{Username}.json", data={"bio_raw": fullBio}, headers={"Api-Key": apiKey, "Api-Username": Username})
    obj = req2.json()
    if (obj['success']) & (obj['user']['bio_raw'] == fullBio):
        print(f"bio succuess fully changed to {fullBio}")
    time.sleep(60*5)
