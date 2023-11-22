import csv
import os

from repo.database_operations import DataBaseOperations


class FileDataBaseOperations(DataBaseOperations):
    def __init__(self, name):
        self.name = name
        self.path = "data/databases/"

    def insert_entities(self, id_field: str, entities: list):
        _, _, found_data = self._compare_with_db(
            "create", id_field, entities)
        entity = entities[0]
        class_name = entity.__class__.__name__
        header = list(entity.__dict__.keys())
        values = [list(e.__dict__.values()) for e in entities]

        if found_data:
            raise ValueError(
                f"Error when create {class_name} from database: cannot create " +
                f"entities with {id_field}: {found_data}, it already exists")

        try:
            self._write(self._get_file_name(type(entity)), header, values)
        except Exception as e:
            raise type(e)(
                f"Error when write {class_name} to database: {e}")
        return entities

    def get_entities(self, classs):
        ds = self._read(self._get_file_name(classs))
        return [classs(*d.values()) for d in ds]

    def update_entities(self, id_field: str, entities: list):
        new_data = self._compare_with_db_delete_update(
            "update", id_field, entities)
        entity = entities[0]

        try:
            self._write(self._get_file_name(
                type(entity)), list(entity.__dict__.keys()),
                new_data+[list(e.__dict__.values()) for e in entities], "w")
        except Exception as e:
            raise type(e)(
                f"Error when update {entity.__class__.__name__} to database: {e}")
        return entities

    def delete_entities(self, id_field: str, entities: list):
        new_data = self._compare_with_db_delete_update(
            "delete", id_field, entities)
        entity = entities[0]
        try:
            self._write(self._get_file_name(
                type(entity)), list(entity.__dict__.keys()), new_data, "w")
        except Exception as e:
            raise type(e)(
                f"Error when delete {entity.__class__.__name__} to database: {e}")
        return entities

    def clear(self, classs):
        try:
            os.remove(self._get_file_name(classs))
        except FileNotFoundError:
            pass

    def _compare_with_db(self, op, id_field, entities):
        if entities:
            entity = entities[0]
            class_name = entity.__class__.__name__

            ids_to_delete = [e.__dict__.get(id_field, None) for e in entities]

            ds = self._read(self._get_file_name(entity.__class__))
            new_data = []
            found_data = []
            for d in ds:
                if d.get(id_field, None) not in ids_to_delete:
                    new_data.append(list(d.values()))
                else:
                    found_data.append(d.get(id_field, None))
            return new_data, ids_to_delete, found_data
        raise ValueError(
            f"Error when {op} {class_name} from database: empty values")

    def _compare_with_db_delete_update(self, op, id_field, entities):
        new_data, ids_to_delete, found_data = self._compare_with_db(
            op, id_field, entities)
        if set(ids_to_delete)-set(found_data):
            raise ValueError(
                f"Error when {op} {entities[0].__class__.__name__} from database: " +
                f"cannot {op} entities with {id_field}: " +
                f"{set(ids_to_delete)-set(found_data)}, because not found")
        return new_data

    def _get_file_name(self, classs):
        class_name = classs.__name__
        return f"{self.path}{class_name.lower()}.csv"

    def _read(self, file_name):
        rows = []
        try:
            with open(file_name, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                rows = [row for row in reader]
                csvfile.close()
                return rows
        except FileNotFoundError:
            return []

    def _write(self, file_name, header, values_list, mode='a+'):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        is_empty = self._is_empty(file_name)
        with open(file_name, mode, newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            if is_empty is None or is_empty or ("w" in mode and values_list):
                csv_writer.writerow(header)
            for values in values_list:
                csv_writer.writerow(values)
            csvfile.close()

    @staticmethod
    def _is_empty(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                is_empty = len(list(reader)) <= 0
                csvfile.close()
        except FileNotFoundError:
            is_empty = True
        return is_empty
