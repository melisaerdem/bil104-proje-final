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