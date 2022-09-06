from matplotlib import pyplot as plt
import numpy as np
import model_lib
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

    def get_image_from_path(self, path):
        img = tf.keras.preprocessing.image.load_img(path)
        self.image = tf.keras.preprocessing.image.img_to_array(img)

    def mirror(self):
        self.image = tf.image.flip_left_right(self.image)
        self.mirrored = not self.mirrored
        self.name = self.name + '_mirror' if self.mirrored else self.name.split('_mirror')[0]

    def show(self):
        plt.title(self.name)
        plt.imshow(self.image.astype(np.uint8))

    def predict(self, model, round_val=3):
        return round(model_lib.predict_model(self.image, model), round_val)
