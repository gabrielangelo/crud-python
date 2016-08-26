SESSION = []

def catch_session():
	return SESSION

def set_session(username):
	SESSION.append(username)
