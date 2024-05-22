from flask import Blueprint, render_template, request, redirect, url_for, flash
    from flask_login import login_required, current_user
    from app.models import Patient
    from app import db

    bp = Blueprint('patients', __name__)

    @bp.route('/patients')
    @login_required
    def list_patients():
        patients = Patient.query.all()
        return render_template('list_patients.html', patients=patients)

    @bp.route('/patients/create', methods=['GET', 'POST'])
    @login_required
    def create_patient():
        if request.method == 'POST':
            name = request.form['name']
            lastname = request.form['lastname']
            ci = request.form['ci']
            birth_date = request.form['birth_date']

            patient = Patient(name=name, lastname=lastname, ci=ci, birth_date=birth_date)
            db.session.add(patient)
            db.session.commit()
            return redirect(url_for('patients.list_patients'))
        return render_template('create_patient.html')

    @bp.route('/patients/<int:id>/update', methods=['GET', 'POST'])
    @login_required
    def update_patient(id):
        patient = Patient.query.get_or_404(id)
        if request.method == 'POST':
            patient.name = request.form['name']
            patient.lastname = request.form['lastname']
            patient.ci = request.form['ci']
            patient.birth_date = request.form['birth_date']

            db.session.commit()
            return redirect(url_for('patients.list_patients'))
        return render_template('update_patient.html', patient=patient)

    @bp.route('/patients/<int:id>/delete', methods=['GET', 'POST'])
    @login_required
    def delete_patient(id):
        patient = Patient.query.get_or_404(id)
        if request.method == 'POST':
            db.session.delete(patient)
            db.session.commit()
            return redirect(url_for('patients.list_patients'))
        return render_template('delete_patient.html', patient=patient)