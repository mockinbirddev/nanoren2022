# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lm = Character("Leon and Ms. Martinez")
# The game starts here.

label a1s1:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    ##scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    ##show eileen happy

    # These display lines of dialogue.
    ##e "You've created a new Ren'Py game."
    ##e "Once you add a story, pictures, and music, you can release it to the world!"

    #play sound somberMusic.mp3 -- add in later
    "*alarm is ringing.......*{p}......continues ringing."#was originally one line but split to two to create space
    mom "Adam! Get up! You're going to be late."
    "*knocking scene*"
    a "*sigh*{p}Dad, why did you have to leave...{p}maybe this wouldn't be such a problem if you were still here.{p}It's all mom's fault."
    a "I'm getting up Mom. Don't worry."
    l "That's right boy. Don't let me in there again."

    a "If only things were different..."

    "*random scenes of arguing can be heard*"
    ##show adam -- add in later
    a "I guess I should check my email before I leave. I wonder what is new in the digital world."
    #play sound computerBooting.mp3 -- add in later
    a "I'm glad I convinced Mom to keep this computer. She never really liked this stuff but it's the only way for me to feel closer to you.{p}But now i feel more alone than I do now.{p}No one really gets me and Mom's boyfriend is always over.{p}I can't see how she can quickly move on like that.{p}It just happened so fast."
    a "*sighs*"
    a "But thanks to you Dad, I'm able to learn more about what is going on out there than I would have if I had to do this on my own.{p}Of course, life would have been much clearer for me if youre were still here.{p}But I won't let you down.{p}There's nothing here in this world that can bring me down."
    ##scene bg room #show black scene -- addin later
    ##play sound walkingSound.mp3
    ##with fade
    ##show adam
    ##show parent?
    l "Damn boy. What took you so long?"
    a "Shut up."
    lm "Hey!"
    l "Listen here boy.{p}
    You don't get to talk to me like that.{p}
    You know what I do to little boys who don't act how they're suppose to?{p}
    You don't even have a job you can't walk in here all tall and might thinking you own the place."
    a "Leon. You don't even have a job.{p}
    You don't even live here.{p}
    You're just free loading off of us."
    ##with hpunch for right and left -- apparently this shakes the screen?

    a "Ouch..."
    mom "Leon. You didn't have to hit him!{p}
    Adam apologize now."
    a "Why do I need to apologize?{p}
    He's not even my dad.He's just a deadbeat guy with no job..."
    l "Boy, you better stop talking or else you'll have something else coming for you."
    a "You know what I'm leaving. I don't need to deal with this right now."
    ##hide adam -- add in later

    mom "Why are you always so hard on him?"
    l "that boy needs to learn some manners.{p}
    Damn kids these days....{p}
    Is breakfast ready?"


    # This ends the game.
    return
