from session import set_session
from getpass import getpass
user = {'name':'gabriel', 'password':'1275115'}
def login_menu():
        username = raw_input('username: \n')
        password = getpass('password: \n')
        set_session(user)
	return True
