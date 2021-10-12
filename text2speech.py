import pyttsx3

data = input("Enter text which you want to convert into speech:\n")

engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()




"""
engine = pyttsx3.init()
engine.say("Whosoever holds this hammer, if he be worthy, should possess the power of Thor")
engine.runAndWait()

"""
