from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Animals
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///animals'
app.config['SQLALCHEM_ECHO']= True
app.config['SECRET_KEY'] = "alluppercaselowercase"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def homepage():
    pets = Animals.query.all()
    return render_template("home.html", pets=pets)

@app.route("/add_pet", methods=['GET', 'POST'])
def add_pet_form():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data or 'https://static.vecteezy.com/system/resources/thumbnails/004/141/669/small/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg'
        age = form.age.data
        notes = form.notes.data
        available = form.available.data 


        new_pet = Animals(
            name=name, 
            species=species, 
            photo_url=photo_url, 
            age=age, 
            notes=notes, 
            available=available  
        )
        

        db.session.add(new_pet)
        db.session.commit()

        flash('Pet added successfully!', 'success')
        return redirect("/")
    
    return render_template("petForm.html", form=form)
    
@app.route("/pet/<int:petId>/edit", methods=['GET', 'POST'])
def pet_edit(petId):
    pet = Animals.query.get_or_404(petId)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data or 'https://static.vecteezy.com/system/resources/thumbnails/004/141/669/small/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg'
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        
        flash('Pet edited successfully!', 'success')
        return redirect("/") 
    
    return render_template("editPet.html", form=form)