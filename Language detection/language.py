import langid

def detect_language(text):
    return langid.classify(text)[0]

text = input("Enter the text to check for language: ")
print(detect_language(text))
