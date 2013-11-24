import smtplib
import email
from config import settings


def alert(subject, message):
    _send([address for name, address in settings.ADMINS], subject, message)


def notify(subject, message):
    _send([address for name, address in settings.NOTIFY], subject, message)


def _send(recipients, subject, message):
    to = ", ".join(recipients)

    # Encode message
    msg = email.MIMEText.MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = settings.EMAIL_ADDY
    msg['To'] = to

    # Connect
    host = '%s:%s' % (settings.EMAIL_HOST, settings.EMAIL_PORT)
    server = smtplib.SMTP(host)
    if settings.EMAIL_STLS:
        server.starttls()
    server.login(settings.EMAIL_USER, settings.EMAIL_PASS)

    # Send
    server.sendmail(
        settings.EMAIL_ADDY,
        recipients,
        msg.as_string()
    )
    server.quit()
