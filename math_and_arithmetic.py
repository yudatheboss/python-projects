import math

x = 3.14
y = 4
z = 5
friends = 10

#print("x = ", x, "\ny = ", y,"\nz = ", z)
#print(f"you have {friends} friends")

#### add and substract
#friends += 1
#friends = friends + 1
#friends -= 1
#friends = friends - 1

#### multiplication
#friends = friends * 3
#friends *= 3

#### division
#friends = friends / 2
#friends /= 2

#### exponents
#friends = friends ** 2
#friends **= 2

#### module list (remainder of division) (divides and returns the remainder)
#remainder = friends % 3
#print(f"After dividing your friend group in 3, you now have {remainder} friend(s) left")

#### rounding
#result = round(x)

#### absolute value (distance away from 0 as a whole number)
#result = abs(y)

#### exponents (to the power of)
#result = pow(5,5)

#### max/min value
#result = max(x, y, z)
#result = min(x, y, z)

# math library #
#print(math.remainder(4,7))
#(math.pi)
#print(math.e)

####square root
#result = math.sqrt(x)

####rounding up/down
#result = math.ceil(x)
#result = math.floor(x)



#### circumference and area calc (i = 2 times π times r (radius)

radius = float(input('circumference and area calculator:\n enter the radius of a circle: '))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius, 2)

print(f"The circumference is: {round(circumference, 2)}.\nThe area is {round(area, 2)}^2")

#### calculate the hypotenuse of a right-angled triangle
a = float(input("Enter side A: "))
b = float(input("Enter side A: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"side C = {round(c, 2)}")




