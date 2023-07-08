import openai
import pyttsx3
import speech_recognition as sr
from API_Seecrets import apikey

openai.apikey = apikey

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
converstion = ""
user_name = "Your Name"

while True:
    with mic as source:
        print("lisitening....")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
        print("No Longer lisiting")
        try:
            user_input = r.recognize_google(audio)
        except:
            continue

        prompt = user_name + ":" + user_input + "/nBot:"
        converstion += prompt

        response = openai.Completion.create(engine='text-davinci-003', prompt=converstion, max_tokens=100)
        response_str = response["choices"][0]["text"].replace("/n","")
        response_str = response.split(user_name + ":",1)[0].split("Bot: ",1)[0]

        converstion += response_str + "/n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()
