import re
print("password strength checker")
password=input("Enter your password:")
strength=0
if(len(password)>=8):
    strength+=1
if(re.search("[A-Z]",password)):
    strength+=1
if(re.search("[0-9]",password)):
    strength+=1
if(re.search("[!@#$%^&*]",password)):
    strength+=1

if(strength<=1):
    print("Weak Password")
elif(strength==2):
    print("Medium Password")   
else:
    print("Strong Password")