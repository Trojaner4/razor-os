#!/usr/bin/python3
#copyright Janl.
import time
import os
os.system('clear')
print("""
██████╗░░█████╗░███████╗░█████╗░██████╗░░░░░░░░█████╗░░██████╗
██╔══██╗██╔══██╗╚════██║██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔════╝
██████╔╝███████║░░███╔═╝██║░░██║██████╔╝█████╗██║░░██║╚█████╗░
██╔══██╗██╔══██║██╔══╝░░██║░░██║██╔══██╗╚════╝██║░░██║░╚═══██╗
██║░░██║██║░░██║███████╗╚█████╔╝██║░░██║░░░░░░╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝░░░░░░░╚════╝░╚═════╝░""")
print("""
<1>--- fortfahren mit setup
<2>---Bereits erledigt!
""")
setup = input("Eigabe-->")
if setup == '1': 
 name = input(str("Bitte Benutzernamen eingeben-->"))
 passwort = input(str("Bitte Passwort eigeben-->"))

 lines = [name]
 with open('user2/benutzername.txt', "w") as f:
  f.writelines(lines)
#da das "os" noch in der beta steckt gibt es keine verschlüsselung!
 lines4 = [passwort]
 with open('user2/passwort.txt', "w") as f:
  f.writelines(lines4)
 os.system('./home.py')

if setup == '2':
 login_pass = open('user2/passwort.txt')
 login_name = open('user2/passwort.txt')
 l_p = login_pass.read()
 l_n = login_name.read()
 while True:
  login = input("bitte Passwort eingeben -->")
  if login == l_p:
   os.system('./home.py')
   break
  else:
   print("Falsches passwort!")



