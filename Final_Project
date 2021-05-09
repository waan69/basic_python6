#Sumber kode pythonindo.com dan otak-keren.blogspot.com

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Membuat penyimpanan email
def toaddr():
    file = open("receiver_list.txt", "a+")
    file.write("\n" + text)
    
#Login ke email dan masukan email penerima
fromaddr = input("Masukan Email Pengirim: ") 
pawd = input("Masukan Password: ")
toaddr = input("Masukan Email Penerima: ")

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = input("Masukan Subjek: " ) 
body = input("Masukan Isi Pesan: ")
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, pawd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

