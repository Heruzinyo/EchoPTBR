# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=True, who_window_style = "say_who_window"):

    default two_window = True

        # Decide if we want to use the one-window or two-window variant.
    if not two_window:
        # The one window variant.
        vbox:
            style "say_two_window_vbox"
            
            window:
                id "window"
                yoffset -13

                text what id "what":
                    size 28
                    line_spacing 10

    else:
        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            window:
                id "window"
                has vbox:
                    style "say_vbox"

                text what id "what":
                    size 28
                    line_spacing 10
            if who:
                window:
                    style who_window_style
                    text who id "who"
    
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    use extra_menu

init -1:
    
    $ config.keymap['rollback'].append('mouseup_3')
    $ config.keymap['game_menu'].remove('mouseup_3')
    
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("say_sfx", "sfx", False)

##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action [Play ("ex_sfx", "sfx/click.wav"), action]
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        size 24
        idle_color "#fff"
        hover_color "#d87000"
        yoffset 6

    style menu_choice_button is button:
        background Frame("ui/choice_idle.png", 0, 0)
        xminimum int(config.screen_width * 0.60)
        xmaximum int(config.screen_width * 0.60)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
init -2:
    style readback_window:
        background None
        
    style readback_frame:
        yoffset -13
        xoffset -35
        background "ui/options_bg.png"

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    #on "show" action Play("movie", "cover.ogv", loop = True)
    #on "hide" action Stop("movie")
    #on "replaced" action Stop("movie")

#############################################

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        background "ui/mm/cover_new.jpg"
        #xmargin 0
        #frame:
        #    style "new_menu_01"
        #frame:
        #    style "new_menu_02"
        #frame:
        #    style "new_menu_08"
        imagebutton auto "ui/mm/water_%s.png" action [Play ("menu_sfx", "underwater.ogg"), ShowMenu("imagegallery"), With(fade), mr.Play("deadlybeauty.ogg")] ypos 188 at menu_water     
        imagebutton:
            idle "ui/mm/null.png"
            hover "ui/mm/new_game_hover.png" 
            action [Play ("menu_sfx", "sfx/ping.wav"), Start("saturday")] xoffset 83 yoffset 514 at menu_eff 
        imagebutton:
            idle "ui/mm/null.png"
            hover "ui/mm/load_game_hover.png" 
            action [Play ("menu_sfx", "sfx/ping.wav"), ShowMenu("load")] xoffset 80 yoffset 559 at menu_eff
        imagebutton:
            idle "ui/mm/null.png"
            hover "ui/mm/options_hover.png" 
            action [Play ("menu_sfx", "sfx/ping.wav"), ShowMenu("preferences")] xoffset 81 yoffset 603 at menu_eff
        imagebutton:
            idle "ui/mm/null.png"
            hover "ui/mm/help_hover.png" 
            action [Play ("menu_sfx", "sfx/ping.wav"), Help()] xoffset 80 yoffset 651 at menu_eff
        imagebutton:
            idle "ui/mm/null.png"
            hover "ui/mm/quit_hover.png" 
            action [Play ("menu_sfx", "sfx/ping.wav"), Quit(confirm=False)] xoffset 79 yoffset 698 at menu_eff

init -2:

    # Make all the main menu buttons be the same size.
    
    #style mm_frame:
    #    background None
        
    #style new_menu_01:
    #    background "ui/mm/01_left.jpg"
    #    yoffset -25
    #    xoffset -30
        
    #style new_menu_02:
    #    background "ui/mm/02_top.jpg"
    #    yoffset -25
    #    xoffset 53
        
    #style new_menu_08:
    #    background "ui/mm/08_right.jpg"
    #    yoffset 486
    #    xoffset 283
        
    transform menu_eff:
        on hover:
            alpha 0.0
            easein 0.5 alpha 1
            easein 0.7 alpha 0
            repeat
        on idle:
            alpha 1

    transform menu_water:
        on hover:
            alpha 0.0
            easein 0.8 alpha 0.8
            easeout 0.8 alpha 0
            repeat
    


# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("menu_sfx", "sfx", False)


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_nav"
    
    frame:
    
        style_group "nav_pref"
        background None
        xfill True
        ypos 570
        hbox:
            textbutton _("Quit Game") action Quit()
            textbutton _("Main Menu") action MainMenu()
            textbutton _("Save Game") action ShowMenu("save")
            textbutton _("Load Game") action ShowMenu("load")
            textbutton _("Help") action Help()
            textbutton _("Back") action Return()

init -2:

    # Make all game menu navigation buttons the same size.
    
    $ style.gm_nav_window.background = None
    
    style gm_nav is default
       
    style nav_pref_frame:
        background None
        xmargin 5
        xfill False
        
    style nav_pref_button:
        is default
        background None
        xpadding 030

    style nav_pref_button_text:
        size 16
        idle_color "#ffffff"
        hover_color "#d87000"
        insensitive_color "#000"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    modal True

    window:
        style_group "config_bg"
        xpadding 115
        use bottom_menu
        #imagebutton auto "ui/bt_back_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Return()]  xoffset 707 yoffset 575

        frame:
            background "ui/options_bg.png"
            xmaximum 808
            ymaximum 458
            yalign 0.5
            has vbox
            frame:
                style_group "file_picker"
                top_margin 0.08
                background None
                $ columns = 2
                $ rows = 5

                # Display a grid of file slots.
                grid columns rows:
                    transpose True
                    xfill False
                    spacing -25

                    # Display ten file slots, numbered 1 - 10.
                    for i in range(1, columns * rows + 1):

                        # Each file slot is a button.
                        button:
                            action FileAction(i)
                            xfill False
                            xpadding 65
                            yoffset -20
                            yminimum 50
                            background None
                            has hbox

                            # Add the screenshot.
                            add FileScreenshot(i)

                            $ file_name = FileSlotName(i, columns * rows)
                            $ file_time = FileTime(i, empty=_("Empty"))
                            $ save_name = FileSaveName(i)

                            text " [file_name]. [file_time!t]\n[save_name!t]"

                            key "save_delete" action FileDelete(i)

            # File Navigator
            hbox:
                yoffset -50
                xoffset 60
                style_group "file_picker_nav"
                
                textbutton _("Auto"):
                    action FilePage("auto")
                    
                text "  |   " color "#888"

                textbutton _("Quick"):
                    action FilePage("quick")
                    
                text "  |   " color "#888"

                textbutton _("Previous"):
                    action FilePagePrevious()

                for i in range(1, 9):
                    textbutton str(i):
                        action FilePage(i)

                textbutton _("Next"):
                    action FilePageNext()
                
screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu

    use file_picker

init -2:

    #$ style.option_bg_window.background = Frame("ui/bg.jpg", 0, 0)
    
    #style option_bg_window is default

    style save_load_nav_button:
        xalign 0
        xpadding 10
        ypadding 0
        ymargin 0
        background None

    style file_picker_frame is menu_frame
    style file_picker_nav_button is save_load_nav_button
    style file_picker_nav_button_text is echo_pref_button_text
    style file_picker_button is large_button
    style file_picker_text is echo_pref_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    # This ensures that any other menu screen is replaced.
    tag menu

    # Put the navigation columns in a container.        
    window:
        use bottom_menu
        style_group "config_bg"
        frame:
            style_group "prefs"

            # Container for the options.
            hbox:
                xoffset -80
                yoffset -40
                vbox:
                    frame:
                        top_margin 0.10
                        style_group "echo_pref"
                        label _("Display")
                    frame:
                        style_group "echo_pref"
                        label _("Transitions")
                    frame:
                        style_group "echo_pref"
                        label _("Text Speed")
                    frame:
                        style_group "echo_pref"
                        label _("Skip")
                    frame:
                        style_group "echo_pref"
                        label _("After Choices")
                    frame:
                        style_group "echo_pref"
                        label _("Music Volume")
                    frame:
                        style_group "echo_pref"
                        label _("Sound Volume")

                    if config.has_voice:
                        frame:
                            style_group "echo_pref"
                            label _("Voice Volume")

                            bar value Preference("voice volume")
                            textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                            if config.sample_voice:
                                textbutton _("Test"):
                                    action Play("voice", config.sample_voice)
                                    style "soundtest_button"
                vbox:
                    frame:
                        top_margin 0.10
                        style_group "echo_pref"
                        xfill True
                        yoffset 5
                        has hbox
                    
                        hbox:
                            textbutton _("Window") action Preference("display", "window")
                            textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    
                    frame:
                        style_group "echo_pref"
                        xfill True
                        has hbox
                    
                        hbox:
                            textbutton _("All") action Preference("transitions", "all")
                            textbutton _("None") action Preference("transitions", "none")
                    frame:
                        style_group "echo_pref"
                        xfill True
                        xpadding 80
                        has hbox
                    
                        hbox:
                            bar value Preference("text speed")
                    frame:
                        style_group "echo_pref"
                        xfill True
                        yoffset 27
                        xoffset 100
                        has hbox
                    
                        hbox:
                            textbutton _("Seen Messages") action Preference("skip", "seen")
                            textbutton _("All Messages") action Preference("skip", "all")
                    frame:
                        style_group "echo_pref"
                        xfill True
                        yoffset 30
                        xoffset 90
                        has hbox
                    
                        hbox:
                            textbutton _("Stop Skipping") action Preference("after choices", "stop")
                            textbutton _("Keep Skipping") action Preference("after choices", "skip")
                    frame:
                        style_group "echo_pref"
                        xfill True
                        xpadding 80
                        yoffset 35
                        has hbox
                    
                        hbox:
                            bar value Preference("music volume")
                    frame:
                        style_group "echo_pref"
                        xfill True
                        xpadding 80
                        yoffset 55
                        has hbox
                    
                        hbox:
                            bar value Preference("sound volume")
                            
                    if config.has_voice:
                        frame:
                            style_group "echo_pref"
                            xfill True
                            has hbox
                    
                            hbox:
                                bar value Preference("voice volume")
                                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                                if config.sample_voice:
                                    textbutton _("Test"):
                                        action Play("voice", config.sample_voice)
                                        style "soundtest_button"
init -2:
        
    style config_bg_window:
        background "images/Cover.png"
        xpadding 115

    style gallery_bg_window:
        background "ui/gallery/gallery_bg.png"
        #xpadding 115
        
    style prefs_frame:
        background "ui/options_bg.png"
        xmaximum 808
        ymaximum 458
        yoffset -17
        yalign 0.5
    
    style echo_pref_slider:
        left_bar "ui/slider_full.png"
        right_bar "ui/slider_empty.png"
        thumb "ui/slider_thumb.png"
        xmaximum 200
        xalign 1.0
        ymaximum 24
    
    style echo_pref_frame:
        background None
        xmargin 5
        xfill False
        xoffset 80
        yoffset 5

    style pref_frame:
        xfill True
        xmargin 5
        top_margin 0
        background None

    style pref_vbox:
        xfill True

    style echo_pref_button:
        size_group "pref"
        xalign 0
        xpadding 50
        ypadding 0
        ymargin 0
        background None

    style echo_pref_button_text:
        selected_color "#d87000"
        idle_color "#888888"
        hover_color "#FFFFFF"
        selected_hover_color "#FFFFFF"

    style soundtest_button:
        xalign 1.0



##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True
    
    window:
        style "yesno_window"

    frame:
        style_group "yesno"

        xfill False
        yfill False
        yoffset 200
            
        label _(message):
            xalign 0.5
            yoffset 10

        hbox:
            xalign 0.5

            imagebutton auto "ui/bt_yes_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), yes_action]  xoffset -10 yoffset 95
            imagebutton auto "ui/bt_no_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), no_action]  xoffset 10 yoffset 95

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:    
    style yesno_window is default
    
    style yesno_frame:
        background "ui/quit_bg.png"

    style yesno_button:
        size_group "yesno"
        background None
        
    style yesno_button_text:
        idle_color "#aaaaaa"
        hover_color "#ff8f00"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
        

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xoffset -165
        xalign 1.0
        yalign 1.0
      
        textbutton _("Backlog") action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("text_history")] 
        textbutton _("Fast Forward") action Skip(fast=True, confirm=True)
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        
        

init -2:
    style quick_button:
        is default
        background None
        xpadding 15

    style quick_button_text:
        is default
        size 16
        idle_color "#8888"
        hover_color "#ca971b"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
##############################################################################
# Extra Menu
#
# A screen that's included by the default say screen, adding four buttons
# on either side of the window.
screen extra_menu():

    # Add an in-game extra menu.
    hbox:
        style_group "extra"

        imagebutton auto "ui/bt_config_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("preferences")]  xoffset 60 yoffset 650
        imagebutton auto "ui/bt_quit_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Quit()]  xoffset -70 yoffset 700
        imagebutton auto "ui/bt_save_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("save")]  xoffset 665 yoffset 650
        imagebutton auto "ui/bt_load_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("load")]  xoffset 600 yoffset 700

init python:
    renpy.music.register_channel("ex_sfx", "sfx", False)
    
##############################################################################
# Bottom Menu
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen bottom_menu():

    modal True

    # The background of the game menu.
    window:
        style "gm_nav"
        imagebutton auto "ui/bt_quit_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Quit()]  xoffset 0 yoffset 575
        imagebutton auto "ui/bt_title_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), MainMenu(confirm=True)]  xoffset 139 yoffset 575
        #imagebutton auto "ui/bt_save_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("save")]  xoffset 284 yoffset 575
        #imagebutton auto "ui/bt_load_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("load")]  xoffset 426 yoffset 575
        imagebutton auto "ui/bt_help_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Help()]  xoffset 568 yoffset 575
        imagebutton auto "ui/bt_back_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Return()]  xoffset 707 yoffset 575

screen bottom_menu_alt():

    modal True

    # The background of the game menu.
    window:
        style "gm_nav"
        imagebutton auto "ui/bt_quit_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Quit()]  xoffset 50 yoffset 640
        imagebutton auto "ui/gallery/image_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("imagegallery")]  xoffset 200 yoffset 640
        imagebutton auto "ui/gallery/scene_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("scenegallery")]  xoffset 350 yoffset 640
        imagebutton auto "ui/gallery/music_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), ShowMenu("music_room")]  xoffset 500 yoffset 640  
        imagebutton auto "ui/bt_help_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Help()]  xoffset 650 yoffset 640
        imagebutton auto "ui/bt_title_%s.png" action [Play ("ex_sfx", "sfx/click.wav"), Return()]  xoffset 800 yoffset 640

init -2:
    style gm_nav_window:
        background None
        
    style gm_nav is default


################################################################################
#Gallery, music, replay
################################################################################



## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## The spacing between file slots.
define gui.slot_spacing = 10

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    background "ui/bg.jpg"

style game_menu_navigation_frame:
    xsize 280
    yfill True


style game_menu_content_frame:
    left_margin 87
    right_margin 61
    top_margin 120
    bottom_margin 150


style game_menu_viewport:
    xsize 920

style chatlog_frame:
    background None
    left_margin 342
    right_margin 315
    top_margin 172
    bottom_margin 85

style user_page:
    background None
    left_margin 340
    right_margin 340
    top_margin 168
    bottom_margin 90

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

########################################################
#Music List
########################################################


init python:
    style.music_list = Style(style.button_text)
    style.music_list.clear()
    style.music_list_button_text.color = "#FFF"
    style.music_list_button_text.hover_color = "#F2C34E"
    style.music_list_button_text.selected_color = "#F2C34E"
    #style.music_list.outlines=[(2, "#FFF", 0, 0)]
    style.music_list_button_text.size=40
    style.music_list.background=None
    style.music_list.hover_background=None
    style.music_list.yminimum = 1
    style.music_list.xminimum = 1

###################################################






############ phone code here########
# This script is based on https://lemmasoft.renai.us/forums/viewtopic.php?t=40245 phone message system by Nadia Nova and other contributers of the forum.


init 5:
    style phone_message_vbox:
        xalign 0.5
        yalign 0
        ypos 180
        xsize 260
        xoffset -18
        
    style phone_message_frame:
        background Solid("#696969")
        ypadding 5
        xpadding 10
        
    style phone_message_frame2:
        background Solid("#0088df")
        ypadding 5
        xpadding 10

    style phone_message_contents:
        spacing 10
        xalign 0.5

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 0
        yalign 0

        
    style phone_message2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 0
        yalign 0
        
        
    style phone_message_who is phone_message:
        color "#ecf0f1"
        size 25

    style phone_message_what is phone_message:
        color "#ffffff"
        size 19
        font "ui/arcon.otf"
        spacing 5

    style phone_reply is default:
        size 18
        xalign 0.5
        xsize 435
        background Solid("#666")
        hover_background Solid("#78E8A0")
        ypadding 10
        xpadding 10
        
        
screen phone_message(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        add "ui/phone/bubble-tip.png" at phone_message_bubble_tip
        
        frame:
            style_group "phone_message"
            
            vbox:
                style "phone_message_contents"
                #text who style "phone_message_who"
                text what style "phone_message_what"

#player choice reply
screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset 40
        xalign 0.5       
        #xpos 200
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "ui/phone/bubble-tip2.png" at phone_message_bubble_tip2
        
        frame:
            style_group "phone_message2"
            background Solid("#0088df")
            #xsize 200
            
            vbox:
                style "phone_message_contents"
                xsize 223
                #text who style "phone_message_who"
                text what style "phone_message_what"
                
#scripted mc reply useless
screen phone_message3(what): 
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -290        
        xalign 1.0
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "ui/phone/bubble-tip2.png" at phone_message_bubble_tip2
        
        frame:
            style_group "phone_message2"
            background Solid("#0088df")
            xsize 200
            
            vbox:
                style "phone_message_contents"
                ##text who style "phone_message_who"
                text what style "phone_message_what"
                
screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5
        
        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"

# here is a new menu that has more options than two
# basically i just added one more textbutton here, and the additional labels needed in the call 
# if you wish to make a menu with one or four just copy the code below and modify it a bit       
screen phone_reply3(reply1, label1, reply2, label2, reply3, label3,):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5
        
        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"
        

style phone_reply_text:
    xalign 0.5

screen phone_message_image(who, what, img):
    vbox at incoming_message:
        xoffset 3
        style_group "phone_message"
        # this one adds the triangular tip for the bubble, if you change colors you change this images too
        add "images/bubble-tip.png" at phone_message_bubble_tip
        
        frame:
            style_group "phone_message"
            
            vbox:
                style "phone_message_contents"
                #text who style "phone_message_who"
                text what style "phone_message_what"
                add img

############# phone code ends ############
init python:
    style.recent_text = Style(style.button_text)
    style.recent_text.clear()
    style.recent_text_button_text.color = "#9e9e9e"
    style.recent_text_button_text.hover_color = "#9e9e9e"
    style.recent_text_button_text.selected_color = "#9e9e9e"
    #style.music_list.outlines=[(2, "#FFF", 0, 0)]
    style.recent_text_button_text.size=15
    style.recent_text.background=None
    style.recent_text.hover_background=None
    style.recent_text.yminimum = 1
    style.recent_text.xminimum = 1

