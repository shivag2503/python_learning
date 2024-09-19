#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

city_code = FlightSearch()
data_manager = DataManager()

destination_data = data_manager.get_destination_data()

for data in destination_data:
    if data["iataCode"] == "":
        code = city_code.get_destination_code(data["city"])
        resp = data_manager.update_iata_code(data["id"], code)
        pprint(resp.text)

updated_data = data_manager.get_destination_data()
pprint(updated_data)

# for data in google_sheet_response["prices"]:
#     city = data["city"]
#     sheet_inputs = {
#         "price": {
#             "IATA Code": city_code.get_destination_code(city)
#         }
#     }
#     resp = requests.post(SHEETY_URL, json=sheet_inputs)
#     print(resp.text)

