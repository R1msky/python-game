from esc.entity import Entity


class EntityManager:
    def __init__(self):
        self.entities = list()
        self.last_entity_id = 1

    def create_entity(self, tag):
        self.last_entity_id += 1
        entity = Entity(tag, self.last_entity_id)
        self.entities.append(entity)
        return entity

    def delete_entity(self):
        pass

    def remove_entities(self):
        self.entities.clear()

    def find_first_by_tag(self):
        pass

    def get_entities(self):
        return self.entities
