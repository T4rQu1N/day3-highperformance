class Person(object):
	def __init__(self, firstName, lastName):
		'''Constructor for this class. '''
		self.firstName = firstName
		self.lastName = lastName

	def fullName(self):
		return (self.firstName + " " + self.lastName)

	def __str__(self):
		return "%s %s" % (self.firstName, self.lastName)


class Student(Person):
	def __init__(self, firstName, lastName, subjectArea):
		'''Constructor for this class. '''
		super(Student, self).__init__(firstName, lastName)
		self.subjectArea = subjectArea

	def subjectArea(self):
		return self.subjectArea

	def __str__(self):
		return "%s %s, %s" % (self.firstName, self.lastName, self.subjectArea)

class Teacher(Person):
	def __init__(self, firstName, lastName, teachingArea):
		'''Constructor for this class. '''
		super(Teacher, self).__init__(firstName, lastName)
		self.teachingArea = teachingArea

	def teachingArea(self):
		return self.teachingArea

	def __str__(self):
		return "%s %s, %s" % (self.firstName, self.lastName, self.teachingArea)