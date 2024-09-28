import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('contato.csv', header=None, names=['Contato'])

# Separar nome e telefone, tratando erros
split_columns = df['Contato'].str.split(': ', expand=True, n=1)

# Criar colunas separadas, assegurando que não geramos um erro
df['Nome'] = split_columns[0]  # Coluna 0 é o nome
df['Telefone'] = split_columns[1] if 1 in split_columns else ''  # Verifica se existe a coluna 1

# Preencher as colunas vazias com strings vazias
df['Telefone'] = df['Telefone'].fillna('')

# Remover '+12' do final da coluna 'Telefone' e manter o número completo
df['Telefone'] = df['Telefone'].str.replace(r'\+12$', '', regex=True).str.strip()

# Salvar o novo arquivo CSV
df[['Nome', 'Telefone']].to_csv('contatos_separados.csv', index=False)
