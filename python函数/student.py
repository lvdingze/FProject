#define  student class

class student(object):
	"""docstring for student"""
	def __init__(self, name,age,sex):
		super(student, self).__init__()
		self.name = name
		self.age = age
		self.sex = sex

	def __str__(self):
		msg = self.name + " is "  + str(self.age) + " old and sex is " + self.sex
		return msg



s = student("lvdingze",18,"man")

print (student)
