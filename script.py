import os
from subprocess import call
from subprocess import Popen
import time
for i in range(4):
    command = 'python main.py 889{} id{}'.format(i+1,i+1)
    # can't create peers too fast. 
    time.sleep(0.2) 
    Popen(['xterm','-e',command])
