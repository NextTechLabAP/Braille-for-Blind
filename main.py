import imagebraille
import imagevoice
import speechtotext
import textspeech
import speechbraille
import textbraille

print("Here are the following features of our Project.")
choice = ["Image to Braille", "Image to Voice", "Text to Speech", "Text to Braille", "Speech to Text", "Speech to Braille"]
n=0
for i in choice:
    n+=1
    print(n, "", i)

choose = input("Choose what you want to do?\n")

if choose == "Image to Braille" or choose == "1":
    imagebraille.calling()

elif choose == "Image to Voice" or choose == "2":
    imagevoice.calling()

elif choose == "Text to Speech" or choose == "3":
    textspeech.calling()

elif choose == "Text to Braille" or choose == "4":
    textbraille.calling()

elif choose == "Speech to Text" or choose == "5":
    speechtotext.calling()

elif choose == "Speech to Braille" or choose == "6":
    speechbraille.calling()