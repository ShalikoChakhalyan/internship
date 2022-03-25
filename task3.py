#1 Create a function, which takes 2 dictionaries as an argument. The first dictionary is the main one,
#  there is a need to update the first dictionary data with the second one. If the key exists update the value,
#  otherwise add the item to the first dictionary.

# def dicts_(dict1: dict, dict2: dict):
#     dict1.update(dict2)
#     return dict1
# dict1_ = {"a": 10, 5: 7, "b": 21}
# dict2_ = {5: "b", 1: 2}
# print(dicts_(dict1_,dict2_))

#2 Create a function to get unique values from the list and return them as a tuple.

# def unique(list1: list):
#     unique_list = []
#     for i in list1:
#         if i not in unique_list:
#             unique_list.append(i)
#     return unique_list
# listt = [10, 20 , 10, 30, 20, 1, 30, 3]
# print(unique(listt))

#3 Create a function to remove {empty string, None, False, 0} values from the list.

# def remove_values(list_: list):
#     for i in list_:
#         if i == "" or i == None or i == False or i == 0:
#             list_.remove(i)
#     return list_

# listt = ["", False, 12, "ad"]
# print(remove_values(listt))

#4 Create a function, which takes 2 arguments: a list of dictionaries, a dictionary.
#  The first argument is the main one, there is a need to remove the items from the list of the dictionaries,
#  which exist in the second argument - dictionary.

# def lists(list_of_dicts: list, dict_: dict):

#     for i in list_of_dicts:
#         if isinstance(i, dict):
#             for key1, value1 in list(i.items()):
#                 for key2, value2 in list(dict_.items()):
#                     if key1 == key2 :
#                         # del i[key1]
#                         i.pop(key1)     
#     return list_of_dicts

# a = [{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5}, {"f": 6}]
# b = {"g": 7,"h": 4, "d": 9, "a": 10, }
# print(lists(a, b))

#5 There is a dictionary of the user names with name and email information.
#For example:
#users_list = [{“name”: “Lilly”, “email”: “lily@example.com”}, {“name”: “Eren”, “email”: “eren@example.com”}]
#Create a function to add a new dictionary whose keys will be the values of the users_list “email” and
#the values will be the users_list “name”.
#For example:
#new_dict = {“lily@example”: “Lilly”, “eren@example.com”: “Eren”}

def users(users_list: list):
    dict_ = {}
    for i in users_list:
        if isinstance(i, dict):
            for key, value in i.items():
                
                    
a = [{'name': 'Lilly', 'email': 'lily@example.com'}, {'name': 'Eren', 'email': 'eren@example.com'}]
print(users(a))
