import requests
from pprint import pprint

SHEETY_URL = "https://api.sheety.co/693cc7545208d3adb511003814c02560/flightDeals/prices"

# google_headers = {
#     "Authorization": ""
# }


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        google_sheet_response = requests.get(SHEETY_URL)
        data = google_sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_code(self, fid, code):
        body = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(SHEETY_URL + "/" + str(fid), json=body)
        return response
