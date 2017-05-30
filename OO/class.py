import sys
print len(sys.argv)

class Animal:
    def __init__(self, name):
        self.name = name
    def speaking(self):
        print "I am animal"

class Dog(Animal):
    def __init__(self, name, age, sex):
        Animal.__init__(self, name) #must (self, ..)
        self.age = age
        self.sex = sex
    def sparking(self):
        print "wang wang wang"
    def attribute(self):
        print "%s %d %s" %(self.name, self.age, self.sex)
        self.speaking()
D = Dog("small dog", 20, "male")
D.sparking()
D.attribute()
print D.name
