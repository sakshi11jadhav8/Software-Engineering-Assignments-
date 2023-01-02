import random  #random module to get random integers to create OTP
import senders_data #email and password of sender from another file
import smtplib  #simple message transfer protocol#library to send email to users email_address


#function to generate otp 
def generate_OTP(n):
    OTP=""
    for i in range(n):
        OTP+=str(random.randint(0,9))#OTP will append any random digits[index] 
    return (OTP)




#function to login and add tls to the server
# def login_into_sendersemail(Senders_email,Senders_password):

#     server.starttls()   #transferred layer security
#     server.login(Senders_email,password=Senders_password)  #Login into sender's mail
#     return server


#function to send email
def send_email(senders_data,receivers_name,receivers_email, otp_var): 
    Senders_email = senders_data.email
    Senders_password= senders_data.password

    
    #create gmail server
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()   #transferred layer security
    server.login(Senders_email,password=Senders_password)  #Login into sender's mail
   
    
    # login_into_sendersemail(Senders_email,Senders_password)
   
    msg=("Hi "+ receivers_name +"\n"+ str(otp_var)+" is your OTP ")
    server.sendmail(Senders_email,receivers_email,msg)
    server.quit() #to quit the server



if __name__ == '__main__': 
    #generate_otp function called
    n=(int(input("Enter your range of otp ")))  #getting the input for length of otp

    otp_var=generate_OTP(n)

    receivers_name= 'Sakshi'  #input("Enter receivers name ") 
    receivers_email= 'sakshipjadhav118@gmail.com'  #input("Enter receivers email ")

    #send emailfunction called
    send_email(senders_data,receivers_name,receivers_email, otp_var)
    print("email has been sent!")

