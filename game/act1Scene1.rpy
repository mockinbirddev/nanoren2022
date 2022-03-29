label a1s1:

    play music badSequential volume 0.2
    play sound alarm volume 0.2
    "*alarm is ringing.......*{p}......continues ringing."#was originally one line but split to two to create space
    mom "Adam! Get up! You're going to be late."
    stop sound
    play sound knock volume 0.2
    "*knock knock knock*"
    stop sound
    a "*sigh*{p}Dad, why did you have to leave...{p}Maybe this wouldn't be such a problem if you were still here.{p}It's all mom's fault."
    a "I'm getting up Mom. Don't worry."
    l "That's right boy. Don't make me come in there again."

    a "If only things were different..."

    show bg bedroom
    with fade
    show adam neutral
    with fade
    a "I guess I should check my email before I leave. I wonder what is new in the digital world."
    play sound boot volume 0.2
    a "I'm glad I convinced Mom to keep this computer. She never really liked this stuff, but it's the only way for me to feel closer to you."
    a "But now I feel more alone than ever.{p}No one really gets me, and Mom's boyfriend is always over."
    a "I can't see how she can quickly move on like that.{p}It just happened so fast."
    stop sound
    a "*sighs*"
    a "But thanks to you Dad, I'm able to learn more about what is going on out there than I would have if I had to do this on my own."
    a "Of course, life would have been much clearer for me if youre were still here.{p}But I won't let you down.{p}There's nothing here in this world that can bring me down."
    ##scene bg room #show black scene -- addin later
    hide adam neutral
    scene bg apartment1
    play sound wood volume 0.2
    pause (2)
    ##with fade
    show leon neutral
    with fade
    l "Damn boy. What took you so long?"

    show adam talking at right
    a "Shut up."
    show adam neutral

    show leon angry
    show mom upset at left
    lm "Hey!"

    l "Listen here boy.{p}You don't get to talk to me like that.{p}You know what I do to little boys who don't act how they're suppose to?"
    l "You don't even have a job you can't walk in here all tall and might thinking you own the place."

    show adam angry
    a "Leon, you don't even have a job!{p}You don't even live here!{p}You're just free loading off of us!"
    hide adam
    hide leon
    hide mom

    play sound punch volume 0.2
    show bg apartment1 with vpunch

    show adam neutral at right
    a "Ouch..."

    show mom neutral at left
    mom "Leon. You didn't have to hit him!{p}Adam apologize now."

    show adam talking
    a "Why do I need to apologize?{p}He's not even my dad. He's just a deadbeat guy with no job..."
    show adam neutral

    show leon angry
    l "Boy, you better stop talking or else you'll have something else coming for you."

    show adam talking
    a "You know what I'm leaving. I don't need to deal with this right now."
    hide adam

    mom "Why are you always so hard on him?"
    l "That boy needs to learn some manners.{p}Damn kids these days....{p}Is breakfast ready?"

    # This ends the game.
    return
