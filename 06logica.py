usuario_correto = "admin"
senha_correta = "1234"

tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    tentativas += 1

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo! Login efetuado com sucesso.")
        break
    else:
        print(f"Credenciais incorretas. Tentativas restantes: {limite_tentativas - tentativas}")
else:
    for _ in range(3):
        print("Acesso bloqueado")
