import requests
from datetime import datetime

today = datetime.now()
current_date = today.strftime("%d/%m/%Y")
current_month = int(today.month)
current_year = int(today.year)
current_day = int(today.day)
if current_month + 6 > 12:
    final_month = current_month - 6
    final_year = current_year + 1
else:
    final_month = current_month + 6
final_month = str(final_month)
if len(final_month) < 2:
    final_month = f"0{final_month}"

if current_day > 28 and int(final_month) == 2:
    current_day = 28

final_date = f"{current_day}/{final_month}/{final_year}"


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/search"
headers = {
    "apikey": "jcxQSqH42TCKldqEV4lBhIjeZAKE7POK",
}
class FlightData:
    def get_flight_data(self, id):
        params = {
            "fly_from": "LON",
            "fly_to": id,
            "date_from": current_date,
            "date_to": final_date
        }

        response = requests.get(url = TEQUILA_ENDPOINT,  params = params, headers = headers)
        data = response.json()["data"]
        return data
        


