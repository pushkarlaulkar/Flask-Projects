from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
	if(request.method == 'POST'):
		note = request.form.get('note')
		new_note = Note(data=note, user_id = current_user.id)
		db.session.add(new_note)
		db.session.commit()
		flash('Note Added!!', category='success')
	return render_template("home.html", user=current_user)
	
@views.route('/delete/<int:noteid>')
def delete(noteid):
	note_to_delete = Note.query.get(noteid)
	db.session.delete(note_to_delete)
	db.session.commit()
	flash('Note Deleted!!', category='error')
	return redirect(url_for('views.home'))