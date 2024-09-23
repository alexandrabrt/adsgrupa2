"""Scrieti un program care sa valideze nr de telefon al unui utilizator scris de la tastatura.
+40123456789
-> incepe cu +40 (primele 3 caractere sunt +40)
-> are 12 caractere
-> sa aiba caracterele de la 3 la 12 sa fie doar cifre
"""
# numar_telefon = input("Introdu numarul de telefon: ")
# if len(numar_telefon) == 12 and numar_telefon[0: 3] == '+40' and numar_telefon[3: 13].isdigit():
#     print('Numar valid')
# else:
#     print('Numar invalid')


numar_telefon = input("Introdu numarul de telefon: ")
valid = True
if len(numar_telefon) == 12 and numar_telefon[0: 3] == '+40':
    for i in numar_telefon[3:13]:
        if i not in '0123456789':
            valid = False
            break

if valid is True:
    print('Numar valid')
else:
    print('Numar invalid')
