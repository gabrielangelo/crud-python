class P(object):
	
	def __init__(self, n):
		self.n = n
	
	@property
	def n(self):
		return self.__n
	
	@n.setter
	def n(self, n):
		if n > 1000:
			self.__n = 1000
		elif n < 0:
			self.__n = 0 
		else:
			self.__n = n

p = P(-1050)
print p.n
p1 = P(500)
print p1.n
p2 = P(1001)
print p2.n




	
	

