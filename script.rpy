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

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
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
    call a2s2
    call a1s3
    call a2s1
    call a2s2
    call a2s3
    call a2s4

    return
