from flask import Flask, render_template, request, redirect, session                                          
app = Flask(__name__)                     
app.secret_key = "keys"

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/result', methods=['POST'])
def formdata():
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form["comment"]

	return redirect('/showdata')

@app.route('/showdata')
def showdata():
	return render_template("result.html")

app.run(debug=True)