"""Scrieti un program ce va numara cate caractere are un sir de caractere dat de utilizator. Aceasta numarare sa se
realizeze cu ajutorul unui for fara a utiliza len(). La final afisati rezultatul
sir = "Ana are mere"

"""
sir = input("Adauga un sir: ")
count = 0
for i in sir:
    count = count + 1  # count += 1
print(f"Sirul \"{sir}\" are {count} caractere.")
