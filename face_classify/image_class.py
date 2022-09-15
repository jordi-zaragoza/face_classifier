import imageio
from matplotlib import pyplot as plt
import numpy as np

from .general_lib import create_folder
from .model_lib import predict_model
import tensorflow as tf
import face_recognition
import itertools

class Image:

    img_id = itertools.count()

    def __init__(self, image_or_path, name='image'):
        self.img_id = next(self.img_id)
        self.name = name + '_id_' + str(self.img_id)
        self.image = None
        self.get_image(image_or_path)
        self.mirrored = False
        self.face_locations = []

    def get_image(self, image_or_path):
        if isinstance(image_or_path, str):
            self.load_image(image_or_path)

        else:
            self.image = image_or_path

    def img_reshape(self, x0, x1, y0, y1):
        self.image = self.image[
                     round(self.image.shape[0] * x0):round(self.image.shape[0] * x1),
                     round(self.image.shape[1] * y0):round(self.image.shape[1] * y1)]

    def crop_from_coordinates(self, top, right, bottom, left):
        return self.image[top:bottom, left:right]

    def load_image(self, path):
        img = tf.keras.preprocessing.image.load_img(path)
        self.image = tf.keras.preprocessing.image.img_to_array(img)

    def save_image(self, path):
        create_folder(path)
        imageio.imwrite(path + '/' + self.name + '.jpg', self.image)

    def mirror(self):
        img = tf.image.flip_left_right(self.image)
        self.image = tf.keras.preprocessing.image.img_to_array(img)
        self.mirrored = not self.mirrored
        self.name = self.name + '_mirror' if self.mirrored else self.name.split('_mirror')[0]

    def show(self):
        plt.title(self.name)
        plt.imshow(self.image.astype(np.uint8))

    def predict(self, model, round_val=3):
        return round(predict_model(self.image, model), round_val)

    def detect_faces(self):
        face_locations = face_recognition.face_locations(self.image.astype('uint8'))
        if len(face_locations) > 0:
            for location in face_locations:
                self.face_locations.append(location)
        else:
            print('Cannot find any faces on the picture')

