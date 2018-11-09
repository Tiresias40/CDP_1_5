# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
import uuid
import json
import database
db =SQLAlchemy()

def addProject(projectName):
    sql= "INSERT INTO projects (id,name) VALUES (1,'"+projectName+"')"
    result =db.engine.execute(sql)

#def modifyProject(name):


def getProjectWorkspace():
    sql= "Select * from projects"
    return json.dumps(db.engine.execute(sql))
# TODO def getUserWorkspace
