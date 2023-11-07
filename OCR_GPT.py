"""
OCR_GPT.py

07 November 2023

To create a Python Virtual Environment:
a) To create the Python venv, go to Manage > Command Palette > Create Environment (.venv folder should appear in project root).
b) In Terminal type .venv\Scripts\activate (A green (.venv) should appear to the left of the Terminal prompt).

Get API key from https://platform.openai.com/account/api-keys
Then in the Terminal type
    "setx OPENAI_API_KEY <the openai key>"

WARNING: You have to quit out of VS Code and go back in before new system environment variables are avaliable

FYI: To see all system environment variables,
        go to the DOS COMMAND PROMPT and type set

"""
import os
# This code is for v1 of the openai package: pypi.org/project/openai
# pip install openai
from openai import OpenAI

api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)   # openai version 1.1.1






























