""" import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

t.speed(0)

turtle.done()
 """
# UNIT ONE
""" def square(x):
    length = 5
    for i in range(60):
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(90)
        t.forward(length)
        t.left(95)
        length += 5
        square(5)  """

"""   def square(x):
    length = 5
    for i in range(60):
        t.left(5)
        length += 5
        for i in range(x):
            t.forward(length)
            t.left(90)
square(4)  """

""" def star(x)

 x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) 

print(values[0])
print(values[6])
 """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z)

# return is output

def add(x,y):
    return(x + y)
bill = add(5,10)
print(bill)

z = 15
bill = input("whats the bill amount")
print(add(15, int(bill))) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")
 """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" user_input = input("Type message:") #counts letters in input
print(len(user_input)) """
""" 
x = input("type a number")
if x % 2 == 0:
    print(f"{x} is odd")
else:
    print(f"{x} is even") """

bill_total = input("How much is the bill?")
print(bill_total)
service = ["bad","okay","good","great"]
x = "bad"
if x == "bad":
    print(f"the service was bad, i will tip {bill_total * 0}")
elif x == "okay":
    print(f"the service was okay i will tip {bill_total * 0.15}")
elif x == "good":
    print(f"the service was good i will tip {bill_total * 0.2}")
elif x == "great":
    print(f"the service was great i will tip {bill_total * 0.25}")