from bs4 import BeautifulSoup
import requests
import pandas

r = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx', verify=True)
link = BeautifulSoup(r.text, 'html.parser')
table = link.find_all('table', attrs={"class": "cursTable"})[0]
header = []
dataset = []
for tr_index in table.find_all('tr'):
    td_list = []
    if tr_index.find_all('th'):
        # for index_header, th_index in enumerate(tr_index.find_all('th')):
        #     if index_header < 6:
        #         header.append(th_index.get_text().replace('\xa0', ' '))
        header = [th_index.get_text().replace('\xa0', '') for index_header, th_index in enumerate(tr_index.find_all('th')) if index_header < 6]
    variabila = ''
    for index, td_value in enumerate(tr_index.find_all('td')):
        if index == 0 or index == 1:
            variabila = f"{variabila} - {td_value.get_text()}" if index == 1 else td_value.get_text()
            if index == 1:
                # variabila = f"{variabila} - {td_value.get_text()}"
                td_list.append(variabila)
            # else:
            #     variabila = td_value.get_text()
        elif index != 7:
            td_list.append(float(td_value.get_text().replace(',', '.')))
    if len(td_list) > 0:
        dataset.append(td_list)
print(header)
print(dataset)

df = pandas.DataFrame(dataset, columns=header)
df.to_csv('CursBnr.csv', header=header)
