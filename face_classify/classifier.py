from .face_class import Face


def classifier(name='face1', image_or_path='../data/test/open_test/closed5.jpg', show=True, crop_face=False):
    face = Face(name, image_or_path=image_or_path, crop_face=crop_face)

    if show:
        face.show_predictions()
        face.show()

    classification = {'name': name,
                      'blurry': face.blurry,
                      'profile': face.profile,
                      'sunglasses': face.sunglasses,
                      'eyes': face.open_eyes()}

    return classification
