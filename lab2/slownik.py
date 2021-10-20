print('Ładowanie modułu "{0}"'.format(__name__))
############################################
slownik = {}

def zapisz(arg):
    for i in range(len(arg)):
        if int(arg[i]) not in slownik:
            slownik[int(arg[i])] = 1
        else:
            slownik[int(arg[i])] += 1

def wypisz():
    for key, value in slownik.items():
        print(key, end=':')
        print(value, end=', ')

############################################
print('Załadowano moduł "{0}"'.format(__name__))