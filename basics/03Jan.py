'''a= 20
b = 40
c= a+b
print(c)
'''

'''a=40
b=2
c=a/b # division
d=a//b # floor division
e=a-b
f=a**b # power
g=a%b # modulous
print(c)
print(d)
print(e)
print(f)
print(g)'''

# String formating
'''age=26
name='Farooq'
print('{0} will become {1} in the year 2023'.format(name,age))'''

# SAMPLE QUESTION
# find the area and parameter of a rectangle.

'''length=50
breadth=20
area=length * breadth
parameter = 2*area
print('The area of the rectangle will be',area)
print('The parameter of rectangle will be',parameter)
'''

# FIND ALL EVEN AND ODD NUMBERS BETWEEN 1 TO 100 AND PRINT IT

'''for i in range(1,101):
    if i%2==0:
        print(i)
'''

'''for i in range(1,101):
    if i%2:
        print(i)
'''

# FIND THE SUM OF NUMBER FROM 1 TO 10.

'''sum=0
for i in range(1,10):
    sum+=i
    print(sum)
'''

# PYTHON PR0GRAM TO ADD TWO NUMBERS.
'''num1=10
num2=20
num3=num1+num2
print(num3)
'''

# MAXIMUM OF TWO NUMBER OF PYTHON.
'''a=60
b=80
if a>b:
    print(a,"is maximum")
else:
    print(b,"is Maximum")
'''
#PYTHON PROGRAM FOR FACTORIAL OF A NUMBER
'''
n=int(input("Emter your number"))
while n<10:
    factorial=n*(n-1)
    n=n+1
    print(factorial)
'''

#PYTHON PROGRAM FOR GUESS THE CORRECT NUMBER.

'''num=25
guess=int(input('ENTER YOUR NUMBER:'))
if guess==num:
    print("Hurrey,You Guessed Right number")
elif guess<num:
    print("Your Guessed number is smaller than the actual number")
    print("Better luck next time")
else:
    print("Your Guessed number is greater than the actual number")
    print("Better luck next time")
print("Done")
'''
# PYTHON PROGRAM FOR GUESS THE CORRECT NUMBER BY USING WHILE LOOP.

'''num=25
running=True
while running:
    guess=int(input("Enter your number"))
    if guess==num:
        print("Congratulation,You guessed right number")
        running = False
        print("Done")
    elif guess < num:
        print("The Eentered number is smaller than the actual number")
        print("Better luck next time")
    else:
        print("The Eentered number is bigger than the actual number")
        print("Better luck next time")
'''

# python program by using break and continue statement.
'''running=True
while running:
     s=input("Enter your character")
     if s== 'quite':
         break
     if len(s)<3:
         print('To small')
         continue
     print("You number is sufficient")
     running=False'''

# PYTHON PROGRAM BY USING FUNCTION.
'''def max(a,b):
    if a>b:
        print(a,"is maximum")
    elif a==b:
        print(a,"is equal to ",b)
    else:
        print(b,"is maximum")
max(11,10)
X=12
Y=17
max(X,Y)
'''
