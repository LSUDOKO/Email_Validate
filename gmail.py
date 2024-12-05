
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
a=input("Enter Email")
if(re.fullmatch(regex,a)):
    print("Valid Email")
else:
    print("Invalid Email")