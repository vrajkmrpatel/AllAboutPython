from datetime import *

def validateCard(expiryDate):
      if expiryDate > datetime.now().date():
            print("Valid")
      else:
            print("Invalid")

validateCard(date(2028,2,2))
print(datetime.now().date())