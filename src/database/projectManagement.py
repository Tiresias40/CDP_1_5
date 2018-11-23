# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
import database
from database import Project, db, Serializer

def addProject(projectName):
    newProject = Project(name=projectName)
    db.session.add(newProject)
    db.session.commit()

# modify the Project currentId's name  to newName
def modifyProjectNameById(currentId,  newName):
    Project.query.filter_by(id=queryId).update({'name': name})

# modify the Project currentId's name  to newName
def modifyProjectNameByName(currentName,  newName):
    Project.query.filter_by(name=currentName).update({'name': name})

def deleteProject(name):
    projectToDelete = Project.query.filter_by(name=name)
    db.session.delete(projectToDelete)
    db.session.commit()

def getProject(projectId):
    queryResult = Project.query.filter_by(id=projectId).first()
    return queryResult

def getProjectWorkspace():
    queryResult =Project.query.all()
    return (queryResult)
