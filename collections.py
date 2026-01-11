# Strings 

S="  You are awesome  "
print(S)

s1 = """You are 
the creator
of your destiny"""
print(s1)

print(S[0])

print(S*5)

print(len(s1))
print(len(S))

# Slicing
print(S[0:5])
print(S[0:])
print(S[:8])
print(S[-3:-1])

print(S[0:9:2])
print(S[15::-1])
print(S[::-1]) # Reverse a string

# Stripe the String
print(S.strip())
print(S.lstrip())
print(S.rstrip())

print(S.find("awe"))
print(S.count("a"))
print(S.replace("awesome", "super"))

print(S.upper())
print(S.lower())
print(S.title())