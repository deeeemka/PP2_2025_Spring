class a:
    def __init__(self):
        self.userstring = ''
    def getstring(self):
        self.userstring= str(input())
    def printstring(self):
        self.userstring = print(self.userstring.upper())
        self.userstring
    
a = a()
a.getstring()
a.printstring()
