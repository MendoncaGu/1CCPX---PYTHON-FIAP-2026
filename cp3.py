temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_risco = 0
sala_maior_risco = 0


for i in range(len(temperaturas)):
    sala = temperaturas[i]
    media = sum(sala) / len(sala)

    critico = 0

    for temperatura in sala:
        if temperatura >= 33:
            critico += 1

    print(f"Sala {i + 1}")
    print(f"Média: {media}")
    print(f"Registros críticos: {critico}")

    print()


    if critico > maior_risco:
        maior_risco = critico
        sala_maior_risco = i + 1

print(f"Sala com maior risco: Sala {sala_maior_risco}")
