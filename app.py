import pandas as pd

ARQUIVO = 'data.json'

dados = pd.read_json(ARQUIVO)


dados.to_csv('data.csv',
             sep=',', 
             index=False,
             columns=dados.columns[1:])