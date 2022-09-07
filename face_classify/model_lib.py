import numpy as np
import tensorflow as tf
import os

package_directory = os.path.dirname(os.path.abspath(__file__))


def load_model(model_name):
    json_file = open(package_directory + '/model/' + model_name + '.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights(package_directory + '/model/' + model_name + '_weights.h5')
    print('Loaded model: ', model_name)
    return loaded_model


def predict_model(img, model, image_size=(160, 160)):
    x = tf.image.resize(img, image_size)
    x = np.expand_dims(x, axis=0)
    predictions = model.predict_on_batch(x).flatten()
    predictions = tf.nn.sigmoid(predictions)
    return predictions.numpy()[0]