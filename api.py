import requests
from dotenv import load_dotenv 
import os 

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")

HEADERS = {
    "X-Riot-Token": API_KEY,
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com"
}


def getWeeklyChamps():
    url = "https://na1.api.riotgames.com/lol/platform/v3/champion-rotations"
    response = requests.get(url,headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        freeChamps = data["freeChampionIds"]

        return {
            "freeChamps": freeChamps
        }
    
    else:
        print(f"couldn't get champ rotatation: {response.status_code}")
        return None
    

def getGameVersion():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    response = requests.get(url)
    if response.status_code == 200: 
        gameVersion = response.json()
        latest_version = gameVersion[0]
        return latest_version
    else:
        print(f"failed to get most recent game version: {response.status_code}")
        return None 
    

def getChampNamesFromID():
    gameVersion = getGameVersion() 
    if not gameVersion: 
        print("couldn't get game version. riot api out of date?")
        return None
    gameVersionUrl = f"http://ddragon.leagueoflegends.com/cdn/{gameVersion}/data/en_US/champion.json"
    response = requests.get(gameVersionUrl)
    if response.status_code != 200:
        print(f"failed to get champ data: {response.status_code}")
        return None
    
    champData = response.json()["data"]
    idToName = {int(details["key"]): name for name, details in champData.items()}

    champData = getWeeklyChamps()
    if not champData:
        print("couldn't retrieve champ data")
        return None 
    
    freeChampIDs = champData["freeChamps"]
    freeChampNames = [idToName.get(champID, "Unknown") for champID in freeChampIDs]
    return freeChampNames 

    
