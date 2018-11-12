import os


class Config(object):
	# CSRF_ENABLED = True
	# SECRET_KEY = 'you-will-never-guess'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

	OPENID_PROVIDERS = [
	{'name': 'Google','url':'https://www.google.com/accounts/o8/id'},
	{'name':'Yahoo','url':'https://me.yahoolcom'},
	{'name':'AOL','url':'http://openid.aol.com/<username>'},
	{'name':'Flicky','url':'http://www.flickr.com/<username>'},
	{'name':'MyOpenid','url':'https://www.myopenid.com'}
	]