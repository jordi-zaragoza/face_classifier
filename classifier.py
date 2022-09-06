from face_class import Face


def classifier(name='face1', path='../data/test/open_test/closed5.jpg', show=True):
    face = Face(name, image_or_path=path)

    if show:
        face.show_predictions()
        face.show()

    classification = {'name': name,
                      'blurry': face.blurry,
                      'profile': face.profile,
                      'sunglasses': face.sunglasses,
                      'eyes': face.open_eyes()}

    return classification
