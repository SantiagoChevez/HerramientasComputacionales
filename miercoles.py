import pandas as pd


# Crear un Dataframe de ejemplo

data = {
    'Edad': [23, 25, 26, 24, 30, 24, 22, 28, 27, 24],
    'Salario':[48000, 52000, 58000, 49000, 60000, 48000, 50000, 62000, 59000, 54000]
}

df = pd.DataFrame(data)
print(df.describe())
print()

# Medidad de tendencia central
# Calcular la media
media_edad = df['Edad'].mean()
media_salario = df['Salario'].mean()

# Calcular la mediana
mediana_edad = df['Edad'].median()
mediana_salario = df['Salario'].median()

# Calcular la moda
moda_edad = df['Edad'].mode()[0]
moda_salario = df['Salario'].mode()[0]

#Medidas de dispersión
# Calcular el rango
rango_edad = df['Edad'].max() - df['Edad'].min()
rango_salario = df['Salario'].max() - df['Salario'].min()

# Calcular la varianza
varianza_edad = df['Edad'].var()
varianza_salario = df['Salario'].var()

# Calcular la desviación estándar
desviacion_edad = df['Edad'].std()
desviacion_salario = df['Salario'].std()

# Medidas de posición
# Calcular los percentiles
percentil_25_edad = df['Edad'].quantile(0.25)
percentil_50_edad = df['Edad'].quantile(0.50)
percentil_75_edad = df['Edad'].quantile(0.75)

percentil_25_salario = df['Salario'].quantile(0.25)
percentil_50_salario = df['Salario'].quantile(0.50)
percentil_75_salario = df['Salario'].quantile(0.75)

# Calcular los deciles
deciles_edad = df['Edad'].quantile([i/10 for i in range(1, 10)])
deciles_salario = df['Salario'].quantile([i/10 for i in range(1, 10)])

# Mostrar resultados
print('Medidas de tendencia central')
print(f'Media - Edad: {media_edad:0.3}, Salario: {media_salario:0.3}')
print(f'Mediana - Edad: {mediana_edad}, Salario: {mediana_salario}')
print(f'Moda - Edad: {moda_edad}, Salario: {moda_salario}')
print()

print('Medidas de dispersión')
print(f'Rango - Edad: {rango_edad}, Salario: {rango_salario}')
print(f'Varianza - Edad: {varianza_edad:0.3}, Salario: {varianza_salario:0.3}')
print(f'Desviación estándar - Edad: {desviacion_edad:0.3}, Salario: {desviacion_salario:0.3}')
print()

print('Medidas de posición')
print(f'Percentiles - Edad: 25%: {percentil_25_edad}, 50%: {percentil_50_edad}, 75%: {percentil_75_edad}')
print(f'Percentiles - Salario: 25%: {percentil_25_salario}, 50%: {percentil_50_salario}, 75%: {percentil_75_salario}')
print()
print(f'Deciles - Edad: {deciles_edad}')
print(f'Deciles - Salario: {deciles_salario}')
print()

