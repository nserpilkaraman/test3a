import ogretmen
import ogrenci

student_list = list()
teacher_list = list()

student2 = ogrenci.Student("Ayça", "Güven", 21, "Yazılım Kalite ve Test")
student_list.append(student2)
ogrenci.Student.printdetails(student2)

teacher = ogretmen.Teacher("İrem", "Balcı", 25, "Yazılım Kalite ve Test")
teacher_list.append(teacher)
ogretmen.Teacher.printdetails(teacher)




