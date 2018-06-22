import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("jackson.weidmann@gmail.com", "")

msg = "Thanks"
server.sendmail("jackson.weidmann@gmail.com", "ella.onishuk@gmail.com", msg)
server.quit()
