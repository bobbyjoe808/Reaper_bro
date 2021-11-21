import os
import threading
import time

def reaper():
    os.system('python reaper_program.py')


amount = int(input('how many would you like >> '))

for _ in range(amount):
    thread = threading.Thread(target=reaper)
    thread.start()
    time.sleep(1)