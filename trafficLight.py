import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop

# the following code is commented because it needs to be run only once when training the model

# img = image.load_img("D:/TrafficLightDetection/basedata/training/TrafficLight/1.PNG")
#
# print(cv2.imread("D:/TrafficLightDetection/basedata/training/TrafficLight/1.PNG").shape)
#
# training = ImageDataGenerator(rescale=1 / 255)
# validation = ImageDataGenerator(rescale=1 / 255)
#
# training_dataset = training.flow_from_directory("D:/TrafficLightDetection/basedata/training/", target_size=(200, 200),
#                                                 batch_size=3, class_mode='binary')
# validation_dataset = validation.flow_from_directory("D:/TrafficLightDetection/basedata/validation/",
#                                                     target_size=(200, 200), batch_size=3, class_mode='binary')
#
# print(training_dataset.class_indices)
#
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
#     tf.keras.layers.MaxPool2D(2, 2),
#
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPool2D(2, 2),
#
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPool2D(2, 2),
#
#     tf.keras.layers.Flatten(),
#
#     tf.keras.layers.Dense(512, activation='relu'),
#
#     tf.keras.layers.Dense(1, activation='sigmoid')
# ])
#
# model.compile(loss='binary_crossentropy', optimizer=RMSprop(learning_rate=0.001), metrics=['accuracy'])
#
# model_fit = model.fit(training_dataset, steps_per_epoch=3, epochs=30, validation_data=validation_dataset)
# model.save('traffic_light_model.h5')

model = tf.keras.models.load_model('/Users/yusrazainab/Downloads/traffic_light_model.h5')

dir_path = "/Users/yusrazainab/Desktop/traffic lights"
for i in os.listdir(dir_path):
    full_path = os.path.join(dir_path, i)
    if os.path.isfile(full_path):
        img = image.load_img(full_path, target_size=(200, 200))
        plt.show()
        plt.imshow(img)

        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        images = np.vstack([X])
        val = model.predict(images)
        if val == 0:
            print("ntl")
        else:
            print("tl")
    else:
        print(f"Skipping {full_path}, not a file.")