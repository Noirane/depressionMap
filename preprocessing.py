import pandas as pd


selected_columns = ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A', 'Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A', 
                    'gender', 'country', 'education', 'age', 'married']


file_path = 'originalDataset.csv'

# selecionar apenas as colunas desejadas
df = pd.read_csv(file_path, delimiter='\t', usecols=selected_columns)

#  linhas inicialmente no original 
initial_row_count = len(df)
print(f"Número inicial de linhas no originalDataset: {initial_row_count}")

#  'NONE' por NaN
df.replace('NONE', pd.NA, inplace=True)

# Eliminar as linhas com NaN (valores vazios) em qualquer coluna
df.dropna(inplace=True)

#  filtragem
criteria = {
    'education': (1, 4),  
    'gender': (1, 3),     
    'married': (1, 3),    
    'age': (18, 100)      
}

# critério de filtragem ao DataFrame original
for column, (low, high) in criteria.items():
    df = df[df[column].between(low, high)]

# participantes por país
country_counts = df['country'].value_counts()

# países com 30 ou mais participantes
countries_with_min_participants = country_counts[country_counts >= 30].index

# apenas os países com 30 ou mais participantes
df_filtered = df[df['country'].isin(countries_with_min_participants)]

# qts de linhas após todos os filtros (antes da seleção das 24.655 linhas)
filtered_row_count = len(df_filtered)
print(f"Número de linhas após todos os filtros: {filtered_row_count}")


df_balanced = df_filtered.groupby('country').apply(lambda x: x.sample(n=30, random_state=1))


df_balanced.reset_index(drop=True, inplace=True)

#  se o número de linhas restantes é menor que 24.655 e completar com amostras aleatórias
desired_row_count = 24655
remaining_rows_balanced = len(df_balanced)

if remaining_rows_balanced < desired_row_count:
    remaining_needed = desired_row_count - remaining_rows_balanced
    additional_samples = df_filtered.sample(n=remaining_needed, random_state=1)
    

    df_balanced = pd.concat([df_balanced, additional_samples], ignore_index=True)

# Subtrai 1 das questões 
item_columns = ['Q3A', 'Q5A', 'Q10A', 'Q13A', 'Q16A', 'Q17A', 'Q21A', 'Q24A', 'Q26A', 'Q31A', 'Q34A', 'Q37A', 'Q38A', 'Q42A']
df_balanced[item_columns] = df_balanced[item_columns] - 1

# Adicionar a coluna soma_depressao
df_balanced['soma_depressao'] = df_balanced[item_columns].sum(axis=1)

# índice de depressão
def mapear_indice_depressao(pontuacao):
    if pontuacao <= 9:
        return 0
    elif pontuacao <= 13:
        return 1
    elif pontuacao <= 20:
        return 2
    elif pontuacao <= 27:
        return 3
    else:
        return 4

df_balanced['indice_depressao'] = df_balanced['soma_depressao'].apply(mapear_indice_depressao)


df_balanced['country'] = df_balanced['country'].astype('category')

#legenda dos paises 
country_legend = {number: country for number, country in enumerate(df_balanced['country'].cat.categories, 1)}
print("Legenda para a coluna 'country':")
for number, country in country_legend.items():
    print(f"{number}: {country}")

# ssubstituir as siglas 
df_balanced['country'] = df_balanced['country'].cat.codes + 1 

# final 
df_balanced.to_csv('dataset.csv', index=False)


final_row_count = len(df_balanced)
print(f"Número de linhas finais no dataset balanceado: {final_row_count}")


country_counts_balanced = df_balanced['country'].value_counts()
print("Quantidade de participantes por país no balancedDataset final:")
print(country_counts_balanced)

'''Número inicial de linhas no originalDataset: 39775
Número de linhas após todos os filtros: 30893

1: AE
2: AR
3: AT
4: AU
5: BE
6: BN
7: BR
8: CA
9: CH
10: CZ
11: DE
12: DK
13: EG
14: ES
15: FI
16: FR
17: GB
18: GR
19: HK
20: HR
21: HU
22: ID
23: IE
24: IN
25: IT
26: JM
27: JP
28: MX
29: MY
30: NL
31: NO
32: NZ
33: PH
34: PK
35: PL
36: PT
37: RO
38: RS
39: RU
40: SA
41: SE
42: SG
43: TR
44: US
45: VN
46: ZA'''

