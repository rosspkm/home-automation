import client.client as client

import lib.settings as settings
import lib.req as req
import lib.keywords as keywords

import speech_recognition as sr
import pyttsx3
from beeply import notes

""" connect hub to wifi """
class run:

    def __init__(self):
        self.conn = client.connect()
        self.loop = loop()
        self.msg = ""
    
    def input(self, msg):
       self.msg = self.conn.process(msg) 

    def receive(self):
        return self.msg


def process(msg):
    run.input(msg)

def get_data():
    return run.receive()

def loop():
    """ Listen for input, match the modules and respond """
    while True:
        
        if settings.quit_flag:
            break

        if settings.MIC:
            settings.quit_flag = passive_listen()
            text = active_listen()

        else:
            text = input('> ')
            text = text[2:]

        if not text:
            print('No text input received.')
            continue

        else:
            response = req.parse(text)
            # do something with the response
            
            

    print('Exit.')
    settings.quit_flag = False

""" Listen for keyword """
def passive_listen():
    while True:
        try:
            with sr.Microphone() as source:
                global audio
                audio = recognizer.listen(source)

                if keywords.name in recognizer.recognize_google(audio).lower():
                    return False
                elif any(keywords.stop_trigger) in recognizer.recognize_google(audio).lower():
                    return True
                else:
                    continue

        except source:
            engine.say("No microphone detected")
            engine.runAndWait()

""" Active listen after keyword trigger """
def active_listen():
    print("in active listen")
    try:
        mybeep.hear('C',250)
        with sr.Microphone() as source:
            global audio
            audio = recognizer.listen(source)
            print("Input successful")
            return recognizer.recognize_google(audio).lower()

    except LookupError:
        engine.say("Could not understand please try again")
        engine.runAndWait()

mybeep = notes.beeps()

recognizer = sr.Recognizer()
microphone = sr.Microphone()
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    
engine = pyttsx3.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id) # Use female voice

run = run()