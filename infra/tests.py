# -*- coding: utf-8 -*-

import unittest
from domain.entities import Project, WorkItem
import context
from springpython.context import ApplicationContext
    
class Test(unittest.TestCase):
    """
        These are integration tests for domain model
    """

    def getService(self):
        applicationContext = ApplicationContext(context.TaskeryApplicationContext());
        return applicationContext.get_object("taskeryService")
    
    def testShouldCreateAProject(self):
        project = newProject()
        assert(project.id == None);
        id = self.getService().createProject(project);
        assert(id > 0);


    def testListProjects(self):
        self.getService().createProject(newProject());
        self.getService().createProject(newProject());
        assert(self.getService().listAllProjects() >= 2)         
    
    def testGetProject(self):
        project = newProject()
        project.name = "my project"
        id = self.getService().createProject(project);
        assert(id > 0);
        project_ = self.getService().getProjectById(id)
        assert project.name == project_.name
        
        
    def testShouldIncludeWorkItensInAProject(self):
        project = Project();
        self.assertEquals(project.totalItems(), 0, "there should be no item in the project"); 

        wi1 = WorkItem(project=project);
        project.addWorkItem(wi1);
        
        wi2 = WorkItem(project=project);
        project.addWorkItem(wi2);
        
        wi3 = WorkItem(project=project);
        project.addWorkItem(wi3);

        wi4 = WorkItem(project=project);
        project.addWorkItem(wi4);
        
        self.assertEquals(project.totalItems(), 4, "there should be 4 items in project"); 

    def testWorkItemShowldBeValid(self):
        pass
    
    def testShouldAddAWorkItem(self):
        wi = WorkItem
        id = self.getService().addWorkItem(wi, newProject())
        assert(id > 0);
        
    def setUp(self):
        unittest.TestCase.setUp(self)
        
        
def newProject():
    project = Project();
    project.name = "Taskery"
    project.description = "controle de tarefas"
    return project
        
if __name__ == "__main__":
    unittest.main()
