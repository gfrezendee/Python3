def criar_dicionario_pet(nome_pet):

  tipo_pet = input(f"Digite o tipo de {nome_pet}: ")
  nome_dono = input(f"Digite o nome do dono de {nome_pet}: ")

  if not nome_dono:  # Verifica se o nome do dono é vazio
      print("Erro: Nome do dono não pode ser vazio.")
      return None  # Retorna None para indicar erro

  pet_dicionario = {
      "tipo": tipo_pet,
      "nome": nome_pet,
      "nome_dono": nome_dono
  }

  return pet_dicionario

pets = []

while True:
  nome_pet = input("Digite o nome do animal de estimação (ou 0 para finalizar): ").strip()
  if nome_pet.lower() == "0":  # Verifica se o nome em minúsculas é igual a "0"
      break

  pet_dicionario = criar_dicionario_pet(nome_pet)
  pets.append(pet_dicionario)

for pet in pets:
  if pet is None:  # Verifica se houve erro ao criar o dicionário
      continue  # Pula para o próximo animal se houver erro

  print("\nInformações do Animal de Estimação:")
  print(f"Nome: {pet['nome']}")
  print(f"Tipo: {pet['tipo']}")
  print(f"Dono: {pet['nome_dono']}")
