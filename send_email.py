import smtplib, os


USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
message = """
Subject: BLAH

BLAH BLAH BALH
"""

s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login(USERNAME, PASSWORD)
 
# sending the mail
s.sendmail(USERNAME, USERNAME, message)
 
# terminating the session
s.quit()
