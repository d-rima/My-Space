import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_info = {}

    def get_flight_data(self):
        sheety_endpoint = "https://api.sheety.co/6166e2341348334d3e022a68b184e968/prices/prices"
        response = requests.get(sheety_endpoint)
        data = response.json()
        self.destination_info = data["prices"]
        return self.destination_info

    def update_travel_info(self):
        sheety_endpoint = "https://api.sheety.co/6166e2341348334d3e022a68b184e968/prices/prices"
        for city in self.destination_info:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            link = f"{sheety_endpoint}/{city['id']}"
            response = requests.put(url = link, json = new_data)

    def add_user(self):
        sheety_endpoint = "https://api.sheety.co/6166e2341348334d3e022a68b184e968/prices/users"
        first_name = input("What is your first name? ")
        last_name = input("What is your last name? ")
        email_address = input("What is your email address? ")
        confirm_email = input("Confirm your email address: ")
        if email_address == confirm_email:
            new_data = {
                "user": {
                    "firstName": first_name,
                    "lastName": last_name,
                    "email": email_address,
                }
            }
            response = requests.post(url = sheety_endpoint, json = new_data)

    def get_user_info(self):
        sheety_endpoint = "https://api.sheety.co/6166e2341348334d3e022a68b184e968/prices/users"
        response = requests.get(sheety_endpoint)
        data = response.json()
        self.user_info = data["users"]
        return self.user_info