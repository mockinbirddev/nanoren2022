# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 =Character("Classmate A")
define c2 =Character("Classmate B")
define c3 =Character("Classmate C")
define c12 = Character("Classmate A and B")
define t =Character("Teacher")

# The game starts here.

label a1s2:
    ##play sound somberMusic.mp3 -- add in later
    ##with fade
    scene bg busStop

    show finn talking
    f "Adam.{p}Hey Adam?{p}Hello?"
    show finn neutral

    show adam talking at right
    a "Ahh.{p}Sorry. I have a lot on my mind."
    show adam neutral

    show finn talking
    f "Looks like your mom's boyfriend is still over?"
    show finn neutral

    show adam talking
    a "Yeah and I don't think anything is ever going to change."
    show adam neutral

    show finn talking
    f "Why do you say that?{p}We're practically almost done with high school and we can do whatever we want after that."
    f "You can finally get your own place!"
    show finn neutral

    show adam talking
    a "You do realize I don't have a job right?{p}Even if I did, I don't know where I would go. Las Rosa isn't a place where we can just walk down the street and just get a place."
    a "I wouldn't even know where to begin."
    show adam neutral

    show finn talking
    f "I bet the skills your dad taught you should do good.{p}
    Didn't he say computers and the digital world is going to be the future?{p}
    Something about the World Wide Web taking off."
    show finn neutral

    show adam talking
    a "Yeah he did say something like that right."
    show adam neutral

    show finn talking
    f "Look, I know you miss him and it's not something that a lot of people will go through, but it's time like these you know he's waiting for you to make your leap into the real world right."
    f "I mean he wouldn't teach you all these things if they didn't mean anything to him.{p}
    He taught you for a purpose."
    show finn neutral

    show adam talking
    a "Yeah. Yeah."
    a "But you know how it is at school. Everyone who is anyone is always judging and you know I'm always the only person in the computer lab."
    show adam neutral

    show finn talking
    f "Yeah well foget them.{p}
    It's our last semester, don't worry too much about it."
    show finn neutral

    "*short silence*"

    show finn talking
    f "You haven't been thinking... that again...{p}
    Have you ever since.."
    show finn neutral

    show adam talking
    a "No, I'm fine you know that."
    show adam neutral

    show finn talking
    f "I'm not a doctor you know.{p}
    I only believe what you tell me and you know I know when you're lying right?"
    show finn neutral

    show adam talking
    a "Then become a doctor."
    show adam neutral

    hide finn
    hide adam

    scene bg classroom
    with fade

    c1 "Did you guys see the new episode last night?"
    c2 "Oh my gosh. No. Did you see it?"
    c1 "No. Not yet, hopefully no one has and ruins it for everyone."
    c3 "The girl died."
    c12 "WHAT!"
    c1 "Why you have to be like that?{p}
    We haven't even seen it yet."
    c3 "Shouldn't have been talking about it."
    c2 "You're a jerk!"

    ##play sound bellRing.mp3 - add in later
    show teach neutral at right
    t "Everybody take your seats.{p}
    We will begin from page 37 today so please take out your textbooks."
    hide teach

    show adam neutral
    a "I can't tell you when I began thinking like this.{p}
    I guess it was probably around the time I found out my dad died.{p}
    I've never been this apathetic but ever since then life hasn't been that good to me."
    a "Maybe someone would call this depression but I'm well aware of how I am feeling.{p}
    I haven't been focusing a lot at school lately and all I wanna do is keep exploring the world from my computer."
    a "My dad said this holds the key to finding the answers I'm looking for. But what am I loking for?"

    ##with hpunch for right and left -- apparently this shakes the screen?
    ##stop music
    ##play sound intenseMusic.mp3?
    show teach neutral at right
    t "Adam, are you going to answer the question?"

    show adam talking
    a "What question?"
    show adam neutral

    ##play sound laughingSound.mp3
    t "Adam, if you're not going to pay attention how are you going to graduate?{p}Do you even know what the real world is going to do you if you're not prepared?"

    show adam talking
    a "I don't think knowing the story of
    Tom Sawyer will get me that far in
    life."
    a "I don't remember hearing you
    asking me a question though."
    show adam neutral

    t "I am appalled. How did you manage
    to get this far?"

    show adam talking
    a "Wow. Why is it that everyone is
    out to get me?"
    show adam neutral

    show finn talking at left
    f "Hey Adam. You should stay quiet."
    show finn neutral

    show adam angry
    a "I don't need to know how this
    story ends or what the moral is. I
    don't find this important so why
    don't you get off my case!"

    show teach angry
    t "That's it! Get out. I don't need your insubordination in my
    classroom. Get out now!"


    a "Fine. I don't need this. I don't need anyone here!"
    hide adam

    pause (1)

    hide teach
    hide finn
    scene black
    ##play sound laughing.mp3
    f "Adam, we're almost done. What are you doing."

    # This ends the game.
    return
