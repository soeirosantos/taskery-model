# -*- coding: utf-8 -*-

from springpython.config import PythonConfig
from springpython.config import Object
from springpython.context import scope
from services import TaskeryService
from domain.repositories import AllProjects, AllWorkItems
from springpython.database import factory
from infra.database import SpringDaoWrapper


class TaskeryApplicationContext(PythonConfig):
    def __init__(self):
        super(TaskeryApplicationContext, self).__init__()

    @Object(scope.PROTOTYPE)
    def projectService(self):
        return TaskeryService(self.allProjects(), self.allWorkItems(), self.connectionFactory().getConnection());
    
    @Object(scope.PROTOTYPE)
    def allProjects(self):
        daoWrapper = SpringDaoWrapper(self.connectionFactory())
        return AllProjects(daoWrapper)

    @Object(scope.PROTOTYPE)
    def allWorkItems(self):
        daoWrapper = SpringDaoWrapper(self.connectionFactory())
        return AllWorkItems(daoWrapper)
    
    @Object
    def connectionFactory(self):
        return factory.MySQLConnectionFactory(username="root", password="", hostname="localhost", db="taskery_db")
    
    
