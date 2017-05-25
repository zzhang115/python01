#!/usr/bin/env/ python

name = raw_input("your name:")
age = int(raw_input("your age:"))
job = raw_input("your job:")
print "-------------"
if age < 28:
    print "Hi baby, you are still young man"
elif name =="zzc":
    print "oh, I heard you before"
else:
    print "Hi man"
print '''Name: %s
Age: %s
Job: %s ''' %(name, age, job)
