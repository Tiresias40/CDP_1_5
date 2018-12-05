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
import socket
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
        projects = projectManagement.get_project_workspace()

        return render_template("projectManagement.html", projectsContent = projects)


    @app.route('/addProject', methods=['POST'])
    def add_project():
        project_name = request.form['projectname']
        projectManagement.add_project(project_name)
        new_project = projectManagement.get_project(project_name)

        return (database.Serializer.serialize(new_project))


    @app.route('/usersAvailable', methods=['POST'])
    def add_dev():
        try:
            devs = devManagement.getUserWorkspace()
            project_id = int(request.get_data())
            devs_already_assigned = devManagement.getDevs(project_id)
            for element in devs_already_assigned:
                for i in devs:
                    if i.id == element.id:
                        devs.remove(i)
            if len(devs) != 0:
                devs_available = listToJson(devs, 'devs')
        except Exception as e:
            print(str(e))

        return devs_available


    @app.route('/managementPage')
    @login_required
    def management_page():

        try:
            project = projectManagement.get_project_by_id(3)
            users = devManagement.getDevs(3)
        except Exception as e:
            print(str(e))

        return render_template("devManagement.html", project=project, usersAdded=users)

    @app.route('/addDevs', methods=['POST'])
    def add_devs_project():
        devs_result = request.get_data()
        json_result =json.loads(devs_result)
        current_project_id = int(json_result['id'])
        devs_added =[]
        for el in json_result['users']:
            devManagement.addDev(current_project_id, int(el))
            devs_added.append(devManagement.getUser(int(el)))
        devs_added = list_to_json(devs_added,'devs')
        return devs_added


    @app.route('/deleteDev', methods=['DELETE'])
    def delete_confirm():
        data = json.loads(request.get_data())
        #collecting current project_id
        project_id = int(data['project_id'])
        #collecting username to Remove related user from project
        username = data['username']
        devManagement.deleteDev(username, project_id)
        return "200"

    @app.route('/issuesPage')
    @login_required
    #function unfinished
    def issues_page():
        try:
            sprints_list = sprintManagement.getSprints(3)
            issue_list = issueManagement.getProjectWorkspace()
            for issue in issue_list:
                project_list.append(database.Serializer.serialize(issue))
            project_list = str(project_list)
        except Exception as e:
            print(str(e))
        return render_template("issues.html", sprintsContent=sprints_list)


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

    @app.route('/deleteSprint', methods=['DELETE'])
    def delete_sprint():
        sprint_id = request.form['sprintId']
        sprintManagement.deleteSprint(sprint_id)

        return redirect('/sprintsPage')

    @app.route('/setCurrentProject', methods=['POST'])
    def get_current_project_id():
        current_project_id = request.get_data()
        return redirect('/'+current_project_id+'/dashBoardPage')

    @app.route('/<int:project_id>/dashBoardPage')
    def init_dashboard(project_id):
        current_project_content = projectManagement.get_project_by_id(project_id)
        return render_template("dashboard.html", currentProjectContent=current_project_content)

    return app

def list_to_json(list, list_name):
    res='{"'+list_name+'" : ['
    for elt in list:
        res += database.Serializer.serialize(elt)+','
    res = res[:-1]+']}'
    return res




# Start development web server
if __name__=='__main__':

    ip_address = socket.gethostbyname(socket.gethostname())
    app = create_app()
    app.run(host=ip_address, port=5000, debug=True)
