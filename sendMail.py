

import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

class InvalidEMailAddress(Exception):
    def __init__(self, value): 
        self.value = value 

    def __str__(self): 
        return (repr(self.value)) 

def checkEmailAddress(email):

    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    if(re.search(regex, email)):
        return True
    else:
        return False

class SendMail:

    def __init__(self,server,port,username,password,senderEmail):

        self.server      = server
        self.port        = port
        self.username    = username
        self.password    = password
        self.senderEmail = senderEmail

        if checkEmailAddress(self.senderEmail):
            pass
        else:
            raise InvalidEMailAddress("sender email address in config json is wrong")

    def sendNewMail(self):
        

        
        subject        = input("Subject?")
        body           = input("Body?")
        receiver_email = input("Recipient?")

        if checkEmailAddress(receiver_email):
            pass
        else:
            raise InvalidEMailAddress("receiver email address is wrong")


        try:
            message            = MIMEMultipart()
            message["From"]    = self.senderEmail
            message["To"]      = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))
            
            session     = smtplib.SMTP()
            session.connect(self.server,self.port)
            session.starttls()
            session.login(self.username,self.password)
            session.sendmail(self.senderEmail,receiver_email,message.as_string())
            
            print("Email sent! ")
        except Exception as e:
            print(e)
        
if __name__ == "__main__":

    configFileName = "config.json"
    with open(configFileName,'r') as confFile:
        config = json.load(confFile)

    try :
        sender1 = SendMail(**config['serverConfig'])
        sender1.sendNewMail()

    except InvalidEMailAddress as error:
        print(error)

