def dezMaiores(l, quantidade = 10):
    lista = l[:]
    if len(lista) < quantidade:
        quantidade = len(lista)
    maiores = []
    maior = indexMaior = index = 0
    for i in range(quantidade):
        while index < len(lista):
            if lista[index] > maior:
                maior = lista[index]
                indexMaior = index
            index += 1
        maiores.append(lista.pop(indexMaior))
        maior = index = 0
    return maiores
print(dezMaiores)