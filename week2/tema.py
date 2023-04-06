### Week 2 - Temă pentru acasă - CNP Verifier ###

# Verificator
def verificator_cnp(cnp):

    try:
        int(cnp)
    except ValueError:
        print("CNP Invalid.")
    else:
        # S = Sexul și secolul in care s-a născut persoana
        sex = [str(item) for item in list(range(1, 10))]

        # AA = Anul nașterii a persoanei
        anul_nastere = [str(item) for item in list(range(0, 100))]
        anul_nastere[:10] = ["0" + item for item in anul_nastere[:10]]

        # LL = Luna nașterii a persoanei
        luna_nastere = [str(item) for item in list(range(1, 13))]
        luna_nastere[:9] = ["0" + item for item in luna_nastere[:9]]

        # ZZ = Ziua nașterii a persoanei
        ziua_nastere = [str(item) for item in list(range(1, 31))]
        ziua_nastere[:9] = ["0" + item for item in ziua_nastere[:9]]

        # JJ = Județul nașterii sau reședința persoanei
        judet = [str(item) for item in list(range(1, 53))]
        judet[:9] = ["0" + item for item in judet[:9]]

        # NNN = Număr unic alocat persoanei
        numar_unic = [str(item) for item in list(range(1, 1000))]
        number_length_one = []
        number_length_two = []

        for number in numar_unic:
            if len(number) == 1:
                number = "00" + number
                number_length_one.append(number)
                continue
            elif len(number) == 2:
                number = "0" + number
                number_length_two.append(number)

        numar_unic[0:9] = number_length_one
        numar_unic[9:99] = number_length_two

        # C = Cifră de control
        cifra_inmultita = "279146358279"
        cifra_de_control = ""
        suma = 0
        for index, value in enumerate(cnp[0:12]):
            cifra_de_control = int(value) * int(cifra_inmultita[index])
            suma += cifra_de_control

            if suma % 11 == 10:
                cifra_de_control = 1
            else:
                cifra_de_control = suma % 11

        # Decizie validitate
        if cnp[0] in sex and cnp[1:3] in anul_nastere and cnp[3:5] in luna_nastere and cnp[5:7] in ziua_nastere and cnp[7:9] in judet and cnp[9:12] in numar_unic and cnp[-1] == str(cifra_de_control):
            print("CNP Valid.")
        else:
            print("CNP Invalid.")

verificator_cnp("5020205410061")