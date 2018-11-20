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
    app = Flask(__name__)
    app.config.from_object(__name__+'.ConfigClass')

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    #include All models made on DB analysis step, setup Flask-User and specify the User data-model
    db = database.initAllTablesAndSetupUserManager(app,db)

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, database.User)

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        # String-based templates
        return render_template_string("""
            {% include "navSimple.html" %}
            {% extends "flask_user_layout.html" %}
            """)

    # The Members page is only accessible to authenticated users via the @login_required decorator
    @app.route('/members')
    @login_required    # User must be authenticated
    def member_page():
        # String-based templates
        return render_template_string("""
            {% include "navSimple.html" %}
            {% extends "flask_user_layout.html" %}
            """)

    #test including html pages from a template dir

    @app.route('/projects')
    def getProjectList():
        try:
            projectList =[]
            projects = projectManagement.getProjectWorkspace()
            for pr in projects:
                projectList.append(database.Serializer.serialize(pr))
        except Exception ,e:
            print str(e)

        return projectList

    #@app.route('/addProjectDisplay')
    #def add_project_display():



    @app.route('/issuesPage')
    def issues_page():
        try:
            issueList =[]
            issue = issueManagement.getProjectWorkspace()
            for issue in issues:
                projectList.append(database.Serializer.serialize(pr))
            projectList= str(projectList)
        except Exception ,e:
            print str(e)
        return render_template_string("""
            {% include "nav.html" %}
            {% include "issues.html" %}
        """)

    @app.route('/projectsPage')
    def projects_page():
        try:
            projectList =[]
            projects = projectManagement.getProjectWorkspace()
            for pr in projects:
                projectList.append(database.Serializer.serialize(pr))
            projectList= str(projectList)
        except Exception ,e:
            print str(e)

        return render_template_string("""
            {% include "navSimple.html" %}
            {%  block content %}
            {% include "index.html" %}
            {{ listProject }}
            {% endblock %}
        """, listProject = projectList)


    @app.route('/addProject', methods=['POST','GET'])
    def add_project():
        projectName = request.form['projectname']
        projectManagement.addProject(projectName)
        newProject = projectManagement.getProject(projectName)

        return (database.Serializer.serialize(newProject))


    @app.route('/addDev')
    def add_dev():
        devManagement.addDev('Test 1', 'nezout')
        return render_template_string("""
            {% block content %}
                <h2> OK Ajout nezout</h2>
            {% endblock %}
        """)


    @app.route('/managementPage')
    def management_page():
        #projectManagement.addProject('Test 1')
        #projectManagement.addProject('Test 2')

        devSearched = devManagement.searchDev('nezout')

        return render_template_string("""
            {% include "nav.html" %}
            {% include "devManagement.html" %}
            {% block content %}
                <h2> Dev Management Page </h2>
                <p><a href={{ url_for('add_dev') }}>Add Developer</a> </p>
                <p><a href={{ url_for('delete_confirm') }}>Delete Developer</a> </p>

                {{nezoutDev}}
            {% endblock %}
        """, nezoutDev= devSearched)

    @app.route('/deleteDev')
    def delete_confirm():
        devManagement.deleteDev('nezout', 'Test 1')
        return render_template_string("""
            {%  block content %}
                <h2> Dev supprime </h2>
            {% endblock %}
        """)

    return app


# Start development web server
if __name__=='__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
