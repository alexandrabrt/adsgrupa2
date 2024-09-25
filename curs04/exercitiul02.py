"""scrieti un program care itereaza prin primele 10 numere. La fiecare iteratie afiseaza suma dintre iteratorul curent
si urmatorul iterator din sir."""
rezultat = 0
for i in range(1, 11):
    rezultat += 2 * i + 1

print(rezultat)
