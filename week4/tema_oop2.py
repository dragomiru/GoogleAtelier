### Week 4 - Homework OOP #2 ###

class Clasa1:

    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip

    def intrare_culoare(self, culoare):
        self.culoare = culoare

    def afisare_culoare(self, culoare):
        return self.culoare

class Clasa2(Clasa1):

    def interior(self, scaune_incalzite):
        self.scaune_incalzite = scaune_incalzite
        return scaune_incalzite

class Clasa3(Clasa1):

    def faruri(self, blocuri_optice_led):
        self.blocuri_optice_led = blocuri_optice_led
        return blocuri_optice_led

masina1 = Clasa2("ARO", "M461")
masina1.interior("Nu")
masina1.intrare_culoare("rosu")

masina2 = Clasa3("Dacia", "1310")
masina2.faruri("Nu")
masina2.intrare_culoare("negru")

print(masina1.culoare)
print(masina1.scaune_incalzite)
print(masina1.marca)
print(masina1.tip)

print(masina2.culoare)
print(masina2.blocuri_optice_led)
print(masina2.marca)
print(masina2.tip)


