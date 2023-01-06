# PYTHON PROGRAM FOR FACTO-RIAL OF A NUMBER.
'''factorial=1
num=int(input("Enter your number:"))
for i in range(1,num+1):
    factorial=factorial*i
    print(i,"of factorial is",factorial)
'''

# PYTHON PROGRAM BY USING FUNCTION WITH PRINT STATEMENT.

# def myfunc():
#     print("Hello world,this is my first program")
#
# myfunc()

# PYTHON PROGRAM BY USING FUNCTION WITH RETURN STATEMENT.

# def myfunc2():
#     return("Hello world ,This my second program")
#
# print(myfunc2())

# PYTHON PROGRAM BY USING FUNCTION.

# def myfunc3(a,b):
#     c=a*b #local scope or variable
#     return c
# x=myfunc3(2,6)
# print(x)

# PYTHON PROGRAM BY USING FUNCTION.

# def myfunc4(a,b):
#     if a>b:
#         print(a,"is bigger")
#     elif a==b:
#         print(a,"is equal to ",b)
#     else:
#         return b
# x=myfunc4(5,3)
# print(x)

# PYTHON PROGRAM BY USING FUNCTION WITH DOCSTRING.

def myfunc_doc(a,b):
    '''THis program shows the maxixmum number,

    kindly pas the argument to run this following code.'''
#     if a>b:
#         return a
#     elif a==b:
#         print(a,"is equal to ",b)
#     else:
#         return b
#
# x=myfunc_doc(5,6)
# print(x)
# print(myfunc_doc.__doc__)

#PYTHON PROGRAM FOR FINDING FACTORIAL NUMBER BY USING FACTORIAL.
# THIS PROGREAM IS DONE BY RECURSSIVE APROCH
# def factorial(n):
#     if n<1:
#         return 1
#     elif n==1:
#         return 1
#     else:
#         return(n*factorial(n-1))
#
# x=factorial(5)
# print(x)

#Python Program for simple interest

# FORMULA OF SIMPLE INTEREST (p*t*r)/100


# def simple_interest(p,t,r):
#     x=(p*t*r)/100
#     print(x)
#
# simple_interest(100,5,5)

# Python Program for Compound interest

# formula for compound interest A=P(1+R/100)^T

# def compound_interest(p,r,t):
#     amount=(p*(((1+r/100)**t)))
#     ci=amount-p
#     return ci
#
# x=compound_interest(100,5,5)
# print(x)


#PYTHON PROGRAM TO FIND WHETHER THE GIVEN NUMBER IS ARMSTRONG OR NOT.

# num=int(input("Enter your number:"))
# sum=0
# temp=num
# while num>0:
#     rem=num%10 #it will give the remainder
#     sum=sum+(rem*rem*rem)
#     num=num//10
# if sum==temp:
#     print("the given number is an armstrong number")
# else:
#     print("The given number is not an armstrong number")

'''DATA STRUCTURE'''

# LIST
# list1=["apple","banana","orange","cherry"]
# print(list1)
# print(len(list1))
# print(type(list1))
# list1.appst1)end("kiwi")
# # print(list1)
# # list1.sort()
# # print(li
# list1.clear()
# print(list1)
# list1.copy()
# print(list1)
# list2=["grapes","guava","pineapple"]
# list1.extend(list2)
# # print(list1)
# # x=list1.count("cherry")
# # print(x)
# print(list1)
# list1.remove("banana")
# print(list1)
#
#Python program to interchange first and last elements in a list.

# list=[12,52,62,45,78]
# print("The list is before swapping",list)
# lenght=len(list)
# # print(lenght)
# temp=list[0]
# list[0]=list[lenght-1]
# list[lenght-1]=temp
# print("This list is after swapping",list)

# first=list.pop(0)
# last=list.pop(-1)
# list.insert(0,last)
# list.insert(4,first)
# print(list)

# list1=sum(list)
# print(list1)

# PYTHON PROGRAM FOR MULTIPLY THE ELEMENT OF LIST.

# def mylist(list):
#     result=1
#     for i in range(0,len(list)):
#         result=result*list[i]
#     return result
#
# list1=[2,5,6]
# list2=[5,6,8]
# print(mylist(list1))
# print(mylist(list2))