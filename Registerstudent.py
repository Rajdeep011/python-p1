class Student:
  def __init__(self, roll_number,name,class_name):
  
     self.roll_number = roll_number
     self.name = name
     self.class_name = class_name
     self.marks = {}
     
  def add_marks(self,subject,marks):
      if subject in self.marks:
          print(f"{self.marks} already has marks of {subject}")  
      else:
          self.marks[subject] = marks
          
  def calculate_average_marks(self):
      
     if not self.marks:
         print("there is no marks available")    
     total_marks = sum(self.marks.values()) 
     average_marks = total_marks/len(self.marks)   
     return average_marks
 
  def display_student_info(self):
      print(f"Student information")
      print(f"Roll number :{self.roll_number}")
      print(f"name : {self.name}")
      print(f"class : {self.class_name}")
      print(f"marks : {self.marks}")
      print(f"average marks are : {self.calculate_average_marks()}")
      
student1 = Student(28,"rajdeep","10th")
student2 = Student(13,"sarthak","12th")      

student1.add_marks("English",80)
student1.add_marks("Maths",98)  

student2.add_marks("English",55)  
student2.add_marks("Maths",70)

student1.display_student_info()
    