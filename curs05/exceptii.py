text = input("Adauga un nr: ")
try:
    conversie = int(text)
    variabila
except ValueError:
    print("Avem o exceptie de valoare")
    conversie = input("Am zis un numar, nu un string: ")
except NameError:
    variabila = None
    print('Variabila a fost definita')
except Exception:
    print('Exceptie generala')
else:
    print(conversie)
finally:
    print('se executa oricand')
print(conversie)
