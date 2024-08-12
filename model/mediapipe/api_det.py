# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from fastapi import FastAPI, File, UploadFile

# 서버가 뜨기전에 추론기 띄우기
# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(
    model_asset_path="C:/open_cv_models/efficientdet_lite0.tflite"
)
options = vision.ObjectDetectorOptions(
    base_options=base_options, score_threshold=0.5
)  # 박스 0.5 이상인 것만 쓰겠다.
detector = vision.ObjectDetector.create_from_options(options)

# 다른 곳에서 무언가 통신할 수 있는 서버를 만든 것 (PYTHON으로 서버 만들기)
app = FastAPI()

from PIL import Image
import io
import numpy as np
from collections import defaultdict


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    contents = await file.read()  # content미리 읽기 (서버가 받아서 이미지를 읽은 상태)
    #  STEP 3: Load the input image.
    pil_img = Image.open(io.BytesIO(contents))
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=np.asarray(pil_img))

    # STEP 4: Detect objects in the input image.
    detection_result = detector.detect(image)  # 추론

    # STEP 5:
    # 찾은 객체의 종류별 개수 출력하는 코드
    detections = detection_result.detections
    class_names = defaultdict(int)
    for i, detection in enumerate(detections):
        # detection 객체에서 객체의 클래스 이름과 신뢰도를 가져옵니다.
        class_name = detection.categories[0].category_name
        confidence_score = detection.categories[0].score
        class_names[class_name] += 1
    return {"result": class_names}
