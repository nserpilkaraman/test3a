#Bir okul kayıt sistemi kodlayalım
#Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
#Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.
#Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.

class Student:
    def __init__(self, name, surname, age, sınıf) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.sınıf =sınıf

    def printdetails(self):
        print(f"Ad : {self.name} \n Soyad : {self.surname} \n Yaş : {str(self.age)}\n Sınıf : {str(self.sınıf)}")





