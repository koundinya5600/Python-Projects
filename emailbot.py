import smtplib
server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#here you have to enter you mailid and password
server.login('username@gmail.com','password')
#here your mail is required and the receiver mail along with message you want to send
server.sendmail('yourmail@gmail.com',
                'receivermailid@gmail.com',
                'Message to be sent'
                )