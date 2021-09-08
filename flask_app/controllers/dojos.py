from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojos
@app.route('/')
def dojos():
    #call the  get_all classmethod to get instances of all dojos
    dojo=Dojos.get_all()
    # print(dojo)
    return render_template('dojo.html',dojos=dojo)
# Add New Dojos(Location)
@app.route('/',methods=['POST'])
def adddojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
            'name': request.form['name'],  
    }
    # We pass the data dictionary into the save method from the Friend class.
    Dojos.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')   
# Access Each Location seprately
@app.route('/show/<int:id>')
def show(id):
    data={
        'id':id
    }
    one=Dojos.get_one(data)
    return render_template("location.html",one=one)
