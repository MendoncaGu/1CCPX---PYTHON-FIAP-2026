# lista_frutas = ["Morango", "Maça", "Uva"]
#
# print(lista_frutas[1])
#
# lista_frutas.append("Melancia")
# print(lista_frutas[3])
# print()
#
# for i in range(len(lista_frutas)):
#     print(lista_frutas[i])
#
#     print()
#
#     for fruta in lista_frutas:
#         print(fruta)

#METODDO DESCOBERTO

nomes = ["Ana", "Maria", "Vini", "Mat"]
#
for i in range(len(nomes)):
    for j in range(len(nomes)):
        if (i < j):
            print(nomes[i], nomes[j])
print()

# METODO MOSTRADO

for i in range(0, len(nomes)):
    for j in range(i+1,len(nomes)):
        print(nomes[i], nomes[j])