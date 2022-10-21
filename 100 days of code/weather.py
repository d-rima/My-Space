import requests
import smtplib

city= "Riverton"
state_code = 'UT'
country_code = 'USA'
key = "1364c740e2a6f3e912c3ddd077adc318"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"

weather_params = {
    "lat": 43.025,
    "lon": -108.3799,
    "appid": key,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
data = response.json()["weather"][0]["id"]

print(data)

def send_message():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
    subject = "Rain"
    body = "Bring an umbrella, it's raining!"
    msg = f"subject: {subject}\n\n{body} "
    server.sendmail('dallinrima@gmail.com', 'dallinrima@gmail.com', msg)


if int(data) < 700:
    send_message()


