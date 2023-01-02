from Animal import *
class Elang(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, habitat, jenis):
        super().__init__(nama, makanan, hidup, berkembangBiak, habitat, jenis)

    def display_habitat(self):
        print(f"Habitat Elang adalah di {self.habitat}")
    
    def display_jenis(self):
        print(f"Elang termasuk kedalam janis hewan {self.jenis}")
        print("======================================")
