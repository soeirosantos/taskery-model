# -*- coding: utf-8 -*-

from springpython.database.core import DaoSupport, SimpleRowMapper


class BaseRepository():
    def __init__(self, daoWrapper):
        self.daoWrapper = daoWrapper

    def query(self, sql,args=None, entity=None):
        return self.daoWrapper.query(sql, args, entity)
    
    def insert(self, sql, args=None):
        return self.daoWrapper.insert(sql, args);

    def update(self, sql, args=None):
        return self.daoWrapper.update(sql, args);

    def execute(self, sql, args=None):
        return self.daoWrapper.execute(sql, args);

class DaoWrapper():
    """ 
        This wrapper is a contract used for maintain domain model Repositories decoupled from infrastructure necessary to access database 
    """    
    def query(self, sql, entity, args=None):
        """
           Inform sql query and entity to be mapped
           The mapping will be done by convention using
           the columns names or alias returned from 
           query and entity name attrs
        """
        raise NotImplementedError()
    
    def insert(self, sql, args=None):
        """
           Expected simple sql insert statement and its params
           Must return the id of row inserted 
        """
        raise NotImplementedError()
    
    def update(self, sql, args=None):
        """
           Expected simple sql update statement and its params
           Must return the number of rows updates 
        """
        raise NotImplementedError()
    
    def execute(self, sql, args=None):
        """
           Execute any statement
           Must return the number of rows affected 
        """
        raise NotImplementedError()

class SpringDaoWrapper(DaoSupport, DaoWrapper):
    """
        DaoWrapper implementation for Spring Data Access DatabaseTemplate
    """    
    
    def query(self, sql, args=None, entity=None):
        return self.database_template.query(sql, args, rowhandler=SimpleRowMapper(entity))
    
    def insert(self, sql, args=None):
        return self.database_template.insert_and_return_id(sql, args);

    def update(self, sql, args=None):
        return self.database_template.update(sql, args);

    def execute(self, sql, args=None):
        return self.database_template.execute(sql, args);