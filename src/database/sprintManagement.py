# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
from database import Sprint, Serializer
import projectManagement
import datetime

db = SQLAlchemy()

def addSprint(projectName, beginDate):
	endDate = datetime.datetime.strptime(beginDate, "%Y-%m-%d") + datetime.timedelta(days=15)
	sprint_project = projectManagement.getProject(projectName)
	newSprint = Sprint(project_id=sprint_project.id, begin_date=datetime.datetime.strptime(beginDate, "%Y-%m-%d"), end_date=endDate)
	db.session.add(newSprint)
	db.session.commit()

def deleteSprint(sprintId):
	sprintToDelete = Sprint.query.filter_by(id=sprintId).first()
	db.session.delete(sprintToDelete)
	db.session.commit()

def getSprints(projectId):
	queryResult = Sprint.query.filter_by(project_id=projectId).all()
	return queryResult
