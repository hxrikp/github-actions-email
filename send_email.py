import smtplib, ssl, os

port = 465
smtp_server = "smtp.gmail.com"
# USERNAME = os.environ.get('USER_EMAIL')
# PASSWORD = os.environ.get('USER_PASSWORD')
USERNAME = "hahatester10@gmail.com"
PASSWORD = "Tester#1234"
message = """
Subject: BLAH

BLAH BLAH BALH
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, USERNAME, message)