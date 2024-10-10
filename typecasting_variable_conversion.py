#typecasting. the process of converting a variable from one data type to another
from variables import is_CSmajor

name = 'juda'
age = 18
gpa = 3.2
is_CSmajor = True

#identifying variable type
#print(type(gpa))

#changing the gpa value (float) to an int
gpa = int(gpa)
print(gpa)

#converting the age value (int) to a float
age = float(age)
print(age)

#converting the age value (int) to a string
age = str(age)
#concantinating a string (which in this case is a number
age += "1"
print(age)

#changing a string to a booleoan (false if the string is empty)
name = bool(name)
#can be used if user tries logging in without username bool would return false prompting the user to try again
print(name)
