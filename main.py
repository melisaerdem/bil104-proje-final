from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd
# Insan sınıfı için 2 nesne oluşturulması
insan1 = Insan("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk")
insan2 = Insan("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk")
# Issiz sınıfı için 3 nesne oluşturulması
issiz1 = Issiz("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk", {"mavi yaka": 2, "beyaz yaka": 1, "yonetici": 0})
issiz2 = Issiz("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk", {"mavi yaka": 0, "beyaz yaka": 3, "yonetici": 1})
issiz3 = Issiz("45678912345", "Mehmet", "Kara", 35, "Erkek", "Türk", {"mavi yaka": 0, "beyaz yaka": 0, "yonetici": 0})
# Calisan sınıfı için 2 nesne oluşturulması
calisan1 = Calisan("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk", "Bilişim", 24, 12000)
calisan2 = Calisan("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk", "Pazarlama", 36, 18000)
# MaviYaka sınıfı için 2 nesne oluşturulması
mavi_yaka1 = MaviYaka("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk", "Bilişim", 24, 12000, 500)
mavi_yaka2 = MaviYaka("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk", "Pazarlama", 36, 18000, 800)
# BeyazYaka sınıfı için 2 nesne oluşturulması
beyaz_yaka1 = BeyazYaka("12345678901", "Ali", "Yılmaz", 30, "Erkek", "Türk", "Bilişim", 24, 12000, 1000)
beyaz_yaka2 = BeyazYaka("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk", "Pazarlama", 36, 18000, 1500)
# Verilerin bir DataFrame'e aktarılması
data = [
    [insan1.get_tc_no(), insan1.get_ad(), insan1.get_soyad(), insan1.get_yas(), insan1.get_cinsiyet(), insan1.get_uyruk()],
    [insan2.get_tc_no(), insan2.get_ad(), insan2.get_soyad(), insan2.get_yas(), insan2.get_cinsiyet(), insan2.get_uyruk()],
    [issiz1.get_tc_no(), issiz1.get_ad(), issiz1.get_soyad(), issiz1.get_yas(), issiz1.get_cinsiyet(), issiz1.get_uyruk()],
    [issiz2.get_tc_no(), issiz2.get_ad(), issiz2.get_soyad(), issiz2.get_yas(), issiz2.get_cinsiyet(), issiz2.get_uyruk()],
    [issiz3.get_tc_no(), issiz3.get_ad(), issiz3.get_soyad(), issiz3.get_yas(), issiz3.get_cinsiyet(), issiz3.get_uyruk()],
    [calisan1.get_tc_no(), calisan1.get_ad(), calisan1.get_soyad(), calisan1.get_yas(), calisan1.get_cinsiyet(), calisan1.get_uyruk(), calisan1.get_sektor(), calisan1.get_tecrube(), calisan1.get_maas()],
    [calisan2.get_tc_no(), calisan2.get_ad(), calisan2.get_soyad(), calisan2.get_yas(), calisan2.get_cinsiyet(), calisan2.get_uyruk(), calisan2.get_sektor(), calisan2.get_tecrube(), calisan2.get_maas()],
    [mavi_yaka1.get_tc_no(), mavi_yaka1.get_ad(), mavi_yaka1.get_soyad(), mavi_yaka1.get_yas(), mavi_yaka1.get_cinsiyet(), mavi_yaka1.get_uyruk(), mavi_yaka1.get_sektor(), mavi_yaka1.get_tecrube(), mavi_yaka1.get_maas(), mavi_yaka1.get_yipranma_payi()],
    [mavi_yaka2.get_tc_no(), mavi_yaka2.get_ad(), mavi_yaka2.get_soyad(), mavi_yaka2.get_yas(), mavi_yaka2.get_cinsiyet(), mavi_yaka2.get_uyruk(), mavi_yaka2.get_sektor(), mavi_yaka2.get_tecrube(), mavi_yaka2.get_maas(), mavi_yaka2.get_yipranma_payi()],
    [beyaz_yaka1.get_tc_no(), beyaz_yaka1.get_ad(), beyaz_yaka1.get_soyad(), beyaz_yaka1.get_yas(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka1.get_uyruk(), beyaz_yaka1.get_sektor(), beyaz_yaka1.get_tecrube(), beyaz_yaka1.get_maas(), beyaz_yaka1.get_tesvik_primi()],
    [beyaz_yaka2.get_tc_no(), beyaz_yaka2.get_ad(), beyaz_yaka2.get_soyad(), beyaz_yaka2.get_yas(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka2.get_uyruk(), beyaz_yaka2.get_sektor(), beyaz_yaka2.get_tecrube(), beyaz_yaka2.get_maas(), beyaz_yaka2.get_tesvik_primi()]
]
columns = ['TC No', 'Ad', 'Soyad', 'Yaş', 'Cinsiyet', 'Uyruk', 'Sektör', 'Tecrübe', 'Maaş', 'Yıpranma Payı/Tesvik Prim','Yeni Maaş']
df = pd.DataFrame(data, columns=columns)