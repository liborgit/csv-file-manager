import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, body, to_email, from_email, password, attachment_file):
    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    attachment = open(attachment_file, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename(attachment_file)}")

    msg.attach(part)

    # Connect to the SMTP server

    server = smtplib.SMTP("smtp.seznam.cz", 587)  # Connect to the Seznam SMTP server using port 587
    # NOTE: Adjust the SMTP server address ("smtp.seznam.cz") and port (587) if using a different email provider.

    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

    print(f"Email sent to {to_email} with attachment {attachment_file}")

# Usage example
send_email(
    subject="Merged CSV Report",  # Subject of the email
    body="Please find the attached merged CSV file.",  # Body of the email
    to_email="recipient@example.com",  # Replace with the recipient's email address
    from_email="sender@example.com",  # Replace with the sender's email address
    password="example_password",  # Replace with the sender's email password
    attachment_file="merged-datablist.csv"  # The file you want to attach
)