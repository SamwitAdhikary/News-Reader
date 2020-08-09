import pyttsx3
import requests
import json

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("News For Today... Lets Begin...")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=a33b127053db4331819fc90114334461"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news... Listen Carefully...")