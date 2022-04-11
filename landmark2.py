import asyncio
import io
import glob
import os
import sys
import json
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition
# credential = json.load(open('AzureCloudKeys.json'))
# API_KEY = credential['API_KEY']

# ENDPOINT = credential['ENDPOINT']
# This key will serve all examples in this document.
KEY = "d2daa3f6d31f4c51b8bd22bfd3d263f9"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://azure-prac-api.cognitiveservices.azure.com/"
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

image_url='https://media.istockphoto.com/photos/happy-smiling-africanamerican-child-girl-yellow-background-picture-id1168369629?b=1&k=20&m=1168369629&s=170667a&w=0&h=jQ3olVQkcpV63-t86h351w89Cm_cFOZg2eKTxWO5q4s='
image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_03',
    recognition_model='recognition_04',
    return_face_landmarks=True
)
print(vars(response_detected_faces[0]))
print(vars(response_detected_faces[0].face_landmarks).keys())
print(response_detected_faces[0].face_landmarks.mouth_left)

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    # mark the noise tip
    x = face.face_landmarks.nose_tip.x
    y = face.face_landmarks.nose_tip.y
    draw.rectangle(((x, y), (x, y)), outline='white', width=7)

    # draw the bounding box around the mouth
    mouth_left = face.face_landmarks.mouth_left.x, face.face_landmarks.mouth_left.y
    mouth_right = face.face_landmarks.mouth_right.x, face.face_landmarks.mouth_right.y
    lip_bottom = face.face_landmarks.under_lip_bottom.x, face.face_landmarks.under_lip_bottom.y
    draw.rectangle((mouth_left, (mouth_right[0], lip_bottom[1])), outline='yellow', width=2)

img.show()