class Entity:
    def __init__(self, tag, id_):
        self.components = dict()
        self.tag = tag
        self.id = id_

    def set_tag(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag

    def set_id(self, id_):
        self.id = id_

    def get_id(self):
        return self.id

    def get(self, component_name):
        return self.components.get(component_name)

    def add(self, component_name, component):
        self.components.update({component_name: component})

    def contains(self, component_name):
        return self.components.get(component_name) is not None

    def delete(self):
        pass
