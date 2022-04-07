import time
import sys
import itertools
from threading import Thread


class Loader:
    """
        Simple Command line loading animation creator
    """

    def __init__(self, load_sequence: list | tuple = None):
        """
        :param load_sequence: sequence to cycle through default sequence ['|', '/', '-', '|', '\']

            Example:
                >>> loader = Loader(['-_-', '0_-', '-_0', '0_0'])
                >>> loader.start("Please wait...", threaded=True, delay=0.2)
                >>> time.sleep(5) # do something in the background
                >>> loader.stop()
        """
        self._sequence = load_sequence if load_sequence is not None else ['|', '/', '-', '|', '\\']
        self._should_load = True
        self._getting_input = False
        self._input_message = ""

    def stop(self) -> None:
        """
            Stop the loading animation
        :return: None
        """
        self._should_load = False

    def start(self, message: str = "", delay: int | float = 0.2, threaded: bool = False) -> None:
        """
            Start the loading animation
            :param message: message to attach with the loading
            :param delay: loading animation delay the lower, the faster
            :param threaded: should run in animation thread
            :return: None
        """
        if not self._should_load: self._should_load = True

        if threaded:
            Thread(target=self.__start_load, args=(message, delay)).start()
        else:
            self.__start_load(message, delay)

    def __start_load(self, message, delay):
        """
            Main loading function
            do not call this directly, use 'start' function
        """
        for seq in itertools.cycle(self._sequence):
            if not self._should_load: break
            sys.stdout.write(f"\r{seq} {message}")
            sys.stdout.flush()
            time.sleep(delay)
