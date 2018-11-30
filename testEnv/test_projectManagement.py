import unittest
import projectManagement

from flask_sqlalchemy import SQLAlchemy
import database
from database import Project

class TestProjectManagement(unittest.TestCase):
	# is the db different from the main one ?
	def setUp(self):
		db = SQLAlchemy()

		database.initAllTables(db)

	def test_addProject(self):
		# need to create specific db ?
		projectManagement.addProject("test_addProject")
		query_result = Project.query.first()
		self.assertEqual(query_result.name, "test_addProject")

	def test_modifyProject(self):
		# can use name from above ?
		projectManagement.modifyProjectByName("test_addProject", "test_modifyProject")
		query_result = Project.query.first()
		self.assertEqual(query_result.name, "test_modifyProject")

	def test_getProject(self):
		query_result = projectManagement.getProject("test_modifyProject")
		self.assertEqual(query_result.name, "test_modifyProject")

	def test_deleteProject(self):
		projectManagement.deleteProject("test_modifyProject")
		query_result = Project.query.filter_by(name = "test_modifyProject").first()
		# None or query empty, don't know what works best
		self.assertEqual(query_result, None)

	def test_getProjectWorkspace(self):
		projectManagement.addProject("1")
		projectManagement.addProject("2")
		projectManagement.addProject("3")
		query_result = projectManagement.getProjectWorkspace()
		# not sure query_result[] is the right way to go
		self.assertEqual(query_result[0].name, "1")
		self.assertEqual(query_result[1].name, "2")
		self.assertEqual(query_result[2].name, "3")

	def tearDown(self):
		db.session.remove()
		db.dropAll()

if __name__ = '__main__':
	unittest.main()