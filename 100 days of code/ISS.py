import smtplib
import requests

my_latitude = 40.521893
my_longitude = -111.939102


response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_latitude = float(response.json()['iss_position']['latitude'])
iss_longitude = float(response.json()['iss_position']['longitude'])


iss_position = (iss_latitude, iss_longitude)

def send_alert():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
    subject = 'ISS'
    body = "Look up! The ISS is above you now!"
    msg = f"subject: {subject}\n\n{body} "
    server.sendmail('dallinrima@gmail.com', 'dallinrima@gmail.com', msg)

    server.quit()

def check_position():
    if abs(my_latitude - iss_position[0]) < 2 and abs(my_longitude - iss_position[1]) < 2:
        send_alert()


check_position()