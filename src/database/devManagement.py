# devManagement.py

from flask_sqlalchemy import SQLAlchemy
import database
from database import Developers,Project, User, Serializer

db = SQLAlchemy()

def addDev(projectId,userId):
    newDev = Developers(project_id=projectId, user_id=userId)
    db.session.add(newDev)
    db.session.commit()

def getUser(username):
    userId = User.query.filter_by(username=username).first().id
    dev = Developer

def getDevs(projectId):
    devs = Developer.query.filter_by(project_id=projectId)
    resDevs = User.query.join(devs)
    return resDevs

def getUserWorkspace():
    queryResult = User.query.all()
    return queryResult

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

def getDevProjects(userId):
    res = Developers.query.filter_by(user_id=userId)
    return res

def removeAllDevProjects(userId):
    res= Developers.query.filter_by(user_id=userId)
    for i in res:
        db.session.delete(i)
    db.session.commit()

def getDevWorkspace():
    res=  Developers.query.all()
    return res
