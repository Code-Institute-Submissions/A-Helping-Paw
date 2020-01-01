import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'pet_adopt'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@cluster0-wgn6h.mongodb.net/pet_adopt?retryWrites=true"

mongo = PyMongo(app)

@app.route('/')

@app.route('/mysearch')
def mysearch():
    return render_template("SearchPage.html")

@app.route('/showsearch', methods=['POST'])
def showsearch():
    mykeyword = request.form.get('searchPetCat')
    mydata = {"petCat":  mykeyword}
    mypet=mongo.db.pet.find(mydata)
    myuser=mongo.db.user.find()
    return render_template("searchResult.html", pet=mypet,user=myuser)  

@app.route('/add_adv')
def add_adv():
    return render_template("add_adv.html", pet=mongo.db.pet.find())
    
@app.route('/insert_adv/', methods=['POST'])
def insert_adv():
    mongo.db.pet.insert_one( {"petName":request.form.get('petName'), "petCat": request.form.get('petCat'), "gender": request.form.get('gender'), "color": request.form.get('color'), "age": request.form.get('age'), "description": request.form.get('description')} )
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)