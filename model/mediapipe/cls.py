## classification 다루기
import cv2  # 이미지에서 쓰는 것 opencv

# from google.colab.patches import cv2_imshow # 사진 보여주는 utility
import math

IMAGE_FILENAMES = ["images/burger.jpg", "images/cat.jpg"]  # 받은 파일 이름

# 이미지가 있는지 체크하는 코드(하나씩 보여주는 코드)
DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480


# def resize_and_show(image):
#     h, w = image.shape[:2]
#     if h < w:
#         img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h / (w / DESIRED_WIDTH))))
#     else:
#         img = cv2.resize(image, (math.floor(w / (h / DESIRED_HEIGHT)), DESIRED_HEIGHT))
#     # cv2_imshow(img)
#     cv2.imshow("test", img)  # 화면 띄우기
#     cv2.waitKey(0)  # 화면 멈추기


# # Preview the images.

# images = {name: cv2.imread(name) for name in IMAGE_FILENAMES}
# for name, image in images.items():
#     print(name)
#     resize_and_show(image)

# STEP 1: Import the necessary modules.
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python.components import processors
from mediapipe.tasks.python import vision

# STEP 2: Create an ImageClassifier object.
base_options = python.BaseOptions(
    # efficientnet_lite0, efficientnet_lite2
    model_asset_path="C:/open_cv_models/efficientnet_lite2.tflite"  # opencv model은 한글 경로 인식 못함, 따라서 모델 경로 변경
)
options = vision.ImageClassifierOptions(base_options=base_options, max_results=4)
classifier = vision.ImageClassifier.create_from_options(options)
# STEP 3: Load the input image.
image = mp.Image.create_from_file("images/burger.jpg")
"""
light0: 0.98 / light02: 0.72
==> 더 작은 모델에서 더 높은 값이 나옴 (데이터에 잘 맞는 모델 찾기)
"""
# STEP 4: Classify the input image.
classification_result = classifier.classify(image)
# print(classification_result)
# STEP 5: Process the classification result. In this case, visualize it.
top_category = classification_result.classifications[0].categories[0]
print(f"{top_category.category_name} ({top_category.score:.2f})")

# display_batch_of_images(images, predictions)
