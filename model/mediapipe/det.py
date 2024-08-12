# Object detection
# 80개 객체 탐지 가능 ==> 일반적으로 80개 짜리임 coco dataset가지고 찾을 수 있는 dataset
# SSD MobileNetV2 model ==> SSD 붙으면 무조건 벡본

# visualize 하는 코드 (그림그려주는 코드)
import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red


def visualize(image, detection_result) -> np.ndarray:
    """Draws bounding boxes on the input image and return it.
    Args:
      image: The input RGB image.
      detection_result: The list of all "Detection" entities to be visualize.
    Returns:
      Image with bounding boxes.
    """
    for detection in detection_result.detections:
        # Draw bounding_box
        bbox = detection.bounding_box
        start_point = bbox.origin_x, bbox.origin_y
        end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
        cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

        # Draw label and score
        category = detection.categories[0]
        category_name = category.category_name
        probability = round(category.score, 2)
        result_text = category_name + " (" + str(probability) + ")"
        text_location = (MARGIN + bbox.origin_x, MARGIN + ROW_SIZE + bbox.origin_y)
        cv2.putText(
            image,
            result_text,
            text_location,
            cv2.FONT_HERSHEY_PLAIN,
            FONT_SIZE,
            TEXT_COLOR,
            FONT_THICKNESS,
        )

    return image


# 이미지 확인
import cv2

img = cv2.imread("images/cat_and_dog.jpg")
# cv2.imshow("test", img)
# cv2.waitKey(0)

# STEP 1: Import the necessary modules.
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# STEP 2: Create an ObjectDetector object.
base_options = python.BaseOptions(
    model_asset_path="C:/open_cv_models/efficientdet_lite0.tflite"
)
options = vision.ObjectDetectorOptions(
    base_options=base_options, score_threshold=0.5
)  # 박스 0.5 이상인 것만 쓰겠다.
detector = vision.ObjectDetector.create_from_options(options)

# STEP 3: Load the input image.
image = mp.Image.create_from_file("images/cat_and_dog.jpg")

# STEP 4: Detect objects in the input image.
detection_result = detector.detect(image)  # 추론

# ==> 추론 결과를 가지고 사용자에게 무엇을 보여줄꺼냐
# STEP 5: Process the detection result. In this case, visualize it.
image_copy = np.copy(image.numpy_view())
annotated_image = visualize(image_copy, detection_result)

# rgb_annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
# cv2.imshow("test", rgb_annotated_image)
# cv2.waitKey(0)

# 찾은 객체의 종류별 개수 출력하는 코드
from collections import defaultdict

print("detection_result: ", detection_result)
detections = detection_result.detections
class_names = defaultdict(int)

for i, detection in enumerate(detections):
    # detection 객체에서 객체의 클래스 이름과 신뢰도를 가져옵니다.
    class_name = detection.categories[0].category_name
    confidence_score = detection.categories[0].score
    class_names[class_name] += 1
print(class_names)
