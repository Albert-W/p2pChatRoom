import os
from subprocess import call
from subprocess import Popen
import time
for i in range(4):
    command = 'python main.py 889{} id{}'.format(i+1,i+1)
    # print(command)
    time.sleep(0.5) 
    Popen(['xterm','-e',command])