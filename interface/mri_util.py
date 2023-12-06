from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import os


app = FastAPI()


endpoint = "https://diagnosticreportprediction-mv6hb5oqca-ew.a.run.app/"
# MODEL = tf.keras.models.load_model('/Users/yashshrivastava/code/YashS16/final_project/app/model/model3.h5')
MODEL = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__),"..", "model", "model3.h5"))
CLASS_NAMES = ["glioma_tumor", "meningioma_tumor", "no_tumor", "pituitary_tumor"]

@app.get('/')
def ping():

    return {"ok": True}
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).resize((331, 331)))/255
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
    ):
     image = read_file_as_image(await file.read())
     img_batch = np.expand_dims(image, 0)
     prediction = MODEL.predict(img_batch)
     prediction_class = CLASS_NAMES[np.argmax(prediction[0])]
     confidence = np.max(prediction[0])
     return {
         'Class': prediction_class,
        'Confidence': float(confidence)
    }
