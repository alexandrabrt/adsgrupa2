"""Sa da de la tastatura un string. Sa se elimine caracterele din string pornind de la 0 pana la n,
unde n e dat si el de la tastatura
cuvant = ana, n=2, cuvant_nou = a
cuvant = croissant, n=3, cuvant_nou = issant
"""
s = input("Introduceti un string: ")
n = input("Introduceti un numar: ")
if n.isdigit() and (n := int(n)) and n <= len(s):
    s = s[n:]
    print(s)
