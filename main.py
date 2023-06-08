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