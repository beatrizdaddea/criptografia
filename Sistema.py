# Listas e variáveis do sistema
lista_cargo = ['Capitão', 'Almirante']  # Pessoas liberdada para entrar ao navio
acesso = False
cont_tentativa = 0

# Tela de acesso ao navio
decoracao = '-' * 70
print(decoracao)
print('Tela de Controle de Acesso ao Navio'.center(70))
print(decoracao)

# Verifica se a patente está na lista e limita a apenas 3 tentativas de acesso

while cont_tentativa < 3:
    acesso_cargo = input("Digite o seu cargo: ")
    # acesso_cargo = acesso_cargo.replace(" ", "")
    # verifica se o cargo inserida é válido
    for patente in lista_cargo:
        if acesso_cargo == patente:
            acesso = True
    if not acesso:
        # Se o cargo não estiver na lista
        cont_tentativa += 1
        tentativas = 3 - cont_tentativa
        print("Não é possivel acessar ao Navio.")
        if cont_tentativa == 3:
            # Quando o usuário tenta logar por mais de três vezes
            print("O sistema será fechado por segurança")
            exit()
        print("Você tem {} tentativa(s) para acessar.".format(tentativas))
    if acesso:
        # Quando a patetente do usuário é válida irá liberar o login e senha
        login = input("Digite o seu login:")
        senha = input("Digite a sua senha:")

        exit()
        # Precisa comparar com o login e senha do banco de dados para liberar o acesso
