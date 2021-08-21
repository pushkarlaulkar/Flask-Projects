from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
	{
		'author' : 'Pushkar Laulkar',
		'title' : 'Blog Post 1',
		'content' : 'First Post Content',
		'date_posted' : 'Aug 17, 2021'
	},
	{
		'author' : 'Jane Doe',
		'title' : 'Blog Post 2',
		'content' : 'Second Post Content',
		'date_posted' : 'Aug 18, 2021'
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts);

@app.route('/about')
def about():
	return render_template('about.html', title='About');

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if (form.validate_on_submit()):
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)