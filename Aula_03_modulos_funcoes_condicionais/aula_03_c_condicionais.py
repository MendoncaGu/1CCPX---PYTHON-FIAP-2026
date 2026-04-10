#OPERADORES DE ATRIBUICAO
num = 15
print(num)

num = num + 2
print(num)

num *=2
print(num)

#OPERADORES RELACIONAIS

print()
print(6 >= 6)

#OPERADORES LOGICOS
# LOGICA E

print()

verifica_email = True
verifica_senha = True

login = verifica_email and verifica_senha
print(login)

if login:
 print("entrar no programa")
else:
 print("errado")

 #NOTAS...
 print()

nota_final = 3

if nota_final < 4:
 print("reprovado")

elif nota_final < 6:
 print("recuperação")

else:
 print("aprovado")

