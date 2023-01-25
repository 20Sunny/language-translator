import googletrans
import speech_recognition
import gtts
import playsound
print(googletrans.LANGUAGES)
input_lang = input("INPUT LANGUAGE : ")
output_lang = input("OUTPUT LANGUAGE : ")
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("_______________SPEAK NOW________________")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language=input_lang)
    print(text) 
translator = googletrans.Translator()
translation = translator.translate(text, dest=output_lang)
print(translation.text)
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
# 
trans = googletrans.Translator()
audio = trans.translate(text, dest=input_lang)
change = gtts.gTTS(audio.text, lang=input_lang)
change.save("first.mp3")
playsound.playsound("first.mp3")