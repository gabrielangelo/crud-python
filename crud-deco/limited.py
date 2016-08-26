# -*- coding: utf-8 -*-
from getpass import getpass
from decorator import login_required
from session import set_session

@login_required
def limit():	
	print 'vc está logado e pode fazer essa tarefa!'



	


