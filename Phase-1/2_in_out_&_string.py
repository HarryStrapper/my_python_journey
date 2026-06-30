# Take input from the user and greet them. Use f-strings, slicing, and methods like .upper() and .split().

name = input("enter your name :")

part = name.split()

uppercase = name.upper()

lowercase = name.lower()

print(f"Hello {name}! you need one cup of coffee")
print(f"your full name is : {name}")
print(f"your name in uppercase is : {uppercase}")
print(f"your name in lower case is : {lowercase}")
print(f"your names first word is : {part[0]}")
print(f"your names first 3 letter is : {name[:3]}")


#ourput

'''


enter your name :samarth mayur sonavane
Hello samarth mayur sonavane! you need one cup of coffee
your full name is : samarth mayur sonavane
your name in uppercase is : SAMARTH MAYUR SONAVANE
your name in lower case is : samarth mayur sonavane
your names first word is : samarth
your names first 3 letter is : sam


'''