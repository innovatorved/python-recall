from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

speak.Speak("Hello I am Your Assistant")