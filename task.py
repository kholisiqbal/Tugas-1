class Musisi:
    def __init__(self,nama_band, gitar, drum):
        self.nama_band = nama_band
        self.gitar = gitar
        self.drum = drum
        
    def bermain(self):
        print(f"Band {self.nama_band} sedang bermain di studio membawa gitar {self.gitar} dan drum {self.drum}")

    def belajar(self):
        print(f"Band {self.nama_bands} sedang belajar cord {self.gitar} dan tempo drum {self.drum}")

    def show(self):
        print(f"Band {self.nama_band} sedang show di kota Surakarta membawa alat musik membawa gitar {self.gitar} dan drum {self.drum}")


object1 = Musisi("Dewa", "Listrik", "Yamaha")
object2 = Musisi("SHA", "Lagu", "Punk")
object3 = Musisi("Payung Teduh","Listrik", "Yamaha")

object1.bermain()
object2.belajar()
object3.show()
