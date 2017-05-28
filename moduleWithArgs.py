import sys

#common use sys.path, sys.argv, sys.exit
# print "argument[0] is ", sys.argv[0]
# print "arguments is", sys.argv[1], sys.argv[2]

import os
os.system('cd ..')
os.system('df -h')
os.chdir('..') #change current directory
os.system("pwd")
a = os.popen('ls')
# print a.readlines() # form a list

for i in a.readlines():
    print "i: ", i
#os.mkdir("newDir")
#os.chdir("~")
import time
# time.sleep(5)
print "wake up"
print time.time()
print time.strftime("%H:%M:%S %m-%d-%Y")
print time.timezone

import datetime
print datetime.datetime.now()

import newModule
print newModule.version

import logging
print logging._acquireLock()