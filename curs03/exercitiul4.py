"""se da un cuvant de la tastatura. sa se indice cate vocale si cate consoane contine."""

cuvant = input("Adauga un cuvant: ")
vocale = 0
consoane = 0
numere = 0
for i in cuvant:
    if i in '0123456789':
        numere = numere + 1
    elif i in 'aeiou':
        vocale = vocale + 1
    else:
        consoane = consoane + 1

print(f"Numarul total de: \n - vocale: {vocale} \n - consoane: {consoane} \n - cifre: {numere}")
