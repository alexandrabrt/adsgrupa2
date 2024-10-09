var = 'comprehension'
# print(list(var))
# list_for_loop = []
# for caracter in var:
#     list_for_loop.append(caracter)
# print(list_for_loop)
# list_for_loop = [caracter for caracter in var]
# print(list_for_loop)

# numbers_list = []
# for x in range(30):
#     if x % 2 == 0:
#         numbers_list.append(x)
# numbers_list = [x for x in range(30) if x % 2 == 0]
# dictionar = {1: 1, 2: 4, 3: 9}
# numbers_list = [y for x, y in dictionar.items() if x % 2 == 0]

# note_matematica = {"Ana Maria": 5, "Ion Popescu": 4, "Maria Elena": 9}
# numbers_list = [x if y < 5 else '' for x, y in note_matematica.items()]
# print(numbers_list)

# dictionar = {}
# for i in range(1, 11):
#     dictionar[i] = i*i
# dictionar = {i: i*i for i in range(1, 11)}
# dictionar = {i: i*i for i in range(1, 11) if i % 2 == 0}
dictionar = {i: i*i if i % 2 == 0 else 0 for i in range(1, 11)}
# print(type(dictionar))
print(dictionar)
