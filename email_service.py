import smtplib
from email.message import  EmailMessage
import imghdr
import os


KEY = os.getenv("portfolio_password")
SENDER = "itmandjango@gmail.com"
RECEIVER = "itmanco@gmail.com"



def send_email(content, attachment):
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer")

    with open(attachment, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, KEY)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()



if __name__ == "__main__":
    send_email("Nothing", "images/100.png")