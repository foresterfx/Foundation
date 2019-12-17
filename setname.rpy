##for custom cursor caret
image my_caret:
    "caret.png" # white caret
    #"caret-black.png"
    ypos 0.0
    linear 0.75 alpha 1.0
    pause 0.25
    linear 0.75 alpha 0.0
    pause 0.25
    repeat
################################################################################
## Main Menu Name Screen
################################################################################
## setname screen ###########################################################
##
## This screen is included in the main menu. Requires input to set playerName
## and run the Start() function
#############################################################################
screen setname():
    modal True # only interact with this until screen finishes logic
    zorder 200 # position in z axis of screen
    style_prefix "confirm"
    add "gui/overlay/confirm.png" # translucent dark background
    window at truecenter:
        xmaximum 1000
        xalign 0.5
        yalign 0.5

        vbox: # nameBox
            xalign 0.5
            yalign 0.5
            spacing 45

            text _("Enter Name: "):
                xalign 0.5
            input:
                default playerName # default value
                changed name_func # uses function from script.rpy
                length 25 # maximum name length
                xalign 0.5 # centers input in vbox
            hbox: # cancel and submit buttons
                xalign 0.5 # centers cancel/submit buttons
                spacing 200
                textbutton _("Cancel"):
                    action [Notify("You must enter a name."), Hide("setname")]
                textbutton _("Submit"):
                    if playerName == "":
                        action [Notify("You must enter a name."), Hide("setname")]
                    else:
                        action [Hide("setname"), Start()]
        #######################################################################
        # Keys must be indented before hbox to prevent spacing style applying #
        #######################################################################
        key 'K_RETURN': # enter key
            if playerName == "":
                action [Notify("You must enter a name."), Hide("setname")]
            else:
                action [Hide("setname"), Start()]
        key 'K_KP_ENTER': # numpad enter key
            if playerName == "":
                action [Notify("You must enter a name."), Hide("setname")]
            else:
                action [Hide("setname"), Start()]
        key 'K_ESCAPE': # escape key
            action [Notify("You must enter a name."), Hide("setname")]

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
