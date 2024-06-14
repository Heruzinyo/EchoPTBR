# Copyright 2004-2019 Tom Rothamel <pytom@bishoujo.us>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

screen _gamepad_select(joysticks):

    modal True
    style_group ""

    frame:
        xfill True

        has vbox

        label _("Selecione o Controle para Calibrar")

        if not joysticks:
            text _("Nenhum Controle Disponível")
        else:
            for i, name in joysticks:
                textbutton "[i]: [name]" action Return(i) size_group "joysticks"

        null height 20

        textbutton _("Cancelar") action Return("cancel")

screen _gamepad_control(name, control, kind, mappings, back, i, total):

    modal True
    style_group ""

    frame:
        xfill True

        has vbox

        label _("Calibrando [name] ([i]/[total])")

        null height 20

        text _("Aperte ou mova o [kind] [control!r].")


        null height 20

        hbox:
            textbutton _("Cancelar") action Return("cancel")
            if len(mappings) >= 2:
                textbutton _("Pular (A)") action Return("skip")

            if back and len(mappings) >= 3:
                textbutton _("Voltar (B)") action Return(back)

    add _gamepad.EventWatcher(mappings)


init -1200 python in _gamepad:
    from pygame_sdl2 import JOYHATMOTION, JOYAXISMOTION, JOYBUTTONDOWN
    import pygame_sdl2
    import os

    class EventWatcher(renpy.Displayable):

        def __init__(self, mappings):
            renpy.Displayable.__init__(self)
            self.bound = set(mappings.values())
            self.mappings = mappings

        def render(self, width, height, st, at):
            return renpy.Render(0, 0)

        def event(self, ev, x, y, st):

            binding = None

            if ev.type == JOYBUTTONDOWN:
                binding = "b{}".format(ev.button)
            elif ev.type == JOYAXISMOTION and abs(ev.value) > .6:
                binding = "a{}".format(ev.axis)
            elif ev.type == JOYHATMOTION and (ev.value != 0):
                binding = "h{}.{}".format(ev.hat, ev.value)

            if binding not in self.bound:
                return binding

            if len(self.mappings) >= 2:
                if self.mappings['a'] == binding:
                    return "skip"

            if len(self.mappings) >= 3:
                if self.mappings['b'] == binding:
                    return "back"

            return None

    def calibrate(index=None):
        """
        A function that can be called to calibrate an unknown gamepad by
        writing out an updated gamecontrollerdb.txt file.
        """

        if index is None:

            joysticks = [ ]

            # Choose a controller to calibrate.
            for i in range(renpy.display.joystick.count()):

                try:
                    j = pygame_sdl2.joystick.Joystick(i)
                    j.init()
                    name = j.get_name()
                    j.quit()
                except:
                    continue

                if name is None:
                    continue

                joysticks.append((i, name))

            index = renpy.call_screen("_gamepad_select", joysticks)

            if index == "cancel":
                return

#         renpy.display.controller.ignore = True
        renpy.display.controller.quit(index)

        platform = pygame_sdl2.get_platform()

        guid = pygame_sdl2.controller.Controller(index).get_guid_string()
        if guid is None:
            return

        joy = renpy.display.joystick.get(index)
        if joy is None:
            return

        joy.init()
        name = joy.get_name()
        renpy.config.pass_joystick_events = True

        # Clear out the pending event.
        renpy.pause(.25)

        buttons = [
            "a",
            "b",
            "x",
            "y",
            "select",
            "home",
            "start",
            "analógico esquerdo",
            "analógico direito",
            "superior esquerdo",
            "superior direito",
            "direcional para cima",
            "direcional para baixo",
            "direcional para esquerda",
            "direcional para direita",
        ]

        axes = [
            "esquerdo direcional",
            "esquerdo vertical",
            "direito direcional",
            "direito vertical",
            "gatilho esquerdo",
            "gatilho direito",
            ]

        controls = [ (i, "botão") for i in buttons ] + [ (i, "analógico") for i in axes ]

        i = 0
        mappings = { }
        fail = False


        while i < len(controls):

            control, kind = controls[i]

            if control in mappings:
                del mappings[control]

            result = renpy.call_screen("_gamepad_control", name, control, kind, mappings, "back" if i else None, i+1, len(controls))

            if result == "skip":
                i += 1

            elif result == "back":
                i -= 1

            elif result == "cancel":
                fail = True
                break

            else:
                mappings[control] = result
                i += 1


        joy.quit()
        renpy.config.pass_joystick_events = False

        if fail:
            renpy.display.controller.start(index)
            return

        mapping = guid + "," + name + ",platform:" + platform

        for k, v in sorted(mappings.items()):
            mapping += ",{}:{}".format(k, v)

        print("Mapeamento do controle para", name, "é:")
        print(mapping)

        try:
            with open(os.path.join(renpy.config.renpy_base, "gamecontrollerdb.txt"), "a") as f:
                f.write(mapping + "\n")
        finally:
            renpy.display.controller.load_mappings()
            renpy.display.controller.start(index)


init -1200 python:

    def GamepadExists(developer=True):
        """
        :doc: gamepad

        A function that returns true if a gamepad is present, and false otherwise.

        `developer`
            Forces this function to always return true while :var:`config.developer`
            is true.
        """

        return renpy.display.controller.exists()


    def GamepadCalibrate():
        """
        :doc: gamepad

        An action that invokes the gamepad calibration routine.
        """

        if GamepadExists():
            return ui.invokesinnewcontext(_gamepad.calibrate)
        else:
            return None

