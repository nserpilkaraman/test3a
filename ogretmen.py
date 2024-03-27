class Teacher:
    def __init__(self, name, surname, age, branş) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.branş = branş

    def printdetails(self):
        print(f"Ad : {self.name} \n Soyad : {self.surname} \n Yaş : {str(self.age)}\n Branş : {str(self.branş)}")