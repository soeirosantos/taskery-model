# -*- coding: utf-8 -*-

class TaskeryService(object):
    """
        Facade and entry point for domain model
    """
    
    def __init__(self, allProjects=None, allWorkItems=None, conn=None):
        self.conn = conn
        self.allProjects = allProjects
        self.allWorkItems = allWorkItems
    
    def createProject(self, project):
        """
            insert a new project in database
        """
        id = self.allProjects.add(project);
        self.conn.commit()
        return id;

    def listAllProjects(self):
        """
            retrieve all projects
        """
        return self.allProjects.results()
    
    def getProjectById(self, id):
        """
            get a project by its id that represents primary key of database
        """
        
        return self.allProjects.get(id)
    
    def addWorkItem(self, workItem, projectId):
        """
            add a work item and associate it with a project
        """
        id = self.allWorkItems.add(workItem, projectId)
        self.conn.commit()
        return id