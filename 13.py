sandwich_orders = ["atum", "frango", "vegetariano", "queijo", "presunto"]
finished_sandwiches = []

for sandwich in sandwich_orders:
  print(f"Preparando sanduíche de {sandwich}...")

  # Simulando tempo de preparo
  import time
  time.sleep(2)

  finished_sandwiches.append(sandwich)
  print(f"Sanduíche de {sandwich} pronto!")

print("\nTodos os sanduíches estão prontos:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
