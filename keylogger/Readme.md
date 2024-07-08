# Keylogger Script

### What It Does
This script logs all the keys pressed on your keyboard. It saves the logs in a file called logs.cvs

#### Why It Is Used
The script can be used to monitor and record keyboard activity. It tracks when the session starts and ends, and logs every key press.




 ###  How It Works
 - When the script starts, it writes the session start time and user name to the log file.
- It listens for key presses and writes each key to the log file.
- If you press Ctrl+C or send a terminate signal, it asks if you want to exit. If you choose to exit, it writes the session end time to the log file and stops the script.


- #### Dependencies
   - ```pynput```: Used for capturing keyboard events.
   - ```os```: Used for getting the current user.
   - ```datetime```: Used for getting the current date and time.
   - ```signal```: Used for handling termination signals.


