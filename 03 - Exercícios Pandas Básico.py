# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Ler e exibir um arquivo CSV usando pandas

# COMMAND ----------

import numpy as np
import pandas as pd
  
df = spark.read.csv("/FileStore/tables/Online_Retail.csv", header=True, sep=',')
df = df.toPandas()
df.head(5)

# COMMAND ----------

df.info()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Selecionar colunas específicas de um DataFrame usando pandas

# COMMAND ----------

df[['stock_code','unit_price']]

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Filtrar linhas com base em uma condição usando pandas

# COMMAND ----------

df.filter(like = 'no')

# COMMAND ----------

df[df['unit_price']      # Seleção da coluna
   .str.replace(",",".") # Atributo 'str' para fazer o replace e colocar no formato aceitável para conversão pra float
   .astype(float) > 95]  # Conversão e Filtro

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Agrupar dados com base em uma coluna usando pandas

# COMMAND ----------

df['quantity'] = df['quantity'].astype(int)                          # Conversão para int
df.groupby('stock_code').agg(Quantidade_Total = ('quantity', 'sum')) # Agegração da 'quantity' por agrupamento de 'stock_code'

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Usar a função max em alguma coluna do DataFrame

# COMMAND ----------

df['unit_price'].max()