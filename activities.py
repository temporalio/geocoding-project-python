# @@@SNIPSTART python-geocode-tutorial-activity-1
from temporalio import activity


# Tells Temporal that this is an Activity
@activity.defn
async def get_api_key_from_user() -> str:
    return input("Please give your API key: ")


# Tells Temporal that this is an Activity
@activity.defn
async def get_address_from_user() -> str:
    return input("Please give an address: ")


# @@@SNIPEND

# @@@SNIPSTART python-geocode-tutorial-activity-2
import requests
from dataclasses import dataclass


@dataclass
class QueryParams:
    api_key: str
    address: str


@activity.defn
async def get_lat_long(query_params: QueryParams) -> list:
    base_url = "https://api.geoapify.com/v1/geocode/search"

    params = {"text": query_params.address, "apiKey": query_params.api_key}

    response = requests.get(base_url, params=params, timeout=1000)

    response_json = response.json()

    lat_long = response_json["features"][0]["geometry"]["coordinates"]

    return lat_long


# @@@SNIPEND
