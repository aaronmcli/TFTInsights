from enum import Enum

DATA_DRAGON_VERSION = '15.9.1'
UNIT_PREFIX = "unit_TFT14_"
CURRENT_SET_NAME = "TFTSet14"
CURRENT_SET_PREFOX = "TFT14_"
TFT_API_KEY = "" #please get your own

#TFT-LEAGUE-V1
#https://developer.riotgames.com/apis#tft-league-v1
TFT_RANK_LEAGUE_PUUID_PLATFORM       = "/tft/league/v1/by-puuid/{puuid}"   #Get league entries in all queues for a given puuid
TFT_CHALLENGER_LEAGUE_PLATFORM       = "/tft/league/v1/challenger" #Get the challenger league
TFT_LEAGUE_BY_SUMMONER_ID_PLATFORM   = "/tft/league/v1/entries/by-summoner/{summonerId}"
TFT_LEAGUE_BY_TIER_DIVISION_PLATFORM = "/tft/league/v1/entries/{tier}/{division}"
TFT_GRANDMASTER_LEAGUE_PLATFORM      = "/tft/league/v1/grandmaster"
TFT_ASTER_LEAGUE_PLATFORM            = "/tft/league/v1/master"
TFT_QUEUE_TOP_PLATFORM               = "/tft/league/v1/rated-ladders/{queue}/top" #ONLY FOR RANKED_TFT_TURBO
TFT_LEAGUE_ID_PLATFORM               = "/tft/league/v1/leagues/{leagueId}" #UNAVAIABLE 

class PlatformRouting(Enum):
    BR1 = "br1"       # Brazil
    EUN1 = "eun1"     # Europe Nordic & East
    EUW1 = "euw1"     # Europe West
    JP1 = "jp1"       # Japan
    KR = "kr"         # Korea
    LA1 = "la1"       # Latin America North
    LA2 = "la2"       # Latin America South
    NA1 = "na1"       # North America
    OC1 = "oc1"       # Oceania
    PH2 = "ph2"       # Philippines
    RU = "ru"         # Russia
    SG2 = "sg2"       # Singapore
    TH2 = "th2"       # Thailand
    TR1 = "tr1"       # Turkey
    TW2 = "tw2"       # Taiwan
    VN2 = "vn2"       # Vietnam

class RegionalRouting(Enum):
    AMERICAS = "americas"
    ASIA = "asia"
    EUROPE = "europe"
    SEA = "sea"

class RankedTier(Enum):
    IRON = "Iron"
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"
    EMERALD = "Emerald"
    DIAMOND = "Diamond"
    MASTER = "Master"
    GRANDMASTER = "Grandmaster"
    CHALLENGER = "Challenger"

class RankedDivision(Enum):
    IV = "IV"
    III = "III"
    II = "II"
    I = "I"