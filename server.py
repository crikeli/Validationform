from flask import Flask, render_template, request, redirect, session, flash                                          
app = Flask(__name__)                     
app.secret_key = "keysareeverywhere"

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
	session['name'] = request.form['name']
	if len(session['name']) < 1:
		flash("The name field cannot be left blank!")
	else: 
		flash("Success!")
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form["comment"]
	if len(session['comment']) < 1:
		flash("The comment field cannot be left blank!")
	elif len(session['comment']) > 120:
		flash("The comment cannot be greater than 120 characters!")
	else:
		flash("Success!")

	return redirect('/showdata')

@app.route('/showdata')
def showdata():
	return render_template("result.html")

app.run(debug=True)