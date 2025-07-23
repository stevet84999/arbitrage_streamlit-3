import requests
from config import API_KEY

def fetch_odds(sports, bookmakers, regions, markets):
    all_odds = {}
    for sport in sports:
        url = f"https://api.the-odds-api.com/v4/sports/{sport}/odds"
        params = {
            "apiKey": API_KEY,
            "regions": regions,
            "markets": markets,
            "bookmakers": ",".join(bookmakers)
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            all_odds[sport] = response.json()
        else:
            print(f"Failed to fetch odds for {sport}: {response.text}")
    return all_odds
