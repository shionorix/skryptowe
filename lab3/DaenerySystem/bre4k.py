import basicterm

class Break(basicterm.BasicTerm):
    def __init__(self, hour, minute, duration):
        super().__init__(hour, minute, duration)

    @property
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        self.__term = value

    def __str__(self):
        return 'Przerwa'

    def getTerm(self):
        return f'{self.start_time()} - {self.end_time()}'