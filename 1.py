def conta_caracteres(frase):

  dicionario = {}
  for letra in frase:
    if letra in dicionario:
      dicionario[letra] += 1
    else:
      dicionario[letra] = 1
  return dicionario

print("Gerador de dicionário \n")

# Recebendo frase do usuário
frase = input("Digite uma frase: ")

# Gerando e imprimindo o dicionário
contagem_caracteres = conta_caracteres(frase)
print(f"\n {contagem_caracteres}")
