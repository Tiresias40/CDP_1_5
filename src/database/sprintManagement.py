# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
from database import Sprint, Serializer,db
import projectManagement
import datetime



def add_sprint(project_name, begin_date):
	end_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d") + datetime.timedelta(days=15)
	sprint_project = projectManagement.get_project(project_name)
	new_sprint = Sprint(project_id=sprint_project.id, begin_date=datetime.datetime.strptime(begin_date, "%Y-%m-%d"), end_date=end_date)
	db.session.add(newSprint)
	db.session.commit()

def delete_sprint(sprint_id):
	sprint_to_delete = Sprint.query.filter_by(id=sprint_id).first()
	db.session.delete(sprint_to_delete)
	db.session.commit()

def get_sprints(project_id):
	query_result = Sprint.query.filter_by(project_id=project_id).all()
	return query_result
