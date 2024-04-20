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

pessoa_dicionario = criar_dicionario_pessoa()

print(f"Nome: {pessoa_dicionario['first_name']} {pessoa_dicionario['last_name']}")
print(f"Idade: {pessoa_dicionario['age']}")
print(f"Cidade: {pessoa_dicionario['city']}")
