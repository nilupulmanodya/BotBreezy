def send_emails(to,event,reg_no):
    import smtplib

    gmail_user = 'nilupmano@gmail.com'
    gmail_password = '891401310V'

    sent_from = gmail_user
    to = [to]#can be added multiples users
    subject = 'Confirmation of registaring {}'.format(event)
    body = 'Hello Student {}\n\nGreetings from Demo University. This email was sent to inform you that you have successfully registered {}. Which will held on Demo University. Hope to see you in the event.\n\nThank you.\nDemo University'.format(reg_no,event)

    email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
        return 1
    except Exception as ex:
        print ("Something went wrong….",ex)
        return 0

