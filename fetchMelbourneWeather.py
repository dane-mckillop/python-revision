import requests
import json

def fetch_melbourne_data(endpoint, params=None):
    base_url = "http://www.bom.gov.au/fwo/"
    url = base_url + endpoint
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    response.raise_for_status()
    
    return response.json()

# Fetching weather observations for Sydney
try:
    #Generalize nextsolution to accept cmd line input for an api
    melbourne_area = "IDV60901/IDV60901.95936.json"
    data = fetch_melbourne_data(melbourne_area)
    
    print(json.dumps(data, indent=2))
    
    if "observations" in data:
        latest = data["observations"]["data"][0]
        print(f"Temperature: {latest['air_temp']}°C")
        print(f"Humidity: {latest['rel_hum']}%")
        print(f"Wind: {latest['wind_spd_kmh']} km/h from {latest['wind_dir']}")
        
except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
except requests.exceptions.ConnectionError:
    print("Connection Error: Failed to connect to the API")
except json.JSONDecodeError:
    print("JSON Decode Error: Failed to parse the API response")
except KeyError as e:
    print(f"Data structure error: {e} not found in response")