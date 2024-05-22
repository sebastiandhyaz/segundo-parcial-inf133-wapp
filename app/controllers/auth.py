    from flask import Blueprint, render_template, redirect, url_for, request, flash
    from flask_login import login_user, logout_user, login_required, current_user
    from werkzeug.security import generate_password_hash, check_password_hash
    from app.models import User
    from app import db

    bp = Blueprint('auth', __name__)

    @bp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()

            if user and user.check_password(password):
                login_user(user)
                return redirect(url_for('patients.list_patients'))

            flash('Invalid username or password')
        return render_template('login.html')

    @bp.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('auth.login'))

    @bp.route('/users', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form['role']

            user = User(username=username, role=role)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        return render_template('register.html')