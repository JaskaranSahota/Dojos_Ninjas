from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninjas
from flask_app.models.dojo import Dojos
# Adding New Ninja
@app.route('/ninja',methods=["POST","GET"])
def ninja():
    if request.method=="GET":
        dojo=Dojos.get_all()
        return render_template("ninja.html",dojo=dojo)
    else:
        data={
            'dojo':request.form['dojos_id'],
            'first_name':request.form['first_name'],
            'last_name' : request.form['last_name'],
            'age': request.form['age']
        }
        id=data['dojo']
    # We pass the data dictionary into the save method from the Friend class.
    Ninjas.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')