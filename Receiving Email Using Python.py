import imaplib
import getpass


M = imaplib.IMAP4_SSL('imap.gmail.com')

email = input("Email : ")
password = getpass.getpass("Password : ")

M.login(email, password)

M.list()
M.select('inbox')

typ, data = M.search(None, 'BEFORE 14-Aug-2020')