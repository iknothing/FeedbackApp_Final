from . import db
from flask_login import UserMixin
from datetime import date

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    email = db.Column(db.String(255,collation='NOCASE'), unique=True)
    password=db.Column(db.String(255))
    email_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    email_confirmed_at = db.Column(db.DateTime, nullable=True)
    type = db.Column(db.String(255))
    roles = db.relationship('Role', secondary='user_roles')
    projectAssigned = db.Column(db.String(255))


class projectAssigned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectNo = db.Column(db.String(255))
    projectManager = db.Column(db.String(255))


class Project(db.Model):
    __tablename__='projectdetails'
    projectNo= db.Column(db.String(255), primary_key=True)
    customerName=db.Column(db.String(255))
    buyerName=db.Column(db.String(255))
    partName=db.Column(db.String(255))
    partNo=db.Column(db.Integer)
    projectCoordinator=db.Column(db.String(255))
    projectManager=db.Column(db.String(255))
    projectStart=db.Column(db.Date,default=date.today())
    dispatchDate=db.Column(db.Date, default=date.today())
    poQty=db.Column(db.Integer)
    stepCount=db.Column(db.Integer)
    partImage=db.Column(db.LargeBinary)
    usersAssigned = db.Column(db.Text())
    projectApproved = db.Column(db.Boolean, nullable=False, default=False)
    projectRejected = db.Column(db.Boolean, nullable=False, default=True)
    Status=db.Column(db.Boolean, default=False)

class Step(db.Model):
    __tablename__='stepdetails'
    id= db.Column(db.Integer, primary_key=True)
    projectNo=db.Column(db.String(255), db.ForeignKey('projectdetails.projectNo'))
    stepName=db.Column(db.String(255))
    stepDays=db.Column(db.Integer)
    stepStart = db.Column(db.Date, default=date.today())
    stepEnd = db.Column(db.Date, default=date.today())
    stepStatus = db.Column(db.String(255))
    stepActualCompletion = db.Column(db.Date, default=stepEnd)
    index=db.Column(db.Integer)

class Feedback(db.Model):
    __tablename__='feedback'
    feedbackId=db.Column(db.String(255), primary_key=True)
    projectNo = db.Column(db.String(255), db.ForeignKey('projectdetails.projectNo'))
    email=db.Column(db.String(255), db.ForeignKey('user.email'))
    password=db.Column(db.String(255), db.ForeignKey('user.password'))
    role=db.Column(db.String(255))
    curDate=db.Column(db.Date, default=date.today())
    remarks=db.Column(db.Text())
    feedbackImage=db.Column(db.LargeBinary)
    indexforFeedback=db.Column(db.Integer)
    filename=db.Column(db.String(255))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

class UserProject(db.Model):
    __tablename__ = 'user_project'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    projectNo = db.Column(db.String(255), db.ForeignKey('projectdetails.projectNo', ondelete='CASCADE'))