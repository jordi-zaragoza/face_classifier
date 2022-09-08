from .image_class import Image
from .eye_class import Eye
from .model_lib import load_model
import face_recognition


class Face(Image):
    model_sunglasses = load_model('model_sunglasses')
    model_blurry = load_model('model_blurry')
    model_profile = load_model('model_profile')

    def __init__(self, name, image_or_path=None, eyes_num=2, thresholds=(0.5, 0.5, 0.5, 0.5), crop_face=True):
        super().__init__(name, image_or_path)
        self.sunglasses = None
        self.profile = None
        self.blurry = None
        self.eyes = None
        self.thresholds = thresholds
        self.eyes_num = eyes_num
        if crop_face:
            self.crop_face()
        self.predictions()

    def get_eyes(self, eyes):
        if eyes == 1:
            eye1 = Eye(self.name, self.image, 'one')
            self.eyes = [eye1]

        elif eyes == 2:
            eye1 = Eye(self.name, self.image)
            eye2 = Eye(self.name, self.image, 'left')
            self.eyes = [eye1, eye2]

        else:
            print('please insert 1 or 2 eyes for this face')

    def open_eyes(self):
        if self.eyes is not None:
            return [eye.open for eye in self.eyes]

    def predict_blurry(self):
        self.blurry = round(1 - self.predict(self.model_blurry), 3)  # not blurry 0 - blurry 1

    def predict_profile(self):
        self.profile = self.predict(self.model_profile)  # not profile 0 - profile 1

    def predict_sunglasses(self):
        self.sunglasses = round(1 - self.predict(self.model_sunglasses), 3)  # not sunglasses 0 - sunglasses 1

    def show_predictions(self):
        if self.blurry > self.thresholds[0]:
            print('Blurry image')
        elif self.profile > self.thresholds[1]:
            print('Profile image')
        elif self.sunglasses > self.thresholds[2]:
            print('Sunglasses image')
        else:
            if self.eyes[0].open > self.thresholds[3] and self.eyes[1].open > self.thresholds[3]:
                print('Open eyes:')
            elif self.eyes[0].open < self.thresholds[3] and self.eyes[1].open < self.thresholds[3]:
                print('Closed eyes:')
            else:
                print('Unknown:')

    def crop_face(self):
        face_locations = face_recognition.face_locations(self.image.astype('uint8'))
        if len(face_locations) == 1:
            top, right, bottom, left = face_locations[0]
            self.image = self.image[top:bottom, left:right]
        elif len(face_locations) < 1:
            print('Cannot find any faces on the picture')
        else:
            print('More than 1 faces found')

    def predictions(self):
        self.predict_blurry()
        if self.blurry < self.thresholds[0]:
            self.predict_profile()
            if self.profile < self.thresholds[1]:
                self.predict_sunglasses()
                if self.sunglasses < self.thresholds[2]:
                    self.get_eyes(eyes=2)
                    self.open_eyes()
            else:
                # This should be another type of sunglasses and open eyes predictor
                # self.predict_sunglasses()
                self.get_eyes(eyes=1)
                # self.open_eyes()
