import pandas as pd

# df = pd.read_csv('MenuMcDonalds.csv',encoding = 'latin1')
df = pd.read_csv('MenuMcDonalds.csv')
#print(df.head())

print(df.info())
print(df.describe())
print(df.isnull().sum())

print(df[['Calories', 'Total Fat', 'Protein', 'Carbohydrates']].mean())

print(df.groupby('Category')[['Calories', 'Total Fat', 'Protein', 'Carbohydrates']].mean())

desayunos_saludables = df[(df['Category']=='Breakfast') & (df['Calories']<500) & (df['Protein']>17) & (df['Carbohydrates']<60) & (df['Total Fat']<20)]
desayunos_saludables.to_csv('desayunos_saludables.csv', index=False)

comidas_saludables = df[(df['Calories']<500) & (df['Protein']>17) & (df['Carbohydrates']<60) & (df['Total Fat']<20)]
comidas_saludables.to_csv('comidas_saludables.csv', index=False)

print(comidas_saludables[['Category','Item','Calories','Protein','Carbohydrates','Total Fat']])

print('¿Cuál es el alimento más calórico del menú?')
#print(df.loc[df['Calories'].idxmax(), ['Item', 'Calories']])
print(df.sort_values('Calories', ascending=False).head(5)[['Item', 'Calories']])




print('¿Cuál tiene más proteína?')
print(df.loc[df['Protein'].idxmax(), ['Item', 'Protein']])



print('Promedio de calorías por tipo de comida:')




print(df.groupby('Category')['Calories'].mean().sort_values(ascending=False))

print('Proporción entre proteína y grasa (indicador de "saludable"):')



df['Protein_to_Fat'] = df['Protein'] / df['Total Fat']
print(df.sort_values('Protein_to_Fat', ascending=False).head(10))

