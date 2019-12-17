# Game Script #

# Character Definitions #
define unknown = Character(("Stranger"), color="#c8fec8")
define j = Character("Jomo Senpai")

image man1 animated:
    "man1 look"
    choice:
        "man1 look"
        pause 1.25
        "man1 blink50"
        pause 0.015
        "man1 blink"
        pause 0.1
        "man1 blink50"
        pause 0.015
        "man1 look"
    choice:
        "man1 look"
        pause 1.25
        "man1 look talk50"
        pause 0.02
        "man1 look talk"
        pause 0.25
        "man1 look talk50"
        pause 0.02
        "man1 look"
        pause 0.75
    repeat
image bg black = "#000000"

## define doesn't change; default can
###############################################################################
#### Pregame Name Function Start ####
init:
    default playerName = ""

init python:
    def name_func(nameString):
        store.playerName = nameString.strip()
        renpy.restart_interaction() #continually updates (required)
    #### Pregame Name Caret Styles Start ####
    style.input.caret = "my_caret"
    style.input.size = 40
    style.input.color = "#000"
    #### Pregame Name Caret Styles End ####
define player = Character("[playerName]", color="#c8ffc8")
#### Pregame Name Function End ####
###############################################################################
# Game Start #
label start:
    stop music fadeout 1.0 # fade menu music out
    show black # black background
    with dissolve # fades into black
    pause 1.0  # waits 1 second
    play music "/audio/open pianocomp2.mp3"
    #window show

    scene forest
    with dissolve
    show jomo speak
    with dissolve
    j "Hi! [player], how are u"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    hide jomo
    show man1 animated

    # These display lines of dialogue.

    j "You've created a new Ren'Py game."

    j "Once you add a story, pictures, and music, you can release it to the world!"

    player "Hi. Testing variable assignment."

    # This ends the game.

    return
