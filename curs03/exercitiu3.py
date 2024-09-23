"""sa se scrie un program care sa returneze True in cazul in care primul si ultimul element dintr-o lista sunt la fel.
Altfel, returnati False."""

# lista = [12, 34, 23, 5, 1]  # False
lista = [12, 3, 56, 2, 12]  # True

la_fel = False
if len(lista) > 1:
    if lista[-1] == lista[0]:
        la_fel = True

if la_fel is True:
    print('Elementele sunt la fel')
else:
    print('Elementele sunt diferite')
