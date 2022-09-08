from matplotlib import pyplot as plt
import numpy as np
from .model_lib import predict_model
import tensorflow as tf


class Image:

    def __init__(self, name, image_or_path):
        self.image = None
        self.name = name
        self.get_image(image_or_path)
        self.mirrored = False

    def get_image(self, image_or_path):
        if isinstance(image_or_path, str):
            self.get_image_from_path(image_or_path)

        else:
            self.image = image_or_path

    def img_reshape(self, x0, x1, y0, y1):
        self.image = self.image[
                     round(self.image.shape[0] * x0):round(self.image.shape[0] * x1),
                     round(self.image.shape[1] * y0):round(self.image.shape[1] * y1)]

    def get_image_from_path(self, path):
        img = tf.keras.preprocessing.image.load_img(path)
        self.image = tf.keras.preprocessing.image.img_to_array(img)

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
