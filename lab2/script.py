import sys

args = sys.argv[1:]

if '--lista' in args:
    import lista
    lista.zapisz(args[-1])
    lista.wypisz()

if '--slownik' in args:
    import slownik
    slownik.zapisz(args[-1])
    slownik.wypisz()