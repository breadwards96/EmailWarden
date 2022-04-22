import Crypto
import ssl
import smtplib

def email_alert_test():
    # port = 0  # SSL port
    enc_pass = b'gAAAAABiYWuPXXRr-IuPx-ubIXZlmv7G12JamFJQtwjnhub4c7bBA50aWrBwNvE_yBx0x-yNxlbkO1Z4lCLJ1pUW1dECenu1iA=='

    try:
        enc_file = open(r'C:\Users\bedwards\PycharmProjects\EmailWarden\venv\key.txt')
        key = enc_file.read()
        enc_file.close()
        password = Crypto.decrypt(enc_pass, key)
    except FileNotFoundError:
        try:
            enc_file = open("key.txt")
            key = enc_file.read()
            enc_file.close()
            password = Crypto.decrypt(enc_pass, key)
        except FileNotFoundError:
            print("Key file not found")
            password = ""

    smtp_server = "smtp.gmail.com"
    sender_email = "HFFErrorAlert@gmail.com"
    reciever_email = "bedwards@hickmanseggs.com"
    message = "Testing External Email Alert System. Disregard"

    # Create SSL Context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, context=context) as server:
        server.login("HFFErrorAlert@gmail.com", password.decode())
        server.sendmail(sender_email, reciever_email, message)