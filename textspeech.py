#!/usr/bin/env python
# -*- coding: utf-8 -*

from PIL import Image
import pytesseract
import speech_recognition as sr
from google_speech import Speech
def ocr_str(image_name):    #converts image to string and returns that string
    im=Image.open(image_name)
    text=pytesseract.image_to_string(im,lang="eng")
    return text

def write():                          #writes the ocr returned string in a text file
    text=open("string.txt","w+")
    text.write(ocr_str(a))
    text.close()
#write()
def braille(x):                                                                       #braille mapped dictionary prints argumented text into braille
    brail_dic={' ':'   ', '!':'⠮','"':'⠐', '#':'⠼', '$':'⠫', '%':'⠩', '&':'⠯', "'":"⠄", '(':'⠷', ')':'⠾', '*':'⠡',
           '+':'⠬', ',':'⠠', '-':'⠤', '.':'⠨', '/':'⠌', '0':'⠴', '1':'⠂', '2':'⠆', '3':'⠒', '4':'⠲', '5':'⠢',
           '6':'⠖', '7':'⠶', '8':'⠦', '9':'⠔', ':':'⠱', ';':'⠰', '<':'⠣', '=':'⠿', '>':'⠜', '?':'⠹', '@':'⠈',
           'a':'⠁', ' b':'⠃', 'c':'⠉', 'd':'⠙', 'e':'⠑', 'f':'⠋', 'g':'⠛', 'h':'⠓', 'i':'⠊', 'j':'⠚', 'k':'⠅',
           'l':'⠇', 'm':'⠍', 'n':'⠝', 'o':'⠕', 'p':'⠏', 'q':'⠟', 'r':'⠗', 's':'⠎', 't':'⠞', 'u':'⠥', 'v':'⠧',
           'w':'⠺', 'x':'⠭', 'y':'⠽', 'z':'⠵', '[':'⠪', ']':'⠻', '^':'⠘', '_':'⠸', 'A':'⠠⠁', 'B':'⠠⠃', 'C':'⠠⠉',
           'D':'⠠⠙', 'E':'⠠⠑', 'F':'⠠⠋', 'G':'⠠⠛', 'H':'⠠⠓', 'I':'⠠⠊', 'J':'⠠⠚', 'K':'⠠⠅', 'L':'⠠⠇', 'M':'⠠⠍',
           'N':'⠠⠝', 'O':'⠠⠕', 'P':'⠠⠏', 'Q':'⠠⠟', 'R':'⠠⠗', 'S':'⠠⠎', 'T':'⠠⠞', 'U':'⠠⠥', 'V':'⠠⠧', 'W':'⠠⠺',
           'X':'⠠⠭', 'Y':'⠠⠽', 'Z':'⠠⠵'}
    for i in x:
        try:        
            print(brail_dic[i],end='')  
        except:
            print("",end='')  
#braille(ocr_str(a))
def speech_to_text():                     #converts what you speak to text and returns string of the text
# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
def text_to_speech(a):                                             #converts the passed text into speech
    a = Speech(a,"en")
    effects=("speed","1.1")
    a.play(effects)
def calling():
    a=input('write what you want to convert')
    print(a)
    text_to_speech(a)