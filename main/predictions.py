import base64  # for handling base64 images
import os  # for performing os relatec work

import tensorflow as tf  # for deep learning


# function to malaria
def predict_malaria(base64image) -> bool:
    """
    A function to predict whether microscope image has malaria bacteria or not
    :param base64image: an image in base64 format
    :return: a bool value wether malaria is detected or not.
    """
    # load malaria model
    cwd = os.path.dirname(__file__)
    model = tf.keras.models.load_model(
        os.path.join(cwd, './trained_models/cnn_malaria.h5'))

    # get image path and open it using tf

    img_decode = tf.image.decode_image(
        base64.b64decode(base64image.split(';base64,').pop()))
    # resize image based on model arch
    image_to_predict = tf.image.resize(img_decode, size=[
        150, 150
    ]) / 255.0  # normalize img by dividing by 255.0

    # predict image
    return model.predict(tf.reshape(image_to_predict, shape=[-1, 150, 150, 3
                                                             ])) < 0


# function to predict pneumonia
def predict_pneumonia(base64image) -> bool:
    """
    A function to predict whether an x ray image is having pneumonia or not
    :param base64image:
    :return: bool value about whether pneumonia is detected or not
    """

    img_decode = tf.image.decode_image(
        base64.b64decode(base64image.split(';base64,').pop()))

    # resize image based on model arch
    image_to_predict = tf.image.resize(img_decode, size=[
        150, 150
    ]) / 255.0  # normalize img by dividing by 255.0

    cwd = os.path.dirname(__file__)
    model = tf.keras.models.load_model(
        os.path.join(cwd, './trained_models/cnn_pneumonia.h5'))

    return model.predict(
        tf.reshape(image_to_predict, shape=[-1, 150, 150, 1])) > 0.75