from Animal import *
class lumba_lumba(Animal):
    def __init__(self, nama, makanan, hidup, berkembangBiak, habitat, jenis):
        super().__init__(nama, makanan, hidup, berkembangBiak, habitat, jenis)

    def display_habitat(self):
        print(f"Habitat Lumba-lumba adalah di {self.habitat}")
    
    def display_jenis(self):
        print(f"Lumba-lumba termasuk kedalam janis hewan {self.jenis}")
        print("======================================")
