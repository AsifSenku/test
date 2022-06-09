import sys

import requests
                           

usern = "Ghoul"
passwd = "Ghoul_eye"

inpuser = str(input("Enter your Username: "))
inppass = str(input("Enter your password: "))

if usern == inpuser and passwd == inppass:
	print("User and password is correct")
	pass
	
else:
	print("Wrong Username and password")
	sys.exit()

print("Trying to login.....")
print("Login Succesful")



