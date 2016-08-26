from session import catch_session
from menus import login_menu

def login_required(f):
	def wrapper(*args, **kwargs):
		session = catch_session()
		if len(session) > 0:
			f()
		elif login_menu():
			f()
		else:
			return wrapper()
	return wrapper()


			
	
	
