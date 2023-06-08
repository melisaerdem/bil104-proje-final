rom Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statuler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = statuler
    def get_statuler(self):
        return self.__statuler
    
    def set_statuler(self, statuler):
        self.__statuler = statuler
    def statu_bul(self):
        try:
            mavi_yaka_etkisi = self.__statuler.get('mavi yaka', 0)
            beyaz_yaka_etkisi = self.__statuler.get('beyaz yaka', 0)
            yonetici_etkisi = self.__statuler.get('yonetici', 0)
            
            mavi_yaka_oran = 0.2
            beyaz_yaka_oran = 0.35
            yonetici_oran = 0.45
            
            en_uygun_statu = max(mavi_yaka_etkisi * mavi_yaka_oran,
                                 beyaz_yaka_etkisi * beyaz_yaka_oran,
                                 yonetici_etkisi * yonetici_oran)
            
            if en_uygun_statu == mavi_yaka_etkisi * mavi_yaka_oran:
                return 'mavi yaka'
            elif en_uygun_statu == beyaz_yaka_etkisi * beyaz_yaka_oran:
                return 'beyaz yaka'
            else:
                return 'yonetici'
        except:
            return ''
    def __str__(self):
        statu = self.statu_bul()
        return super().__str__() + f"\nEn Uygun Statü: {statu}"    