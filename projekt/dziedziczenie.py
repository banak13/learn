class ptak:

    def __init__(self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość

    def leć(self):
        print("Tu", self.gatunek, ". Startuje, i zaraz osiągne prędkość", self.szybkość)

    def wydajOdgłos(self):
        pass


class orzeł(ptak):

    def poluj(self):
        print("Tu", self.gatunek, ". Rozpoczołem polowanie")


class pingwin(ptak):

    def ślizgaj(self):
        print("Tu", self.gatunek, ". Rozpoczołem ślizg")

    def leć(self):
        print("Tu", self.gatunek, ". Przykro mi, ale nie latam")