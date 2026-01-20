'''class Student:

      def __init__(self):
            self.__id = 123 # private fields if we use __id (double underscore)
            self.__name = "John"

      # inorder to access private fields use methods
      def display(self):
            print(self.__id)
            print(self.__name)

s = Student()
# s.display()

# Even though fields are private you can use it using Name mangling
print(s._Student__id)
print(s._Student__name)
'''
# Above is not actually encapsulation 
# We can implement that using setters and getters

class Student:
      def setId(self, id):
            self.id = id 
      def getId(self):
            return self.id 
      def setName(self, name):
            self.name = name
      def getName(self):
            return self.name 

s = Student()
s.setId(123)
s.setName("John")

print(s.getId())
print(s.getName())