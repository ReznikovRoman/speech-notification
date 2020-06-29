from datetime import datetime
import time
import pyttsx3

from plyer import notification

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')
tts.setProperty('rate', 135)
tts.setProperty('volume', 0.85)


def set_voice(): # Найти и выбрать нужный голос по имени
    voices = tts.getProperty('voices')
    for voice in voices:
        if voice.name == 'Aleksandr':
           tts.setProperty('voice', voice.id)
        else:
            pass


def say_msg(msg):
    set_voice()  # Настроить голос
    tts.say(msg)
    tts.runAndWait()  # Воспроизвести очередь реплик и дождаться окончания речи


first_delta = 5
second_delta = 20


def create_msg():
    msg = "Пора сделать перерыв"
    say_msg(msg)
    notification.notify(
        title='Перерыв',
        message='Пора сделать перерыв',
        app_name='SpeechNotification',
    )


while True:
    create_msg()
    time.sleep(first_delta)
    create_msg()
    time.sleep(second_delta)


