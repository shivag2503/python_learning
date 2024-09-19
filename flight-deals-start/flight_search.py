import requests

API_KEY = ""
API_SECRET = ""
TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
IASA_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

class FlightSearch:

    def __init__(self):
        self.api_key = API_KEY
        self.api_secret = API_SECRET
        self.token = self.get_api_token()

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self.token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        flight_response = requests.get(IASA_URL, params=query, headers=headers)
        print(flight_response.json())
        code = flight_response.json()["data"][0]["iataCode"]
        return code

    def get_api_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        resp = requests.post(TOKEN_URL, headers=header, data=body)
        print(resp.json())
        return resp.json()["access_token"]
