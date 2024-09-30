# print("Ana")
# input()
# def functia_mea(param_1, param_2):
#     return "Ana are mere", "Ana are pere"


# rezultat = functia_mea(1, 2)
# print(rezultat)


def suma(a: int = 1, b: int = 2, c: int = 3, *args, **kwargs) -> (int, float):
    print(type(kwargs))
    # print(kwargs['d'])
    suma = a + b + c + kwargs['d']
    for i in args:
        suma = suma + i
    for i in kwargs.values():
        suma = suma + i
    return suma, a - b


# rezultat_suma, rezultat_diferenta = suma(1, 3)
# rezultat_suma, rezultat_diferenta = suma(b=3)
# rezultat_suma, rezultat_diferenta = suma(1, 2, 3, 4, 5, 6, 7, 9, 10)
rezultat_suma, rezultat_diferenta = suma(5, 10, 15, 1, 2, 3, d=5, e=6)
print(rezultat_suma, rezultat_diferenta)
