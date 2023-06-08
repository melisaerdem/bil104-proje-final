from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi
    def get_tesvik_primi(self):
        return self.__tesvik_primi
    
    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
    def zam_hakki(self):
        try:
            tecrube_yil = self.get_tecrube() / 12
            maas_oran = self.get_maas() / tecrube_yil
            
            if tecrube_yil < 2:
                return self.__tesvik_primi
            elif tecrube_yil >= 2 and tecrube_yil <= 4 and self.get_maas() < 15000:
                return (self.get_maas() / tecrube_yil) * 5 + self.__tesvik_primi
            elif tecrube_yil > 4 and self.get_maas() < 25000:
                return (self.get_maas() / tecrube_yil) * 4 + self.__tesvik_primi
            else:
                return self.get_maas()
        except:
            return self.get_maas()
