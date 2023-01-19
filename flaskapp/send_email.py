import os.path
import smtplib
from email.message import EmailMessage
def send_email(email,projectNo,curDate, role, remarks,basedirauth):
    msg = EmailMessage()
    msg['Subject'] = 'new feedback submission'
    msg['From'] = 'email1@example.com'
    msg['To'] = 'email2@example.com'
    msg.set_content(f'New Feedback Submission for {projectNo} on {curDate}\nName:{email}\nUserType:{role}\nchanges/remarks :{remarks}')
    with open(os.path.join(basedirauth,"worksheets",projectNo+".xlsx"),'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='xlsx', filename=file_name)
    with smtplib.SMTP_SSL('smtp.mailtrap.io', 2525) as smtp:
        #login credentails from mailtrap.io
        smtp.login('', '')
        smtp.send_message(msg)
        smtp.quit()
