from .general_lib import *
from .group_picture_class import *


def sort_group_closed_eyes(path='./output'):
    image_list = os.listdir(path)
    image_list = filter_images(image_list)

    for image_name in image_list:
        path_image = path + '/' + image_name
        group_picture = GroupPicture(path_image, image_name)

        any_closed_eyes = any(group_picture.results.prediction.apply(lambda x: x == 'Closed eyes'))
        if any_closed_eyes:
            move_file(image_name, path, path + '/closed_eyes')


def classifier(image_or_path, crop_face=False, name='img'):
    face = Face(image_or_path=image_or_path, crop_face=crop_face, name=name)
    face.show()
    return face.classification
