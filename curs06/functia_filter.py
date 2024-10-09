# def filtrare(x: list) -> list:
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#     return lista_forloop
#
#
# lista_1 = [1, 5, 4, 6, 8, 11, 2, 12]
# lista_2 = filtrare(lista_1)
# print(lista_2)

lista_1 = [1, 5, 4, 6, 8, 11, 2, 12]
lista_2 = list(filter(lambda x: x % 2 == 0, lista_1))
print(lista_2)
