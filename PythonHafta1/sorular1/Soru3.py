class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    def kareyi_yazdir(self):
        for i in range(self.kenar):
            print("* " * self.kenar)

kare1 = Kare(5)
kare1.kareyi_yazdir()

