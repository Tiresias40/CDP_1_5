# devManagement.py

from flask_sqlalchemy import SQLAlchemy
import database
from database import Developers,Project, User, db, Serializer


def addDev(projectName,userUsername):
    projectID = Project.query.filter_by(name=projectName).first().id
    userID = User.query.filter_by(username=userUsername).first().id
    newDev = Developers(project_id=projectID, user_id=userID)
    db.session.add(newDev)
    db.session.commit()

def deleteDev(userUsername, projectName):
    userID =  User.query.filter_by(username=userUsername).first().id
    projectID = Project.query.filter_by(name=projectName).first().id
    projectDevToDelete = Developers.query.filter_by(user_id=userID, project_id=projectID).first()
    db.session.delete(projectDevToDelete)
    db.session.commit()

def searchDev(userUsername):
    userID = User.query.filter_by(username=userUsername).first().id
    devContent = Developers.query.filter_by(user_id=userID).first()
    return (devContent)
