import pyttsx3
#file = open(filename, encoding="utf8")
book=open(r"When Dimple Met Rishi (Menon Sandhya) (z-lib.org).txt",encoding="utf8")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    print(i)
    engine.say(i)
    engine.runAndWait()
