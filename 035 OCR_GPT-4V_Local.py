"""
OpenAI API Experiments

OCR_GPT-V4_Local.py
Loads a local image file and OCRs it.

09 November 2023

To create a Python Virtual Environment:
a) To create the Python venv, go to Manage > Command Palette > Create Environment (.venv folder should appear in project root).
b) In Terminal type ".venv\Scripts\activate" (A green (.venv) should appear to the left of the Terminal prompt).

To get an API key:
Create an account with OpenAI.
After logging into OpenAI (https://openai.com/)
in the top left hand corner of the screen you will see the OpenAI logo.
Click it to open the side bar and click "API keys".

Then in the Terminal type
    "setx OPENAI_API_KEY <the openai key>"
 
WARNING: You have to quit out of VS Code (this IDE) and go back in before the new system environment variables are avaliable

FYI: To see all system environment variables,
        go to the DOS COMMAND PROMPT and type "set"

-----------------------------------------------------------------------------------   
On November 6th, 2023, OpenAI released a vision-enabled version of the GPT-4 API. 

This API, referred to by the gpt-4-vision-preview identifier,
enables you to ask a question and provide an image as context. 


If you get a RateLimitError - You need a pay-as-you-go account with OpenAI
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.', 
                                                    'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

You can view the rate and usage limits for your organization under the limits section of your account settings.                                                    
OpenAI Icon > Settings > Limits

"""
import os
# This code is for v1 of the openai package: pypi.org/project/openai
# pip install openai
from openai import OpenAI
import base64
import requests

my_api_key = os.environ["OPENAI_API_KEY"]


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    
# Path to your image
image_path = ".\\SourceImages\\some_text.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

# Loads a local image file and OCRs it.
# https://platform.openai.com/docs/guides/vision

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {my_api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
}

try:
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    print(response.json())

except Exception as ex:
    print("Exception:", ex)

"""
'This is an image of a herbarium specimen label from the RBG Kew Herbarium. 
The label gives detailed information about a particular plant specimen. 
It includes the name of the species (Chaetanthera microphylla), the collector\'s name (M. Rosas), and the collection date (31/01/2011). 
The label also mentions the location where the specimen was collected (Chile: O\'Higgins: Cachapoal) along with the latitude, longitude, and elevation.
\n\nThere is also reference to the Millennium Seed Bank Project and a cautionary 
note that states "RESTRICTED MATERIAL NOT TO BE LOANED OR SAMPLED WITHOUT WRITTEN PERMISSION."
\n\nAdditionally, there are details about the habitat where the plant was found, the kind of plant it is (annual herb), 
and an instruction that the sample belongs to the RBG Kew Herbarium and should be sent for loan/sampling requests to a specific email address. 
There is also mention of a type of collaboration with the Instituto de Investigaciones Agropecuarias (INIA) in Chile.
\n\nThis type of label is common in botanical collections where precise data is crucial for research and reference purposes.'

"""










