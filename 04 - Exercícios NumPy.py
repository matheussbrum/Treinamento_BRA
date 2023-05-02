# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Criar um array com 10 números inteiros aleatórios entre 1 e 50 e calcular a média e o desvio padrão

# COMMAND ----------

import numpy as np

arr = np.random.rand(50)
print(np.mean(arr))
print(np.std(arr))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Criar um array de 10 números aleatórios e calcular a raiz quadrada de todos os valores menores ou iguais a 0,5

# COMMAND ----------

arr_2 = np.random.rand(10)
print(arr_2)

for i in arr_2:
  if i <= 0.5:
    print(np.sqrt(i))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Criar uma matriz 3D de tamanho 3x3x3 com valores aleatórios e exibir o valor máximo de cada linha de cada matriz 2D dentro dessa matriz 3D

# COMMAND ----------

matriz_3D = np.random.rand(3,3,3)
max_linha = np.amax(matriz_3D, axis = 1) # Axis = 1 --> Linha / Axis = 0 --> Coluna

print("Valor de cada linha:\n", matriz_3D)
print("\nValor máximo de cada linha:\n",max_linha)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Criar uma matriz de tamanho 5x5 com valores aleatórios e subtrair a média de cada linha dessa matriz

# COMMAND ----------

matriz_5x5 = np.random.rand(5,5)
 
media = np.average(matriz_5x5, axis = 1) # Axis = 1 --> Linha / Axis = 0 --> Coluna
sub_media = matriz_5x5 - media[:, np.newaxis]

print("Matriz:\n", matriz_5x5)
print("\nMédia de cada linha:\n", media)
print("\nSubtração da média de cada linha:\n", sub_media)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Criar uma matriz de tamanho 4x4 com valores aleatórios e calcular a média e o desvio padrão das diagonais da matriz

# COMMAND ----------

matriz_4x4 = np.random.rand(4,4)
diagonais_matriz = np.diag(matriz_4x4)
media_matriz_4x4 = np.average(diagonais_matriz)
desvio_matriz_4x4 = np.std(diagonais_matriz)

print("Matriz 4x4:\n",matriz_4x4)
print("\nDiagonais da matriz:\n", diagonais_matriz)
print("\nMedia das diagonais da matriz:\n", media_matriz_4x4)
print("\nDesvio padrão das diagonais da matriz:\n ", desvio_matriz_4x4)