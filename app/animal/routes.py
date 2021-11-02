from flask import render_template, redirect, url_for

from app import db
from app.animal import bp
from app.models import Animal
from app.auth.decorators import admin_required
from .forms import AddAnimalForm, EditAnimalForm

@bp.route('/')
@admin_required
def animal_list():
    ''' A route for a list of all animals in the register. '''
    animals = Animal.query.all()
    return render_template('animal_list.html', title = 'Animals', animals = animals)

@bp.route('/<int:id>')
@admin_required
def animal_details(id):
    ''' A route that shows the details for a specific animal in the collection. '''
    animal = Animal.query.get_or_404(id)
    return render_template('animal_details.html', title = 'Animal details', animal = animal)

@bp.route('/add', methods = ['GET', 'POST'])
@admin_required
def animal_add():
    ''' A route for showing a form and processing form for adding a new animal. '''
    form = AddAnimalForm()

    # When the form has been submitted, process the form and save new animal to database
    if form.validate_on_submit():
        animal = Animal()
        form.populate_obj(obj=animal)
        db.session.add(animal)
        db.session.commit()
        # Return back to the view that shows the list of animals in the register
        return redirect(url_for('animal.animal_list'))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('animal_add.html', form = form, title = 'Add animal')

@bp.route('/<int:id>/edit', methods = ['GET', 'POST'])
@admin_required
def animal_edit(id):
    ''' A route for showing a form and processing form when editing an animal. '''
    animal = Animal.query.get_or_404(id)
    form = EditAnimalForm(obj=animal)

    # When the form has been submitted, process the form and save changes to database
    if form.validate_on_submit():
        form.populate_obj(obj=animal)
        db.session.commit()
        return redirect(url_for('animal.animal_details', id=animal.id))

    # When doing a GET request or there are errors in the form, return the view with the form
    return render_template('animal_edit.html', title = 'Animal edit', form = form, animal = animal)

@bp.route('/<int:id>/delete')
def animal_delete(id):
    ''' A route that retrieves and deletes an animal for the given id. '''

    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()

    # Once the animal is deleted, return back to the list of remaining animals in collection
    return redirect(url_for('animal.animal_list'))