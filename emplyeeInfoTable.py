import fileinput
f = file("EmployeeInfo")
line = f.readline()
while len(line) != 0:
    print line
    line = f.readline()
    print f.tell()
f.close()
w = file("result", "w")
w.write("hello boy, finish reading!")
w.write("Hello, I am zzc ")
w.close()

with open("result", "a") as w: #this is for writing string appends to existing file a represent append
    w.write("Hello")
    w.close()
for line in fileinput.input("result", inplace=0):
    line = line.replace("Hi", "Hello")
    print "line:", line #it mean get everything from result file and after replacing, it will write line back

with open("result", "r+") as f:
    old = f.read() #read everything in the file
    f.seek(10) #rewind it means set the file's current position to 10,
    f.write("new line\n" + old) #write the new add new line string after cursor position 10
