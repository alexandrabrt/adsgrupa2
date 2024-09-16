dictionar = {1: "Ana", "2": 'Mere', "3": 'pere', 4: "prune", "1": "Antonia"}
# print(type(dictionar))
# print(dictionar["2"])
# print(dictionar["22"])
# print(dictionar.get("22", "Nu gaseste nimic"))
# dictionar["22"] = "valoare noua"
dictionar.update({"22": "Valoare noua", "33": 'Alta valoare'})
# print(dictionar.keys())
# print(dictionar.values())
print(dictionar.items())
