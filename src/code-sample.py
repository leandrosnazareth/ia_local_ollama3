import pandas as pd

data = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Júlia'],
    'Idade': [25, 32, 45, 29, 35, 28, 40, 33, 22, 41],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre', 'Recife', 'Fortaleza', 'Salvador', 'Brasília', 'Natal']
}

df = pd.DataFrame(data)

print("DataFrame Original:")
print(df)

filtered_df = df[df['Idade'] > 30]

print("\nDataFrame Filtrado (idade > 30):")
print(filtered_df)
