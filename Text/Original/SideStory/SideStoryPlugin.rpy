## Character Name Resize #######################################################
# If the characters' names look strange, this can be used to fix all of them
# Set resize_names to True to activate, and use the following two float variables to adjust as needed (I found left = 20, right = 60 to work for me)
# See Readme for more details
init -2 python:
    resize_names = False

    charname_left_margin = 20
    charname_right_margin = 60


## CGs #########################################################################
image cg lights = Frame("images/SideStory-Lights.png", 0, 20)


## Backgrounds #################################################################
image bg chapel = "chapel.png"
image bg chapelbasement = "chapel-basement.png"
image bg conveniencenight = "convenience-night.png"
image bg fastfoodext = "fastfood-exterior.png"
image bg fastfoodint = "fastfood-interior.png"
image bg jashouse2 = "jashouse2.png"
image bg lightsroad = "lights-road.png"
image bg lightsparty = "lights-party.png"
image bg parkinglotdusk = "ParkinglotDusk.png"
image bg paytonnight = "payton-night.png"
image bg puebloapt = "pueblo-apt.png"
image bg scraptrailernight = "scraptrailernight.png"
image bg tjbedroom = "tj-bedroom.png"
image bg tjdiningroom = "tj-diningroom.png"
image bg theater = "theater.png"
image bg theaterext = "theater-ext.png"
image bg trailerinteriornight = "trailerinteriornight.png"
image bg univincent = "uni-vincent.png"
image bg unisunset = "uni-sunset.png"
image bg warehouseext = "warehouse-ext.png"
image bg warehouseint = "warehouse-int.png"


## Character Images ############################################################
image Carlu Pants = "Carlu_alt.png"

init python:
    ## Audio Channels ##########################################################
    renpy.music.register_channel("music2", "sfx", loop=True, tight=True)
    renpy.music.register_channel("background2", "sfx", loop=True, tight=True)

    ## Character Definitions ###################################################
    # Sarah
    sa = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_sarah",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Vincent
    vi = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_vincent",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Lana
    la = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_lana",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Mom
    mom = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_mom",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Dad (gray)
    dadg = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_dadg",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Jas
    jas = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_jasmynn",
        ctc="ctc_blink",
        ctc_position="nestled")

    # Jas
    se = Character(' ',
        color="#FFFFFF",
        show_two_window=True,
        show_who_window_style="say_sean",
        ctc="ctc_blink",
        ctc_position="nestled")

    ## Helper Functions ########################################################
    def vol(channel, vol=1, delay=0):
        """
        More concise way to change the volume of a channel
        """
        renpy.music.set_volume(vol, delay=delay, channel=channel)

    def pan(channel, pan=0, delay=0):
        """
        More concise way to pan an audio channel
        """
        renpy.music.set_pan(pan, delay=delay, channel=channel)

    def reset_channel(channel, delay=0):
        """
        Sets an audio channel to its default volume and panning
        """
        vol(channel, delay=delay)
        pan(channel, delay=delay)

    def stop_all_audio(fadeout=0, reset=False, subset=None):
        """
        Stops all audio at the same time, with a default fadeout time of 0, and
        with the option to reset all channels' volume and panning while we're
        at it. If subset is not None, this will only affect channels in given
        iterable
        """
        if subset is not None:
            affected_channels = subset
        else:
            affected_channels = sidestory_audio_channels
        for channel in affected_channels:
            renpy.music.stop(channel, fadeout)
            if reset:
                reset_channel(channel, delay=fadeout)

    # Default list of audio channels
    sidestory_audio_channels = [
        "music", "music2", "background", "background2", "sound", "loop"]


## Character Names #############################################################
init -1 python hide:
    style.say_sarah = Style ('say_who_window')
    style.say_sarah.background = Frame("ui/speaker_sarah.png", 0, 0)
    style.say_sarah.xalign = 0.20
    style.say_sarah.yalign = 0.0
    style.say_sarah.yoffset = -195
    style.say_sarah.xfill = True
    style.say_sarah.yfill = True
    style.say_sarah.ymaximum = 33
    style.say_sarah.xmaximum = 104

    style.say_vincent = Style ('say_who_window')
    style.say_vincent.background = Frame("ui/speaker_vincent.png", 0, 0)
    style.say_vincent.xalign = 0.20
    style.say_vincent.yalign = 0.0
    style.say_vincent.yoffset = -195
    style.say_vincent.xfill = True
    style.say_vincent.yfill = True
    style.say_vincent.ymaximum = 33
    style.say_vincent.xmaximum = 104

    style.say_lana = Style ('say_who_window')
    style.say_lana.background = Frame("ui/speaker_lana.png", 0, 0)
    style.say_lana.xalign = 0.20
    style.say_lana.yalign = 0.0
    style.say_lana.yoffset = -195
    style.say_lana.xfill = True
    style.say_lana.yfill = True
    style.say_lana.ymaximum = 33
    style.say_lana.xmaximum = 104

    style.say_mom = Style ('say_who_window')
    style.say_mom.background = Frame("ui/speaker_mom.png", 0, 0)
    style.say_mom.xalign = 0.20
    style.say_mom.yalign = 0.0
    style.say_mom.yoffset = -195
    style.say_mom.xfill = True
    style.say_mom.yfill = True
    style.say_mom.ymaximum = 33
    style.say_mom.xmaximum = 104

    style.say_dadg = Style ('say_who_window')
    style.say_dadg.background = Frame("ui/speaker_dadg.png", 0, 0)
    style.say_dadg.xalign = 0.20
    style.say_dadg.yalign = 0.0
    style.say_dadg.yoffset = -195
    style.say_dadg.xfill = True
    style.say_dadg.yfill = True
    style.say_dadg.ymaximum = 33
    style.say_dadg.xmaximum = 104

    style.say_jasmynn = Style ('say_who_window')
    style.say_jasmynn.background = Frame("ui/speaker_jasmynn.png", 0, 0)
    style.say_jasmynn.xalign = 0.20
    style.say_jasmynn.yalign = 0.0
    style.say_jasmynn.yoffset = -195
    style.say_jasmynn.xfill = True
    style.say_jasmynn.yfill = True
    style.say_jasmynn.ymaximum = 33
    style.say_jasmynn.xmaximum = 104

    style.say_sean = Style ('say_who_window')
    style.say_sean.background = Frame("ui/speaker_sean.png", 0, 0)
    style.say_sean.xalign = 0.20
    style.say_sean.yalign = 0.0
    style.say_sean.yoffset = -195
    style.say_sean.xfill = True
    style.say_sean.yfill = True
    style.say_sean.ymaximum = 33
    style.say_sean.xmaximum = 104


## RenPy Subroutines ###########################################################
label sidestory_title(msg, fade=1.5, kerning=10, lock=True, end=False, size=32):
    # Displays text in the center of the screen
    # If end, fades out the text, if not, fades it in
    # If lock, we hard pause for the duration of the fade
    if not end:
        show text "{size=[size]}{k=[kerning]}[msg]":
            xalign 0.5
            yalign 0.5
            alpha 0.0
            ease fade alpha 1.0
    else:
        show text "{size=[size]}{k=[kerning]}[msg]":
            ease fade alpha 0.0
    if lock:
        $ renpy.pause(fade + 0.05, hard=True)
    return


## Transitions and ATL #########################################################
define medium_dis = { "master" : Dissolve(1) }

transform sidestory_trip:
    zoom 1.1
    xalign 0.5
    yalign 0.5
    rotate 0
    alpha 0.3
    parallel:
        ease 3 xalign 0.51
        ease 3 xalign 0.49
        repeat
    parallel:
        ease 5 rotate renpy.random.randint(1, 3)
        ease 5 rotate renpy.random.randint(-3, -1)
        repeat
    parallel:
        ease renpy.random.randint(3, 10) alpha 0.2
        ease renpy.random.randint(3, 10) alpha 0.4
        repeat


## Character Name Resize (see top for explanation) #############################
init python hide:
    if resize_names:
        say_characters = [
            style.say_chase,
            style.say_flynn,
            style.say_ryan,
            style.say_carl,
            style.say_unknown,
            style.say_leo,
            style.say_daxton,
            style.say_clint,
            style.say_jenna,
            style.say_tj,
            style.say_kud,
            style.say_raven,
            style.say_duke,
            style.say_brian,
            style.say_janice,
            style.say_sydney,
            style.say_micha,
            style.say_heather,
            style.say_jeremy,
            style.say_mayor,
            style.say_casey,
            style.say_mike,
            style.say_julian,
            style.say_dad,
            style.say_dev,
            style.say_cam,
            style.say_mrbronson,
            style.say_injy,
            style.say_lana,
            style.say_vincent,
            style.say_sarah,
            style.say_mom,
            style.say_dadg,
            style.say_jasmynn,
            style.say_sean
        ]

        def _resize_names(character):
            character.left_margin = charname_left_margin
            character.right_margin = charname_right_margin

        for character in say_characters:
            _resize_names(character)
