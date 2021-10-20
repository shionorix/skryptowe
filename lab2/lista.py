print('Ładowanie modułu "{0}"'.format(__name__))

lista = []

def zapisz(arg):
    for i in range(0,10):
        count = arg.count(str(i))
        if count != 0:
            lista.append([i, count])

def wypisz():
    for i in range(len(lista)):
        print(lista[i][0], end=':')
        print(lista[i][1], end=', ')

print('Załadowano moduł "{0}"'.format(__name__))