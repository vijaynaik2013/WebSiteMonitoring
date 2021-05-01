import os
import requests
import datetime
import smtplib

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_ADDRESS = 'myemail@domain.com'
EMAIL_PASSWORD = 'mypassowrd'
initial = datetime.datetime.now()

def notify_user():
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

            subject = 'YOUR SITE IS DOWN!'
            body = 'Make sure the server restarted and it is back up'
            msg = f'Subject: {subject}\n\n{body}'

            # logging.info('Sending Email...')
            smtp.sendmail(EMAIL_ADDRESS, 'vijaynaik2013@gmail.com', msg)

try:
        r = requests.get('http://qhtpl.com:8080/', timeout=5)
        str1 = str(r.elapsed.total_seconds())
        File_object = open(r"C:\Users\myfolder\Results.txt", "a+")
        File_object.writelines("Response time:" + str1 + 'secs' + " on " \
                               + str(initial) + '\n')
        if r.status_code != 200:
            notify_user()
except Exception as e:
        notify_user()
