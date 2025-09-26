""" import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

t.speed(0) """
 
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

""" def star(x):
    length = 5
    for i in range(60):
        t.left(5)
        length += 5
        for i in range(x):
            t.forward(length)
            t.left(144)
star(5)

t.done() """
# UNIT TWO

""" x = 3
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

""" def user_input(x):   ODD / EVEN GENERATOR
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd") 
user_input(11)
 """
""" bill_total = input("How much is the bill?")
print(f"{bill_total} dollars")
service = ["bad","okay","good","great"]
x = "okay"
if x == "bad":
    print("the service was bad, i will tip 0%")
elif x == "okay":
    print("the service was okay, i will tip 15%")
elif x == "good":
    print("the service was good, i will tip 20%")
elif x == "great":
    print("the service was great, i will tip 25%")  """

""" def factors(x,y):  #DETERMINES THE FACTORS OF X (Y)
    if x % y == 0:
        print(f"{y} is a factor of {x}")
    else:
        print(f"{y} is not a factor of {x}")
factors(25,5) """

""" #Determines all factors of a number
def user_input(x,y):  #y must be the greater value for loop to function properly
    for i in range(1,y):
        if x % i == 0 and y % i == 0:  #determines if both x and y can divide values of i, if so, the value of i is a factor of x AND y
            print(f"{i} is a factor of {x} and {y}")
user_input(1, 30) """

#TRUE FALSE PROJECT
""" rideheight = True
withparent = False
HeathIssues = False
def rider():
    if (rideheight or withparent) and HeathIssues == False:
        print("You are allowed to ride")
    else:
        print("You are not allowed to ride")
rider() """

""" dooropen = False
windowopen = False
def alarm():
    if dooropen == False and windowopen == False:
        print("Alarm is silent")
    else:
        print("Alarm is active")
alarm() """

""" #number guessing game
import random
random_number = random.randint(1,10)
user_input = input("Guess a random number!:")
if user_input == random_number:
    print("You got it correct in 1 try!")
else:
    while user_input is not random_number:
        if user_input is not random_number:
            user_input = input("Your answer is incorrect, guess again!:")
        if user_input == random_number:
            print("You got it right!")
            break """

#dictionary project
dictionarys = ["Dictionary of empty space","Dictionary of value","Dictionary of worthlessness","Dictionary of riches"]
customer_input = input(f"Would you like to get any of the following?: {dictionarys}")
Name_1 = dictionarys[0]
Price_1 = "10"
Color_1 = "White"
Name_2 = dictionarys[1]
Price_2 = "100"
Color_2 = "Rainbow"
Name_3 = dictionarys[2]
Price_3 = "1"
Color_3 = "Brown"
Name_4 = dictionarys[3]
Price_4 = "250"
Color_4 = "Gold"
if customer_input == "1":
    customer_input = input(f"Would you like to get {Name_1}?")
    if customer_input == "yes":
        print(f"The dictionary is ${Price_1} and is {Color_1}")
    elif customer_input == "no":
        customer_input = input("Alright, would you like to get something else than?")
if customer_input == "2":
    customer_input = input(f"Would you like to get {Name_2}?")
    if customer_input == "yes":
        print(f"The dictionary is ${Price_2} and is {Color_2}")
    elif customer_input == "no":
        customer_input = input("Alright, would you like to get something else than?")
if customer_input == "3":
    customer_input = input(f"Would you like to get {Name_3}?")
    if customer_input == "yes":
        print(f"The dictionary is ${Price_3} and is {Color_3}")
    elif customer_input == "no":
        customer_input = input("Alright, would you like to get something else than?")
if customer_input == "4":
    customer_input = input(f"Would you like to get {Name_4}?")
    if customer_input == "yes":
        print(f"The dictionary is ${Price_4} and is {Color_4}")
    elif customer_input == "no":
        customer_input = input("Alright, would you like to get something else than?")