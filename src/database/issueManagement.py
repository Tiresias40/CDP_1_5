# issueManagement.py
from flask_sqlalchemy import SQLAlchemy
import uuid
import database
from database import Issue, db, Serializer



#
def add_issue(desc, priority, diff, sprint_id,project_id):
    new_issue = Issue(description=desc, priority=priority, difficulty=diff, sprint_id=sprint_id, project_id=project_id)
    db.session.add(new_issue)
    db.session.commit()

def get_issue(id):
    result_issue =Issue.query.filter_by(id=id)
    return result_issue.first()
#
def modify_issue(current_issue_id, desc, priority, diff, sprint_id,project_id):
    current_issue = get_issue(current_issue_id)
    current_issue.description =desc
    current_issue.priority = priority
    current_issue.difficulty =diff
    current_issue.sprint_id=sprint_id
    current_issue.project_id = project_id
    db.session.commit()

#
def delete_issue(issue_id):
    issue_to_delete =  get_issue(issue_id)
    db.session.delete(issue_to_delete)
    db.session.commit()
