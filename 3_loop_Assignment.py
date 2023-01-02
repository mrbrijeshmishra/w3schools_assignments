#Q1 WAP to print all even and odd numbers between 1 and 100
for i in range(1,101):
    if i%2==0:
        print(i,"Is Even number")
    else:
        print(i,"Is Odd Number")
print("")


#Q2 WAP to print all even and odd numbers between 100 and 1

for i in range(101,0,-1):
    if i%2==0:
        print(i,"Is Even number")
    else:
        print(i,"Is Odd Number")
print("")

#Q3 WAP to print sum of numbers from 1 and 100
add=0
for i in range(1,101):
    add=add+i
print(add) 
print("")

#Q4 WAP to print sum of the following series: 1^2+2^2+3^2+…..+10^2
sqr=0
for i in range(1,11):
    sqr=sqr+i**2
print(sqr) 
print("")

#Q5 WAP to print  calculate the factorial of number entered through keyboard

fac=int(input("Enter the number to find factorial:"))
cal=1
for i in range(fac,0,-1):
    cal=cal*i
print(cal)
print("")

#Q6 Write a Python program to find those numbers which are
#divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

for i in range(1500,2701):
    if i%5==0 and i%7==0:
        print(i,"Is divisible and multiple of 7 and 5")
print("")

#Q7 Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
for i in range(1,7):
    if (i==3 or i==6):
        continue
    print(i)
print("")


#Q8 Write a Python program to get the Fibonacci series between 0 to 50.  
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
first=0
second=1
for n in range(0,51):
    if(n<=1):
        n1=n
    else:
        n1=first+second
        first=second
        second=n1
    print(n1)
print("")


e=0
c=1
su=0
i=1
while(i<=50):
    print(su)
    e=c
    c=su
    su=e+c
    i+=1
print("")


#Q9 Calculate the cube of all numbers from 1 to a given number.
cube=0
n=int(input("Enter number:"))
for i in range(1,n+1):
    cube=cube+i**3
print(cube)
print("")


#Q10 Write a program to count the total number of digits in a number
#For example, the number is 75869, so the output should be 5.
num=int(input("Enter long number:"))
num=str(num)
print(len(num))
print("")






