# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
import uuid
import json

db =SQLAlchemy()

def addProject(projectName):
    sql= "INSERT INTO projects (id,name) VALUES (1,'"+projectName+"')"
    result =db.engine.execute(sql)

#def modifyProject(name):


def getProjectWorkspace():
    return json.dump(Project.query.all())
# TODO def getUserWorkspace
