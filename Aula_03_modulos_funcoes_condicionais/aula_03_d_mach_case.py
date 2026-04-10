#programa que recebe a escolha do usuario
# 0 = sair
# 1 = entrar
# --- = erro

escolha_usuario = 1

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("erro 404")
