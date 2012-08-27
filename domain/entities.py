# -*- coding: utf-8 -*-

from datetime import date

class Entity(object):
    def __init__(self, id = None):
        self.id = id
   
    def isNew(self):
        return self.id is None

class Project(Entity):

    def __init__(self, id=None, name=None, description=None):
        Entity.__init__(self, id)
        self.name = name
        self.items = list()
        self.description = description

    
    def addWorkItem(self, wi):
        """
        add a WorkItem to a specific project
        the list of items is used for proccess any calculations
        from items of a project, like total estimated hours and
        others
        """
        self.items.append(wi)
        wi.project = self

    
    def totalItems(self):
        return len(self.items)
    
class WorkItem(Entity):
    def __init__(self, id=None, project=None, name=None, importance=None, estimative=None, testCase=None, notes=None, referece=None, status=None, requester=None, type=None):
        Entity.__init__(self, id)
        self.name = name
        self.importance = importance
        self.estimative = estimative
        self.testCase = testCase
        self.notes = notes
        self.reference = referece
        self.requester=requester
        self.status = status    # [not yet started, started, and finished]
        self.type = type        #[Feature, Task, Bug]
        self.project = project
        
class WorkEffort(object):
    def __init__(self,initDate=None,endDate=None,workDate=date.today(),totalTime=None,workItem=None,developer=None):
        self.initDate=initDate
        self.endDate=endDate
        self.workDate=workDate
        self.totalTime=totalTime
        self.workItem=workItem
        self.developer=developer