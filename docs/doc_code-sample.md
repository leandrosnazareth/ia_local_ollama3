
    **Title:** Filtering a DataFrame using Pandas in Python

**Description:**

In this example, we demonstrate how to filter a Pandas DataFrame based on a specific condition. We use the `pandas` library to create a DataFrame from a dictionary and then apply filtering using Boolean indexing.

**Code:**
```python
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
```

**Output:**

**DataFrame Original:**
```
   Nome  Idade          Cidade
0    Ana     25       São Paulo
1   Bruno     32      Rio de Janeiro
2  Carlos     45   Belo Horizonte
3   Diana     29      Curitiba
4 Eduardo     35    Porto Alegre
5 Fernanda     28         Recife
6 Gabriel     40       Fortaleza
7 Helena     33        Salvador
8    Igor     22     Brasília
9   Júlia     41          Natal
```

**DataFrame Filtrado (idade > 30):**
```
      Nome  Idade          Cidade
1    Bruno     32      Rio de Janeiro
2  Carlos     45   Belo Horizonte
4 Eduardo     35    Porto Alegre
6 Gabriel     40       Fortaleza
7 Helena     33        Salvador
9   Júlia     41          Natal
```

In this example, we create a DataFrame `df` from the dictionary `data`. Then, we filter the DataFrame to only include rows where the value in the `Idade` column is greater than 30. The resulting filtered DataFrame is printed to the console.

    ## Source Code (`./src/code-sample.py`)
    
    