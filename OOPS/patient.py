class Patient:
      def setId(self, id):
            self.id = id 
      def getId(self):
            return self.id 
      def setName(self, name):
            self.name = name
      def getName(self):
            return self.name 
      def setSSN(self,ssn):
            self.ssn = ssn 
      def getSSN(self):
            return self.ssn

s = Patient()
s.setId(123)
s.setName("John")
s.setSSN("123-45-678")

print(s.getId())
print(s.getName())
print(s.getSSN())