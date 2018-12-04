# devManagement.py

from flask_sqlalchemy import SQLAlchemy
from database import Developers, Project, User, Serializer,db


def addDev(projectId,userId):
    newDev = Developers(project_id=projectId, user_id=userId)
    db.session.add(newDev)
    db.session.commit()

def getUser(userId):
    queryResult = User.query.filter_by(id=userId).first()
    return queryResult

def getDevs(projectId):
    resDevs =(db.session.query(User).join(Developers, User.id==Developers.user_id)).filter_by(project_id=projectId).all()
    return resDevs

def getUserWorkspace():
    queryResult = User.query.all()
    return queryResult

def deleteDev(userUsername, projectId):
    userID =  User.query.filter_by(username=userUsername).first().id
    projectID = Project.query.filter_by(id=projectId).first().id
    projectDevToDelete = Developers.query.filter_by(user_id=userID, project_id=projectID).first()
    db.session.delete(projectDevToDelete)
    db.session.commit()

def searchDev(userUsername):
    userID = User.query.filter_by(username=userUsername).first().id
    devContent = Developers.query.filter_by(user_id=userID).first()
    return (devContent)

def getDevProjects(userId):
    res = Developers.query.filter_by(user_id=userId).all()
    return res

def removeAllDevProjects(userId):
    res= Developers.query.filter_by(user_id=userId).all()
    for i in res:
        db.session.delete(i)
    db.session.commit()

def deleteAll():
    tmp= getDevWorkspace()
    for i in tmp:
        db.session.delete(i)
    db.session.commit()

def getDevWorkspace():
    res=  Developers.query.all()
    return res
