lista = ['Final',1,2,3,4]
lista.insert(len(lista), 5)
print(lista)
for i in range(1):
    lista.insert(1, lista[-1])
    lista.pop()
    print(lista)