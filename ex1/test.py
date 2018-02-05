import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

from google.cloud.vision import types
from os import listdir
# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
# file_name = os.path.join(
#     os.path.dirname(__file__),
#     'input.jpg')

file_name = os.path.join(
    os.path.dirname(__file__),
    'download/out.mp4')




# Loads the image into memory
with io.open(file_name, 'rb') as document_file:
   	 content = document_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)