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

image_url='https://images.hindustantimes.com/img/2021/10/13/550x309/india-new-jersey_1634114268092_1634114275156.jpg'
image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_03',
    recognition_model='recognition_04'

)

print(response_detected_faces)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='red', width=5)
img.show()