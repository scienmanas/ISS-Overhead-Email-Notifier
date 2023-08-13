import smtplib

class StartConnection:
    
    def __init__(self) :
        self.MailAddress = "your_emailaddress"
        self.Password = "your app password"
        self.Message = "Subject: View Overhead Right Now!\n\nThe International Space Station is Passing from obove the sky. Have a look above.\n\nHappy skywatching\n\nWith Regards\nManas"
        
    def SendMail(self) :
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(self.MailAddress,self.Password)
        connection.sendmail(from_addr=self.MailAddress,to_addrs="iamscientistmanas@gmail.com", msg=self.Message)
        
