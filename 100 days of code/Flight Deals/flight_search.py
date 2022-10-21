import requests
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
headers = {
    "apikey": "jcxQSqH42TCKldqEV4lBhIjeZAKE7POK",
}
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url = TEQUILA_ENDPOINT, params = params, headers = headers)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

