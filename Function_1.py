import os, io
from tkinter import filedialog, Tk
from google.cloud import vision
from google.cloud .vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccountToken.json'

FileName = "testimg.jpg"
FolderPath = os.getcwd()
FullPath = os.path.join(FolderPath,FileName)

def GetText(FilePath):
	client = vision.ImageAnnotatorClient()


	with io.open(FilePath,'rb') as image:

		content = image.read()

	image = vision.types.Image(content=content)
	response = client.document_text_detection(image=image)
	return (response.full_text_annotation.text)

print(GetText(FullPath))