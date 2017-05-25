f = file("EmployeeInfo")
line = f.readline()
while len(line) != 0:
    print line
    line = f.readline()
f.close()
# w = file("result", "w")
# w.write("hello boy, finish reading!")
# w.write("Hello, I am zzc ")
with open("result", "a") as w: #this is for writing string appends to existing file
    w.write("Hello")
    w.close()
