from .image_class import Image
from .model_lib import load_model


class Eye(Image):
    model = load_model('model_eye_right')

    def __init__(self, image, name_face, side='right'):
        self.open = None
        self.name_face = name_face
        self.side = side
        super().__init__(image, name_face + '_' + side + '_eye')
        self.crop_eye()
        self.predict_open()

    def crop_eye(self, amplitude=0.45, height=0.1, wide=0.1):
        params = {
            'right': (height, height+amplitude, wide, wide+amplitude),
            'left': (height, height+amplitude, 1-amplitude-wide, 1-wide)
        }.get(self.side, (height, height+amplitude, 2*wide, 1-2*wide))
        self.img_reshape(*params)

    def predict_open(self):
        if self.side == 'left':
            self.mirror()
        self.open = self.predict(self.model)  # closed 0 - open 1

