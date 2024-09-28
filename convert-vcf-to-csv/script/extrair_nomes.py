import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('contato.csv', header=None, names=['Contato'])

# Separar nome e telefone
split_columns = df['Contato'].str.split(': ', expand=True)

# Criar uma nova coluna só com os nomes
df['Nome'] = split_columns[0]

# Salvar em um novo arquivo, incluindo apenas a coluna de nomes
df[['Nome']].to_csv('nomes_separados.csv', index=False)
