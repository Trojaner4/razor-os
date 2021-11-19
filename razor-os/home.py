#!/usr/bin/python3
import os
os.system('clear')
print("""
██████╗░░█████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗
██╔══██╗██╔══██╗╚════██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝
██████╔╝███████║░░███╔═╝██║░░██║██████╔╝█████╗██║░░██║╚█████╗░
██╔══██╗██╔══██║██╔══╝░░██║░░██║██╔══██╗╚════╝██║░░██║░╚═══██╗
██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░
""")
print("""
[1]---Mail
[2]--Terminal
[3]--Browser
[4]--Benutzer deffenierte systeme
""")
while True:
 Auswahl = input("Auswahl--->")
 if Auswahl == '1':
  os.system('clear')
  os.system('./programme/razor-mail.py')
  
 
  break
 if Auswahl == '2':
  os.system('clear')
  os.system('./terminal.py')
  break
 if Auswahl == '3':
  os.system('clear')
  os.system('./browser.py')
 
  break
 if Auswahl == '4':
  os.system('clear')
  os.system('./userdef.py')
  break

else:
  print("Error code:01 Eingabe unkorrekt!")




