# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
from database import Project, Serializer, db



def addProject(projectName):
    newProject = Project(name=projectName)
    db.session.add(newProject)
    db.session.commit()

# modify the Project currentId's name  to newName
def modifyProjectNameByName(currentName,  newName):
    Project.query.filter_by(name=currentName).first().update({'name': newName})

def deleteProject(name):
    projectToDelete = Project.query.filter_by(name=name).first()
    db.session.delete(projectToDelete)
    db.session.commit()

def getProject(projectName):
    queryResult = Project.query.filter_by(name=projectName).first()
    return queryResult

def getProjectById(projectId):
    queryResult = Project.query.filter_by(id=projectId).first()
    return queryResult

def getProjectWorkspace():
    queryResult = Project.query.all()
    return queryResult
