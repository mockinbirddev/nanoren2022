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
    ##scene busScene

    ##show Finn -- add in later
    f "Adam.{p}
    Hey Adam?{p}
    Hello?"

    ##show MC -- add in later
    a "Ahh.{p}
    Sorry. I have a lot on my mind."
    f "Looks like your mom's boyfriend is still over?"
    a "Yeah and I don't think anything is ever going to change."
    f "Why do you say that?{p}
    We're practically almost done with high school and we can do whatever we want after that.
    You can finally get your own place!"
    a "You do realize I don't have a job right?{p}
    Even if I did, I don't know where I would go. Las Rosa isn't a place where we can just walk down the street and just get a place.{p}
    I wouldn't even know where to begin."
    f "I bet the skills your dad taught you should do good.{p}
    Didn't he say computers and the digital world is going to be the future?{p}
    Something about the World Wide Web taking off."
    a "Yeah he did say something like that right."
    f "Look. I know you miss hima nd it's something that a lot of people will go through but it's time like these you know he's waiting for you to make your leap into the real world right.{p}
    I mean he wouldn't teach you all these things if they didn't mean anything to him.{p}
    He taught you for a purpose."
    a "Yeah. Yeah.{p}
    But you know how it is at school. Everyone who is anyone is always judging nad you know I'm always the only person in the computer lab."
    f "Yeah well foget them.{p}
    It's our last semester don't worry too much about it."

    "*short silence*"
    f "You haven't been thinking that again...{p}
    Have you ever since.."

    a "No, I'm fine you konw that."
    f "I'm not a doctor you know.{p}
    I only believe what you tell me and you know I know ehere you're lying right?"
    a "Then become a doctor."

    ##scene classroom -- addin later
    ##with fade

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
    t "Everybody take your seats.{p}
    We will begin from page 37 tofay so pelase take out your text books."

    ##show mc -- addin later
    a "I can't tell you when I began thinking like this.{p}
    I guess it was probably around the time I found out my dad died.{p}
    I never been this apathetic but ever since then life hasn't been that good to me.{p}
    Maybe someone would call this depression but I'm well aware of how I am feeling.{p}
    I haven't been focusing a lot at school lately and all i wanna do is keep exploring the world from my computer.{p}
    My dad said this holds the key to finding the answers I am looking for.But what am I loking for?"
    ##with hpunch for right and left -- apparently this shakes the screen?
    ##stop music
    ##play sound intenseMusic.mp3?
    t "Adam, are you going to answer the question?"
    a "What question?"

    ##play sound laughingSound.mp3
    t "Adam, if you're not going to pay
    attention how are you going to
    graduate? Do you even know what
    the real world is going to do you
    if you're not prepared?"
    a "I don't think knowing the story of
    Tom Sawyer will get me far in
    life."
    a "I don't remember hearing you
    asking me a question though."
    t "I am appalled. How did you manage
    to get this far?"
    a "Wow. Why is it that everyone is
    out to get me?"

    ##show finn -- addin later
    f "Hey Adam. You shoudl stay quiet."
    a "I don't need to know how this
    story ends or what the moral is. I
    don't find this important so why
    don't you get off my case!"

    t "That's it! Get out. I don't need your insubordination in my
    classroom. Get out now!"
    a "Fine. I don't need this. I don't
    need anyone here."
    ##exit MC?

    ##scene blackScene -- add later
    ##play sound laughing.mp3
    f "Adam, we're almost done. What are
    you doing."




    # This ends the game.
    return
