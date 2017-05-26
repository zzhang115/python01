nameList = ["abc", "def", "ghi"]
print nameList[2]
print nameList[-1]
# nameList.pop(1)
nameList.remove("abc")
print nameList
nameList.append("lmn")
print nameList
nameList.insert(1, "opqr")
print nameList
print nameList.count("lmn")
print nameList.__len__()
print nameList.index("lmn")
nameList.pop(-1)
print nameList
nameList.sort()
print nameList
nameList.reverse()
print nameList
nameList[1]="lmn"
print nameList
nameList[nameList.index("def")]="newdef"
print nameList
