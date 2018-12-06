# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
from database import Project, Serializer, db



def add_project(project_name):
    new_project = Project(name=project_name)
    db.session.add(new_project)
    db.session.commit()

def modify_project_name(current_name, new_name):
    Project.query.filter_by(name=current_name).first().update({'name': new_name})

def delete_project(name):
    project_to_delete = Project.query.filter_by(name=name).first()
    db.session.delete(project_to_delete)
    db.session.commit()

def get_project(project_name):
    query_result = Project.query.filter_by(name=project_name).first()
    return query_result

def get_project_by_id(project_id):
    query_result = Project.query.filter_by(id=project_id).first()
    return query_result

def get_project_workspace():
    query_result = Project.query.all()
    return query_result
