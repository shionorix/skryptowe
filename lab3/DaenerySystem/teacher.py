class Teacher(object):

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, value):
        self.__imie = value

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        self.__nazwisko = value

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
