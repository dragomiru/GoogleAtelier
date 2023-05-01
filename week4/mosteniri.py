class Exemplu1:
    counter = 1
    def name(self):
        return "Smith"


class Exemplu2:

    counter = 2
    def name(self):
        return "Dove"


class Exemplu3(Exemplu1, Exemplu2):
    pass

    # def name(self):
    #     return "John"

obiect1 = Exemplu3()
# print(obiect1.name())
print(obiect1.counter)