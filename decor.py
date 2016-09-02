# *-* encoding: utf-8 *-*


def geometricForms(option):
	def retangle():
		return 'retangle'
	def triangle():
		return 'triangle'
	def square():
		return 'square'
	options = {'1': retangle, '2':triangle,'3':square}
	try:
		function = options[str(option)]
		return function()
	except KeyError:
		print 'valor inválido !'

def square(x):
	return x**2

def foo(func):
	print 'the name of function is ' + func.__name__
	value = 0
	for i in range(1,4):
		value+=func(i)
	return value

def checkNum(function):
	def wrapper(number):
		if number > 1 and type(number) == int:
			return function(number)
		elif number == 1:
			return 1
		raise Exception('invalid !')
	return wrapper

@checkNum
def fat(n):
	return n*fat(n-1)



	

