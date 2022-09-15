from .image_class import Image
from .eye_class import Eye
from .model_lib import load_model


class Face(Image):
    model_sunglasses = load_model('model_sunglasses')
    model_blurry = load_model('model_blurry')
    model_profile = load_model('model_profile')

    def __init__(self, image_or_path=None, name='face', eyes_num=2, thresholds=(0.25, 0.999, 0.3, 0.1), crop_face=False):
        super().__init__(image_or_path, name)
        self.classification = None
        self.sunglasses = None
        self.profile = None
        self.blurry = None
        self.eyes = None
        self.thresholds = thresholds
        self.eyes_num = eyes_num
        if crop_face:
            self.crop_face()
        self.predictions()
        self.classifier()

    def get_eyes(self, eyes):
        if eyes == 1:
            eye1 = Eye(self.image, self.name, 'one')
            self.eyes = [eye1]

        elif eyes == 2:
            eye1 = Eye(self.image, self.name)
            eye2 = Eye(self.image, self.name, 'left')
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

    def get_prediction(self):
        if self.blurry > self.thresholds[0]:
            return 'Blurry image'
        elif self.profile > self.thresholds[1]:
            return 'Profile image'
        elif self.sunglasses > self.thresholds[2]:
            return 'Sunglasses image'
        else:
            if self.eyes[0].open > self.thresholds[3] and self.eyes[1].open > self.thresholds[3]:
                return 'Open eyes'
            elif self.eyes[0].open < self.thresholds[3] and self.eyes[1].open < self.thresholds[3]:
                return 'Closed eyes'
            else:
                return 'Unknown'

    def classifier(self):
        self.classification = {'name': self.name,
                               'blurry': self.blurry,
                               'profile': self.profile,
                               'sunglasses': self.sunglasses,
                               'eyes': self.open_eyes(),
                               'prediction': self.get_prediction()}

    def crop_face(self):
        self.detect_faces()
        if len(self.face_locations) == 1:
            self.image = self.crop_from_coordinates(*self.face_locations[0])
        elif len(self.face_locations) > 1:
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
