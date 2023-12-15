import pyttsx3

wel = "welcome to RoboSpeaker version 1.1"
print(wel)

engine = pyttsx3.init()
engine.say(wel)
engine.runAndWait()

print("if you wanna stop this program write 'STOP' ")
while(True):
    speech = input("Please type what you want to speak: ")
    if(speech=="STOP"):
        break        

    engine.say(speech)
    engine.runAndWait()