import smtplib
import datetime as dt
import random

now = dt.datetime.now()
current_month = now.month
current_day = now.day

people = []

class person:
    def __init__(self, name, month, day, email):
        self.name = name
        self.month = month
        self.day = day
        self.email = email


people.append(person("Doug", 8, 21, 'broncos54321@gmail.com'))
people.append(person("Chris", 8, 22, 'broncos54321@gmail.com'))
people.append(person("Paul", 8, 23, 'broncos54321@gmail.com'))


def send_mail(directory):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
    subject = 'Your special day!'
    body = f'{random.choice(messages)}'
    msg = f"Subject: {subject}\n\n{body} "
    server.sendmail(
        'dallinrima@gmail.com',
        directory,
        msg
    )
    
    server.quit()

for human in people:
    if human.month == current_month and human.day == current_day:
        messages = [f"Happy Birthday {human.name}!", "Another year older!", f"Have an amazing day! Happy Birthday {human.name}!"]
        directory = human.email
        send_mail(directory)
