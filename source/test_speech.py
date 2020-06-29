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


def create_msg(msg):
    say_msg(msg)
    notification.notify(
        title='Перерыв',
        message=msg,
        app_name='SpeechNotification',
    )


def main():
    first_delta = 5

    # Inputs
    # is_change = int(input("Do you want to change settings - yes-1, no-2 ?: "))
    # is_change = True if is_change == 1 else False

    # if is_change:
    #     custom_msg = input("Type in your custom message: ")
    ''''''
    # TODO: Добавать изменение настроек + профили

    default_delta = 2700  # 45 min
    default_msg = "Пора сделать перерыв"

    while True:
        create_msg(default_msg)
        time.sleep(first_delta)
        create_msg(default_msg)
        time.sleep(default_delta)


if __name__ == '__main__':
    main()


