import smtplib
import imghdr
from email.message import EmailMessage
import pickle
import colorama
import getpass 
import sys
user = input(f"{colorama.Fore.RED}Enter your mail address : {colorama.Fore.LIGHTWHITE_EX}")
password = getpass.getpass(f"{colorama.Fore.RED}Enter the application password(Not the account password) : ")
try :
	f = open("mail.txt","rb")
	sendto = pickle.load(f)
	f.close()
except :
	sendto = []
	f = open('mail.txt',"wb")
	pickle.dump(sendto,f)
	f.close()

def addinlist(sendto):
	while True :
		try :
			mail = input(f"{colorama.Fore.GREEN}Enter mail address : {colorama.Fore.LIGHTWHITE_EX}")
		except KeyboardInterrupt :
			break
		if mail != "":
			if mail in sendto :
				pass
			else :
				sendto.append(mail)
		else :
			break
	return sendto
add_mail_to_list = input(f"{colorama.Fore.GREEN}Do you want to add a new mail to the list [Y/n] :{colorama.Fore.LIGHTWHITE_EX}")
if add_mail_to_list == 'y' or add_mail_to_list == 'Y' :
	newsendto = addinlist(sendto)
	sendto = newsendto
	print(sendto)
	f = open("mail.txt","wb")
	pickle.dump(sendto,f)
	f.close()
else :
	if sendto == []:
		sys.exit()
	pass
contacts = list(sendto)
msg = EmailMessage()
try :
	Subjectmail = input(f"{colorama.Fore.GREEN}Enter the subject of the message : {colorama.Fore.LIGHTWHITE_EX}")
	Frommail = input(f"{colorama.Fore.GREEN}Enter the sender's name : {colorama.Fore.LIGHTWHITE_EX}")
	file_send_path = input(f"{colorama.Fore.GREEN}Enter the file path, if any : {colorama.Fore.LIGHTWHITE_EX}")
	msgtext = input(f"{colorama.Fore.GREEN}Enter the text of the message : {colorama.Fore.LIGHTWHITE_EX}")
except KeyboardInterrupt :
	exit()
msg['Subject'] = Subjectmail
msg['From'] = Frommail
msg['To'] = contacts
msg.set_content(f'Peace, mercy and blessings of God : ')
if file_send_path != "":
	try :
		f = open(file_send_path,"rb")
		file_data = f.read()
		fname = f.name
	except FileNotFoundError :
		file_send_path = ""
		print(f"{colorama.Fore.RED}This file cannot be found, the message will be sent without it{colorama.Fore.GREEN}")
msg.add_alternative(f"""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:Verydark;">{msgtext}</h1>
    </body>
</html>
""", subtype='html')
if file_send_path != "":
	msg.add_attachment(file_data,maintype='application',subtype="octet-stream",filename=fname)
try :
	print(f"\r{colorama.Fore.LIGHTBLACK_EX}Try to login ...{colorama.Fore.GREEN}",end="\r")
	smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp.login(user, password)
	print(f"\r{colorama.Fore.LIGHTBLACK_EX}Login succeeded{colorama.Fore.GREEN}",end="\r")
	try :
		print(f"\r{colorama.Fore.LIGHTBLACK_EX}trying to send the message ...{colorama.Fore.GREEN}", end="\r")
		smtp.send_message(msg)
		print(f"\r{colorama.Fore.LIGHTBLACK_EX}Message sent successfully{colorama.Fore.GREEN}",end="\r")
	except :
		print(f"\r{colorama.Fore.RED}Error while sending !{colorama.Fore.GREEN}",end="\r")
except :
	print(f"\r{colorama.Fore.RED}Error while logging in !{colorama.Fore.GREEN}",end="\r")
	sys.exit()
