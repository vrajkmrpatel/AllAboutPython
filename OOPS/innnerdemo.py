# Inner class demo
class Car:
      def __init__(self,make, year):
            self.make = make
            self.year = year
      
      class Engine:
            def __init__(self, number):
                  self.number = number
            def start(self):
                  print("Engine Started...")

c = Car("BMW",2010)
e = c.Engine(123) # call inner class using outer class object
e.start()