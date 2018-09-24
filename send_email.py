import smtplib
from email.mime.text import MIMEText

def send_email(target,data,valid,option):
    smtp_ssl_host = 'smtp-mail.outlook.com'
    smtp_ssl_port = 587
    username = 'pythontestimap@outlook.com'
    password = 'Sid@1234'
    sender = 'pythontestimap@outlook.com'
    targets = [target]

    if valid:
        if option == 'balance':
            msg = MIMEText('Hi '+data[1]+',\nyour balance is '+data[3])
        else:
            msg = MIMEText('Hi,'+data[1]+'\n please send an email with subject ending with balance..')
            
    else:
        msg = MIMEText('Hi ,\nyou are not regestered')
    msg['Subject'] = 'Hello'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP(smtp_ssl_host, smtp_ssl_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    print 'email sent to',target
    server.quit()

send_email('varma.ece007@gmail.com',['a','srikant','a','234'],True,'balance')
