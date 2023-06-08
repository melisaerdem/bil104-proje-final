from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
    def zam_hakki(self):
        try:
            tecrube_yil = self.get_tecrube() / 12
            maas_oran = self.get_maas() / tecrube_yil
            
            if tecrube_yil < 2:
                return self.get_maas() + (self.__yipranma_payi * 10)
            elif tecrube_yil >= 2 and tecrube_yil <= 4 and self.get_maas() < 15000:
                return (self.get_maas() / tecrube_yil) / 2 + (self.__yipranma_payi * 10)
            elif tecrube_yil > 4 and self.get_maas() < 25000:
                return (self.get_maas() / tecrube_yil) / 3 + (self.__yipranma_payi * 10)
            else:
                return self.get_maas()
        except:
            return self.get_maas()
    def __str__(self):
        yeni_maas = self.zam_hakki()
        return super().__str__() + f"\nYıpranma Payı: {self.__yipranma_payi}\nYeni Maaş: {yeni_maas}"
