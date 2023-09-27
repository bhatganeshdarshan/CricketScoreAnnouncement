import time
import requests
import pyttsx3
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY=os.getenv("API_KEY")

engine = pyttsx3.init()

def get_live_data():
    api_url = f'https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0'
    response = requests.get(api_url)
    data = response.json()
    return data

def announce_match_status():
    live_matches = get_live_data()
    for match in live_matches['data']:
        teams = match.get('teams', [])
        for team in teams:
            if 'India' in team:
                innings = match.get('score', [])
                for inning in innings:
                    r = inning.get('r', '')
                    w = inning.get('w', '')
                    o = inning.get('o', '')
                    inning_name = inning.get('inning', '')

                    if "India" in inning_name:
                        announcement = f"In the match between {', '.join(teams)}, {team} are {r} for {w} wickets at {o} overs in {inning_name}."
                        engine.say(announcement)
                        engine.runAndWait()

while True:
    announce_match_status()
    time.sleep(240)
