from flask import render_template, Blueprint, session, flash

from .auth import access_required
from .models import User, Role, projectAssigned
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_feedback')
@login_required
def add_feedback():
    return render_template('feedback.html')

@main.route('/projects')
@login_required
@access_required('Admin or ProjectManager')
def create_project():
    projects = projectAssigned.query.filter_by(projectManager=session['user']).all()
    employees = User.query.filter(Role.name == "Employee").outerjoin(Role, Role.id == User.id).all()
    if projects:
        return render_template('projects.html', projects=projects,employees=employees)
    flash('You are not assigned to any project and hence cannot create a  new project, pls contact admin')
    return render_template('index.html')

@main.route('/steps', methods=['POST'])
@login_required
@access_required('Admin or ProjectManager')
def steps():
    return render_template('steps.html')

if __name__ == '__main__':
    app.run(debug=True)
