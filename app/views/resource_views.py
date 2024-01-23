# FISIteka/app/views/resource_views.py

from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Resource
from app.forms import ResourceForm
from flask_login import login_required, current_user

@app.route("/")
@app.route("/index")
def index():
    resources = Resource.query.all()
    return render_template('index.html', resources=resources, current_user=current_user)

@app.route("/resource/<int:resource_id>")
@login_required
def resource_detail(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    return render_template('resource_detail.html', resource=resource)

@app.route("/resource/new", methods=['GET', 'POST'])
@login_required
def new_resource():
    form = ResourceForm()
    if form.validate_on_submit():
        resource = Resource(title=form.title.data, description=form.description.data, uploaded_by=current_user.id)
        db.session.add(resource)
        db.session.commit()
        flash('Recurso creado exitosamente.', 'success')
        return redirect(url_for('index'))
    return render_template('new_resource.html', form=form)


