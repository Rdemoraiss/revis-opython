idades = [12, 17, 18, 22, 15, 30]
maiores_de_idade = []

indice = 0

while indice < len(idades):
    if idades[indice] >= 18:
        maiores_de_idade.append(idades[indice])
    indice += 1

print(maiores_de_idade)  