#*-* encoding: utf-8 *-* 
class Person(object):
	seq = 0
	persons =  [] 

	def __init__(self, name, last_name, email, salary = 0.0):
		self.name = name
		self.last_name = last_name
		self.email = email
		self.salary = salary
		self.id = id		

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if len(name) < 51:
			self.__name = name
		else:
			raise Exception('valor muito grande')
	
	@property
	def last_name(self):	
		return self.__last_name

	@last_name.setter
	def last_name(self, last_name):
		if len(last_name) < 31:
			self.__last_name = last_name
	
	@property
	def salary(self):
		salary = '%.2f'% self.__salary
		return salary

	@salary.setter
	def salary(self, salary):
		if salary >= 0 and type(salary) == float:	
			self.__salary = salary
		else:
			raise Exception('entrada inválida')

	@property
	def email(self):
		return self.__email
	
	@email.setter
	def email(self, email):
		if '@' and '.com' in email:
			self.__email = email
		else:
			raise Exception('formato de email inválido !')
	@property
	def id(self):
		if self.__id is not None:
			return self.__id
		else:
			return -1
	@id.setter
	def id(self, id):
		if self.__class__.seq is not None:
			self.__id = id
		else:
			raise Exception('id já estar preenchida !')
	
	@classmethod
	def all(cls):
		return persons
	
	def add(self):
		self.__class__.seq+=1
		self.id = self.__class__.seq
		self.__class__.persons.append(self)
	
	def __repr__(self):
		name = self.name
		return '{}:{}'.format(self.__class__.__name__,name)


						
	
