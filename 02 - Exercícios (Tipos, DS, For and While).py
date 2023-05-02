# Databricks notebook source
# MAGIC %md
# MAGIC ### 1. Crie um programa em Python que receba uma string como entrada e imprima uma nova string com os caracteres na ordem inversa.

# COMMAND ----------

string_inicial = str(input("Insira uma string: "))
string_inversa = string_inicial[::-1]
print(string_inversa)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras em ordem inversa.

# COMMAND ----------

palavras = string_inicial.split()
palavras_inversas = palavras[::-1]
texto_inverso = " ".join(palavras_inversas)
print(texto_inverso)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 3. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as vogais substituídas por asteriscos (*)

# COMMAND ----------

vogais = "aeiouAEIOU"
string_asterisco = ""

for letra in string_inicial:
  if letra in vogais:
    string_asterisco += "*"
  else:
    string_asterisco += letra
print(string_asterisco)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 4. Crie um programa em Python que receba uma string como entrada e imprima outra string com todas as palavras que começam com letra maiúscula.

# COMMAND ----------

for palavra in palavras:
  if palavra == palavra.title():
    print(palavra, end=" ")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 5. Crie um programa em Python que receba uma string como entrada e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma da esquerda para a direita e da direita para a esquerda).

# COMMAND ----------

texto = input("Digite uma string: ").lower().replace(" ", "")
if texto[::-1] == texto:
  print(f"{texto.upper()} é um palíndormo")
else:
  print(f"{texto.upper()} não é um palíndormo")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 6. Crie um programa em Python que receba uma string como entrada e verifique se ela é um anagrama de outra string. (ou seja, se elas possuem as mesmas letras em quantidades diferentes)

# COMMAND ----------

texto1 = input("Digite a primeira string: ")
texto2 = input("Digite a segunda string: ")

# Usando apenas Len
print("--- Usando for e if ---")
count = 0
if len(texto1) == len(texto2):
  for i in texto1:
    for j in texto2:
      if i == j:
        count += 1
        if count == len(texto1):
          print("É um Anagrama")
else:
  print("Não é um Anagrama")

# Usando sorted
print("--- Usando Sorted ---")
texto1_ordenado = sorted(texto1)
texto2_ordenado = sorted(texto2)

if texto1_ordenado == texto2_ordenado:
  print("É um Anagrama")
else:
  print("Não é um Anagrama")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 7. Crie um programa em Python que receba uma string como entrada e imprima outra string que é formada pela primeira letra de cada palavra da string original.

# COMMAND ----------

texto = input("Digite uma string: ")
nova_string = ""

for palavra in texto.split():
  nova_string += palavra[0]
print(nova_string)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 8. Crie um programa em Python que receba uma tupla de números inteiros como entrada e retorne uma nova tupla contendo apenas os números primos.

# COMMAND ----------

numeros = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
lista_primos = []

for num in numeros:
  if num > 1:
    for i in range(2,num):
      if num % i == 0:
        break
    else:
      lista_primos.append(num)
        
print(tuple(lista_primos))      

# COMMAND ----------

# MAGIC %md
# MAGIC ### 9. Crie um programa em Python que receba duas tuplas de números inteiros como entrada e retorne uma nova tupla contendo apenas os elementos que aparecem em ambas as tuplas.

# COMMAND ----------

lista1 = []
lista2 =[]
lista_3 = []

qntd_itens = int(input("Digite a quantidade de itens desejados (No máximo 5): "))   

for i in range(0,qntd_itens):
  a = int(input(f"Digite o {i+1}º valor da tupla 1: "))
  lista1.append(a)
print(f"A primeira tupla é a seguinte: {tuple(lista1)}") 

for j in range(0,qntd_itens):
  b = int(input(f"Digite o {j+1}º valor da tupla 2: "))
  lista2.append(b)
print(f"A segunda tupla é a seguinte: {tuple(lista2)}")

for num_1 in lista1:
  for num_2 in lista2:
    if num_1 == num_2:
      lista_3.append(num_1)
print(f"Os elementos que aparecem em ambas as tuplas são: {tuple(lista_3)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 10. Crie um programa em Python que receba uma tupla de strings como entrada e retorne uma nova tupla contendo apenas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

lista_4 = []
tupla = ("arara", "casa", "mala", "ovo", "paralelepípedo", "pato")
for palavra in list(tupla):
  if palavra[0] == palavra[-1]:
    lista_4.append(palavra)
      
nova_tupla = tuple(lista_4)
print(nova_tupla)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 11. Crie um programa em Python que receba uma lista de números inteiros como entrada e retorne uma nova lista contendo apenas os números que aparecem um número ímpar de vezes.

# COMMAND ----------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1,3]
contagem = []

for num in numeros:
  if (numeros.count(num) % 2) != 0:
      contagem.append(num)
print(list(set(contagem)))

# COMMAND ----------

# MAGIC %md
# MAGIC ### 12. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em pelo menos uma das listas, mas não em ambas.

# COMMAND ----------

lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [4, 5, 6, 7, 8, 9, 10]
lista3 = []

for i in lista1:
    if i not in lista2:
      lista3.append(i)
for j in lista2:
    if j not in lista1:
      lista3.append(j)
      
print(lista3)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 13. Crie um programa em Python que receba duas listas de números inteiros como entrada e retorne uma nova lista contendo apenas os elementos que aparecem em ambas as listas, mas sem repetições.

# COMMAND ----------

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

lista3 = list(set(lista1).intersection(set(lista2)))
print(lista3)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 14. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um produto com nome e preço, e retorne o nome do produto mais caro.

# COMMAND ----------

produtos = [{"nome": "celular", "preco": 1500},
            {"nome": "notebook", "preco": 3500},
            {"nome": "tablet", "preco": 1200},
            {"nome": "fones de ouvido", "preco": 200},
            {"nome": "smartwatch", "preco": 800}]

produto_mais_caro = max(produtos, key=lambda produto: produto["preco"])["nome"]
print(produto_mais_caro)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 15. Crie um programa em Python que receba um dicionário como entrada, onde as chaves representam nomes de produtos e os valores representam as quantidades disponíveis em estoque, e retorne o nome do produto com estoque mais baixo.

# COMMAND ----------

estoque = {"celular": 50, "notebook": 20, "tablet": 100, "fones de ouvido": 5, "smartwatch": 15}
valor_mais_baixo = max(estoque.values())
nome = ""

for produto, valores in estoque.items():
  if valores < valor_mais_baixo:
    valor_mais_baixo = valores
    nome = produto
print(nome.upper())

# COMMAND ----------

# MAGIC %md
# MAGIC ### 16. Crie um programa em Python que receba uma lista de dicionários como entrada, onde cada dicionário representa um aluno com nome e notas em diferentes disciplinas, e retorne o nome do aluno com a maior média ponderada, sendo que a média ponderada deve ser calculada utilizando as notas como pesos.

# COMMAND ----------

alunos = [{"nome": "João", "notas": {"Matemática": 8.5, "Português": 9.0, "História": 7.0}},
          {"nome": "Maria", "notas": {"Matemática": 9.5, "Português": 8.5, "História": 6.0}},
          {"nome": "Pedro", "notas": {"Matemática": 7.0, "Português": 6.5, "História": 9.0}},
          {"nome": "Ana", "notas": {"Matemática": 8.0, "Português": 7.5, "História": 8.0}}]
maior_media = 0
nome_aluno = ""

for aluno in alunos:
  media = sum(aluno["notas"].values()) / len(aluno["notas"])
  if media > maior_media:
    maior_media = media
    nome_aluno = aluno["nome"]
print(f"O aluno com a maior média é {nome_aluno} com a seguinte nota: {round(maior_media,2)}")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 17. Crie um programa em Python que receba três números como entrada e imprima "Maior" se o primeiro número for maior do que a soma dos outros dois, "Menor" se o primeiro número for menor do que a soma dos outros dois, ou "Igual" caso contrário.

# COMMAND ----------

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > (num2 + num3):
  print("Maior")
elif num1 < (num2 + num3):
  print("Menor")
else:
  print("Igual")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 18. Crie um programa em Python que receba a idade e a altura de uma pessoa como entrada e classifique-a de acordo com as seguintes regras: se a idade for menor do que 18 anos e a altura for menor do que 1,60 m, imprimir "Adolescente Baixo"; se a idade for menor do que 18 anos e a altura for maior do que 1,60 m, imprimir "Adolescente Alto"; se a idade for maior ou igual a 18 anos e a altura for menor do que 1,60 m, imprimir "Adulto Baixo"; se a idade for maior ou igual a 18 anos e a altura for maior do que 1,60 m, imprimir "Adulto Alto".

# COMMAND ----------

idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

if idade < 18 and altura < 1.60:
  print("Adolescente Baixo")
elif idade < 18 and altura > 1.60:
  print("Adolescente Alto")
elif idade >= 18 and altura < 1.60:
  print("Adulto Baixo")
elif idade >= 18 and altura > 1.60:
  print("Adulto Alto")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 19. Crie um programa em Python que receba uma string como entrada e imprima "Palíndromo" se a string for um palíndromo (ou seja, se a string lida de trás para frente for igual à string original), ou "Não Palíndromo" caso contrário.

# COMMAND ----------

texto = input("Digite um texto: ").lower().replace(" ", "")
if texto == texto[::-1]:
  print(f"{texto} é um palíndromo")
else:
  print(f"{texto} não é um palíndromo")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 20. Crie um programa em Python que receba uma lista de números inteiros como entrada e calcule a soma dos quadrados dos números ímpares da lista.

# COMMAND ----------

numeros = [2, 5, 9, 12, 18, 23, 27, 30, 35, 40]
soma = 0

for numero in numeros:
  if numero % 2 != 0:
    soma += (numero ** 2)
print(soma)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 21. Crie um programa em Python que receba uma string como entrada e imprima a string sem as vogais.

# COMMAND ----------

vogais = "aeiouAEIOU"
string = str(input("Digite uma string: "))
string_sem_vogal = ""

for letra in string:
  if letra in vogais:
    string_sem_vogal += ""
  else:
    string_sem_vogal += letra
print(string_sem_vogal)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 22. Crie um programa em Python que imprima a soma dos n primeiros números primos, onde n é um número fornecido pelo usuário.

# COMMAND ----------

n = int(input("Digite um número: "))
lista = []
soma = 0

for i in range(0,n):
  lista.append(i)
  
for numero in lista:
  if numero > 1:
    for i in range(2,numero):
      if numero % i == 0:
        break
    else:
      soma += numero

print(f"A soma de todos os valores primos que antecedem o número {n} é {soma}.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 23. Crie um programa em Python que receba uma lista de números e imprima a soma dos números pares e a soma dos números ímpares presentes na lista.

# COMMAND ----------

numeros = [1, 2, 3, 4, 5, 6]
total_par = 0
total_impar = 0

for numero in numeros:
  if numero % 2 == 0:
    total_par += numero
  else:
    total_impar += numero
print(f"A soma total dos valores pares é de {total_par} e a soma total dos valores ímpares é de {total_impar}.")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 24. Crie um programa em Python que receba uma lista de strings e retorne uma lista com todas as strings que começam e terminam com a mesma letra.

# COMMAND ----------

palavras = ["amor", "futebol", "verdade", "banana", "arara", "casa", "sol"]
palavras_selecionadas = []
for palavra in palavras:
  if palavra[0] == palavra[-1]:
    palavras_selecionadas.append(palavra)
print(palavras_selecionadas)

# COMMAND ----------

# MAGIC %md
# MAGIC ### 25. Crie um programa em Python que leia um número do usuário e verifique se ele é um número perfeito. Um número perfeito é aquele que é igual à soma de seus divisores próprios (ou seja, a soma de seus fatores inteiros positivos, excluindo ele próprio).

# COMMAND ----------

numero = int(input("Digite um número: "))
lista = []
soma = 0

for n in range(1,numero):
  if numero % n == 0:
    lista.append(n)
    soma += n

if soma == numero:
  print(f"{numero} é perfeito")
else:
  print(f"{numero} não é perfeito")

# COMMAND ----------

# MAGIC %md
# MAGIC ### 26. Crie um programa em Python que calcule a série de Fibonacci para um determinado número de termos fornecido pelo usuário. A série de Fibonacci é uma sequência em que cada número é a soma dos dois números anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ...

# COMMAND ----------

termos = int(input("Digite o número de termos desejados: "))
fibonacci = [0, 1]
i = 2

for n in range(termos - i):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(fibonacci)