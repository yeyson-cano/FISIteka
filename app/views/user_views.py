# FISIteka/app/views/user_views.py

from flask import render_template, url_for, flash, redirect
from app import app, db
from app.models import User
from flask_login import login_required, current_user

@app.route("/user/<int:user_id>")
@login_required
def user_profile(user_id):
    user = User.query.get_or_404(user_id)
    
    # Solo los usuarios autenticados pueden ver perfiles de usuario
    if current_user.id != user_id:
        flash('No tienes permisos para ver este perfil.', 'danger')
        return render_template('error.html')

    return render_template('user_profile.html', user=user)
