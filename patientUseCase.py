id=1
firstName="John"
lastName="        Bailey"
ssn="123-45-6789"
hasInsurance=True
billingAmount="10000"
print(type(billingAmount))
billingAmount = float(billingAmount)
print(type(billingAmount))

print(id,firstName,lastName.lstrip(),ssn,hasInsurance,billingAmount, ssn[7:])