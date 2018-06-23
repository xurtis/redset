'''
Redshift configuration GUI.
'''

import gi
gi.require_version('Gtk', '3.0')

from sys import exit, argv

from gi.repository import Gtk

from .redshift import Redshift, MIN_TEMPERATURE, MAX_TEMPERATURE

class ControlPanel(Gtk.Window):

    def __init__(self, app):
        super(ControlPanel, self).__init__(
            title="Redset",
            application=app
        )
        self.__redshift = Redshift()

        self.set_default_size(480, 80)

        grid = Gtk.Grid()
        grid.set_column_spacing(4)
        grid.set_row_spacing(4)
        grid.set_border_width(8)

        temperature = self.__add_scale(
            self.__redshift.temperature,
            MIN_TEMPERATURE, MAX_TEMPERATURE, 500.0,
            self.__change_temperature,
        )
        grid.attach(Gtk.Label(label="Colour Temperature"), 0, 0, 1, 1)
        grid.attach(temperature, 1, 0, 1, 1)

        scales = [
            ("Brightness", self.__change_brightness),
            ("Gamma Red", self.__change_gamma_red),
            ("Gamma Green", self.__change_gamma_green),
            ("Gamma Blue", self.__change_gamma_blue),
        ]

        for i, (label, callback) in enumerate(scales):
            scale = self.__add_scale(
                callback=callback,
            )
            grid.attach(Gtk.Label(label=label), 0, 1 + i, 1, 1)
            grid.attach(scale, 1, 1 + i, 1, 1)

        self.add(grid)

    def __add_scale(
        self,
        value=1.0,
        lower=0.1,
        upper=1.0,
        step=0.05,
        callback=None,
    ):
        scale = Gtk.Scale(
            orientation=Gtk.Orientation.HORIZONTAL,
            adjustment=Gtk.Adjustment(
                value,
                lower,
                upper,
                step,
            )
        )
        scale.connect("value-changed", callback)
        scale.set_draw_value(False)
        scale.set_hexpand(True)
        return scale

    def __change_temperature(self, scale):
        self.__redshift.temperature = scale.get_value()

    def __change_brightness(self, scale):
        self.__redshift.brightness = scale.get_value()

    def __change_gamma_red(self, scale):
        self.__redshift.gamma_red = scale.get_value()

    def __change_gamma_green(self, scale):
        self.__redshift.gamma_green = scale.get_value()

    def __change_gamma_blue(self, scale):
        self.__redshift.gamma_blue = scale.get_value()

class Redset(Gtk.Application):

    def __init__(self):
        super(Redset, self).__init__()

    def do_activate(self):
        panel = ControlPanel(self)
        panel.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


def run():
    redset = Redset()
    exit(redset.run(argv))
