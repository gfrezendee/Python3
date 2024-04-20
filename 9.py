def comparar_listas_detalhado():
  """
  Esta função permite ao usuário inserir duas listas e compara-as, 
  mostrando um histórico detalhado das modificações.
  """

  # Lista inicial
  lista_inicial = []
  while True:
    try:
      valor = int(input("Digite um valor para a Lista Inicial (ou 0 para finalizar): "))
      if valor == 0:
        break
      lista_inicial.append(valor)
    except ValueError:
      print("Valor inválido. Digite um número inteiro.")

  # Lista final
  lista_final = []
  while True:
    try:
      valor = int(input("Digite um valor para a Lista Final (ou 0 para finalizar): "))
      if valor == 0:
        break
      lista_final.append(valor)
    except ValueError:
      print("Valor inválido. Digite um número inteiro.")

  conjunto_inicial = set(lista_inicial)
  conjunto_final = set(lista_final)

  # Elementos que não mudaram
  iguais = conjunto_inicial & conjunto_final
  nao_mudaram = list(iguais)

  # Novos elementos
  novos = conjunto_final - conjunto_inicial
  novos_elementos = list(novos)

  # Elementos removidos
  removidos = conjunto_inicial - conjunto_final
  removidos_elementos = list(removidos)

  # Imprimindo o histórico de modificações
  print("\nHistórico de Modificações:")
  print(f"Elementos que não mudaram: {nao_mudaram}")
  print(f"Novos elementos: {novos_elementos}")
  print(f"Elementos removidos: {removidos_elementos}")

# Chamando a função para iniciar o programa
comparar_listas_detalhado()
