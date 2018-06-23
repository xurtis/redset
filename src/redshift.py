'''
Wrapper for the redshift command line program.
'''

from subprocess import call
from os import path

from .defs import BINDIR

REDSHIFT='redshift'

DEFAULT_TEMPERATURE = 6500
MIN_TEMPERATURE = 1000
MAX_TEMPERATURE = 8000
DEFAULT_BRIGHTNESS = 1.0
DEFAULT_GAMMA = (1.0, 1.0, 1.0)

class Redshift(object):

    def __init__(
        self,
        temperature=6500,
        brightness=1.0,
        gamma=(1.0, 1.0, 1.0)
    ):
        self.__temperature = temperature
        self.__brightness = brightness
        self.__gamma = gamma
        self.reset()

    @property
    def gamma_red(self):
        red, _, _ = self.__gamma
        return red

    @gamma_red.setter
    def gamma_red(self, red):
        _, green, blue = self.__gamma
        self.__gamma = (red, green, blue)
        self.refresh()

    @property
    def gamma_green(self):
        _, green, _ = self.__gamma
        return green

    @gamma_green.setter
    def gamma_green(self, green):
        red, _, blue = self.__gamma
        self.__gamma = (red, green, blue)
        self.refresh()

    @property
    def gamma_blue(self):
        _, _, blue = self.__gamma
        return blue

    @gamma_blue.setter
    def gamma_blue(self, blue):
        red, green, _ = self.__gamma
        self.__gamma = (red, green, blue)
        self.refresh()

    @property
    def gamma(self):
        return self.__gamma

    @gamma.setter
    def gamma(self, gamma):
        self.__gamma = gamma
        self.refresh()

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature
        self.refresh()

    @property
    def brightness(self, brightness):
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness):
        self.__brightness = brightness
        self.refresh()

    def reset(self):
        '''
        Reset the screen to default settings.
        '''
        self.__temperature = DEFAULT_TEMPERATURE
        self.__brightness = DEFAULT_BRIGHTNESS
        self.__gamma = DEFAULT_GAMMA
        call([path.join(BINDIR, REDSHIFT), '-x'])

    def refresh(self):
        '''
        Call redshift to update the settings.
        '''
        call([
            path.join(BINDIR, REDSHIFT),
            '-O', str(self.__temperature),
            '-b', str(self.__brightness),
            '-g', ':'.join([str(c) for c in self.__gamma]),
        ])

