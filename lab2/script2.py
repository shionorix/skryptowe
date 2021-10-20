import getopt
import sys

opts, args = getopt.getopt(sys.argv[1:], ':slownik:lista',['modul='])


if 'slownik' in opts[0]:
    import slownik
    slownik.zapisz(args[0])
    slownik.wypisz()

if 'lista' in opts[0]:
    import lista
    lista.zapisz(args[0])
    lista.wypisz()