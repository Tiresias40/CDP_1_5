# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
from database import Sprint, Serializer

db = SQLAlchemy()

def addSprint(projectId, beginDate, endDate):
    newSprint = Sprint(project_id=projectId, begin_date=beginDate, end_date=endDate)
    db.session.add(newSprint)
    db.session.commit()

def deleteSprint(sprintId):
	sprintToDelete = Project.query.filter_by(id=sprintId)
    db.session.delete(sprintToDelete)
    db.session.commit()

def getSprints(projectId):
	queryResult = Sprint.query.all()
	return (queryResult)