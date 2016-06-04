import smtplib
from email.mime.text import MIMEText
_user = "xxx@126.com"
_pwd = ""
_to = "ttt@126.com"

msg = MIMEText("send from python")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP("smtp.126.com", timeout=30)
s.login(_user, _pwd)
s.sendmail(_user, _to, msg.as_string())
s.close()

