from inspect import signature

def argumenty(defaultArgs): 
    def decorator(func): 
        def argsProcessing(*args): 
            functionArgs = [arg for arg in args] #argumenty przekazane w wywołaniu
            neededArgs = len(list(signature(func).parameters)) #ile argumentów jest potrzebne do funkcji
            if len(functionArgs) + len(defaultArgs) < neededArgs: 
                raise TypeError("Za mało argumentow")

            index = 0 
            while len(functionArgs) < neededArgs: #dodawanie brakujących elementów w działaniu
                functionArgs.append(defaultArgs[index])
                index += 1
            
            func(*functionArgs)

            try: # zwracanie pierwszej niedodanej liczby z defaultowych 
                return defaultArgs[index]
            except IndexError:
                return None

        return argsProcessing
        
    return decorator

class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')
    
    def rawSuma(self, a, b, c):
        print(f'{a} + {b} + {c} = {a + b + c}')

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def rawRoznica(self, x, y):
        print(f'{x} - {y} = {x - y}')

    def __setitem__(self, name, value):
        if name == "suma":
            self.argumentySuma=value
            self.suma = argumenty(self.argumentySuma)(self.rawSuma)
        if name == "roznica":
            self.argumentyRoznica=value
            self.roznica = argumenty(self.argumentyRoznica)(self.rawRoznica)

if __name__ == '__main__':
    op = Operacje()
    op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
    op.suma(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'

    try:
        op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
    except Exception as e:
        print(e)

    op.roznica(2, 1)  # Wypisze: 2-1=1
    op.roznica(2)  # Wypisze: 2-4=-2
    wynik = op.roznica()  # Wypisze: 4-5=-1
    print(wynik)  # Wypisze: 6

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma'] = [1, 2]
    # oznacza, że   argumentySuma=[1,2]
    print(op.argumentySuma)

    # Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica'] = [1, 2, 3]
    # oznacza, że   argumentyRoznica=[1,2,3]
    print(op.argumentyRoznica)