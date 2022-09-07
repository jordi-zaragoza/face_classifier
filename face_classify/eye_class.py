from .image_class import Image
from .model_lib import load_model


class Eye(Image):
    model = load_model('model_eye_right')

    def __init__(self, name_face, image, side='right'):
        self.open = None
        self.name_face = name_face
        self.side = side
        super().__init__(name_face + '_' + side + '_eye', image)
        self.predict_open()

    def predict_open(self):
        if self.side == 'left':
            self.mirror()
        self.open = self.predict(self.model)  # closed 0 - open 1
