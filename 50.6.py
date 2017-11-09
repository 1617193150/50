import smtplib
import email.mime.multipart
import email.mime.text

msg=email.mime.multipart.MIMEMultipart()
msg['from']='2711887060@qq.com'
msg['to']='18762695380@qq.com'
msg['subject']='test'
content='''''
    你好，
            这是一封来自网络161，50号发的一封邮件。


'''
txt=email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp=smtplib.SMTP()
smtp.connect('smtp.163.com','25')
smtp.login('tomyemail@163.com','zqf521')
smtp.sendmail('tonymail@163.com','18762695380@qq.com',str(msg))
smtp.quit()