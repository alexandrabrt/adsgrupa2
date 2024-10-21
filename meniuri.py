# def afisare_meniu():
#     print("\n--- Meniu Principal ---")
#     print("1. Adăugare categorii")
#     print("2. Listare taskuri")
#     print("3. Sortare taskuri")
#     print("4. Filtrare taskuri")
#     print("5. Adăugare task nou")
#     print("6. Editare task")
#     print("7. Ștergere task")
#     print("8. Ieșire")
#
#
# def afisare_meniu_sortare():
#     print("\n--- Sortare Taskuri ---")
#     print("1. Sortare ascendentă după task")
#     print("2. Sortare descendentă după task")
#     print("3. Sortare ascendentă după dată")
#     print("4. Sortare descendentă după dată")
#     print("5. Sortare ascendentă după persoana responsabilă")
#     print("6. Sortare descendentă după persoana responsabilă")
#     print("7. Sortare ascendentă după categorie")
#     print("8. Sortare descendentă după categorie")
#
#
# def afisare_meniu_filtrare():
#     print("\n--- Filtrare Taskuri ---")
#     print("1. Filtrare după task")
#     print("2. Filtrare după dată")
#     print("3. Filtrare după persoana responsabilă")
#     print("4. Filtrare după categorie")
#
#
# def main():
#     while True:
#         afisare_meniu()
#         optiune = input("Alegeți o opțiune (1-8): ")
#
#         if optiune == "1":
#             # Adăugare categorii
#             adaugare_categorii(categorii)
#         elif optiune == "2":
#             # Listare taskuri
#             print("Listarea taskurilor...")
#             # Aici se va apela o funcție de listare a taskurilor
#         elif optiune == "3":
#             afisare_meniu_sortare()
#             opt_sortare = input("Alegeți o opțiune de sortare (1-8): ")
#             # Apelați funcțiile de sortare pe baza opțiunii
#         elif optiune == "4":
#             afisare_meniu_filtrare()
#             opt_filtrare = input("Alegeți o opțiune de filtrare (1-4): ")
#             # Apelați funcțiile de filtrare pe baza opțiunii
#         elif optiune == "5":
#             # Adăugare task nou
#             print("Adăugare task nou...")
#             # Aici se va apela o funcție de adăugare task
#         elif optiune == "6":
#             # Editare task
#             print("Editare task...")
#             # Aici se va apela o funcție de editare task
#         elif optiune == "7":
#             # Ștergere task
#             print("Ștergere task...")
#             # Aici se va apela o funcție de ștergere task
#         elif optiune == "8":
#             print("Ieșire din program.")
#             break
#         else:
#             print("Opțiune invalidă, vă rugăm să alegeți din nou.")
