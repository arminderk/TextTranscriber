import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
file = sr.AudioFile('audios/male.wav')

with file as source:
    audio = r.record(source)

translator = Translator()
translated = translator.translate(r.recognize_google(audio), dest='pa')

text_file = open("output.txt", "w")
text_file.write(translated.text.encode('utf-8'))
text_file.close()