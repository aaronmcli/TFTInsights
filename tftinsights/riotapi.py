import requests
import time
import json
import os
from datetime import datetime
from .config import *
from enum import Enum


HEADERS = {"X-Riot-Token": TFT_API_KEY}
MATCH_URL = "https://americas.api.riotgames.com/tft/match/v1/matches/"
PUUID_TO_SUMMONER_URL = "https://na1.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/"
SUMMONER_TO_RANK_URL = "https://na1.api.riotgames.com/tft/league/v1/entries/by-summoner/"

RIOT_API_URL = "https://{route}.api.riotgames.com"

MATCH_URL_REGION = "/tft/match/v1/matches/{matchId}"
PUUID_TO_SUMMONER_URL_PLATFORM = "/tft/match/v1/matches/by-puuid/{puuid}/ids"

SUMMONER_TO_RANK_URL_PLATFORM = "/tft/league/v1/entries/by-summoner/{summonerId}"



WAIT_TIME = 0.9
MATCH_REGION_PREFIX = "NA1_"

def get_ranked_data_puuid ( puuid ):
    try:

        print ( f"\t🔍Getting Summoner for PUUID: {puuid}")
        # Get summonerId from puuid
        summoner_resp = requests.get(f"{PUUID_TO_SUMMONER_URL}{puuid}", headers=HEADERS)
        time.sleep(WAIT_TIME)  # Avoid hammering the API
        
        
        for key, value in summoner_resp.headers.items():
             if 'Rate-Limit' in key:
                 print(f'\t\t{key}: {value}')
                 
        if summoner_resp.status_code != 200:
            print ( "\t\t!!!failed!!!")
            return summoner_resp.status_code, None
        summoner_id = summoner_resp.json()["id"]
                         
        # Get ranked TFT info

        print ( f"\t🔍Getting Rank info for Summoner {summoner_id}...")
        rank_resp = requests.get(f"{SUMMONER_TO_RANK_URL}{summoner_id}", headers=HEADERS)
        time.sleep(WAIT_TIME) 
        
        for key, value in rank_resp.headers.items():
             if 'Rate-Limit' in key:
                 print(f'\t\t{key}: {value}')

        if rank_resp.status_code != 200:
            return rank_resp.status_code, None
             
        entries = rank_resp.json()
        for entry in entries:
            if entry.get("queueType") == "RANKED_TFT":
                return rank_resp.status_code, {
                    "tier": entry.get("tier"),
                    "rank": entry.get("rank"),
                    "leaguePoints": entry.get("leaguePoints"),
                    "wins": entry.get("wins"),
                    "losses": entry.get("losses")
                    #,"read_time": datetime.now().timestamp()
                }
    except Exception as e:
        print(f"Error fetching rank for {puuid}: {e}")
    return rank_resp.status_code, None