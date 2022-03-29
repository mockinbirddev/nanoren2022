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

image labAss neutral = "lab assistant.png"

image classA = "classmate1.png"
image classB = "classmate2.png"
image classC = "classmate3.png"

image banker = "classmate2.png"

image bankMan = "classmate3.png"

image cleo = "cleo.png"

image helpNISB = "helpful nisb.png"

image nisb = "nisb.png"

image snake = "lab assistant.png"

image gabriel evil = "gabriel evil.png"
image gabriel neutral = "gabriel neutral.png"

#bg
image black = "#000"
image bg apartment1 = im.Scale("modernBG/18_condo_10/condo_Day 01.jpg", 1280, 720)
image bg apartment2 = im.Scale("modernBG/18_condo_10/condo_day 05.jpg", 1280, 720)
image bg bedroom = im.Scale("bedroom.jpg", 1280, 720)
image bg busStop = im.Scale("bus_station.jpg", 1280, 720)
image bg classroom = im.Scale("classroom.jpg", 1280, 720)
image bg computerLab = im.Scale("modernBG/that_couch.jpg", 1280, 720)
image bg office = im.Scale("modernBG/19_condo_4/cheap_condo_morning.jpg",1280,720)
image bg bank = im.Scale("modernBG/19_condo_4/cheap_condo_noon.jpg",1280,720)
image bg park = im.Scale("modernBG/20_scenic-road_10/_scenic_road_noon.jpg", 1280, 720)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Adam")
define f = Character("Finn")
define ga = Character("Gabriel Andrews")
define c = Character("Cleo")
define mom = Character("Ms. Martinez")
define l = Character("Leon")
define lm = Character("Leon and Ms. Martinez")

#audio
define audio.badSequential = "audio/BadSequential.mp3"
define audio.fanfare = "audio/Fanfare.mp3"
define audio.tetheredFate = "audio/TetheredFate.mp3"


#sound effects from freesound.org; copyright to their respective artists/owners
define sound.typing = "audio/typing.mp3"
define sound.alarm = "audio/alarm.wav"
define sound.knock = "audio/knocking.mp3"
define sound.boot = "audio/boot.wav"
define sound.punch = "audio/punch.mp3"
define sound.wood = "audio/wood.mp3"
define audio.outside = "audio/outside.wav"
define sound.talking = "audio/talking.wav"
define sound.laugh = "audio/laugh.wav"
define sound.bell = "audio/bell.mp3"
define sound.beep = "audio/beep.mp3"
define sound.phone = "audio/phone.wav"
define sound.honk = "audio/honk.wav"
define sound.siren ="audio/siren.mp3"
define sound.running ="audio/running.wav"
define sound.dramatic ="audio/dramatic.mp3"
define sound.dooropen ="audio/dooropen.wav"

#effects
define fade = Fade(0.5, 0.0, 0.5)

# The game starts here.
label start:
    #act 1
    call a1s1
    call a1s2
    call a1s3
    #act 2
    call a2s1
    call a2s2
    call a2s3
    call a2s4

    return
