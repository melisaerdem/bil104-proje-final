rom Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statuler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = statuler
    def get_statuler(self):
        return self.__statuler
    
    def set_statuler(self, statuler):
        self.__statuler = statuler