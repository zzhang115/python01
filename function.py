def sayHello():
    print "hello world"

def saySth(name):
    print "hello baby %s" %name

sayHello()
saySth("zzc")
def name_info(name, age, job, nationnality="Chinese"):
    global gl, gl1
    gl = 123
    gl1 = 100
    print "your name: %s age %d your nationnality:%s" %(name, age, nationnality)
    return name
result = name_info("zzc", 23, "programmar", )
print result
print gl, gl1

import os
os.system("ls")
