import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("RAWG_API_KEY")
BASE_URL = "https://api.rawg.io/api"

# Function to output recommendations based on a game name or keyword
def keyword(query):
    url = f"{BASE_URL}/games"
    parameters = {
        "key": API_KEY,
        "search": query,
        "page_size": 5
    }

    # Make a GET request to the RAWG API    
    response = requests.get(url, params=parameters)
    data = response.json()

    # Return the list of recommended games
    return data.get("results", [])

# Function to get details for a game using a game ID
def game_details(game_id):
    url = f"{BASE_URL}/games/{game_id}"
    parameters = {
        "key": API_KEY
    }

    # Make a GET request to the RAWG API
    response = requests.get(url, params=parameters)
    data = response.json()

    # Return the game details
    return data