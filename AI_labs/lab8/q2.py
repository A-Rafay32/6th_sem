import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import adam_v2

# Assuming you have a dataset directory with 'train' and 'test' folders and subfolders for each class
train_dir = r"C:\Users\Rafay\Documents\AI_Labs\lab8\train_dir"
test_dir = r"C:\Users\Rafay\Documents\AI_Labs\lab8\test_dir"

# Data augmentation and normalization
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary'  # Assuming binary classification (face vs. not face)
)

validation_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(64, 64),
    batch_size=32,
    class_mode='binary'
)

# Building the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')  # For binary classification
])

# Compiling the model
model.compile(optimizer= adam_v2.Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Training the model
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=20
)

# Save the model
model.save('face_recognition_model.h5')

# Example to predict on a new image
import numpy as np
from tensorflow.keras.preprocessing import image

def predict_face(img_path, model):
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        print("Face detected")
    else:
        print("Face not detected")

# Predict on a new image
predict_face(r'C:\Users\Rafay\Documents\AI_Labs\lab8\train_dir\download.jpeg', model)
