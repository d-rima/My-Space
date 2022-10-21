#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
import requests

data_manager = DataManager()
sheet_data = data_manager.get_flight_data()
user_info = data_manager.get_user_info()

new_profile = input("would you like to add a new user? (Type 'y or 'n'): ")
if new_profile == "y":
    data_manager.add_user()


if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_info = sheet_data
data_manager.update_travel_info()


cheap_flights = []
from flight_data import FlightData
flight_data = FlightData()

for row in sheet_data:
    data = flight_data.get_flight_data(row["iataCode"])
    for flight in data:
            if int(flight["price"]) < int(row["lowestPrice"]) and row["city"] not in cheap_flights:
                cheap_flights.append(row["city"])

from notification_manager import NotificationManager

notification_manager = NotificationManager()

for user in user_info:
    directory = user["email"]
    notification_manager.send_mail(cheap_flights, directory)
