
class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_info(self):
        
        print(f"Name: {self.name}, Age: {self.age}")



class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  
        self.student_id = student_id 

    def display_info(self):
        
        super().display_info()  
        print(f"Student ID: {self.student_id}")



class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  
        self.subject = subject  

    def display_info(self):
       
        super().display_info()  
        print(f"Subject: {self.subject}")



if __name__ == "__main__":
  
    person = Person("ahmet", 20)
    person.display_info()
    print()  

    
    student = Student("Ayşe", 20, "S25748")
    student.display_info()
    print()  

    # Teacher nesnesi
    teacher = Teacher("murat", 40, "matematik")
    teacher.display_info()
