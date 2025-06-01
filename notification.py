import smtplib
from email.mime.text import MIMEText
import logging

def send_email(subject, body, to_email="aynur.mustafayeva@euruni.edu"):
    sender = "mustafayevaaynur26@gmail.com"
    app_password = "aximdatvtddeooxb"  # Replace with your Gmail app password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, app_password)
            server.send_message(msg)
        logging.info("📧 Alert email sent.")
    except Exception as e:
        logging.error(f"❌ Failed to send email: {e}")
