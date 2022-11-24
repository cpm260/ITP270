#!/usr/bin/env python3

class School:
		
	## Accepting recommendations for implemeting Input validation logic on contructors
	## Maybe it would be better to do all of this input validation outside of the class before calling the constructor method
	## Or perhaps each get method should run a check to see if the attribute exists and if it is empty.
	## if the input validation at he constructor detects wrong input it will fail to initalize the class object
	## maybe the input validation should be separate functions that collect input for these variables and checks if its valid before passing to contructor.

	def __init__(self, name, level, numberOfStudents):

		if type(name) == str:
			self.name = name
		else:
			print(f'Error: Parameter "name" is of invalid type {type(name)}')
			print(f'Parameter must be of type string')
		
		if type(level) == str:	
			if level.lower() == 'primary' or 'middle' or 'high':
				self.level = level
			else:
				print(f'Parameter "level" of invalid value.')
				print(f'Acceptable values are "primary", "middle", "high"')
		else:
			print(f'Error: Parameter "level" is of invalid type {type(level)}')
			print(f'Parameter must be of type string')
			
		if type(numberOfStudents) == int:
			self.numberOfStudents = numberOfStudents
		else:
			print(f'Error: Parameter "numberOfStudents" is of invalid type {type(numberOfStudents)}')
			print(f'Parameter must be of type integer')
	
	def get_name(self):
		return self.name
	
	def get_level(self):
		return self.level
		
	def get_numberOfStudents(self):
		return self.numberOfStudents
		
	def set_numberOfStudents(self, numberOfStudents):
		if type(numberOfStudents) == int:
			self.numberOfStudents = numberOfStudents
		else:
			print(f'Error: Parameter "numberOfStudents" is of invalid type {type(numberOfStudents)}')
			print(f'Parameter must be of type integer')
		
	def __repr__(self):
		return f'A {self.level} School named {self.name} with {self.numberOfStudents} students.'
		
class PrimarySchool(School):
	def __init__(self, name, numberOfStudents, pickupPolicy):
		if type(name) == str:
			if type(numberOfStudents) == int:
				super().__init__(name, "Primary", numberOfStudents)
			else:
				print(f'Error: Parameter "numberOfStudents" is of invalid type {type(numberOfStudents)}')
				print(f'Parameter must be of type integer')
		else:
			print(f'Error: Parameter "name" is of invalid type {type(name)}')
			print(f'Parameter must be of type string')

		if type(pickupPolicy) == str:
			self.pickupPolicy = pickupPolicy
		else:
			print(f'Error: Parameter "pickupPolicy" is of invalid type {type(pickupPolicy)}')
			print(f'Parameter must be of type string')

	def get_pickupPolicy(self):
		return self.pickupPolicy

	def __repr__(self):
		return super().__repr__() + "\n" + f"Also, the pickup policy is {self.pickupPolicy}"
		
class HighSchool(School):
	def __init__(self, name, numberOfStudents, sportsTeams):
		if type(name) == str:
			if type(numberOfStudents) == int:
				super().__init__(name, "High", numberOfStudents)
			else:
				print(f'Error: Parameter "numberOfStudents" is of invalid type {type(numberOfStudents)}')
				print(f'Parameter must be of type integer')
		else:
			print(f'Error: Parameter "name" is of invalid type {type(name)}')
			print(f'Parameter must be of type string')
		self.sportsTeams = []
		if type(sportsTeams) == str:
			self.sportsTeams.append(sportsTeams)
		else:
			print(f'Error: Parameter "pickupPolicy" is of invalid type {type(pickupPolicy)}')
			print(f'Parameter must be of type string')


	def get_sportsTeams(self):
		return self.sportsTeams

	def set_sportsTeams(self, sportsTeams):
		if type(sportsTeams) == str:
			self.sportsTeams.append(sportsTeams)
		else:
			print(f'Error: Parameter "pickupPolicy" is of invalid type {type(pickupPolicy)}')
			print(f'Parameter must be of type string')

	def __repr__(self):
		return super().__repr__() + "\n" + f"and the sports Teams are {self.sportsTeams}"
		
test_school = School("George Mason", "High", 3167)
print(f'{test_school.get_name()} {test_school.get_level()}')
print(f'Student Population: {test_school.get_numberOfStudents()}')
test_school.set_numberOfStudents(3058)
print(f'Student Population: {test_school.get_numberOfStudents()}')
print(f'{test_school.__repr__()}')

test_primary = PrimarySchool("Nottingham", 600, "School Bus")
print(f'{test_primary.get_name()} {test_primary.get_level()}')
print(f'Student Population: {test_primary.get_numberOfStudents()}')
print(f'Pickup Policy: {test_primary.get_pickupPolicy()}')
print(f'{test_primary.__repr__()}')

test_high = HighSchool("Freedom", 1000, "Fighters")
print(f'{test_primary.get_name()} {test_primary.get_level()}')
print(f'Student Population: {test_primary.get_numberOfStudents()}')
print(f'Sport Teams: {test_high.get_sportsTeams()}')
print(f'{test_high.__repr__()}')
test_high.set_sportsTeams("Pidgeons")
for team in test_high.get_sportsTeams():
	print(f'Sport Teams: {team}')

