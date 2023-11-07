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

"""
import os
# This code is for v1 of the openai package: pypi.org/project/openai
# pip install openai
from openai import OpenAI

api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)   # openai version 1.1.1

try:

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)

except Exception as ex:
    print("Exception:", ex)

"""
RateLimitError
Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.', 
                                                    'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}

You can view the rate and usage limits for your organization under the limits section of your account settings.                                                    
OpenAI Icon > Settings > Limits

If you want to use the new GPT-4 AI model, you'll just need to subscribe to ChatGPT Plus. 
For developers, you can access the GPT-4 API. 
This wikiHow guide will teach you how to use the GPT-4 language model by upgrading to ChatGPT Plus, using the API, and accessing Bing Chat.

"""






























