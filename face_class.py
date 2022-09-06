from image_class import Image
from eye_class import Eye
import model_lib


class Face(Image):
    model_sunglasses = model_lib.load_model('model_sunglasses')
    model_blurry = model_lib.load_model('model_blurry')
    model_profile = model_lib.load_model('model_profile')

    def __init__(self, name, image_or_path=None, eyes=2):
        super().__init__(name, image_or_path)
        self.sunglasses = None
        self.profile = None
        self.blurry = None
        self.eye = None
        self.predictions()

    def get_eyes(self, eyes):
        if eyes == 1:
            print('Not implemented yet')

        if eyes == 2:
            eye1 = Eye(self.name, self.crop_eye())
            eye2 = Eye(self.name, self.crop_eye(side='left'), 'left')

            self.eye = (eye1, eye2)

    def open_eyes(self):
        if self.eye is not None:
            return self.eye[0].open, self.eye[1].open

    def crop_eye(self, side='right', amplitude=0.45, height=0.1, wide=0.1):
        if side == 'right':
            image_eye = self.image[
                        round(self.image.shape[0] * height):round(self.image.shape[0] * (height + amplitude)),
                        round(self.image.shape[1] * wide):round(self.image.shape[1] * (amplitude + wide))]
        else:
            image_eye = self.image[
                        round(self.image.shape[0] * height):round(self.image.shape[0] * (height + amplitude)),
                        round(self.image.shape[1] * (1 - (amplitude + wide))):round(self.image.shape[1] * (1 - wide))]
        return image_eye

    def predict_blurry(self):
        self.blurry = round(1 - self.predict(self.model_blurry), 3)  # not blurry 0 - blurry 1

    def predict_profile(self):
        self.profile = self.predict(self.model_profile)  # not profile 0 - profile 1

    def predict_sunglasses(self):
        self.sunglasses = round(1 - self.predict(self.model_sunglasses), 3)  # not sunglasses 0 - sunglasses 1

    def show_predictions(self, threshold=0.5):
        if self.blurry > threshold:
            print('Blurry image')
        elif self.profile > threshold:
            print('Profile image')
        elif self.sunglasses > threshold:
            print('Sunglasses image')
        else:
            if self.eye[0].open > threshold and self.eye[1].open > threshold:
                print('Open eyes:')
            elif self.eye[0].open < threshold and self.eye[1].open < threshold:
                print('Closed eyes:')
            else:
                print('Unknown:')

    def predictions(self, threshold=0.5):
        self.predict_blurry()
        if self.blurry < threshold:
            self.predict_profile()
            if self.profile < threshold:
                self.predict_sunglasses()
                if self.sunglasses < threshold:
                    self.get_eyes(eyes=2)
                    self.open_eyes()
