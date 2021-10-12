import smtplib

to = input("Enter email of the recipient: ")

content = input("Enter the content of the mail: ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mail@gmail.com', 'password')
    server.sendmail('mail@gmail.com', to, content)
    server.close()


sendEmail(to, content)
