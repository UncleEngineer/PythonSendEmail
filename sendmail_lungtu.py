import smtplib


'''
-------------------------
ตั้งค่าให้เป็นสีเขียวก่อนส่ง แล้วลองรีเฟรชดู ( on )
https://myaccount.google.com/lesssecureapps

'''

def send_email(mailto,subject,msg):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()

		sender_email = 'loong.wissawakorn@gmail.com'
		sender_password = 'abc123456'

		server.login(sender_email,sender_password)
		message = 'Subject: {}\n\n{}'.format(subject,msg)
		server.sendmail(sender_email,mailto,message)
		server.quit()
		print('Success: Email sent')
	except:
		print('Email failed to send' )


###########Start sending#############

subject = 'Hello Lungtu Krub'
msg = '''Hello lungtu Krub
Pom Yung Maidai 5000 Bath
Oon hai pom duai
'''
send_email('loong.wissawakorn@gmail.com',subject,msg)
#send_email('Lungtu@gamil.com',subject,msg)