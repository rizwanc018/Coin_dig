from concurrent.futures import process
from signal import signal
import webbrowser
import psutil
import time
# import os
# import signal
# import pyautogui
# import keyboard

# backup_url = "https://dsearch.com/search?q="
url = "https://www.presearch.org/extsearch?term="
process_name = "brave"
pid = None
i = 0

brave_path = "/usr/bin/brave-browser"
webbrowser.register('brave', None,
                     webbrowser.BackgroundBrowser(brave_path))

webbrowser.get('brave').open(url+"open")

time.sleep(3)
file = open("raft.txt","r")

for item in file:
    webbrowser.get('brave').open_new_tab(url+item)
    time.sleep(16)
    i+=1
    
    if i >= 20:
        i = 0
        for proc in psutil.process_iter():
            if process_name in proc.name():
                proc.kill()
        time.sleep(5)
        webbrowser.get('brave').open(url+"open")
        time.sleep(5)


    
    
# time.sleep(15)
# print("jilled")
# os.system(command + str(pid)) 
# os.kill(int(pid),signal.SIGKILL)
# # pyautogui.hotkey("ctrl",  "w")
# # keyboard.press_and_release("ctrl+w")
file.close()


