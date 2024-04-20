def comparar_listas():

  # Lista 1
  lista1 = []
  while True:
    try:
      valor = int(input("Digite um valor para a Lista 1 (ou 0 para finalizar): "))
      if valor == 0:
        break
      lista1.append(valor)
    except ValueError:
      print("Valor inválido. Digite um número inteiro.")

  # Lista 2
  lista2 = []
  while True:
    try:
      valor = int(input("Digite um valor para a Lista 2 (ou 0 para finalizar): "))
      if valor == 0:
        break
      lista2.append(valor)
    except ValueError:
      print("Valor inválido. Digite um número inteiro.")

  # Elementos em comum
  em_comum = []
  for elemento in lista1:
    if elemento in lista2:
      em_comum.append(elemento)

  # Elementos únicos na Lista 1
  unicos_lista1 = []
  for elemento in lista1:
    if elemento not in lista2:
      unicos_lista1.append(elemento)

  # Elementos únicos na Lista 2
  unicos_lista2 = []
  for elemento in lista2:
    if elemento not in lista1:
      unicos_lista2.append(elemento)

  # Imprimindo os resultados
  print("\nResultados da comparação:")
  print(f"Lista 1: {lista1}")
  print(f"Lista 2: {lista2}")
  print(f"Elementos em comum: {em_comum}")
  print(f"Elementos únicos na Lista 1: {unicos_lista1}")
  print(f"Elementos únicos na Lista 2: {unicos_lista2}")

# Chamando a função para iniciar o programa
comparar_listas()
