import speech_recognition as sr
from guessing_game import recognize_speech_from_mic


r = sr.Recognizer()
m = sr.Microphone()
recognize_speech_from_mic(r, m)
male = sr.AudioFile('male600.wav')
with male as source:
  r.adjust_for_ambient_noise(source, duration=0.5)
  audio = r.record(source)

r.recognize_google(audio)