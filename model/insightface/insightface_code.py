import argparse
import cv2
import sys
import numpy as np
import insightface_code
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

# assert insightface_code.__version__ >= "0.3"

# parser = argparse.ArgumentParser(description="insightface app test")
# # general
# # parser.add_argument("--ctx", default=0, type=int, help="ctx id, <0 means using cpu")
# parser.add_argument("--det-size", default=640, type=int, help="detection size")
# args = parser.parse_args()

# step2: 추론기
app = FaceAnalysis()
app.prepare(ctx_id=0, det_size=(640,640))

# step3: load input image
img1 = cv2.imread("images/iu3.jpg")
img2 = cv2.imread("images/iu5.jpg")
# img = ins_get_image("t1")

# step4: inference
faces1 = app.get(img1)
faces2 = app.get(img2)
# 얼굴이 하나하나 잘 출력이 되는지 확인하기
assert len(faces1) == 1
assert len(faces2) == 1
print(len(faces1), len(faces2))

# step5: face similarity
# rimg = app.draw_on(img, faces)
# # cv2.imshow("test", rimg)
# # cv2.waitKey(0)
# cv2.imwrite("images/t1_output.jpg", rimg)

# # then print all-to-all face similarity
# feats = []
# for face in faces:
feat1 = np.array(faces1[0].normed_embedding, dtype = np.float32)
feat2 = np.array(faces2[0].normed_embedding, dtype = np.float32)

# feats = np.array(feats, dtype=np.float32)
sims = np.dot(feat1, feat2.T)
print(sims)

# img 3,4 ==> 0.36092624
# img 3,5 ==> 0.72380626