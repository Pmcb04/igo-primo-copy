import os
import shutil
import countries
from dotenv import load_dotenv

load_dotenv()

# Import env variables
BUILDING=os.getenv('BUILDING')
CAR=os.getenv('CAR')
DEM=os.getenv('DEM')
LANG=os.getenv('LANG')
LICENSE=os.getenv('LICENSE')
MAPS=os.getenv('MAPS')
PHONEME=os.getenv('PHONEME')
POI=os.getenv('POI')
SCHEME=os.getenv('SCHEME')
SKIN=os.getenv('SKIN')
SPEEDCAM=os.getenv('SPEEDCAM')
TMC=os.getenv('TMC')
USERDATA=os.getenv('USERDATA')
DESTINATION=os.getenv('DESTINATION')

# get the full list of paths
building = os.listdir(BUILDING)
car = os.listdir(CAR)
dem = os.listdir(DEM)
lang = os.listdir(LANG)
license = os.listdir(LICENSE)
maps = os.listdir(MAPS)
phoneme = os.listdir(PHONEME)
poi = os.listdir(POI)
scheme = os.listdir(SCHEME)
skin = os.listdir(SKIN)
speedcam = os.listdir(SPEEDCAM)
tmc = os.listdir(TMC)
userdata = os.listdir(USERDATA)

def get_all_countries():
    module = globals().get('countries', None)
    countries = []
    if module:
        countries = [value for key, value in module.__dict__.items() if not (key.startswith('__') or key.startswith('_'))]
    return countries

def get_by_country(country, list):
    return [item for item in list if country in item]

#country = COUNTRIES.VATICAN_CITY
#print(country)
#print("---------------")
#print(get_by_country(country, building))
#print(get_by_country(country, maps))
#print(get_by_country(country, phoneme))
#print(get_by_country(country, poi))
#print(get_by_country(country, speedcam))
#print(get_by_country(country, tmc))