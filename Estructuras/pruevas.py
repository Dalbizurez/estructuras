lista = ['cola', '<>', '1', '<>', '2', '<>', '3', '<>', '4']


for x in range(1, 4 + 1):
    lista = ['cola', '<>', '1', '<>', '2', '<>', '3', '<>', '4']

    lista.insert(-((x * 2)), '<>')
    lista.insert(-((x * 2)), '5')

    print(lista, x)
