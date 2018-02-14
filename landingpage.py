from flask import Flask, render_template,request, redirect 
app = Flask(__name__)
@app.route('/')
def greeting():
  return render_template('index.html')
@app.route('/ninjas')
def ninjas():
  return render_template('ninjas.html')

@app.route('/dojos/new')
def index():
  return render_template("dojos.html")
app.run(debug=True)   
@app.route('/dojos/new', methods=['POST'])
def create_user():
   print "Got Post Info"
   name = request.form['name']
   email = request.form['email']
   return redirect('/dojos/new')
app.run(debug=True)