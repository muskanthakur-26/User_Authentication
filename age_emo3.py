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
SOURCE_DIR='img'

with open('img1.jpg', 'rb') as f:
    img_file = f.read()

response_detection = face_client.face.detect_with_stream(
    image=img_file,
    detection_model='detection_01',
    recognition_model='recognition_04',
    return_face_attributes=['age', 'emotion'],
)
img = Image.open(img_file)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(r'M:\webd\Azure_project\OpenSans-Bold.ttf', 25)
for face in response_detection:
    age = face.face_attributes.age
    emotion = face.face_attributes.emotion
    neutral = '{0:.0f}%'.format(emotion.neutral * 100)
    happiness = '{0:.0f}%'.format(emotion.happiness * 100)
    anger = '{0:.0f}%'.format(emotion.anger * 100)
    sandness = '{0:.0f}%'.format(emotion.sadness * 100)

    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    draw.text((left - 4, bottom), 'Age: ' + str(int(age)), fill=	(255,0,0),font=font)
    draw.text((left - 4, bottom+35), 'Neutral: ' + neutral, fill=	(255,0,0),  font=font)
    draw.text((left - 4, bottom+70), 'Happy: ' + happiness, fill=	(255,0,0),font=font)
    draw.text((left - 4, bottom+105), 'Sad: ' + sandness, fill=	(255,0,0),font=font)
    draw.text((left - 4, bottom+140), 'Angry: ' + anger, fill=	(255,0,0),font=font)

img.show()