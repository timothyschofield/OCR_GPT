"""
OpenAI API Experiments

OCR_GPT-V4.py
Given an image URL it OCRs it.

08 November 2023

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

my_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)   # openai version 1.1.1

try:

    # https://platform.openai.com/docs/guides/vision
    # https://help.openai.com/en/articles/8555496-gpt-v-api

    request = "Please OCR this hebarium lable and extract collector and collector number, altitude, latitude, longitude, location, country, description, language and the barcode number which begins with the letter 'K'"
    
    test_url = "https://d2seqvvyy3b8p2.cloudfront.net/17ab52f8bf423934e72f326506e26850.jpg"

    ocr_output = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": request},
                    {
                        "type": "image_url",
                        "image_url": test_url
                    }
                ]
            }  
        ],
        max_tokens=500,  
    )
    
    # Works
    # print(ocr_output.choices[0].message)
   
    json_output = client.chat.completions.create(
        model="gpt-4", 
        # Grammar correction
        messages=[
            {"role": "system", "content": "First, delete all occurances of '\n  '. Format this as JSON where 'Collector', 'Altitude', 'Location', 'Country', 'Description' and 'Barcode number' are keys"},
            
            # {"role": "system", "content": "First, delete all occurances of '\n  '. Format this as an SQL INSERT statement where 'Collector', 'Altitude', 'Location', 'Country', 'Description' and 'Barcode number' are columns"},
            
            {"role": "user", "content": str(ocr_output.choices[0].message)}
            ]
    )

    print(json_output.choices[0].message.content)
    """
    {
    "Collector": "P. S. Lavarack",
    "Collector number": "PSL4001",
    "Altitude": "2 m",
    "Latitude": "18°23'S",
    "Longitude": "146°05'E",
    "Location": "12km S of Cardwell, W of highway near clearing",
    "Country": "Australia",
    "Description": "Habenaria praecox Lavarack & Dockrill, Herbaceous viridiflora woodland, poorly drained. Type specimen",
    "Language": "English",
    "Barcode number": "The barcode appears to be obscured in the image provided, and without a clear view, I cannot accurately identify the barcode number that begins with a 'K.'"
    }

    """



except Exception as ex:
    print("Exception:", ex)






























