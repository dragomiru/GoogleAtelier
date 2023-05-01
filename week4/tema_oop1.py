### Week 4 - Homework OOP #1 ###

class Catalog:

    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
        self.materii = {}
        self.absente = 0

    def adauga_absenta(self):
        self.absente += 1
        return self.absente

    def sterge_absenta(self):
        self.absente -= 1
        return self.absente

    def __str__(self):
        return self.absente


class Extensie1(Catalog):

    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)
        self.medie_list = []
        self.medie = 0

    def adauga_materie_si_note(self, materia, notele):
        self.materia = materia
        self.notele = notele
        self.materii[f"{self.materia}"] = self.notele
        return self.materii

    def afisare_materii(self):
        return f"Materiile lui {self.prenume} sunt: {list(self.materii.keys())}."

    def afisare_materii_si_medie(self):
        for lista_note in list(self.materii.values()):
            for nota in lista_note:
                if isinstance(nota, int):
                    self.medie += nota
                else:
                    break
            self.medie_list.append(self.medie)
            self.medie = 0
        for index, value in enumerate(self.medie_list):
            self.medie_list[index] /= len(list(self.materii.values())[index])

        return f"Materiile lui {self.prenume} sunt: {list(self.materii.keys())}, iar mediile pe subiecte sunt: " \
               f"{self.medie_list}"

# Creati un student numit Ion Roata.
obiect1 = Catalog("Roata", "Ion")

# Modificati argumentul absente sa fie incrementat de 3 ori prin metoda creata.
obiect1.adauga_absenta()
obiect1.adauga_absenta()
obiect1.adauga_absenta()
# print(obiect1.absente)

# Stergeti doua absente prin metoda creata.
obiect1.sterge_absenta()
obiect1.sterge_absenta()
# print(obiect1.absente)

# Creati al doilea student numit George Cerc.
obiect2 = Catalog("Cerc", "George")
obiect2.adauga_absenta()
obiect2.adauga_absenta()
obiect2.adauga_absenta()
obiect2.adauga_absenta()
# print(obiect2.absente)

# Stergeti doua absente prin metoda creata.
obiect2.sterge_absenta()
obiect2.sterge_absenta()
# print(obiect2.absente)

# Afisati absentele fiecarui student.
# print(obiect1.absente)
# print(obiect2.absente)

# Adaugati materia "Python" impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare student.
obiect1 = Extensie1("Roata", "Ion")
obiect2 = Extensie1("Cerc", "George")
obiect1.adauga_materie_si_note("Python", [7, 10, 8])
obiect2.adauga_materie_si_note("Python", [5, 7, 9])

# Adaugati materia "Matematica" la al doilea student numit George Cerc si "Romana" pentru studentul Ion Roata
# impreuna cu o lista formata din 3 numere intre 1-10 pentru fiecare student.
obiect1.adauga_materie_si_note("Matematica", [10, 10, 6])
obiect2.adauga_materie_si_note("Matematica", [9, 4, 10])

# Verificati ce materii are fiecare student prin metoda ce permite afisarea tuturor materiilor unui student.
# print(obiect1.afisare_materii())
# print(obiect2.afisare_materii())

# Verificati ce materii si ce note mediate au studentii.
print(obiect1.afisare_materii_si_medie())
print(obiect2.afisare_materii_si_medie())
