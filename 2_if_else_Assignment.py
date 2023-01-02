#Q1 An Integer is Input through keyboard.
# Write a program to find whether it is odd or even number.

print("Question no 1")
num=int(input("Enter a number:"))
if (num%2==0):
    print("Even Number")
else:
    print("Odd Number")
print()



#Q2 If cost price and selling price of an item is input through keyboard.
# Write a program to determine how much profit he made or how much loss he got.


print("Question no 2")
cost_price=int(input("Enter cost price:"))
sell_price=int(input("Enter selling price:"))

if (sell_price > cost_price):
    amt=sell_price-cost_price
    print("Yeah, Profit of rs",amt)

elif (sell_price==cost_price):
    amt=sell_price-cost_price
    print("Sold At Rate")

else:
    amt=sell_price-cost_price
    print("Loss is incurred of rs",abs(amt))
print()


#Q3 WAP to test a number is divisible by 3 or 5 and both.

print("Question no 3")
inte=int(input("Enter a number:"))
if (inte%3==0 and inte%5==0):
    print("Divisible by 3 and 5 both")

elif (inte%3==0):
    print("Divisible by 3")

elif (inte%5==0):
    print("Divisible by 5")
else:
    print("Not Divisible")
print()


#Q4 WAP to find the greatest of three numbers entered through keyboard

print("Question no 4")
n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))

if (n1>n2 and n1>n3):
    print("Greater number is:",n1)
elif (n2>n1 and n2>n3):
    print("Greater number is:",n2)
else:
    print("Greater number is:",n3)
print()


#Q5 The marks obtain by a student in 5 different subjects are input through keyboard. The student gets the division as per the following rules:
#Percentage above or equal to 60- first division
#Percentage between 50 and 59- second division
#Percentage between 40 and 49 – third division
#Percentage below 40 - fails.

print("Question no 5")
n1=int(input("Enter English marks:"))
n2=int(input("Enter Hindi marks:"))
n3=int(input("Enter Maths marks:"))
n4=int(input("Enter Science marks:"))
n5=int(input("Enter Social Science marks:"))

avg=n1+n2+n3+n4+n5
per=int(avg/500*100)

if (per>=60 and per<=100):
    print(per)
    print("First Division")
elif (per>=50 and per<=59):
    print(per)
    print("Second Division")
elif (per>=40 and per<=49):
    print(per)
    print("Third Division")
else:
    print(per)
    print("Failed")
print()

#Q6 Admission to professional course in a college according to following conditions:
# Marks in Mathematics are greater than or equal to 60 and marks in physics is greater than or equal to 50 and marks in chemistry is greater than or equal to 40
#			OR
# Total marks in mathematics, physics and chemistry is greater than or equal to 200.
#					OR
# Total marks in mathematics and physics are greater than or equal to 150.
# Marks of all three subjects will be entered through the keyboard. WAP to tell whether a student is qualifying for admission or not.

print("Question no 6")
mt=int(input("Enter Mathematics marks:"))
py=int(input("Enter Physics marks:"))
cm=int(input("Enter Chemistry marks:"))

sub=mt+py
avg=mt+py+cm

if (mt>=60 and py>=50 and cm>=40):
    print("Eligible for Admission according to First criteria")
elif (avg>=200):
    print("Eligible for Admission according to Second criteria")
elif (sub>=150):
    print("Eligible for Admission according to Third criteria")
else:
    print("Sorry not Eligible")
print()


#Q7 Write a program that has following menu:
#Enter 1 to find the area of rectangle.
#Enter 2 to find the area of circle.
#Values for length and width of a rectangle and value of a radius of circle will be entered through keyboard.

#Enter 1 to find the area of rectangle.
#Enter 2 to find the area of circle.

print("Question no 7\n")
print("""This program performs these task:

 1. Finds Area of Rectangle          2. Finds radius of Circle""")

user=int(input("Enter the number to perform the task:"))
if user==1:
    leng=int(input("Enter the length of rectangle:"))
    bre=int(input("Enter the breadth of rectangle:"))
    area=leng*bre
    print("Area of Rectangle is:",area)
if user==2:
    rad=float(input("Enter radius of circle:"))
    pi=3.14
    area=pi*rad*rad
    print("Area of Circle is:",area)
print()


#Q8 Write a program that has following menu:
#Enter 1 to find out whether the entered number is even or odd.
#Enter 2 to find out whether the entered number is positive or negative.

print("Question no 8")
print("""This program performs these task:

 1. Checks Even or Odd          2. Checks whether number is positive or not""")

user=int(input("Enter the number to perform the task:"))
if user==1:
    chec=int(input("Enter the number:"))

    if (chec%2==0):
        print("Even number")
    else:
        print("Odd number")
    
if user==2:
    chec=int(input("Enter the number:"))
    if(chec>0):
        print("Positive number")
    else:
        print("Negative number")
print()


#Q9 WAP that implements the simple calculator that has following menu:
#Enter 1 to find the addition of two numbers.
#Enter 2 to find the subtraction of two numbers.
#Enter 3 to find the multiplication of two numbers.
#Enter 4 to find the division of two numbers.
#Enter 5 to find the square of a number.
#Enter 6 to find the cube of a number.

print("Question no 9")
print(""" Press the button to perfrom specified task:

1. add two number                     2. Subtraction of two number
3. Multiplication of two number       4. Division of two number
5. Square of a number                 6. Find Cube of a number
""")
user=int(input("Enter the option from above displayed menu:"))

if (user==1):
    nu1=int(input("Enter a number:"))
    nu2=int(input("Enter another number:"))
    add=nu1+nu2
    print(add)
elif(user==2):
    nu1=int(input("Enter a number:"))
    nu2=int(input("Enter another number:"))
    sub=nu1-nu2
    print(sub)
elif (user==3):
    nu1=int(input("Enter a number:"))
    nu2=int(input("Enter another number:"))
    mul=nu1*nu2
    print(mul)
elif(user==4):
    nu1=int(input("Enter a number:"))
    nu2=int(input("Enter another number:"))
    div=nu1/nu2
    print(div)
elif(user==5):
    nu1=int(input("Enter a number:"))
    print(nu1**2)
elif(user==6):
    nu1=int(input("Enter a number:"))
    print(nu1**3)
else:
    print("Sorry wrong input")
print()


#Q10 Write a program that has following menu:
#Enter code w for withdraw.
#Enter code d for deposit.
#Enter code c for checking balance.

#Note: 1 take initial amount as input from user.

#Note:2 You can withdraw an amount only if balance is greater than or equal to 500
#and withdrawing amount should be less than balance.

print("Question no 10")
amnt=int(input("Enter your Balance:"))
print(""" Press the button to perfrom specified task:

Enter w to Withdraw               Enter d to Deposit
Enter c to Check Balance        
""")
user=input("Enter the option from above displayed menu:")
if user=="w" or user=="W":
    withd=int(input("Enter the amount to withdraw:"))
    if (withd>=500 and withd<=amnt):
        amnt=amnt-withd
        if (amnt>=500):
            print("Collect your cash")
            print("Your remaining balance is:",amnt)
        else:
            print("You cannot withdraw. \nPlease Maintain Average Balance of 500")
    else:
        print("Sorry Insufficient Balance")
elif user=='d' or user=='D':
    dep=int(input("Enter the amount to deposit:"))
    amnt=amnt+dep
    print("Deposit successful")
    print("Your new Balance is:",amnt)
elif user=='c' or user=='C':
    print("Your account balance is:",amnt)
else:
    print("Sorry wrong input")

print()
