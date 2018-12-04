# This file contains an example Flask-User application.
# To keep the example simple, we are applying some unusual techniques:
# - Placing everything in one file
# - Using class-based configuration (instead of file-based configuration)
# - Using string-based templates (instead of file-based templates)

from flask import Flask, render_template_string, request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_user import login_required, UserManager, UserMixin
import sys
import os
sys.path.insert(0, os.getcwd()+"/database")
sys.path.insert(1, os.getcwd()+"/templates")
import database
import projectManagement
import devManagement
import sprintManagement
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
    database.initAllTables(db)

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, database.User)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        # String-based templates
        return render_template("index.html")

    @app.route('/projectsPage')
    @login_required
    def projects_page():
        projects = projectManagement.getProjectWorkspace()

        return render_template("projectManagement.html", projectsContent = projects)


    @app.route('/addProject', methods=['POST'])
    def add_project():
        projectName = request.form['projectname']
        projectManagement.addProject(projectName)
        newProject = projectManagement.getProject(projectName)

        return (database.Serializer.serialize(newProject))


    @app.route('/usersAvailable', methods=['POST'])
    def add_dev():

        devsAvailable="Empty"
        try:
            devs = devManagement.getUserWorkspace()
            projectId = int(request.get_data())
            devsAlreadyAssigned = devManagement.getDevs(projectId)
            for element in devsAlreadyAssigned:
                for i in devs:
                    if i.id==element.id:
                        devs.remove(i)
            if len(devs) != 0:
                devsAvailable =listToJson(devs, 'devs')
        except Exception ,e:
            print str(e)

        return devsAvailable


    @app.route('/managementPage')
    @login_required
    def management_page():

        try:
            project = projectManagement.getProjectById(3)
            users = devManagement.getDevs(3)
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
        currentProjectId = int(jsonResult['id'])
        devsAdded =[]
        for elt in jsonResult['users']:
            devManagement.addDev(currentProjectId, int(elt))
            devsAdded.append(devManagement.getUser(int(elt)))
        devsAdded = listToJson(devsAdded,'devs')
        return devsAdded


    @app.route('/deleteDev', methods=['DELETE'])
    def delete_confirm():
        data = json.loads(request.get_data())
        #collecting current project_id
        projectId=int(data['project_id'])
        #collecting username to Remove related user from project
        username = data['username']
        devManagement.deleteDev(username,projectId)
        return "200"

    @app.route('/issuesPage')
    @login_required
    def issues_page():
        try:
            #currentProjectId=request.get_data()
            issueList =[]
            sprintsList =sprintManagement.getSprints(3)
            issue = issueManagement.getProjectWorkspace()
            for issue in issues:
                projectList.append(database.Serializer.serialize(pr))
            projectList = str(projectList)
        except Exception as e:
            str(e)
        return render_template("issues.html", sprintsContent=sprintsList)


    @app.route('/addIssue')
    @login_required
    def add_issue():
        return ""


    @app.route('/sprintsPage')
    @login_required
    def sprints_page():
        try:
            sprints = sprintManagement.getSprints(3)
        except Exception as e:
            print(str(e))
        return render_template("sprintManagement.html", sprintsContent=sprints)

    @app.route('/addSprint', methods=['POST'])
    def add_sprint():
        sprint_begin_date = request.form['beginDate']
        sprint_project_name = request.form['projectName']
        sprintManagement.addSprint(sprint_project_name, sprint_begin_date)
        #print(str(sprintManagement.getSprints()))

        return redirect('/sprintsPage')
        # Can also do return redirect(url_for('sprints_page')) too if import url_for from flask

    @app.route('/deleteSprint', methods=['DELETE'])
    def delete_sprint():
        sprint_id = request.form['sprintId']
        sprintManagement.deleteSprint(sprint_id)

        return redirect('/sprintsPage')

    @app.route('/setCurrentProject', methods=['POST'])
    def get_current_project_id():
        currentProjectId=request.get_data()
        return redirect('/'+currentProjectId+'/dashBoardPage')

    @app.route('/<int:project_id>/dashBoardPage')
    def init_dashboard(project_id):
        currentProjectContent = projectManagement.getProjectById(project_id)
        return render_template("dashboard.html", currentProjectContent=currentProjectContent)

    return app




# Start development web server
if __name__=='__main__':

    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
