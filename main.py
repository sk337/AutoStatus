import os
import time
import requests
import re


Username = "" # Discourse Username Here
IGN = "" # Swordbattle in game name Here
bio = "Basic bio 3%place%" # user %place% as a placeholder


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
    req2 = requests.put(f"https://forum.codergautam.dev/users/{Username}.json", data={"bio_raw": fullBio}, headers={"Api-Key": apiKey, "Api-Username": Username})
    obj = req2.json()
    try:
        if (obj['success']):
            print(f"bio succuess fully changed to {fullBio}")
        else:
            print("Failed to set bio")
            print(obj)
    except:
        print(obj)
    time.sleep(60*5)