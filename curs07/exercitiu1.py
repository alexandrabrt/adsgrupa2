import pandas as pd
import numpy as np
import datetime

# din lista
# lista = [10, 40, 20, 30, 50]
# eticheta = ['a', 'b', 'c', 'd', 'e']
# serie = pd.Series(lista, index=eticheta)
# print(serie)

# print(serie['b'])
# print(serie[['b', 'c', 'e']])
# print(serie['b': 'd'])
# print(serie[1: 4])
# print(serie[serie > 20])

# din array NumPy
# array_date = np.array([10, 20, 30, 40, 50])
# serie = pd.Series(array_date)
# print(serie)

# din dictionar
# dict_date = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
# serie = pd.Series(dict_date)
# print(serie)

# data_si_timp = [datetime.datetime(2024, 1, 21),
#                 datetime.datetime(2024, 2, 22),
#                 datetime.datetime(2024, 3, 22)]
# ser_temporala = pd.Series([10, 20, 40], index=data_si_timp)
# print(ser_temporala['2024-03-22'])
# print(ser_temporala['2024-02-22': '2024-03-22'])

# data = {'Nume': ['Ana', 'Cristina', 'Bogdan'],
#         'Varsta': [25, 30, 22],
#         'Salariu': [50000, 60000, 20000]}
# df = pd.DataFrame(data)
# print(df)
# nume = df['Nume']
# print(nume)
# salariu_bogdan = df.at[1, 'Salariu']
# print(salariu_bogdan)
# df['Experienta'] = [2, 5, 1]
# print(df)
# print(df.loc[1])
# print('========================')
# df.set_index('Nume', inplace=True)
# print(df)
# print('========================')
# print(df.loc['Bogdan'])
# print('========================')
# print(df.iloc[1])
# df_filtrat = df[df['Varsta'] > 25]
# df_filtrat = df[df['Salariu'] > 40000]
# print(df_filtrat)
# df_filtrare = df[(df['Varsta'] > 25) & (df['Experienta'] > 1)]
# print(df_filtrare)
# df_sortat = df.sort_values(by='Varsta', ascending=False)
# print(df_sortat)
# df.set_index('Nume', inplace=True)
# df_sortat_index = df.sort_index()
# print(df_sortat_index)

# data = {'Nume': ['Ana', 'Bogdan', 'Ana', None, 'Cristina', 'Andrei', 'David', 'Ana'],
#         'Varsta': [25, 30, 25, 23, 22, 24, 35, None],
#         'Salariu': [50000, 60000, 60000, None, 10000, 450000, 70000, 50000]}

# df = pd.DataFrame(data)
# print(df)
# print('===================================')
# df_fara_duplicate = df.drop_duplicates(subset=['Nume', 'Varsta'])
# print(df_fara_duplicate)
# df.dropna(inplace=True)
# print(df)
# df.fillna(0, inplace=True)
# print(df)
# df['Experienta'] = [3, 2, 4, 5, 2, 6]
# print(df)
# df.rename(columns={'Experienta': 'NrAniDeMunca', 'Num': 'Numele'}, inplace=True)
# print(df)
# df['Departament'] = ['IT', 'HR', 'IT', 'Vanzari', 'IT', 'HR']
# print(df)
# grupuri_departamente = df.groupby('Departament')
# for nume_departament, grup in grupuri_departamente:
#     print(f"\nGrupul pentru departamentul: {nume_departament}")
#     print(grup)

# medie_salarii = grupuri_departamente['Salariu'].mean()
# print('\nMedia salariilor pentru fiecare departament:')
# print(medie_salarii)

# rezultate_agregare = grupuri_departamente.agg({'Varsta': 'mean', 'Salariu': ['sum', 'median'], 'Nume': 'count'})
# print('\nDate agragate:')
# print(rezultate_agregare)

# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Nume': ['Cristina', 'David'], 'Varsta': [22, 35]})
# df_concatenare_randuri = pd.concat([df1, df2], ignore_index=True)
# print(df_concatenare_randuri)

# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]})
# df2 = pd.DataFrame({'Salariu': [50000, 60000], 'Experienta': [2, 5]})
# df_concatenare_coloane = pd.concat([df1, df2], axis=1)
# print(df_concatenare_coloane)
# df1 = pd.DataFrame({'ID': [1, 2, 4], 'Nume': ['Ana', 'Bogdan', 'Cristina']})
# df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salariu': [60000, 40000, 50000]})
# df_concatenare = pd.merge(df1, df2, on='ID', how='inner')
# print(df_concatenare)

# df1 = pd.DataFrame({'Nume': ['Ana', 'Bogdan'], 'Varsta': [25, 30]}, index=[1, 2])
# df2 = pd.DataFrame({'Salariu': [50000, 60000], 'Experienta': [2, 5]}, index=[2, 3])
# df_imbinat_index = df1.join(df2, how='inner')
# print(df_imbinat_index)

data = {'Nume': ['Ana', 'Bogdan', 'Ana', None, 'Cristina', 'Andrei', 'David', 'Ana'],
        'Varsta': [25, 30, 25, 23, 22, 24, 35, None],
        'Salariu': [50000, 60000, 60000, None, 10000, 450000, 70000, 50000]}
df = pd.DataFrame(data)
df.dropna(inplace=True)
df['Departament'] = ['IT', 'HR', 'IT', 'Vanzari', 'IT', 'HR']
# print(df)
df.to_csv('date.csv', index=False)
df = pd.read_csv('date.csv')
print(df)
