import sys
print len(sys.argv)

class Dog:
    def sparking(self, name):
        self.N = name
        print "wang wang wang"

D = Dog()
D.sparking("dog")
print D.N
