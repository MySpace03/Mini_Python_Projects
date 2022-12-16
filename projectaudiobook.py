import pyttsx3
#file = open(filename, encoding="utf8")
book=open(r"D:\VS Code\When Dimple Met Rishi (Menon Sandhya).txt",encoding="utf8")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    print(i)
    engine.say(i)
    engine.runAndWait()
