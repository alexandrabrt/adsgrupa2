"""
Scrieti un program care sa faca split dupa al n-lea element intr-o lista:

lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

"""
lista_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
# result = [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
result = []
a = len(lista_start)
lista_noua = []
for i in range(n):
    lista_micuta = []
    for j in range(a):
        if j % n - i == 0:
            lista_micuta.append(lista_start[j])
    print(lista_micuta)
    lista_noua.append(lista_micuta)
print(lista_noua)

# alina, roberto, loredana, teodora
