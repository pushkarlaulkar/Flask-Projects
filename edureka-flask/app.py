from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/hello/<name>')
def hello_world1(name):
	return 'Hello %s' % name

@app.route('/blog/<int:postid>')
def blog(postid):
	return 'Blog number %d' % postid

@app.route('/rev/<float:revno>')
def revno(revno):
	return 'Revision number %f' % revno
	
@app.route('/admin')
def admin():
	return 'Hello Admin'

@app.route('/guest/<guest>')
def guest(guest):
	return 'Hello Guest %s' % guest

@app.route('/user/<name>')
def hello_user(name):
	if(name == 'admin'):
		return redirect(url_for('admin'))
	else:
		return redirect(url_for('guest', guest = name))

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)