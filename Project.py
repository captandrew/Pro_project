import os
import time
import re

def new_process():
    while True:
        proc1 = os.popen('ps -eo user,cmd').read()

        time.sleep(3)
        proc2 = os.popen('ps -eo user,cmd').read()
        if proc1 != proc2:
            print('New program!')
            #return variable
            break

def add_to_dbase():
    pass


new_process()
