# issueManagement.py
from flask_sqlalchemy import SQLAlchemy
import uuid
import database
from database import Issue, db, Serializer



#
def addIssue(desc, priority, diff, sprintId,projectId):
    newIssue = Issue(description=desc, priority=priority, difficulty=diff, sprint_id=sprintId, project_id=projectId)
    db.session.add(newIssue)
    db.session.commit()

def getIssue(id):
    resultIssue =Issue.query.filter_by(id=id)
    return resultIssue.first()
#
def modifyIssue(currentIssueId, desc, priority, diff, sprintId,projectId):
    currentIssue = getIssue(currentIssueId)
    currentIssue.description =desc
    currentIssue.priority = priority
    currentIssue.difficulty =diff
    currentIssue.sprint_id=sprintId
    currentIssue.project_id = projectId
    db.session.commit()

#
def deleteIssue(issueID):
    issueToDelete =  getIssue(issueID)
    db.session.delete(issueToDelete)
    db.session.commit()
