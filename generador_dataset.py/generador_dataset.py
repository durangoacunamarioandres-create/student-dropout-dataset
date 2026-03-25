import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

#  DEMOGRÁFICAS
edad = np.random.randint(17, 35, n)
genero = np.random.choice(['Masculino', 'Femenino'], n)
estado_civil = np.random.choice(['Soltero', 'Casado'], n)

#  ACADÉMICAS
promedio = np.round(np.random.uniform(2.0, 5.0, n), 2)
horas_estudio = np.random.randint(0, 10, n)
asistencia = np.random.randint(50, 100, n)

#  FINANCIERAS
beca = np.random.choice(['Si', 'No'], n)
prestamo = np.random.choice(['Si', 'No'], n)
nivel = np.random.choice(['Bajo', 'Medio', 'Alto'], n)
trabaja = np.random.choice(['Si', 'No'], n)

#  DROPOUT (lógica realista)
dropout = []
for i in range(n):
    riesgo = 0
    
    if promedio[i] < 3.0:
        riesgo += 2
    if horas_estudio[i] < 2:
        riesgo += 1
    if asistencia[i] < 70:
        riesgo += 2
    if nivel[i] == 'Bajo':
        riesgo += 1
    if trabaja[i] == 'Si':
        riesgo += 1

    if riesgo >= 3:
        dropout.append(np.random.choice(['Si', 'No'], p=[0.7, 0.3]))
    else:
        dropout.append(np.random.choice(['Si', 'No'], p=[0.2, 0.8]))

# Crear DataFrame
df = pd.DataFrame({
    'edad': edad,
    'genero': genero,
    'estado_civil': estado_civil,
    'promedio_notas': promedio,
    'horas_estudio': horas_estudio,
    'asistencia': asistencia,
    'beca': beca,
    'prestamo': prestamo,
    'nivel_socioeconomico': nivel,
    'trabaja': trabaja,
    'dropout': dropout
})

#  INTRODUCIR VALORES NULOS (5%)
for col in df.columns:
    df.loc[df.sample(frac=0.05).index, col] = np.nan

#  INTRODUCIR OUTLIERS
df.loc[df.sample(10).index, 'horas_estudio'] = 20
df.loc[df.sample(10).index, 'promedio_notas'] = 1.0
df.loc[df.sample(5).index, 'edad'] = 60

# Guardar
df.to_csv('dataset_estudiantes.csv', index=False)

print(df.head())