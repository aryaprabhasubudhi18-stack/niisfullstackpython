class Person:
	def display_person(self):
		print("i am a person")
class Student(Person):
	def display_Student(self):
		print("i am a student")
class Engineering(Student):
	def display_Engineering(self):
		print("i am a engineer student")
ob=Engineering()
ob.display_person()
ob.display_Student()
ob.display_Engineering()