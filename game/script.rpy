# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music "habahaba.mp3" 
    scene bg room

    python:
        name = renpy.input("Input your name")

        name = name.strip() or "Guy Shy"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "I wake up and it's a day like any other."

    "But there's something of an energy in the air..."

    "I have a good feeling about today. I'm putting myself out there. So I must, at least..."

    "Make progres..."

    e "[name]! "

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
