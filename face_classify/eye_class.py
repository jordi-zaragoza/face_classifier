import numpy as np

from .image_class import Image
from .model_lib import load_model
import cv2


class Eye(Image):
    model = load_model('model_eye')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    def __init__(self, image, name_face, side='right'):
        self.open = None
        self.name_face = name_face
        self.side = side
        super().__init__(image, name_face + '_' + side + '_eye')
        self.crop_eye(use_detector=True)
        self.predict_open()

    def crop_eye(self, amplitude=0.45, height=0.1, wide=0, use_detector=True):
        params = {
            'right': (height, height+amplitude, wide, wide+amplitude),
            'left': (height, height+amplitude, 1-amplitude-wide, 1-wide)
        }.get(self.side, (height, height+amplitude, 2*wide, 1-2*wide))
        self.img_reshape(*params)
        if use_detector:
            self.detect_eye()

    def detect_eye(self):
        img = np.array(self.image, dtype='uint8')
        eyes = self.eye_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4)
        if len(eyes) > 0:
            if len(eyes) == 1:
                x, y, w, h = eyes[0]
                self.image = self.crop_from_coordinates(y, x+h, y+w, x)

            if len(eyes) > 1:
                max_size = 0
                x_f, y_f, w_f, h_f = eyes[0]
                for x, y, w, h in eyes:
                    size = w * h
                    if size > max_size:
                        x_f, y_f, w_f, h_f = x, y, w, h

                self.image = self.crop_from_coordinates(y_f, x_f + h_f, y_f + w_f, x_f)
            #     print(self.name, 'more than one eye detected')

        # else:
        #     print(self.name, 'no eye detected')

    def predict_open(self):
        if self.side == 'left':
            self.mirror()
        self.open = self.predict(self.model)  # closed 0 - open 1

