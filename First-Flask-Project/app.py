from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World';

@app.route('/foo')
def hello_world_foo():
	return '''
			<style>
				h1{
					color: green;
				}
			</style>
			<h1>Hello World foo again</h1>
			''';

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)