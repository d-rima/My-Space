

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_mail(self, destinations, directory):
        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('dallinrima@gmail.com', 'vssmrbtsppxqznxs')
        subject = 'Cheap Flights!'
        body = f'There are cheap flights to {destinations}! Book NOW!'
        msg = f"Subject: {subject}\n\n{body} "
        server.sendmail(
            'dallinrima@gmail.com',
            directory,
            msg
        )
        
        server.quit()