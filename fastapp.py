from fastapi import FastAPI, status
import requests
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from models import Route

app = FastAPI()


# berlin = ['52.5160,13.3779', '52.5200,13.4050'] # Coordinates in Berlin


# @app.get("/")
# async def root():
#    return {"message": "Hello World"}


@app.get("/route", status_code=status.HTTP_200_OK)
async def city(start: str, finish: str, profil: str):
    url = 'http://localhost:8989/route'
    geolocator = Nominatim(user_agent="app")
    geo_1 = geolocator.geocode(start)
    geo_2 = geolocator.geocode(finish)
    params = {
        'point': [f"{geo_1.latitude},{geo_1.longitude}", f"{geo_2.latitude},{geo_2.longitude}"],
        'profile': profil,
        'layer': 'OpenStreetMap',
        'points_encoded': 'false'
    }

    response = requests.get(url, params=params)
    route_data = response.json()

    return route_data


