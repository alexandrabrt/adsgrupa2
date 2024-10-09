# my_numbers = {2, 5, 3, 5, 4, 1, 2}
# doubled = len(my_numbers) * 2
# print(doubled)
"""
a. TypeError
b. 10 (correct)
c. 14
d. 12
"""

# for x in range(20):
#     if x / 2 == 0:
#         print(x)
# var_1 = [x for x in range(20) if x / 2 == 0]
# print(var_1)
"""
a. [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
b. [2]
c. [0] (correct)
d. [0, 1]
"""

# char = 'cha'
# cha = 'char'
# print(len(char) * 'char')
"""
a. charcharcharchar
b. chachachacha
c. chachacha (correct)
d. charcharchar
"""
# new_str = "Py'th\\'on"
# print(new_str[::-1])
"""
a. Py'th'on
b. no'\\ht'yP
c. Py'th\\'on
d. no'\ht'yP (correct)
"""

# planets = [['Mercury', 'Venus', 'Earth'],
#            ['Mars', 'Jupiter', 'Saturn'],
#            ['Uranus', 'Neptune', 'Pluto']]
# flatten_planets = []
# for sublist in planets:
#     for planet in sublist:
#         if len(planet) < 6:
#             flatten_planets.append(planet)
# print(flatten_planets)
"""
a. [5, 4, 5]
b. ['V','e','n','u','s',  'M','a','r','s',  'P','l','u','t','o']
c. ['Venus', 'Earth', 'Mars', 'Pluto'] (correct)
d. ['Venus', 'Mars', 'Pluto']
"""
# var_1 = ['abc', 'def', 'ghi']
# for item in var_1:
#     if type(item) == 'str':
#         item.upper()
#     else:
#         item.title()
# print(var_1)
"""
a. None
b. ['ABC', 'DEF', 'GHI']
c. ['abc', 'def', 'ghi'] (correct)
d. ['Abc', 'Def', 'Ghi'
"""

# print("ana are mere".capitalize())

# def double_number(n):
#     return lambda x: x * n
#
# result = double_number(5)
# result = lambda x: x * 5
# print(result(3-1))
"""
a. 4
b. 10 (correct)
c. Error
d. None
"""


# new_dict = {'item_1': 2, 'item_3': 1, 'item_2': 3}
# result = list(new_dict.keys()) + list(new_dict.values())
# print(str(result))
"""
a. ['item_1', 'item_3', 'item_2']
b. "['item_1', 'item_3', 'item_2', 2, 1, 3]" (correct)
c. "item_1, item_3, item_2, 2, 1, 3"
d. Error
"""

# def new_function(x, y) -> str:
#     new_result = x * 2 + y
#     if new_result % 2 != 0:
#         print("Not even")
#     else:
#         return 'Orice'
#
#
# print(new_function(2, 3))
"""
a. Not even
   None (correct)
b. Not even
c. Error
d. None
"""


# def function_1():
#     print("Variabila definita cu valoare", var)
#
#
# var = 10
# function_1()
# print(var)


# var_obj = {'key_1': 'val_1', "val_2": "key_2", "key_3": "val_3"}
# var_obj["key_2"] = 'val_2'
# var_obj.update({'key_2': 'val_2'})
# print(var_obj)

# try:
#     value = int('test')
# except Exception as e:
#     print(e)

# new_list = list(set([1, 4, 5, 4, 2, 6, 3]))
# print(new_list[1: 6])
# del(new_list[1: 6])
# print(new_list[-1])

# text_var = 'Python skills'
# try:
#     if "py" in text_var:
#         print("Python")
#     rrr
# except Exception as e:
#     print('skills')
# else:
#     print("execute")
# finally:
#     print('pass')

def my_function():
    l = list()
    for i in range(1, 4):
        l.append(i**2)
        return l
    print(l)


print(my_function())
