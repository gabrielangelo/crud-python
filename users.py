# -*- coding: utf-8 -*-

import pickle
salt = '58bda42c74a94a9f93ededf5653ccada'
#lista que irá conter todos os usuários(objetos) logados
SESSION = []

def all_users():
	file_read = open('db.pkl','rb')
	persons = []
	try:
		while True:
			person = pickle.load(file_read)
			persons.append(person)
	except EOFError:
		print 'fim de arquivo'
		file_read.close()
		return persons

def search_user(**kwargs):
	pass

#funcção remover 
def remove():
	pass

#função alterar
def alter():
	pass 

def create_user(**kwargs):
	import hashlib
	file_input = open('db.pkl','wb')
	new_password = hashlib.sha512(kwargs['password'] + salt).hexdigest()
	user = {'email' : kwargs['email'], 'username' : kwargs['username'],
	'password' : new_password}
	pickle.dump(user,file_input, pickle.HIGHEST_PROTOCOL)
	file_input.close()

def authenticate(username, password):
	import hashlib
	file_search = open('db.pkl','rb')
	new_user = search_user(username)
	new_password = hashlib.sha512(password + salt).hexdigest()
	if new_user:
		try:
			while True:
				user = pickle.load(file_search)
				if user['password'] ==  new_password:
					return user
		except EOFError:
			return None
	return None

def login(user):
	pass
def unlog(user):
	pass
		
	


