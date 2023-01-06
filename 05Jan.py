# Python Ways to check if element exists in list.

# list=[2,54,63,58]
# if 54 in list:
#     print("Element exits")
# else:
#     print("Element does not exits")

# Python program to find sum of elements in list.
# list=[2,5,8,9]
# result=0
# for i in range(0,len(list)):
#     result=result+list[i]
# print("The sum of list",result)

# Python program to find smallest number and Greater number4 in a list.
# list=[5,9,8,6,1]
#
# print(min(list))
# print(max(list))

# Python program to find multiply of elements in list.
# list=[2,5,3]
# result=1
# for i in range(0,len(list)):
#     result=result*list[i]
# print("The multiply of the given list is:",result)

# Python program to find second largest number in a list

# list1=[2,56,84,78,2]
# list1.sort()
# print(list1)
# print("The Second largest element of the given list:",list1[-2])

# Python program to find N largest elements from a list

# list=[56,87,56,89,52,54,87]
# n=3
# list.sort()
# print(list)
# # print(list)
# print("The N largest number from the given list:",list[-n:])

# Python program to print even numbers in a list
# i=1
# list=[54,26,41,23,22,87,56]
# for i in list:
#     if i%2==0:
#         print(i)

# Python program to print all even numbers in a range
# result=1
# list=[27,45,23,54,56,78,24,51]
# for i in range(0,len(list)):
#     result=list[i]
#     if result%2==0:
#         print(result)

# Python program to print positive numbers in a list.

# list=[56,23,-98,45,-21,22]
# for i in list:
#     if i>0:
#         print(i)

# Python program to print negative numbers in a list

# list=[56,23,-98,45,-21,22]
# for i in list:
#     if i<0:
#         print(i)

# Python program to print all positive numbers in a range.

# list=[12,54,56,87,45,-54,-65,-24,58,32]
# print("Below numbers are positive number of the given list:")
# for i in range(0,len(list)):
#     if list[i]>0:
#         print(list[i])


# Python program to print all negative numbers in a range

# list=[12,54,56,87,45,-54,-65,-24,58,32]
# print("Below numbers are negative number of the given list:")
# for i in range(0,len(list)):
#     if list[i]<0:
#         print(list[i])
#

'''Dictonary'''

# Python – Extract Unique values dictionary values.

# mydict={
#     "name":"Farooq",
#     "Name":"Sanobar",
#     "age":26,
#     "Role":"Odoo developer",
#     "Age":26,"Deignation":"Odoo developer"
#
# }
# print(mydict)
# x=mydict.values()
# print("Dictonary Values=",x)
# list=list(set(x))
# print("The Unique values=",list)

# Python program to find the sum of all items in a dictionary

# def mydict(dict):
#     sum=0
#     for i in dict:
#         sum+=dict[i]
#     return sum
# dict={"vada pav":20,
#       "Sandwhich":30,
#       "Coldrink":50}
# print("The sum of all item present in dictonary:",mydict(dict))

# Python Ways to remove a key from dictionary

# dict={"vada pav":20,
#       "Sandwhich":30,
#      "Coldrink":50
# }
# # print(dict)
# # print(dict.pop("Sandwhich"))
# dict.pop("Sandwhich")
# print(dict)

# Python | Remove empty tuples from a list

# def removetuple(tuple):
#     for i in tuple:
#         if (i==()):
#             tuple.remove(i)
#         return tuple
#
# tuple=([(),("Farooq",26),("Sanobar",23),("Neha",23)])
# print("The final tuple",removetuple(tuple))

# Python  Merging two Dictionaries
# dict1={"vada pav":20,
#       "Sandwhich":30,
#      "Coldrink":50}
# dict2={"Breakfast":"Sandwhich",
#        "lunch":"Rice plate",
#        "Dinner":"chinese "
#
# }
# dict1.update(dict2)
# print(dict1)

# BY USING FUNCTION

# def mergedict(dict1,dict2):
#     return (dict1.update(dict2))
#
#
# dict1={"vada pav":20,
#       "Sandwhich":30,
#      "Coldrink":50}
# dict2={"Breakfast":"Sandwhich",
#        "lunch":"Rice plate",
#        "Dinner":"chinese "
# }
# print("The merge dictionary:",mergedict(dict1,dict2))
# print(dict1)

# Python – Convert key-values list to flat dictionary

# mydict={
#     "languages":["python","java","c++","javascript"],
#     "year":[1991,1995,1980,1995]
# }
# print("Original dictonary:",(mydict))
# dict2=dict(zip(mydict["languages"],mydict["year"]))
# print("Flattened Dictionary",(dict2))

'''Tuple'''

# Python program to Find the size of a Tuple

# s=(2,54,"Jelly","Glue","Farooq","Neha")
#
# print(str(s.__sizeof__()) + " bytes")

# Python – Maximum and Minimum K elements in Tuple

# mytuple=(2,5,1,24,32,8,88,1)
# print("The original tuple is",mytuple)
# k=2
# mylist=list(mytuple)
# temp=sorted(mylist)
# print(temp)
# result=tuple(temp[:k]+ temp[-k:])
# print(result)

# Create a list of tuples from given list having number and its cube in each tuple

# list=[2,5,8,9]
# for i in list:
#     res=(i,i**3)
#     print(res)

# Python – Adding Tuple to List and vice – versa

# mytuple=(2,5,3,4)
# list1=[5,4,8,7]
# mylist=list(mytuple)
# list2=(mylist+list1)
# print(tuple(list2))

# Python – Join Tuples if similar initial element

