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
import time
# This code is for v1 of the openai package: pypi.org/project/openai
# pip install openai
from openai import OpenAI

my_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)   # openai version 1.1.1

try:

    # https://platform.openai.com/docs/guides/vision
    # https://help.openai.com/en/articles/8555496-gpt-v-api

    
    # test_url = "https://d2seqvvyy3b8p2.cloudfront.net/2ca62a26221a397d6942874b6ee7a225.jpg" # better handwritting
    
    # test_url = "https://d2seqvvyy3b8p2.cloudfront.net/d1f65c385d649f6770035348dd05c7ee.jpg" # shit handwritten
    #test_url = "https://d2seqvvyy3b8p2.cloudfront.net/17ab52f8bf423934e72f326506e26850.jpg" # printed
    
    #request = "Please OCR this old handwriting"
    #test_url = "https://c7.alamy.com/comp/MF9K2X/facsimile-of-a-portion-of-the-letter-written-by-oliver-cromwell-to-william-lenthall-speaker-of-the-house-of-commons-announcing-the-victory-at-the-battle-of-naseby-in-1645-from-old-england-a-pictorial-museum-published-1847-MF9K2X.jpg"
    
    request = "Please OCR this hebarium lable and extract collector and collector number, date, family, genus, species, altitude, latitude, longitude, location, country, description, language and the barcode number which begins with the letter 'K'"
    """
    url_list = ["https://d2seqvvyy3b8p2.cloudfront.net/650cef96509839e53586e9cb770ce2f3.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/f76836bbb9d6f938e47d1008d8f09dd2.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/368a769e34246aca7a392b5c20efbd78.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/7a90cfd7e9a4e3c621c32d32d9514c96.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/a3ee08998385e8402b8aa4c5b9b9f613.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/bb7be423df727cd8a79dad1a4fce9640.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/7f1f4ee4d91b3713a59ab993aa7eee13.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/871bf83bb330c2cd2b9b114d6590f89d.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/bbeee4e27aa37443638383ad7b14d016.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/6b947a6fa40888bd7cd4882973715db6.jpg",
    "https://d2seqvvyy3b8p2.cloudfront.net/26a1f3f5985e1f11421528e4715bb466.jpg"]
    """
    url_list = ["https://d2seqvvyy3b8p2.cloudfront.net/2ca62a26221a397d6942874b6ee7a225.jpg"]

    print("========================== START OUTPUT =============================")

    for test_url in url_list:

        print(test_url)
       
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
        json_input = ocr_output.choices[0].message.content
        print(json_input)
    
        json_output = client.chat.completions.create(
            model="gpt-4", 
            # Grammar correction
            messages=[
                {"role": "system", "content": "First, delete all occurances of '\n  '. Format this as JSON where 'Collector', 'Collector number', 'Date', 'Family', 'Genus', 'Species','Altitude', 'Location', 'Latitude', 'Longitude', 'Country', 'Description' and 'Barcode number' are keys"},
                {"role": "user", "content": str(json_input)}
                ]
        )

        sql_input = json_output.choices[0].message.content

        print(sql_input)
        sql_output = client.chat.completions.create(
            model="gpt-4", 
            # Grammar correction
            messages=[
                {"role": "system", "content": "This input is JSON. Format the input as an SQL INSERT statement for a table named 'specimenCards' where the keys are the column names and the values are values"},
                {"role": "user", "content": str(sql_input)}
                ]
        )

        print(sql_output.choices[0].message.content)

        time.sleep(5)

    print("========================== STOP OUTPUT =============================")   

except Exception as ex:
    print("Exception:", ex)






























