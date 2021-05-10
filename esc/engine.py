from esc.entity_manager import EntityManager


class Engine:
    entity_manager = EntityManager()

    def get_entity_manager(self):
        return self.entity_manager
