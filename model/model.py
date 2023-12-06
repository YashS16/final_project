
from colorama import Fore, Style
import numpy as np
import tensorflow as tf
from tensorflow.keras import models, layers

IMAGE_SIZE = 244
BATCH_SIZE = 32
INPUT_SHAPE = (BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, 3)

def fetch_data():
    X = tf.keras.preprocessing.image_dataset_from_directory(
    "/content/drive/MyDrive/raw_data/COVID Chest X-Ray/train_data",
    shuffle=True,
    image_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE)

    return X

def get_dataset_partitions(data, train_split=0.7):
    data_size = len(data)

    train_size = int(train_split * data_size)
    #val_size = int(val_split * data_size)

    X_train = data.take(train_size)
    X_val = data.skip(train_size)

    return X_train, X_val

def initialize_model(input_shape: tuple):
    """
    Initialize the Neural Network with random weights
    """
    rescale = tf.keras.Sequential(layers.experimental.preprocessing.Rescaling(1.0/255))

    augmentation = tf.keras.Sequential([
    layers.experimental.preprocessing.RandomFlip('horizontal_and_vertical'),
    layers.experimental.preprocessing.RandomRotation(0.2)])


    model = models.Sequential([
    rescale,
    augmentation,
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(BATCH_SIZE, IMAGE_SIZE, IMAGE_SIZE, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(2, activation='softmax')])

    model.build(input_shape=input_shape)

    print("✅ Model initialized")

    return model


def compile_model(model):
    """
    Compile the Neural Network
    """
    model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer='adam',
    metrics=['accuracy']
)

    print("✅ Model compiled")

    return model

def train_model(
        model,
        X_train,
        batch_size,
        X_val
    ):
    """
    Fit the model and return a tuple (fitted_model, history)
    """
    print(Fore.BLUE + "\nTraining model..." + Style.RESET_ALL)

    history = model.fit(
    X_train,
    epochs=40,
    batch_size=batch_size,
    validation_data=X_val,
    verbose=1,
)

    print(f"✅ Model trained on {len(X_train)} rows with min val MAE: {round(np.min(history.history['val_mae']), 2)}")

    return model, history

def evaluate_model(
        model,
        X_test,
        batch_size=32
    ):
    """
    Evaluate trained model performance on the dataset
    """

    print(Fore.BLUE + f"\nEvaluating model on {len(X_test)} rows..." + Style.RESET_ALL)

    if model is None:
        print(f"\n❌ No model to evaluate")
        return None

    metrics = model.evaluate(
        X_test,

        batch_size=batch_size,
        verbose=1,
        return_dict=True
    )

    loss = metrics["loss"]
    accuracy = metrics["accuracy"]

    print(f"✅ Model evaluated, ACCURACY: {round(accuracy, 2)}")

    return metrics

# model.save(f"../app/{model}")
