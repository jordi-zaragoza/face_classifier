import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from face_classify import Image, Face
import cv2


class GroupPicture(Image):

    def __init__(self, image_or_path, name='group_pic'):
        super().__init__(image_or_path, name)
        self.results = None
        self.faces = []
        self.detect_faces()
        self.retrieve_faces()
        self.calculate_results()

    def retrieve_faces(self):
        for face_location in self.face_locations:
            self.faces.append(Face(self.crop_from_coordinates(*face_location)))

    def square_faces(self):
        img_copy = self.image.copy()
        for num, face_location in enumerate(self.face_locations):
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            cv2.rectangle(img_copy,
                          (left, top),
                          (right,
                           bottom), (0, 255, 0), 2)

            cv2.putText(img_copy, 'face_'+str(num), (left, top-5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.75, (0, 255, 0), 2, cv2.LINE_AA)

            plt.imshow(img_copy.astype(np.uint8))

    def calculate_results(self):
        dc = {}
        for num, face in enumerate(self.faces):
            new_element = {
                num: face.classification
            }
            dc = dc | new_element

        self.results = pd.DataFrame(dc).transpose()