import os 
import math 
import random 
import smtplib 

digits = "0123456789"
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random()*10)]
msg = "Hello, your OTP is "+ str(OTP)
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
emailid = "sakshipjadhav118@gmail.com"
s.login("sakshijadhav046@gmail.com","hfeqlrhqfasyosss")
s.sendmail("sakshijadhav046@gmail.com", emailid, msg)

a = input("Enter your OTP >>: ")
if a == OTP:
    print("Verified...!!")
else:
    print("Incorrect OTP")