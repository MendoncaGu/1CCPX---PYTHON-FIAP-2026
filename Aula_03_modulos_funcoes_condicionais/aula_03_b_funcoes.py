def print_lyrics():
    print("e o caba vai indoida é?")

    print_lyrics()
    print_lyrics()

def boas_vindas(nome):
    print(f"Olá {nome}!! Seja bem-vindo")

nome_digitado = input("digite seu nome: ")
boas_vindas(nome_digitado)

def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(27, 12))
print(type(nome_digitado))