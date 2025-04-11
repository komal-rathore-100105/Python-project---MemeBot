import smtplib
import ssl
from email.message import EmailMessage

def send_meme_email(receiver_email,quote):
    # Your email credentials
    sender_email = "komalrathor2005@gmail.com"
    sender_password = "ibnk pyaf clek xlyn"  # use App Password if 2FA is enabled

    # Email content
    subject = "😂 Your Meme from MemeBot!"
    body = "Hope this brings a smile to your face! Hey, if this lands in spam, please mark it as Not Spam — so MemeBot can keep spreading the laughs!" #f"Here's your meme:\n\n{quote}\n\nStay funny! 🤪"
    meme_file = "generated_meme.jpeg"
    
    msg = EmailMessage()
    msg.set_charset("utf-8")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body, charset ="utf-8")
    
    # Attach the image
    with open(meme_file, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=meme_file)

    # Send the email
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("✅ Meme sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
 
# import smtplib
# import ssl
# from email.message import EmailMessage
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# 
# def send_meme_email(receiver_email, quote):
    # sender_email = "komalrathor2005@gmail.com"
    # app_password = "ibnk pyaf clek xlyn"
# 
    # subject = "Your Meme from MemeBot 🤖"
    # body = f"""Hey there,
# 
# Hope you're having a great day! Here's your meme:
# 
# "{quote}"
# 
# Keep smiling and spread the laughter 😄
# 
# -- 
# Sent with ❤️ by MemeBot - your Python-powered meme buddy.
# """
# 
    # Compose email"
    # message = MIMEMultipart()
    # message["From"] = sender_email
    # message["To"] = receiver_email
    # message["Subject"] = subject
    # message.attach(MIMEText(body, "plain", _charset="utf-8"))
    # 
    # meme_file = "generated_meme.jpg"
    # Attach the image"
    # with open(meme_file, "rb") as f:
        # file_data = f.read()
        # # msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=meme_file)
# 
# 
    # Send the email"
    # context = ssl.create_default_context()
# 
    # try:
        # with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # server.starttls()
            # server.login(sender_email, app_password)
            # server.sendmail(sender_email, receiver_email, message.as_string())
            # print("✅ Meme emailed successfully!")
    # except Exception as e:
        # print(f"❌ Failed to send email: {e}")
# 