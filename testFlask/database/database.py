# database.py

from flask_user import  UserManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
import uuid

#db = SQLAlchemy()



def initAllTablesAndSetupUserManager(app,db):

    # Define the User data-model.
    # NB: Make sure to add flask_user UserMixin !!!
    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True, unique=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        # User authentication information. The collation='NOCASE' is required
        # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
        username = db.Column(db.String(100, collation='NOCASE'), nullable=False, unique=True)
        password = db.Column(db.String(255), nullable=False, server_default='')
        email_confirmed_at = db.Column(db.DateTime())

        # User information
        first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
        last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')


    # Define the Issue data-model.
    # NB:
    class Issue(db.Model):
        __tablename__ = 'issues'
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.Text(), nullable=False, unique=True)
        priority = db.Column(db.String(10), nullable=False, unique=False)
        difficulty = db.Column(db.Integer)
        sprint_id = db.Column(db.Integer)
        project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

        def __repr__(self):
            return '<Issue %r %r %r>' % (self.id, self.description, self.priority)

    # Define the Project data-model.
    # NB:
    class Project(db.Model):
        __tablename__ = 'projects'
        id = db.Column( db.Integer, primary_key=True)
        name = db.Column(db.String(20), nullable=False)
        # foreign keys relationship usefull for simple query acces
        sprints = db.relationship('Sprint', backref='projects')
        issues = db.relationship('Issue', backref='projects')

        def __init__(self, name):
            self.name= name

        def __repr__(self):
            return '<Project %r %r>' % (self.id, self.name)



    # Define the Sprint data-model.
    # NB:
    class Sprint(db.Model):
        __tablename__ = 'sprints'
        id = db.Column(db.Integer, primary_key=True)
        begin_date = db.Column(db.DateTime())
        end_date = db.Column(db.DateTime())
        project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
        tasks = db.relationship('Task', backref='sprints')

        def __repr_(self):
            return '<Sprint %r %r %r %r %r>' % (self.id, self.begin_date, self.end_date, self.id, self.tasks)


    # Define the Task data-model.
    # NB:
    class Task(db.Model):
        __tablename__ = 'tasks'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(5), nullable=False)
        description = db.Column(db.Text(), nullable=False)
        costs = db.Column(db.Float, nullable=True)
        status = db.Column(db.String(5), nullable=False)
        sprint_id = db.Column(db.Integer, db.ForeignKey('sprints.id'), nullable=False)
        dependencies = db.Column(db.String(50), nullable=True)


    class Developers(db.Model):
        __tablename__ = 'developers'
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
        project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)

    # Create all database tables
    db.create_all()

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    return db
