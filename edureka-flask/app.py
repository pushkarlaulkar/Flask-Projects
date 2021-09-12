from flask import Flask, redirect, url_for, request, render_template, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World'

@app.route('/hello/<name>')
def hello_world1(name):
	return render_template('hello.html', name = name)

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

@app.route('/success/<name>')
def success(name):
	return 'Welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
	if(request.method == 'POST'):
		user = request.form['nm']
		return redirect(url_for('success', name = user))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success', name = user))

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
	if(request.method == 'POST'):
		user = request.form['nm']
	
	resp = make_response(render_template('readcookie.html'))
	resp.set_cookie('userid', user)
	
	return resp

@app.route('/getcookie')
def getcookie():
	name = request.cookies.get('userid')
	return '<h1>Welcome '+name+'</h1>'
		
if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)