#!/usr/bin/python3
#copyright and visualized by Janl coded by Cyber coding
import smtplib
import ssl

print("""
██████╗░░█████╗░███████╗░█████╗░██████╗░░░░░░░███╗░░░███╗░█████╗░██╗██╗░░░░░
██╔══██╗██╔══██╗╚════██║██╔══██╗██╔══██╗░░░░░░████╗░████║██╔══██╗██║██║░░░░░
██████╔╝███████║░░███╔═╝██║░░██║██████╔╝█████╗██╔████╔██║███████║██║██║░░░░░
██╔══██╗██╔══██║██╔══╝░░██║░░██║██╔══██╗╚════╝██║╚██╔╝██║██╔══██║██║██║░░░░░
██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░░░░██║░╚═╝░██║██║░░██║██║███████╗
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝ """)
print("RICHTIGEN ANBIETER AUSGEWÄHLT? Beta v1.3")

port = 465
context = ssl.create_default_context()
email = input("Enter Email: ")
password = input("Enter Password: ")
receivers = input("Enter Recivers: ")
message = input("Enter Message: ")
with smtplib.SMTP_SSL("smtp.mail.de", port, context=context) as server:
# hier den anbieter auswählen|   
 server.login(email, password)
 server.sendmail(email, receivers, message)
 print("Email Sent")
 input()





