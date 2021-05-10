class SceneManager:
    def __init__(self, context):
        self.scenes = None
        self.current_scene = ''
        self.context = context

    def render(self):
        pass

    def close(self):
        self.current_scene.exit()

    def put(self, name, scene):
        self.scenes.update({name: scene})
