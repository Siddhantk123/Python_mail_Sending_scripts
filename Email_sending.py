
#run this code on anaconda use command python filename.py
import smtplib
try:
    ob=smtplib.SMTP('smtp.gmail.com','587') # mail service provider(g-mail) domain name,and its port number
    ob.ehlo()
    ob.starttls()
    ob.login('senders mail id','password')
    ob.sendmail('senders mail id','receivers mail id','SUBJECT: With regard to bla bla bla ...\n\n\n  hello this is siddhant kumar mishra reporting from home ')#attributes-'senders mail','recievers mail','mail'
    ob.quit()
    print("successful")

except:
    print("run time error")
