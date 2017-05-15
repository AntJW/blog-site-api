import smtplib
from email.mime.text import MIMEText
from app import config


def send_email(sender_name, sender_email, sender_phone, sender_message):
    msg_body = """Hi!\nMessage from my website, \nSent By: {}
                  \nReturn Email:  {}\nPhone: {}\nMessage: {}
               """.format(sender_name, sender_email, sender_phone, sender_message)
    msg = MIMEText(msg_body)
    msg['Subject'] = "Blog Site Message"
    msg['From'] = config["DEFAULT"]["MAIL_DEFAULT_SENDER"]
    msg['To'] = config["DEFAULT"]["MAIL_DEFAULT_RECEIVER"]

    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login(config["DEFAULT"]["MAIL_DEFAULT_SENDER"], config["DEFAULT"]["MAIL_DEFAULT_PASSWORD"])
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
