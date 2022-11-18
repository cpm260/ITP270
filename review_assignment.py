#!/usr/bin/env python3

from datetime import date
import subprocess
class Student:
	def __init__(self, name, year):
		self.name = name
		self.year = year
		self.grades = []
		self.attendence = {}
		
	def add_grade(self, grade):
		print(type(grade))
		if type(grade) == Grade:
			self.grades.append(grade.score)
		else:
			pass
	
	def get_average(self):
		return sum(self.grades)/len(self.grades)
class Grade:
	minimum_passing = 65
	
	def __init__(self, score):
		self.score = score
		
	def is_passing(self, score):
		
		if grade.score >= self.minimum_passing:
			print("isPassing == True")
			return True
		else:
			print("isPassing == False")
			return False
		
class iscdhcpserver:
	
	def __init__(self):
		self.package_name = "isc-dhcp-server"
	
	def install(self):
		completed_process = subprocess.run(["sudo", "apt", "install", "-y", self.package_name], capture_output=True)
		print(completed_process.stdout.decode("utf-8"))
		
		
	
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(84))
pieter.add_grade(Grade(100))
pieter.add_grade(Grade(87))
pieter.add_grade(Grade(49))
pieter.add_grade(Grade(65))

print(pieter.grades)
grade = Grade(100)
grade.is_passing(grade.score)
pieter.get_average()

print(pieter.get_average())

today = date.today()
pieter.attendence[today] = True

print(pieter.attendence[today])

dhcp_server = iscdhcpserver()
dhcp_server.install()
