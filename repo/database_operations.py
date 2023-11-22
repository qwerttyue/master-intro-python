from abc import ABC, abstractmethod


class DataBaseOperations(ABC):

    @abstractmethod
    def insert_entities(self, id_field: str, entities: list):
        """
        Insert entities to database. 
        params:
            id_field: pk field name
            entities: entities to insert
        """

    @abstractmethod
    def get_entities(self, classs):
        """
        Get entities from database. 
        params:
            classs: class of entities to retrive from database
        """

    @abstractmethod
    def update_entities(self, id_field: str, entities: list):
        """
        Update entities of database. 
        params:
            id_field: pk field name
            entities: entities to update
        """

    @abstractmethod
    def delete_entities(self, id_field: str, entities: list):
        """
        Delete entities from database. 
        params:
            id_field: pk field name
            entities: entities to delete
        """
