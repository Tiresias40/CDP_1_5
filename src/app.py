# This file contains an example Flask-User application.
# To keep the example simple, we are applying some unusual techniques:
# - Placing everything in one file
# - Using class-based configuration (instead of file-based configuration)
# - Using string-based templates (instead of file-based templates)

from flask import Flask, render_template_string, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin
import sys
import os
sys.path.insert(0, os.getcwd()+"/database")
sys.path.insert(1, os.getcwd()+"/templates")
import database
import projectManagement
import devManagement
import json

# Class-based application configuration
class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///quickstart_app.sqlite'    # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-User settings
    USER_APP_NAME = "Scrum Tool App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = False      # Disable email authentication
    USER_ENABLE_USERNAME = True    # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form


def create_app():
    """ Flask application factory """

    # Create Flask app load app.config
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(__name__+'.ConfigClass')

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    #include All models made on DB analysis step, setup Flask-User and specify the User data-model

    db = database.initAllTables(db)



    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, database.User)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        # String-based templates
        return render_template("index.html")

    # The Members page is only accessible to authenticated users via the @login_required decorator
    @app.route('/members')
    @login_required    # User must be authenticated
    def member_page():
        # String-based templates
        return render_template_string("""
            {% extends "layout.html" %}
            """)

    #test including html pages from a template dir


    @app.route('/issuesPage')
    @login_required
    def issues_page():
        try:
            issueList =[]
            issue = issueManagement.getProjectWorkspace()
            for issue in issues:
                projectList.append(database.Serializer.serialize(pr))
            projectList= str(projectList)
        except Exception ,e:
            print str(e)
        return render_template("issues.html")

    @app.route('/projectsPage')
    @login_required
    def projects_page():
        projects = projectManagement.getProjectWorkspace()

        return render_template("projectManagement.html", projectsContent = projects)


    @app.route('/addProject', methods=['POST'])
    def add_project():
        projectName = request.form['projectname']
        projectManagement.addProject(projectName)
        newProject = projectManagement.getProjectByName(projectName)

        return (database.Serializer.serialize(newProject))


    @app.route('/usersAvailable', methods=['POST'])
    def add_dev():
        devs = devManagement.getUserWorkspace()
        devsAvailable="Empty"
        try:
            projectId = int(request.get_data())

            devsAlreadyAssigned = devManagement.getDevs(projectId)
            print(str(devsAlreadyAssigned)+"okok")
            for elt in devsAlreadyAssigned:
                if elt in devs:
                    devs.remove(elt)
            if len(devs) != 0:
                print(str(devs)+"users dispo")
                devsAvailable =listToJson(devs, 'devs')
        except Exception ,e:
            print str(e)

        return devsAvailable


    @app.route('/managementPage')
    @login_required
    def management_page():

        try:
            project = projectManagement.getProject(6)
            users = devManagement.getDevs(6)
            print(str(users)+"devs deja Add")
        except Exception ,e:
            print str(e)

        return render_template("devManagement.html", project=project, usersAdded=users)

    def listToJson(list, listName):
        res='{"'+listName+'" : ['
        for elt in list:
            res += database.Serializer.serialize(elt)+','
        res = res[:-1]+']}'
        return res

    @app.route('/addDevs', methods=['POST'])
    def add_devs_project():
        devsResult = request.get_data()
        jsonResult =json.loads(devsResult)
        for elt in jsonResult['users']:
            devManagement.addDev(int(jsonResult['id']), int(elt))
        devsToDisplay = listToJson(devManagement.getDevs(int(jsonResult['id'])),'devs')
        return devsToDisplay


    @app.route('/deleteDev', methods=['DELETE'])
    def delete_confirm():
        data = json.loads(request.get_data())
        #collecting current project_id
        projectId=int(data['project_id'])
        #collecting uusername to Remove related user from project
        username = data['username']
        devManagement.deleteDev(username,projectId)
        return "200"
    return app



# Start development web server
if __name__=='__main__':

    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
