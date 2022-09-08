from .image_class import Image
from .model_lib import load_model


class Eye(Image):
    model = load_model('model_eye_right')

    def __init__(self, name_face, image, side='right'):
        self.open = None
        self.name_face = name_face
        self.side = side
        super().__init__(name_face + '_' + side + '_eye', image)
        self.crop_eye()
        self.predict_open()

    def crop_eye(self, amplitude=0.45, height=0.1, wide=0.1):
        if self.side == 'right':
            self.img_reshape(height, height+amplitude,
                             wide, wide+amplitude)
        elif self.side == 'left':
            self.img_reshape(height, height+amplitude,
                             1-amplitude+wide, 1-wide)
        else:
            self.img_reshape(height, height+amplitude,
                             2*wide, 1-2*wide)

    def predict_open(self):
        if self.side == 'left':
            self.mirror()
        self.open = self.predict(self.model)  # closed 0 - open 1

