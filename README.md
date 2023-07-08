# Speech-to-Text-ChatGPT

A simple chatbot that uses speech recognition and the OpenAI API to convert speech to text and generate responses.

## Description

This chatbot application allows users to have a conversation with the bot using voice input. The user's speech is converted to text using the speech recognition library, and then the text is used as a prompt for the OpenAI API to generate a response. The response is then converted back to speech using the pyttsx3 library for text-to-speech conversion.

## Prerequisites

- Python 3.x
- Install the required libraries:
  - openai
  - pyttsx3
  - speech_recognition

## Installation

1. Clone the repository:

   ```shell
   git clone <repository_url>
   
#  Install the required libraries:
pip install openai pyttsx3 SpeechRecognition

Obtain an API key from OpenAI and update the API_Seecrets.py file with your API key.

# Usage
Run the script:
python chatbot.py
Speak into the microphone when prompted and wait for the bot's response.

# Configuration
You can customize the chatbot behavior by modifying the following variables in the script:

user_name: The name of the user interacting with the chatbot.
engine: Configuration options for the pyttsx3 speech synthesis engine.
mic: Configuration options for the speech recognition microphone.





