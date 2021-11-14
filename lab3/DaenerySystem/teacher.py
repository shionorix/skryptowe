class Teacher(object):

    def __init__(self, imie: str, nazwisko: str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__workduration = 0

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, value):
        if type(value) is str:
            self.__imie = value
        else: 
            raise TypeError('Imię musi być typu str')

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, value):
        if type(value) is str:
            self.__nazwisko = value
        else:
            raise TypeError('Nazwisko musi być typu str')

    @property
    def workduration(self):
        return self.__workduration

    @workduration.setter
    def workduration(self, value):
        self.__workduration = value

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
