define hw = Character("Helpful NISB Worker")
label a2s4:

    scene bg park
    with fade

    play music badSequential

    show adam neutral
    a "*panting*"

    a "**Okay, so where is this bench...**"

    a "**Ah, it's gotta be that one. Alright, got the backpack too.**"

    a "**Strange that there isn't anyone around. What a weird park. But let's get this backpack open.**"

    a "**Here is the laptop. Okay, Cleo told me to open this and they will do the rest. Let's boot it up.**"

    a "**Ah, a message already.**"

    show cleo at right
    c "Okay, no questions so just pay attention. This laptop is connceted via a satellite card so you're able to communicate with me."

    c "Right now, I have an associate taking picutres of the NISB raiding your apartment."

    #show pictures

    c "Nice place, I suppose, but he just reported that he did see The Snake."

    show adam talking
    a "Can you tell me what's going on?"
    show adam neutral

    c "My network has been trying to figure out how The Snake was involved but it looks like you did the groundwork for us."

    c "We didn't think it was someone form the NISB. The next part is going to be hard, but my contact at the NISB will be able to help you."

    show adam talking
    a "Wait, what?"
    show adam neutral

    c "You're going to go back to the NISB as a witness because we are going to take down The Snake as well as uncover his plans with the I-504 and his involvement with the Triads here."

    show adam talking
    a "The Snake is working with the Triads? So he is money laundering for them and making sure it stays safe?"
    show adam neutral

    c "That is the gist of it. And with your help I can report my findings with my contact at the NISB and we can finally nail this guy once are all."

    c "For the record, he wasn't going to arrest you. Most likely, he was going to toss you to the Triads."

    c "From what I was told, there were moles in the NISB and undercover agents working along side him which you can say have disappeared."

    c "I didn't think Gabriel Andrews would be the one, but now that we're onto him, we can do this."

    show adam talking
    a "What are my next steps so that I don't die? I'm only in highschool dammit!"
    show adam neutral

    c "Don't worry. My contact at the NISB office knows you are coming. I have arranged for a car to come pick you up. It should be arriving shortly."

    c "Since knowing The Snake is actually Gabriel Andrews, I have an associate following him, especially because something was triggered at the NISB office and I was notified."

    c "I didn't think it was a coincidence but we have pictures of him associating with high level Triad members, and now the cyber attack on you."

    c "Don't worry. We'll get him. I'll contact you soon."
    hide cleo

    #honk Sounds
    play sound honk volume 0.2

    "*car honk*"

    a "**Wow. I guess this is it.**"

    a "**Who is this Cleo person? Another mystery I'll have to figure out as soon as I get out of this mess.**"

    scene bg bank
    with fade
    show adam neutral at left

    a "**Looks like no one recognized me yet. Maybe they don't have a picture. I should be safe.**"

    a "**I need to get to the front desk or maybe I should just wait in the lobby.**"

    show helpNISB
    hw "You must be Adam. Don't look so shocked. A mutual friend of ours sent me here."

    show adam talking
    a "Ahh. Hi. I'm not sure what I can do."
    show adam neutral

    hw "Don't worry. As long as you have this laptop, everything will be fine. "

    hw "Though I may be a regular worker here, Cleo's family has strong influence here. Nothing will fall under the cracks now."

    menu:
        hw "Are you ready?"

        "Yes" :
            show adam talking
            a "Yeah, I guess. What are we doing?"
            show adam neutral

        "No" :
            show adam talking
            a "No, I think I'll go home actually."
            show adam neutral
            hw "Hah, funny. Let's get started."
            show adam talking
            a "Fine.. What are we doing?"
            show adam neutral

    hw "Not just us, but in a few seconds the police will arrive to arrest Gabriel Andrews."

    show adam talking
    a "Wait, are you kidding?"
    show adam neutral


    hw "Look, the police are arriving now."


    play sound siren
    pause 2

    play sound running

    show gabriel evil at right
    ga "Wait, what are you doing? Why are you coming at me?"

    ga "No, it can't be. You won't get away with this kid."

    hide gabriel
    hide adam
    hide helpNISB
    scene black
    play sound fanfare volume 0.2

    a "**And just like that, the NISB officers asked me for the laptop that I was carrying and just as Cleo said, it helped.**"

    a "**Everything to incriminate The Snake was there. It also helped that a lawyer was there to represent both of us.**"

    a "**The NISB worker that helped me was an undercover agent planted by the CIA to investigate in-house crimes and look into The Snake.**"

    a "**I helped take down a crime lord and a master hack within these last couple of days, and I have to tell you, I am tired.**"

    a "**I don't need this. I don't know how it all happened but everything was connected.**"

    a "**It felt like I was in a movie. A scripted scene. Whatever Cleo said and the timing of it all worker out so well. **"

    a "**I never did get the chance to ask the agent how they knew Cleo or who they even are.**"

    scene bg apartment2

    "...typing"
    play sound typing volume 0.2

    "*email ding*"
    play sound beep

    show adam neutral

    a "**Looks like I got an email.**"

    a "**Cleo, huh. Let's see what it says.**"

    a "**\"Good thing you trusted me. But you did good work for an amateur. I see some potential in you, but for now you should focus on graduating.\"**"

    a "**\"When you do, send me a message. We can do some work together. I could use someone like you in my Network. We'll talk soon. -Cleo\"**"

    a "**\"PS, I moved all the money back from your account before the police found out. Don't worry, the apartment is paid for until you begin work with me.\"**"

    a "**Work with Cleo huh? I hope it's a paid position.**"

    a "**Wait, what! I'm not a millionaire anymore? I was hoping I could get away with that..**"

    a "**Oh well, at least it looks like everything will go back to normal. I-504 went into hiding now that Cleo is tracking them, so no more cyber attacks for me.**"

    a "**But there is one more thing I should do...**"

    play sound phone volume 0.2
    pause 5

    "???" "Hello?"

    show adam talking
    a "Hey mom."
    show adam neutral

    scene black with dissolve
    pause (2)
    "Thank you for playing..."
    "Echoes that Sing was written by DJKNITEX and developed by the mockinbird.dev team for nanoren 2022"
    "The team consisted of.."
    "Jenna - Artist"
    "Mei - Background Artist"
    "Sawada14 - Main Coder"
    "Mendoxee - Coder"
    "oozy_q - Music"
    "Our credits for assets will be included in the README but we would like to offer quick thanks to:"
    "freepik for the title screen flower and "
    "the number of resources we gather from the Ren'py forums: Lemma soft Forums"
    "THE END"
    pause(2)

    return
