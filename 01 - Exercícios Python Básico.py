# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Some todos os números de 1 até 100

# COMMAND ----------

i = 0
for num in range(1,101):
    i += num
print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Some todos os números pares de 1 até 100

# COMMAND ----------

i = 0
for num in range(1,101):
  if num % 2 == 0:
    i += num
print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Some todos os números ímpares de 1 até 100

# COMMAND ----------

i = 0
for num in range(1,101):
  if num % 2 != 0:
    i += num
print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Dada a lista abaixo, some todos os elementos inteiros positivos

# COMMAND ----------

lista = [-2, 2, 'celular', 10, -99, False]
lista

# COMMAND ----------

i = 0
for elemento in lista:
  if type(elemento) == int:
    if elemento > 0:
      i += elemento
print(i)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Dada a String

# COMMAND ----------

string = 'pYthOn É A mELhoR LiNguaGEM De PRoGRaMaçãO'

# COMMAND ----------

# MAGIC %md
# MAGIC Formate-a com as primeiras letras maiúsculas:

# COMMAND ----------

string.title()

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras minúsculas

# COMMAND ----------

string.lower()

# COMMAND ----------

# MAGIC %md
# MAGIC Com todas as letras maiúsculas

# COMMAND ----------

string.upper()