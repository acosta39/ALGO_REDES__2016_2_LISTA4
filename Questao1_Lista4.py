nummeros = [

    [(input("Digite sua senha: ")), (input("Digite sua senha: "))],
    [(input("Digite sua senha: ")), (input("Digite sua senha: "))]

        ]

contador_senhas = 0

for linha in nummeros:
    for num in linha:
        if num == "4808":
            contador_senhas = contador_senhas + 1

            print('Bem vindo!')

            exit(0)


        else:
            print("Usuário não cadastrado")
