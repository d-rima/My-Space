import requests
from datetime import datetime

today = datetime.now()
quantity = input("How many pages did you read today? ")


Token = "aslhfie29834ihuqe4wa8p342rilaewhfrap8r3489"
Username = "dallin27"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "aslhfie29834ihuqe4wa8p342rilaewhfrap8r3489",
    "username": "dallin27",
    "agreeTermsOfService": "yes",
    "notMinor": "yes" 
}

# Create a profile
# response = requests.post(url = pixela_endpoint, json = user_params)

graph_endpoint = f"{pixela_endpoint}/{Username}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Readihng Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": Token
}

# response = requests.post(url = graph_endpoint, json = graph_params, headers = headers)

pixel_endpoint = f"{graph_endpoint}/{ID}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}

response = requests.post(url = pixel_endpoint, json = pixel_params, headers = headers)
print(response.text)