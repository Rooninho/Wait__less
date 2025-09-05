# import pyttsx3

# engine = pyttsx3.init()

# def announce_customer(customer, desk):
#     message = f"{customer}, please proceed to {desk}."
#     print(message)
#     engine.say(message)
#     engine.runAndWait()

# announcer.py
# announcer.py
import pyttsx3
import threading

def _speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
    engine.stop()

def announce_customer(customer, desk):
    message = f"{customer}, please proceed to {desk}."
    print(message)
    # Run each announcement in its own thread
    threading.Thread(target=_speak, args=(message,)).start()






