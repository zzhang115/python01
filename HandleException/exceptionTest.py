a = [1, 2, 3, 4]

if 3 in a:
    print("yes")

try:
    print (a[5])
except IndexError:
    print ("\033[34;1mindexException\033[0m")
'''
AttributeError # try to access a object which has no attributes
IOError
ImportError
IndentationError
IndexError # no need to describe
KeyError # try to use a unexists key in dic
KeyboardInterrupt
NameError #use a var which has no given object
SyntaxError
TypeError
UnboundLocalError # trying to access a unintialized local var,
ValueError # if you pass a unexpected value,
'''

a = { "1" : "abc",
      "2" : "efg"
    }
try :
    print (a["1"])
except KeyError:
    print ("key is not exits in this dic")

# while 1:
#     print "run"
# import time
# for i in range(1, 100):
#     try:
#         print i
#         time.sleep(3)
#     except KeyboardInterrupt:
#         print "this is keyboardInterrupt, you cannot do it"
#         continue

# build our own exception
# class MyException(Exception):

try:
    for i in a:
        print (i)
        raise IndexError #if in some case we need to create a exception manually, use raise
except IndexError:
    print ("this a raised IndexError")
finally: # usually used to close some connection like socket
    print ("arrive finally")

print ("after Error")
try:
    for i in a:
        print (i)
        raise IndexError #if in some case we need to create a exception manually, use raise
except IndexError:
    print ("this a raised IndexError")
else:
    print ("no exception")
