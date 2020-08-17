import smtplib
import getpass


smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

email = input("Your Email : ")

# Turn On Two Step Verification
# Additionally you can add app password and use the password generated to keep you secure


password = getpass.getpass("Your Password : ")
smtp_object.login(email, password)

from_address = email

to_address = input("To Email : ")

subject = input("Enter your subject : ")

message = input("Enter your message : ")

msg = "Subject: " + subject + '\n' + message

smtp_object.sendmail(from_address, to_address, msg)





