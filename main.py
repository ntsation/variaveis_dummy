import pandas as pd


data = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro'],
    'Idade': [28, 34, 29, 40],
    'País': ['Brasil', 'Portugal', 'Brasil', 'Espanha']
}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)


df_dummies = pd.get_dummies(df, columns=['País'], prefix='País')
print("\nDataFrame com variáveis dummy:")
print(df_dummies)
