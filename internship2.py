#1 There is a list of dictionaries. Create a function to get the values of the dictionaries creating the new one. 

def list_of_dicts(list_):
    list1 = []
    for i in list_:
        if isinstance(i,dict):
            for j in i.values():
                list1.append(j)
    return list1
 
a = [{'a':2, 8:9}, {3:11, 7:9}, {1:7, 3:8}]

print(list_of_dicts(a))

#2 Create a function to get the index of the max value in the list. Using the list - index method.

# def max_index(list_:list):
#     max_ = list_[0]
#     for i in list_:
#         if i > max_:
#             max_ = i
#     return f"The max value is {max_} and his index {list_.index(max_)}" 

# print(max_index([5, 10, 1, 25]))

#3 Create a function to get the index of the text occurrence in the string. Using the string - find method.


#4 Create a function to concatenate 2 lists of numbers and sort them numerically.

# def conc_sort(list1:list, list2:list):
#     list1.extend(list2)
#     for i in range(len(list1)):
#         for j in range(i + 1, len(list1)):

#             if list1[i] > list1[j]:
#                 list1[i], list1[j] = list1[j], list1[i]
#     return list1

# print(conc_sort(list1 = [2,3,9,1], list2 = [10,2,7]))

#5 Create a function with an arbitrary number of positional arguments, which will save them in a list and return it.


#6 Create a function with an arbitrary number of keyword arguments, which will save them in a dictionary and return it.
 
# def full_name(**kwargs):
#     for key, value in kwargs.items():
#         print("%s is %s" % (key,value))


#7 Create a function, which takes 2 numbers - one number to be divided by the second one

# def divide_numbers(first, second=2):
#     divided = first/second
#     return divided
# print(divide_numbers(first = 7))


