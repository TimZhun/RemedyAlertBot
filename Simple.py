#! python
import smtplib
import ssl
import sys
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_config(file_path="config.json"):
    with open(file_path, "r") as config_file:
        config = json.load(config_file)
    return config

def send_email(subject, body):
    config = load_config()

    sender_email = config["sender_email"]
    sender_password = config["sender_password"]
    recipient_email = 'z.a.timur@gmail.com'

    # Set up text
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    
    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Set up the connection
    port = 465  # For SSL
    smtp_server = 'mail.telecom.kz'
    
    try:
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            # Log in to the email account
            server.login(sender_email, sender_password)
            
            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
        print(sender_email, recipient_email, message.as_string())    
        print("Email sent successfully.")
    
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <event_description>")
        sys.exit(1)

    event_description = sys.argv[1]

    print(event_description)
    send_email("Event Notification", event_description)
