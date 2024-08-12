#  classification 다루기 api서버
# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

from fastapi import FastAPI, File, UploadFile

# STEP 2: Create an ImageClassifier object. ==> 추론기를 먼저 만들어 놓고 서버 띄우기
base_options = python.BaseOptions(
    # efficientnet_lite0, efficientnet_lite2
    model_asset_path="C:/open_cv_models/efficientnet_lite2.tflite"  # opencv model은 한글 경로 인식 못함, 따라서 모델 경로 변경
)
options = vision.ImageClassifierOptions(base_options=base_options, max_results=4)
classifier = vision.ImageClassifier.create_from_options(options)

app = FastAPI()  # 추론기는 서버 꺼질 때까지 재활용할 수 있음

from PIL import Image
import io
import numpy as np


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()
    # STEP 3: Load the input image.
    pil_img = Image.open(io.BytesIO(contents))
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))
    # STEP 4: Classify the input image.
    classification_result = classifier.classify(image)
    # STEP 5: Process the classification result. In this case, visualize it.
    top_category = classification_result.classifications[0].categories[0]
    result = f"{top_category.category_name} ({top_category.score:.2f})"
    return {"result": result}
