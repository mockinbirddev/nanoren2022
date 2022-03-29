# The game starts here.

label a2s1:
    play music tetheredFate
    "...Typing"
    play sound typing volume 0.2

    a "What's going on?"

    a "It's only been 20 minutes and it looks like they're trying to get in."

    a "Thankfully, I have set up a nice firewall protection and my IP is bouncing off different radio towers in the area."

    a "The odds of them finding my exact location are very low and from what I'm told only a handful of people in the world has the necessary skills."

    a "My dad was one of them."

    a "There was a reason why the government employed him."

    a "I need to retrace my steps and make sure everything I have done up till now has been secured."


    scene bg apartment2
    with fade

    show adam neutral
    with dissolve

    # These display lines of dialogue.

    a "Where should I begin and what are they referring to?"

    a "Are they talking about changing my grades?"

    a "Why would an outsider care about that?"

    a "Unless it's someone from the school who works as their IT security, or maybe the school district."

    a "I don't think the school would be that upset with me for exposing flaws so basic that even a grade schooler could point out."

    a "Wait a minute... I did hack into a bank"

    a "Both to be exact."

    a "Let me set up a quick protection protocol to make sure I'm safe to look away from here."

    a "A second monitor would be very useful here but I'll work with what I've got."

    a "I might have a 5 minute window before they try to get back in again."

    a "So let's make sure my bank looks secure."

    a "Nothing has changed from my account except for the money that I sent myself."

    a "The technology here was a little bit difficult, but it helps when you're already a customer with them."

    a "Now Melrose Bank, that was something new that I haven't hacked before."

    a "Their technology was all over the place and their security is out of place."

    a "It was like they left the back door wide open."

    a "The accounts here are very strange. Aside form the money I took, they all have the same amount of money going into them."

    a "They're showing the same balance."

    a "Let me look into their accounts."

    a "One customer here just takes out and puts in $2000 every week... and same with this account."

    a "What is this?"

    a "Let me see who owns these accounts."

    "..."

    a "They're all owned by different people of course, but what's strange is that the names don't sound like names."

    a "They look like they are all names of different types of snakes."

    a "I see Viper here, another named Garter, and another named Vine."

    a "There is a chance, but I'm pretty sure this isn't a coincidence."

    a "Now, looking back at the transactions it looks like they're going to and from different businesses."

    a "But something about these businesses sounds familiar..."

    a "Let me do a quick search here."

    "..."

    a "That's right!!"

    a "These businesses were rumored to be fronts for a crime syndicate that operates out of downtown, but that can't be right. Can it?"

    a "I think it's time to go back."

    a "Let me see the damage done."

    a "I guess they were able to trace the money back to my account.. but I thought I made it where that transaction was undetectable."

    a "Look like they're still pushing through."

    a "I guess I'll unplug the cord here and hopefully that will get them off my back."

    show bg apartment2 with vpunch

    a "I need to call Finn. I should tell him what's going on."

    play sound phone volume 0.2
    "*ring ring ring*"
    pause 3
    stop sound

    show finn talking at left
    f "Hello?"
    show finn neutral

    show adam talking
    a "Hey Finn. It's me, you wouldn't belie---"
    show adam neutral

    show finn talking
    f "Dude what happened? Why did you freak out like that earlier?"
    show finn neutral

    show adam talking
    a "Earlier at school? Man, you know I couldn't deal with that."
    show adam neutral

    show finn talking
    f "You were changing your grades!"
    show finn neutral

    show adam talking
    a "What's the big deal?"
    show adam neutral

    show finn talking
    f "What's the big deal? The big deal is that the police and some NISB officers came to my house looking for you!"
    show finn neutral

    show adam talking
    a "What?"
    a "The police and the National Investigation and Security Bureau came looking for me?"
    a "What do you mean \"came looking for me?\""
    show adam neutral

    show finn talking
    f "Yeah man, I guess changing grades is considered a serious federal crime or something. They said you weren't home, so where are you?"
    show finn neutral

    a "* I'm pretty sure they were there about the bank transactions... *"

    show adam talking
    a "Actually, about that. I got my own place not too far from home. It's pretty affordable."
    show adam neutral

    show finn talking
    f "What did you say? Your own place?"
    f "Adam, you need to call your mom or someone. The police aren't playing around. What if you go to jail??"
    show finn neutral

    show adam talking
    a "You're right. I wasn't really thinking about that.. "
    a "Don't worry, let me figure something out."
    show adam neutral

    show finn talking
    f "You're like my bestest friend. You better not make me visit you in prison."
    show finn neutral

    show adam talking
    a "Got it. Let me call my mom and see what's going on."
    show adam neutral

    hide finn
    #click sound for phone hang up
    "*click*"

    a "*But first, there's something I gotta do."

    # This ends the game.

    return
