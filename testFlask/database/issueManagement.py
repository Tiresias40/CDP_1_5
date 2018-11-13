# projectManagement.py
from flask_sqlalchemy import SQLAlchemy
import uuid
import database
from database import Issue, db, Serializer



#
def addIssue(issue):
    db.session.add(issue)
    db.session.commit()

#
def modifyIssue(currentIssue,newIssue):


#
def deleteIssue(issue):
