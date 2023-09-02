import numpy as np
import os
import glob
import cv2
import matplotlib.pyplot as plt

import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))
swapper = insightface.model_zoo.get_model('inswapper_128.onnx', dowwnload=False, download_zip=False)

# load image
# model = cv2.imread('models/m.jpg')

models_path = [path for path in os.scandir('./models') if path.is_file()]
images_path = [path for path in os.scandir('./images') if path.is_file()]
paths = [(image, model) for image in images_path for model in models_path]
for (image_path, model_path) in paths:
    # check if result already exist
    [model_name, ext] = model_path.name.split(".")
    [image_name, ext] = image_path.name.split(".")
    path = f'./results/{image_name}__{model_name}.{ext}'
    if os.path.exists(path): continue

    print(f'Starting: {path}')

    # load model and detect face
    model = cv2.imread(model_path.path)
    model_face = app.get(model)[0]

    # load image and detect face
    image = cv2.imread(image_path.path)
    image_face = app.get(image)[0]
    image = image.copy()
    
    # swap faces
    res = swapper.get(image, image_face, model_face, paste_back=True)

    # save results
    cv2.imwrite(path, res)