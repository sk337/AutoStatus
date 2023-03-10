import os
import time
import requests
import re
import json

file=open("config.json", "r")
config = json.load(file)
file.close()

Username = config['username']
IGN = config['ign']
bio = config['bio']

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
            print(f"{time.ctime()}: bio changed to")
        else:
            print(f"{time.ctime()}: Failed to set bio")
            print(obj)
    except:
        print(obj)
    time.sleep(60*5)
