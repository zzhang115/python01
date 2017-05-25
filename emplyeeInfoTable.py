f = file("EmployeeInfo")
line = f.readline()
while len(line) != 0:
    print line
    line = f.readline()
f.close()
w = file("result", "w")
w.write("hello boy, finish reading!")
w.close()
