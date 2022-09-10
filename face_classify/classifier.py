from .face_class import Face


def classifier(image_or_path='../data/test/open_test/closed5.jpg', name='face1', show=True, crop_face=False,
               thresholds=(0.25, 0.999, 0.4, 0.01)):

    face = Face(image_or_path=image_or_path,
                name=name,
                crop_face=crop_face,
                thresholds=thresholds)

    if show:
        face.show()

    return face.classification
