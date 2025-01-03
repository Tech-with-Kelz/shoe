from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html", user=current_user)



@views.route('/about')
def about():
    return render_template("about.html", user=current_user)


@views.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you can add code to handle the contact form submission
        # For example, sending an email or saving to database
        flash('Thank you for your message! We will get back to you soon.', category='success')
        return redirect(url_for('views.contact'))
        
    return render_template("contact.html", user=current_user)
