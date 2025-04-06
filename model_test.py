import os
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

# Load the model
model = tf.keras.models.load_model('models/teeth_periodontitis_classifier_Resnet50.h5')

# Prediction on new images
dir_path = "D:/Periodontitis - basedata/lol"
for i in os.listdir(dir_path):
    full_path = os.path.join(dir_path, i)
    if os.path.isfile(full_path):
        img = image.load_img(full_path, target_size=(224, 224))

        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        X /= 255.0

        val = model.predict(X)
        if val < 0.5:
            print(f"Prediction: {val[0][0]}")
            print("Healthy Gums")
        else:
            print(f"Prediction: {val[0][0]}")
            print("Unhealthy Gums")
    else:
        print(f"Skipping {full_path}, not a file.")
