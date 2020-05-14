import smtplib
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("1999arjobasu@gmail.com","ewuqwciugjrbogds")
    subject = "This is a email sent from a python program"
    body="You can too do this if you want by watching this video https://youtu.be/Bg9r_yLk7VY Thank you!"
    msg= f"Subject:{subject}\n\n{body}"
    server.sendmail("1999arjobasu@gmail.com","1999arjobasu@gmail.com",msg)
    print("EMAIL HAS BEEN SENT")
    server.quit()
send_email()
