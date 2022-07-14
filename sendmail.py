
import yagmail
username = "jeffkamau116"
password = "ufkl xpnn ugtz jgxz"
def mail_send(receiver_email,content):
    yag = yagmail.SMTP(username,password)
    yag.send(receiver_email, 'subject', content)






# # Alternatively, with a simple one-liner:
# yagmail.SMTP('jeffkamau116').send('jeffkamau117@gmail.com', 'subject', contents)
