while True:
    username = input("Username?")
    if username != "panda":
        print("Usuário inválido")
        continue
    senha = input("Qual a sua senha?")
    if senha == "1234":
        print(f"Bem vindo, {username}")
        break