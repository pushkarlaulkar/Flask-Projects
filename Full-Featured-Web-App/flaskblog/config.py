class Config:
	SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' #Required for Forms like CSRF in Django
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	#MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_USERNAME = 'flaskblognoreply123456@gmail.com'
	#MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	MAIL_PASSWORD = '7htdv3eh5t'