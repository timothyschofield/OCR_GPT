"""
OCR_GPT.py

07 November 2023

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
https://blog.roboflow.com/gpt-4-image-classification/   
On November 6th, 2023, OpenAI released a vision-enabled version of the GPT-4 API. 
This API, referred to by the gpt-4-vision-preview identifier,
enables you to ask a question and provide an image as context. 
We previously reported on GPT 4V's capabilities, noting impressive performance in image understanding. 
These capabilities are perfect for classification.


"""
import os
# This code is for v1 of the openai package: pypi.org/project/openai
# pip install openai
from openai import OpenAI

my_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)   # openai version 1.1.1

try:

    # "gpt-3.5-turbo", currently points to gpt-3.5-turbo-0613. Will point to gpt-3.5-turbo-1106 starting Dec 11, 2023. 
    
    """
    # post https://api.openai.com/v1/chat/completions
    completion = client.chat.completions.create(
        model="gpt-4", # we want "gpt-4-vision-preview"
        # Grammar correction
        messages=[
            {"role": "system", "content": "You will be provided with statements, and your task is to convert them to standard English."},
            {"role": "user", "content": "She no went to the market."}
            ]
    )

    # Works
    print(completion.choices[0].message)
    """

    """
    # post https://api.openai.com/v1/images/generations
    completion = client.images.generate(
        model="dall-e-3", 
        # Creates an image given a prompt.
        prompt="A cute baby sea otter",
        n=1,
        size="1024x1024",
        quality="standard"
    )

    image_url = completion.data[0].url
    # Works
    print(image_url)
 
    """

    # So we are told the OCR is part of chat completetion



    request = "Please OCR this image."
    test_url = "https://metalbyexample.com/wp-content/uploads/figure-65.png"

    completion = client.chat.completions.create(
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
        max_tokens=300,  
    )
    """
    Choice(finish_reason=None, index=0, 
    message=ChatCompletionMessage(content='The image contains the following text:\n\n"It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."', role='assistant', function_call=None, tool_calls=None), finish_details={'type': 'stop', 'stop': '<|fim_suffix|>'})
    """


    print(completion.choices[0])

except Exception as ex:
    print("Exception:", ex)

"""
RateLimitError
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.', 
                                                    'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

You can view the rate and usage limits for your organization under the limits section of your account settings.                                                    
OpenAI Icon > Settings > Limits
08 Nov 2023 - put my credit limit up to $10.00 (credit card details and everything)
DF84C4A2-0001	Paid  $12.00	8 Nov 2023, 08:34	-- Yay, it works
ChatCompletionMessage(content='She did not go to the market.', role='assistant', function_call=None, tool_calls=None)


If you want to use the new GPT-4 AI model, you'll just need to subscribe to ChatGPT Plus. 
For developers, you can access the GPT-4 API. 
This wikiHow guide will teach you how to use the GPT-4 language model by upgrading to ChatGPT Plus, using the API, and accessing Bing Chat.

"""






























