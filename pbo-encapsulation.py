class Musisi:
    def __init__(self,nama_band, gitar, drum):
        self.__nama_band = nama_band
        self.__gitar = gitar
        self.__drum = drum
        
    def getNama_band(self):
        return self.__nama_band
        
    def setNama_band(self,nama_band):
        self.__nama_band = nama_band

    def getGitar(self):
        return self.__gitar

    def setGitar(self, gitar):
        self.__gitar = gitar
        
    def getDrum(self):
        return self.__drum
    
    def setDrum(self, drum):
        self.__drum = drum

object = Musisi("Dewa", "Listrik", "Yamaha")
print('====== Menampilkan hasil awal ======')
print('Band',object.getNama_band(), 'sedang tampil menggunakan gitar', object.getGitar(), 'dan drum merk', object.getDrum() )

print('')
print('===== Data diubah =====')
object.setNama_band('Peterpan')
object.setGitar('Akustik')
object.setDrum('Rolland')

print('Band',object.getNama_band(), 'sedang tampil menggunakan gitar', object.getGitar(), 'dan drum merk', object.getDrum() )
