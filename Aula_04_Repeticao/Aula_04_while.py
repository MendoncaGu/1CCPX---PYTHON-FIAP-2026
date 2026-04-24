cp = 0
while cp < 3:
    print(f'produto {cp}')
    cp += 1

# while decrecente de 4 até 1 (incluindo)
i = 4
while i >= 0:
    print(i)
    i -= 1

# repetição com entrada do usuario
jogar = "sim"

while jogar.lower() == "sim":
    print("Iniciar ou repetier o jogo?")
    jogar = input("Deseja jogar novamente? ")

i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 10:
        break

    print(f"produto {i}")

