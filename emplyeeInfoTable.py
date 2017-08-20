import fileinput
f = file("EmployeeInfo")
# line = f.readline()
# while len(line) != 0:
#     print line
#     line = f.readline()
#     print f.tell()
# f.close()
w = file("result", "w")
w.write("hello boy, finish reading!")
w.write("Hello, I am zzc ")
w.close()

with open("result", "a") as w: #this is for writing string appends to existing file a represent append
    w.write("Hello")
    w.close()

for line in fileinput.input("result", inplace=0): #replace string in file
    line = line.replace("Hi", "Hello")
    print "line:", line #it mean get everything from result file and after replacing, it will write line back

with open("result", "r+") as f:#r+ means it can be changed
    old = f.read() #read everything in the file
    f.seek(10) #rewind it means set the file's current position to 10,
    f.write("new line\n" ) #write the new add new line string after cursor position 10
w = file("backupfile.txt", "w")
w.write("hello boy, this is test file")
w.close()

for line in fileinput.input("backupfile.txt", backup=".bak", inplace=1):#for this function, it change the content of backupfile.txt
    line = line.replace("hello", "hi")  #and back up one file end with .bak, it wont be replace by hi
    print line

# with open("EmployeeInfo", "r") as f:
#     newText=f.read().replace("9", "6")
#     print newText
# with open("EmployeeInfo", "w") as f:
#      f.write(newText)

for line in fileinput.input("EmployeeInfo", inplace=1):
    line = line.replace("759", "656")
    print line