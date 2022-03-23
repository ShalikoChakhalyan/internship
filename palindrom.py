#1Create a function to check if the string is a palindrome or not

# Please add doctring and correct typing for all functions.

# This is not a  correct solution. 
# please fix it. 
world = input("enter the world ")
world_ = ""
for i in world:
    world_ = i + world_
 
if (world == world_):
    print("Yes")
else:
    print("No")


#2 Create a function to remove the odd indexes from the list.

# Never use list as a default value. 
def remove_odd_fom_list(list_:list, removed_list):
  # Can you use list comprehansion here instead?
    for i in range(len(list_)):
        if not i % 2 != 0:
            removed_list.append(list_[i])
    return removed_list

a = remove_odd_fom_list([2,5,8,4,5,5,1,99,15,32])
print(a)

#3 Create a function to reorder the dictionary keys alphabetically. Assume, that the keys are strings.

# This function is wrong have you tried to see what it returns?? Please fix
def alfabet_dict(dict_:dict): 
    for key in sorted(dict_):
        return "%s: %s" % (key, dict_[key])

a = alfabet_dict({'carl':40,'alan':2,'bob':1,'danny':3})
print(a)

#4 Create a function to join 2 sets

def set_join(set1:set, set2:set):
    set1.update(set2)
    return set1
    
a = set_join({1, 'a', 14, 2}, {'y', 'o', 7})
print(a)

#5 Create a function to split a string into a list (delimiter: ",").

def splited_list(string_: str) -> list:
    spl_string = string_.split(",")
    return spl_string
input_str = "hi, name, sky, world "
print(splited_list(input_str))

#6 Create a function to check if there are integers in the list and remove them.

# Never use list as a default value.
def is_not_digit(list_:list, list1) -> lsit:
    for i in list_:
        if isinstance(i, int):
            list1.append(i)
    return list1
                  
a = ["s", 5, 6, "a", 7, "d", 4.5, 9.1]
print(is_not_digit(a))


#7 Create a function to compare 2 lists and return matches as a list

def matchs(list1:list, list2:list) -> list:
 # This is correct but effective :) 
    a = []
    for i in list1:
        if i in list2:
            a.append(i)
    return a
l1 = [1, 2, 3, 4, 5]
l2 = [5, 6, 7, 3]
print(matchs(l1,l2))

#8 Create a function to find keys with duplicate values and return them.

def dublicate(dict_: dict):
    # You need to return only keys with duplicate values, not the list of all keys. Please fix
    print("Given Dictionary :", dict_)
    k_v_exchanged = {}

    for key, value in dict_.items():
        if value not in k_v_exchanged:
            k_v_exchanged[value] = [key]
        else:
            k_v_exchanged[value].append(key)
    
    return "New Dictionary:", k_v_exchanged

dict1 = {'Sun': 5, 'Mon': 3, 'Tue': 5, 'Wed': 3, 'sat':1}

print(dublicate(dict1))

#9 Create a function to find min and max values of the list and return them.

def min_max(numbers_list: list):
    max_ = numbers_list[0]
    min_ = numbers_list[0]
    for i in numbers_list:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
    return f"maximum of the list {max_} and minimum of list {min_}"

a = [4, 7, 9, 1]
print(min_max(a))

#10 Create a function to remove the keys from the dictionary, which are strings.

# this is a wrong solution. Please fix. 
def remove_key(dict_:dict):
    for key in dict_.keys():
        if  isinstance(key,str):
            new_dict = dict_.pop(key)
            return new_dict

a = {'hi':1, 5:4, 'ok':8, 7:9}
print(remove_key(a))

