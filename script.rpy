# The script of the game goes in this file.

# Splash screen
image logo = "TSKN03.png"
image devLogo = "mbLogo.jpg"
label splashscreen:
    scene black with dissolve
    pause (2)
    show logo with dissolve
    pause (2)
    hide logo with dissolve
    show devLogo with dissolve
    pause (2)
    hide devLogo with dissolve

    return

#images
#characters
image adam angry = "adam angry.png"
image adam happy = "adam happy.png"
image adam neutral = "adam neutral.png"
image adam talking = "adam talking.png"

image finn neutral = "finn neutral.png"
image finn talking = "finn talking.png"

image leon angry = "leon angry.png"
image leon neutral = "leon neutral.png"

image mom neutral = "mom neutral.png"
image mom upset = "mom upset.png"

image teach neutral = "teacher.png"
image teach angry = "teacher.png"

image labAss neutral = "nerd.jpg"

#bg
image black = "#000"
image bg apartment1 = "modernBG/18_condo_10/condo_Day 01.jpg"
image bg apartment2 = "modernBG/18_condo_10/condo_day 05.jpg"
image bg bedroom = "bedroom.jpg"
image bg busStop = "bus_station.jpg"
image bg classroom = "classroom.jpg"
image bg computerLab = "modernBG/that_couch.jpg"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Adam")
define f = Character("Finn")
define ga = Character("Gabriel Andrews")
define c = Character("Cleo")
define mom = Character("Ms. Martinez")
define l = Character("Leon")
define lm = Character("Leon and Ms. Martinez")

# The game starts here.

label start:

    #call prologue
    call a1s1
    call a1s2
    call a1s3
    call a2s1
    call a2s2
    call a2s3
    call a2s4

    return
