#!/usr/bin/python
import sys, os, time

path = sys.argv[1]
filename = path.split("/")[-1]

backup_directory = "~/NewSpace/Python/PythonWorkplace/backupFile/"
backup_filename = '''%s%s_%s.tgz''' %(backup_directory, filename, time.strftime("%H:%M:%S_%m-%d-%y", time.localtime()))

def backupFile(runtime = "now", exclude_file_name = "NONE"):
    if len(sys.argv) == 4:
        print "------exclude file mode------"
        if sys.argv[2] == "-X":
            exclude_file_name = sys.argv[3]
            backup_cmd = "tar cvzfX %s %s %s" %(backup_filename, exclude_file_name, path)
    else:
        print "------normal file mode------"
        backup_cmd = "tar cvzf %s %s" %(backup_filename, path)
    run_cmd = os.system(backup_cmd)
    if run_cmd == 0:
        print "Full Backup", "Success", "N/A", "test"
    else:
        print "Full Backup", "Failure", "N/A", "test"

backupFile()

