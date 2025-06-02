import smtplib
import ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

to_email = os.getenv("TO_EMAIL")
from_email = os.getenv("EMAIL_SENDER")
password = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body, to_email=to_email):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(from_email, password)
            smtp.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", e)

if __name__ == "__main__":
    send_email("🚨 Test Alert", "This is a manual test from notification.py")
