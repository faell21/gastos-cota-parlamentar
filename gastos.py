import json
import pandas as pd

#open the json file from the website https://dadosabertos.camara.leg.br/swagger/api.html#staticfile
with open(r'Ano-2022.json') as file:
    dados = json.load(file)

#create a Dataframe from json file
df1 = pd.DataFrame(data = dados['dados'])

#create a new Dataframe with only necessary data
df2 = pd.DataFrame(data = df1[['nomeParlamentar','siglaPartido','valorLiquido']])

#transforming the column 'valorLiquido' into a float value
df2['valorLiquido'] = pd.to_numeric(df2['valorLiquido'])

#summing the amount spent by each parliamentarian
df3 = df2.groupby(['nomeParlamentar','siglaPartido']).sum()

#sorting the values ​​from who spent the most to the one who spent the least
df4 = df3.sort_values(by='valorLiquido',ascending=False)
