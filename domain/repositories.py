# -*- coding: utf-8 -*-

from infra.database import BaseRepository
from domain.entities import Project


class AllProjects(BaseRepository):
    """
        handles all projects from and to database
    """

    def add(self, project):
        """
            add a project to database
        """
        return self.insert("""
                            INSERT INTO 
                            projects(name, description)
                            VALUES(%s, %s)
                           """, (project.name, project.description))
    
    def get(self, id):
        """
            get a project from database by id
        """
        result = self.query("select name, description from projects where id = %s", (id,), Project)[0]
        return result;
    
    def results(self):
        """
            return all projects from database
        """
        results = self.query("select name, description from projects", entity=Project)
        return results
    
class AllWorkItems(BaseRepository):
    """
        handles all work items from and to database
    """
    
    def add(self, workItem, projectId):
        """
            add a work item and associate it to a specified project
        """
        return self.insert("""
                            INSERT INTO 
                            work_items(project_id, name, importance, 
                                       estimative, test_case, notes, 
                                       reference, status_cod, requester_id,
                                        type_cod)
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                           """, (projectId, workItem.name, workItem.importance, 
                                 workItem.estimative, workItem.testCase,
                                  workItem.notes, workItem.reference, 
                                  2, 2, 
                                  2))