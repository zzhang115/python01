#!/usr/bin/python
import sys, os, time

path = sys.argv[1]
filename = path.split("/")[-1]

backup_directory = "/NewSpace/Python/PythonWorkplace/backupFile/"
backup_filename = '''%s%s_%s.tgz''' %(backup_directory, filename, time.strftime("%H:%M:%S_%m-%d-%y", time.localtime()))

def backupFile()
# def recordLogFile(backupDate, status, files, description = 'NULL'):
#     date = time.strftime("%H:%M:%S %m-%d-%y")
#     recordContent = "%s\t%s\t%s\t%s\n" %(date, backupDate, status, files, description)
#     f = file(, 'a') #append to existing file
#     f.write(recordContent)
#     f.flush()
#     f.close()

