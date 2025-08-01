﻿# Copyright 2004-2019 Tom Rothamel <pytom@bishoujo.us>
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

# This contains code to choose between OpenGL and Software rendering, when
# a system supports both.

init -1500:

    python hide:
        import os
        store.__dxwebsetup = os.path.join(config.renpy_base, "lib", "windows-i686", "dxwebsetup.exe")

    python:
        class _SetRenderer(Action):
            """
            Sets the preferred renderer to one of "auto", "angle", "gl", or
            "sw".
            """

            def __init__(self, renderer):
                self.renderer = renderer

            def __call__(self):
                _preferences.renderer = self.renderer
                renpy.restart_interaction()

            def get_selected(self):
                return _preferences.renderer == self.renderer

    # This is displayed to ask the user to choose the renderer he or she
    # wants to use. It takes no parameters, doesn't return anything, and
    # is expected to call _SetRenderer actions and quit when done.
    #
    # This screen can be customized by the creator, provided the actions
    # remain available.
    screen _choose_renderer:

        frame:
            style_group ""

            has side "c b":
                spacing gui._scale(10)
                xfill True
                yfill True

            fixed:

                vbox:

                    xmaximum 0.48

                    label _("Renderização")

                    null height 10

                    textbutton _("Escolher Automaticamente"):
                        action _SetRenderer("auto")
                        style_suffix "radio_button"

                    if renpy.renpy.windows:
                        textbutton _("Forçar Renderização Angle/DirectX"):
                            action _SetRenderer("angle")
                            style_suffix "radio_button"

                    textbutton _("Forçar Renderização OpenGL"):
                        action _SetRenderer("gl")
                        style_suffix "radio_button"

                    textbutton _("Forçar Renderização por Software"):
                        action _SetRenderer("sw")
                        style_suffix "radio_button"

                    null height 10

                    label _("NPOT")

                    null height 10

                    textbutton _("Habilitar"):
                        action SetField(_preferences, "gl_npot", True)
                        style_suffix "radio_button"

                    textbutton _("Desabilitar"):
                        action SetField(_preferences, "gl_npot", False)
                        style_suffix "radio_button"


                    null height 10

                    label _("Controle")

                    null height 10

                    textbutton _("Habilitar"):
                        action SetField(_preferences, "pad_enabled", True)
                        style_suffix "radio_button"

                    textbutton _("Desabilitar"):
                        action SetField(_preferences, "pad_enabled", False)
                        style_suffix "radio_button"

                    null height 10

                    textbutton _("Calibrar"):
                        action ui.invokesinnewcontext(_gamepad.calibrate)
                        xfill True

                vbox:

                    xmaximum 0.48
                    xpos 0.5

                    label _("Economia de Energia")

                    null height 10

                    textbutton _("Habilitar"):
                        action Preference("gl powersave", True)
                        style_suffix "radio_button"

                    textbutton _("Desabilitar"):
                        action Preference("gl powersave", False)
                        style_suffix "radio_button"

                    null height 10

                    label _("Taxa de Quadros")

                    null height 10

                    textbutton _("Tela"):
                        action Preference("gl framerate", None)
                        style_suffix "radio_button"

                    textbutton _("60"):
                        action Preference("gl framerate", 60)
                        style_suffix "radio_button"

                    textbutton _("30"):
                        action Preference("gl framerate", 30)
                        style_suffix "radio_button"

                    null height 10

                    label _("Tearing")

                    null height 10

                    textbutton _("Habilitar"):
                        action Preference("gl tearing", True)
                        style_suffix "radio_button"

                    textbutton _("Desabilitar"):
                        action Preference("gl tearing", False)
                        style_suffix "radio_button"

                    null height 10

            vbox:

                text _("As mudanças terão efeito na próxima vez que o programa for executado.") substitute True

                null height 10

                hbox:
                    spacing gui._scale(25)

                    textbutton _(u"Sair"):
                        action Quit(confirm=False)
                        yalign 1.0

                    if not renpy.display.interface.safe_mode:
                        textbutton _("Voltar"):
                            action Return(0)
                            yalign 1.0


    # This is displayed when a display performance problem occurs.
    #
    # `problem` is the kind of problem that is occuring. It can be:
    # - "sw" if the software renderer was selected.
    # - "slow" if the performance test failed.
    # - "fixed" if we're operating w/o shaders.
    # - other things, added in the future.
    #
    # `url` is the url of a web page on renpy.org that will include
    # info on troubleshooting display problems.
    screen _performance_warning:

        frame:
            style_group ""

            has vbox

            label _("Aviso de Desempenho")

            null height 10

            if problem == "sw":
                text _("Este computador está usando renderização por software.")
            elif problem == "fixed":
                text _("Este computador não está usando shaders.")
            elif problem == "slow":
                text _("Este computador não está exibindo os gráficos lentamente.")
            else:
                text _("Este computador está tendo problema ao exibir os gráficos: [problem].") substitute True

            null height 10

            if directx_update:
                text _("Seus drivers gráficos podem estar desatualizados ou não estarem funcionando corretamente. Isso pode levar a uma exibição gráfica lenta ou incorreta. Atualizar o DirectX pode corrigir esse problema.")
            else:
                text _("Seus drivers gráficos podem estar desatualizados ou não estarem funcionando corretamente. Isso pode levar a uma exibição gráfica lenta ou incorreta.")

            if directx_update:
                null height 10

                textbutton _("Atualizar DirectX"):
                    action directx_update
                    xfill True

            null height 10

            textbutton _("Continuar, Mostrar esse aviso novamente"):
                action Return(True)
                xfill True

            textbutton _("Continuar, Não mostrar esse aviso novamente"):
                action Return(False)
                xfill True

            null height 10

            textbutton _("Sair"):
                action Quit(confirm=False)
                xfill True

    # Used while a directx update is ongoing.
    screen _directx_update:

        frame:
            style_group ""

            has vbox

            label _("Atualizando DirectX.")

            null height 10

            text _("A instalação web do DirectX foi iniciada. Ela pode começar minimizado na barra de tarefas. Por favor, siga as instruções para instalar o DirectX.")

            null height 10

            text _("{b}Observação:{/b} A instalação web do DirectX da Microsoft instalará, por padrão, a barra de ferramentas do Bing. Se você não quiser essa barra de ferramentas, desmarque a caixa apropriada.")

            null height 10

            text _("Quando a instalação terminar, por favor, clique abaixo para reiniciar o programa.")

            textbutton _("Reiniciar") action Return(True)



init -1500 python:
    # The image that we fill the screen with in GL-test mode.
    config.gl_test_image = "black"

    class __GLTest(renpy.Displayable):
        """
         This counts the number of times it's been rendered, and
         the number of seconds it's been displayed, and uses them
         to make the decisions as to if OpenGL is working or not.
         """

        def __init__(self, frames, fps, timeout):
            super(__GLTest, self).__init__()

            self.target = 1.0 * frames / fps
            self.frames = frames
            self.timeout = timeout

            self.times = [ ]
            self.success = False

            renpy.renpy.display.log.write("- Target is {0} frames in {1} seconds.".format(frames, self.target))

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)

            if self.success:
                return rv

            self.times.append(st)

            renpy.redraw(self, 0)

            renpy.renpy.display.log.write("- Frame drawn at %f seconds." % st)

            if len(self.times) >= self.frames:
                frames_timing = self.times[-1] - self.times[-self.frames]

                renpy.renpy.display.log.write("- %f seconds to render %d frames.", frames_timing, self.frames)

                if frames_timing <= self.target:
                    self.success = True
                    renpy.timeout(0)

            return rv

        def event(self, ev, x, y, st):

            if self.success:
                return True

            if st > self.timeout:
                return False

            renpy.timeout(self.timeout - st)

    config.performance_test = True

    def __gl_test():

        import os

        # If we've entered safe mode, display the renderer choice screen.
        # This screen will cause us to quit.

        if _restart:
            return

        if not config.gl_enable:
            return

        if renpy.display.interface.safe_mode:
            renpy.call_in_new_context("_choose_renderer")

        if not config.performance_test:
            return

        _gl_performance_test()

    def _gl_performance_test():

        import os

        performance_test = os.environ.get("RENPY_PERFORMANCE_TEST", None)

        if performance_test is not None:
            performance_test = int(performance_test)

        if performance_test == 0:
            return

        if not _preferences.performance_test and not performance_test:
            return

        # Don't bother on android or ios - there's nothing the user can do.
        if renpy.mobile:
            return

        renpy.renpy.display.log.write("Performance test:")

        # This will cause the screen to start displaying.
        ui.pausebehavior(0)
        ui.interact(suppress_underlay=True, suppress_overlay=True)

        # The problem we have.
        problem = None

        renderer_info = renpy.get_renderer_info()

        # Software renderer check.
        if config.renderer != "sw" and renderer_info["renderer"] == "sw":
            problem = "sw"

        # Speed check.
        if problem is None:

            # The parameters of the performance test. If we do not hit FPS fps
            # over FRAMES frames before DELAY seconds are up, we fail.
            FRAMES = 5
            FPS = 15
            DELAY = 1.5

            renpy.transition(Dissolve(DELAY), always=True, force=True)
            ui.add(__GLTest(FRAMES, FPS, DELAY))
            result = ui.interact(suppress_overlay=True, suppress_underlay=True)

            if not result:
                problem = "slow"

        # Lack of shaders check.
        if problem is None:
            if not "RENPY_GL_ENVIRON" in os.environ:
                if renderer_info["renderer"] == "gl" and renderer_info["environ"] == "fixed":
                    problem = "fixed"

        if problem is None:
            return

        if renpy.renpy.windows and os.path.exists(__dxwebsetup):
            directx_update = Jump("_directx_update")
        else:
            directx_update = None

        # Give the warning message to the user.
        renpy.show_screen("_performance_warning", problem=problem, directx_update=directx_update, _transient=True)
        result = ui.interact(suppress_overlay=True, suppress_underlay=True)


        # Store the user's choice, and continue.
        _preferences.performance_test = result
        return


label _gl_test:

    # Show the test image.
    scene black
    show expression config.gl_test_image
    with None

    $ __gl_test()

    # Hide the test image.
    scene black

    return

# We can assume we're on windows here. We're also always restart once we
# make it here.
label _directx_update:

    if renpy.has_label("directx_update"):
        jump expression "directx_update"

label _directx_update_main:

    python hide:

        # Start dxsetup. We have to go through startfile to ensure that UAC
        # doesn't cause problems.
        import os
        os.startfile(__dxwebsetup)

        renpy.show_screen("_directx_update")
        ui.interact(suppress_overlay=True, suppress_underlay=True)

        renpy.quit(relaunch=True)

label _choose_renderer:
    scene expression "#000"

    $ renpy.shown_window()
    $ renpy.show_screen("_choose_renderer",  _transient=True)
    $ ui.interact(suppress_overlay=True, suppress_underlay=True)
    return
