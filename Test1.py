import os, io
from tkinter import filedialog, Tk
from google.cloud import vision
from google.cloud .vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

client = vision.ImageAnnotatorClient()

FileName = "Img.jpg"
FolderPath = r"C:\Users\gursi\Documents\seeWat\VisionAPISeeWat"

with io.open(os.path.join(FolderPath,FileName),'rb') as image:

	content = image.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)

print(response.full_text_annotation.text)