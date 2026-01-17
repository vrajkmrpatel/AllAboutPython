def greet(name):
      def message():
            return "Hello "
      return message() + name

res = greet("Vraj")
print(res)