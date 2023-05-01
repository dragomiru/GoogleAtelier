# class FirstClass:
#
#     __counter = 0
#
#     def __init__(self, val=1):
#         self.__first = val
#         FirstClass.__counter += 1
#
# obiect_1 = FirstClass()
# obiect_2 = FirstClass()
# obiect_3 = FirstClass()
#
# print(obiect_1.__dict__, obiect_1._FirstClass__counter)
# print(obiect_2.__dict__, obiect_2._FirstClass__counter)
# print(obiect_3.__dict__, obiect_3._FirstClass__counter)

class Exemplu:
    def __init__(self, val):
        self.val = val
        self.a, self.b = None, None
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

    def denumire(self):
        return self.val

obiect = Exemplu(1)
print(obiect.a)
print(obiect.b)
print(obiect.denumire())
print(obiect.__dict__)
print(Exemplu.__dict__)
# try:
#     print(obiect.b)
# except AttributeError:
#     pass
