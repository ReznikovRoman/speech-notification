import pyttsx3
from pyttsx3.drivers import sapi5
from plyer import notification
from datetime import datetime
import time
from colorama import init, Fore

from utils import (handle_user_input_int, handle_user_input_bool,
                   convert_minutes_to_seconds, )
from decorators import (set_range, )


######################################################################################################################

'''
Pyinstaller Command:

pyinstaller --hidden-import=pyttsx3.drivers --hidden-import=pyttsx3.drivers.dummy --hidden-import=pyttsx3.drivers.espeak --hidden-import=pyttsx3.drivers.nsss --hidden-import=pyttsx3.drivers.sapi5 --hidden-import=colorama --hidden-import=plyer --hidden-import=plyer.platforms.win.notification speech_notification.py --onefile
'''



class SpeechNotification:
    def __init__(self, speech_engine: pyttsx3.Engine, time_delta: int):
        self._speech_engine = speech_engine
        self._time_delta = time_delta
        self.__break_durations = []

    def get_engine(self):
        return self._speech_engine

    def set_engine(self, new_speech_engine):
        self._speech_engine = new_speech_engine

    def get_time_delta(self):
        return self._time_delta

    def set_time_delta(self, new_time_delta: int):
        self._time_delta = new_time_delta

    def say_msg(self, msg: str):
        """
        'Says' message

        Args:
            msg (str): Message that will be said

        Returns:
            None
        """
        self._speech_engine.say(msg)
        self._speech_engine.runAndWait()  # Wait until the message is finished

    def create_msg(self, msg: str):
        """
        'Says' message and creates Windows notification

        Args:
            msg (str): Message that will be said

        Returns:
            None
        """
        self.say_msg(msg)
        print(f"\n{Fore.MAGENTA + msg}\n")
        notification.notify(
            title='Break',
            message=msg,
            app_name='SpeechNotification',
        )

    @property
    def average_break_duration(self):
        try:
            avg_break_duration = sum(self.__break_durations) / len(self.__break_durations)
        except ZeroDivisionError as zde:
            return 0
        else:
            return avg_break_duration

    def handle_break(self):
        time_before_break = datetime.now()
        is_break_over = handle_user_input_bool('Answer', 'Have you taken a break? ')
        time_delta = (datetime.now() - time_before_break).seconds
        break_duration = time.strftime("%H:%M:%S", time.gmtime(time_delta))
        self.__break_durations.append(time_delta)
        print(f"Perfect! Your break lasted {Fore.GREEN + break_duration}. "
              f"Your average break is "
              f"{Fore.BLUE + time.strftime('%H:%M:%S', time.gmtime(self.average_break_duration))}")

    def run(self, greeting_msg, break_msg):
        # Greet user at the launch
        print(Fore.YELLOW + greeting_msg)
        self.say_msg(greeting_msg)

        while True:
            time.sleep(self._time_delta)
            self.create_msg(break_msg)
            self.handle_break()


def setup_engine(speech_engine: pyttsx3.Engine):
    """
    Configures the base settings of the speech engine

    Args:
        speech_engine (pyttsx3.Engine): Current speech engine

    Returns:
        None
    """
    # set male voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)

    # set volume and rate of the speech
    engine.setProperty('rate', 135)
    engine.setProperty('volume', 0.85)


@set_range(lower_boundary=1, upper_boundary=1380, field_name='Timer')
def get_user_timer():
    time_delta = handle_user_input_int(
        input_field='Timer',
        input_msg='Enter how much time (in minutes) do you want to work until the break: ')
    return time_delta


def main(speech_engine: pyttsx3.Engine):

    # Set the timer delta
    time_delta = get_user_timer()
    time_in_seconds = convert_minutes_to_seconds(time_delta)

    # Set the default messages that will be said
    greeting_msg = "Good Morning Roman!"
    break_msg = "Time to take a break"

    # Create SpeechNotification object
    sn = SpeechNotification(speech_engine, time_in_seconds)
    sn.run(greeting_msg, break_msg)


if __name__ == '__main__':
    init()  # initialize colorama
    engine = pyttsx3.init()  # create speech engine
    setup_engine(engine)  # setup engine
    main(engine)



