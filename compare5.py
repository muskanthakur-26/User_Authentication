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


response_detected_faces = face_client.face.detect_with_stream(
    image=open(r'.\images\chk2.jpg', 'rb'),
    detection_model='detection_03',
    recognition_model='recognition_04',  
)
face_ids = [face.face_id for face in response_detected_faces]

img_source = open(r'.\images\chk1.jpg', 'rb')
response_face_source = face_client.face.detect_with_stream(
    image=img_source,
    detection_model='detection_03',
    recognition_model='recognition_04'    
)
face_id_source = response_face_source[0].face_id

matched_faces = face_client.face.find_similar(
    face_id=face_id_source,
    face_ids=face_ids
)



face_verified = face_client.face.verify_face_to_face(
    face_id1=matched_faces[0].face_id,
    face_id2='f6467d16-ac28-4365-856c-8e16b844d874'
)
print(face_verified.is_identical)