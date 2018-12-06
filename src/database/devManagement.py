# devManagement.py

from flask_sqlalchemy import SQLAlchemy
from database import Developers, Project, User, Serializer,db


def add_dev(project_id,user_id):
    new_dev = Developers(project_id=project_id, user_id=user_id)
    db.session.add(new_dev)
    db.session.commit()

def get_user(user_id):
    query_result = User.query.filter_by(id=user_id).first()
    return query_result

def get_devs(project_id):
    query_result =(db.session.query(User).join(Developers, User.id==Developers.user_id)).filter_by(project_id=project_id).all()
    return query_result

def get_user_workspace():
    query_result = User.query.all()
    return query_result

def delete_dev(user_username, project_id):
    user_id =  User.query.filter_by(username=user_username).first().id
    project_id = Project.query.filter_by(id=project_id).first().id
    project_dev_to_delete = Developers.query.filter_by(user_id=user_id, project_id=project_id).first()
    db.session.delete(project_dev_to_delete)
    db.session.commit()

def search_dev(user_username):
    user_id = User.query.filter_by(username=user_username).first().id
    query_result = Developers.query.filter_by(user_id=user_id).first()
    return (query_result)

def get_dev_projects(user_id):
    query_result = Developers.query.filter_by(user_id=user_id).all()
    return query_result

def remove_all_dev_projects(user_id):
    query_result = Developers.query.filter_by(user_id=user_id).all()
    for i in query_result :
        db.session.delete(i)
    db.session.commit()

def delete_all():
    all_dev = get_all_dev()
    for i in all_dev :
        db.session.delete(i)
    db.session.commit()

def get_all_dev():
    query_result =  Developers.query.all()
    return query_result
