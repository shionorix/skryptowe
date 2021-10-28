class Klasa(object):
    tab = [1,2,3]
    def __init__(self, tab, a, b):
        self.tab = tab
        self._zmienna1 = a
        self.__zmienna2 = b
        print("Wywołano metodę '__init__()'")

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def __repr__(self):
        return "Wywołano metodę '__repr__()'"

    def metodaInstancyjna(self):
        print("Wywołano metodę 'metodaInstancyjna()'")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")



# print(obiekt._Klasa__zmienna2)
