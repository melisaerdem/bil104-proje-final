rom Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statuler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler = statuler