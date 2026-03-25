# Dataset Sintético de Deserción Estudiantil

##  Descripción
Este dataset simula información de estudiantes con el objetivo de analizar la deserción estudiantil utilizando técnicas de Machine Learning.

Contiene 500 registros donde cada fila representa un estudiante.

---

##  Variables

###  Demográficas
- edad: Edad del estudiante (17 – 35)
- genero: Masculino, Femenino
- estado_civil: Soltero, Casado

###  Académicas
- promedio_notas: 2.0 – 5.0
- horas_estudio: 0 – 10
- asistencia: 50 – 100

###  Financieras
- beca: Sí/No
- prestamo: Sí/No
- nivel_socioeconomico: Bajo, Medio, Alto
- trabaja: Sí/No

###  Variable objetivo
- dropout: Indica si el estudiante desertó (Sí/No)

---

##  Valores faltantes
Se introdujeron valores nulos de forma aleatoria en el 5% de los datos de cada variable para simular problemas reales.

---

##  Valores extremos (outliers)
Se agregaron valores extremos como:

- horas_estudio: hasta 20 horas  
- promedio_notas: valores bajos como 1.0  
- edad: valores altos como 60 años  

---

##  Herramientas utilizadas
- Python  
- pandas  
- numpy  

---

##  Uso
Este dataset será utilizado para entrenar modelos de Machine Learning para predecir la deserción estudiantil.
