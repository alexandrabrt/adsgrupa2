import pandas as pd
df_financial = pd.read_excel('date_financiare.xlsx')
print(df_financial.head())

# verificam valorile lipsa
valori_lipsa = df_financial.isnull().sum()
print(valori_lipsa)
df_cu_valori_sterse = df_financial.dropna()

exchange_rate = {'USD': 4.2, 'EUR': 4.9, 'RON': 1.0}
df_financial['SUMA_RON'] = df_financial.apply(
    lambda row: row['Suma_Transactie'] * exchange_rate[row['Valuta']], axis=1)
print(df_financial['SUMA_RON'])

suma_clienti = df_financial.groupby('Client')['Suma_Transactie'].sum()
print(suma_clienti)

comision_mediu = df_financial.groupby('Tip_Transactie')['Comision'].mean()
print(comision_mediu)

tranzactie_problematice = df_financial[df_financial['Status_Transactie'] != 'Finalizata']
print(tranzactie_problematice)

trazactii_mari = df_financial[df_financial['Suma_Transactie'] > 5000]
print(trazactii_mari)

df_financial['Luna'] = df_financial['Data_Transactie'].dt.to_period('M')
suna_lunara = df_financial.groupby('Luna')['Suma_Transactie'].sum()
print(suna_lunara)

suma_zilnica = df_financial.groupby(df_financial['Data_Transactie'].dt.date)['Suma_Transactie'].sum()
suma_zilnica = suma_zilnica.sort_index()
print(suma_zilnica)
df_suma_zilnica = suma_zilnica.reset_index()
df_suma_zilnica.columns = ['Data_Transactie', 'Suma_Totala']
df_suma_zilnica.to_csv('Date_trazactii.csv')
