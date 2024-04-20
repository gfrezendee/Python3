def criar_dicionario_pessoa():

  nome = input("Digite o primeiro e último nome da pessoa (separados por espaço): ").split()
  idade = int(input("Digite a idade: "))
  cidade = input("Digite a cidade: ")

  pessoa = {
      "first_name": nome[0],
      "last_name": nome[1],
      "age": idade,
      "city": cidade
  }

  return pessoa

numero_pessoas = 3  # Quantidade de pessoas a cadastrar
people = []

for i in range(numero_pessoas):
  print(f"\nCadastro da Pessoa {i+1}:")
  pessoa = criar_dicionario_pessoa()
  people.append(pessoa)

for pessoa in people:
  print("\nInformações da Pessoa:")
  print(f"Nome: {pessoa['first_name']} {pessoa['last_name']}")
  print(f"Idade: {pessoa['age']}")
  print(f"Cidade: {pessoa['city']}")
