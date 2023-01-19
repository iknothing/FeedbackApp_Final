import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
def send_mail(userName,projectNo,curDate, role, remarks,basedirauth):
    port=2525
    smtp_server='smtp.mailtrap.io'
    #add login credentials from maitrap.io
    login=''
    password=''
    message=f"<h3>New Feedback Submission for {projectNo} on {curDate}</h3><ul><li>Name:{userName}</li><li>UserType:{role}</li><li>changes/remarks :{remarks}</li></ul>"
    sender_email='email1@example.com'
    receiver_email='email2@example.com'
    msg=MIMEMultipart()
    msg['Subject']='New Feedback Submission'
    msg.attach(MIMEText(message, 'html'))
    msg['From']=sender_email
    msg['To']=receiver_email

    part = MIMEBase('application', "octet-stream")
    dirpath = os.path.join(basedirauth, 'worksheets' , projectNo + '.xlsx')
    part.set_payload(open(dirpath, "rb").read())
    encoders.encode_base64(part)
    part.add_header(f'Content-Disposition', f'attachment; filename="{projectNo}.xlsx"')
    msg.attach(part)
    #Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email,receiver_email, msg.as_string())
