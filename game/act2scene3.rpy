define s = Character("The Snake")
# The game starts here.

label a2s3:
    play music tetheredFate volume 0.2
    #typing noises

    scene bg apartment2

    "...typing noises"
    play sound typing volume 0.2
    pause(2)

    show adam neutral
    a "**I booted up my computer and I enabled another layer of security before I begin my mission.**"

    a "**I haven't noticed anything attacking my computer but I did receive a ton of emails from \"I-504.\" All of them are saying the same thing: They're out to get me.**"

    a "**I don't think I've been exposed but it could just be a scare tactic. I can't focus on that right now; I need to find out what Gabriel's end game is.**"

    a "**The NISB security is air tight and I don't have anything remotely unique to them. I'm not a member nor do I work there. **"

    a "**So what are the next steps?**"

    a "**Come on dad, what would you do?**"

    a "**That's right! I can use their phone number to bypass one of their security measures. It's an old hacking trick from the 80's but I can still use it here.**"

    a "**Look! It worked, I'm in!**"

    a "**Almost that is... I'm at the front door, but now I need some sort of credentials or keywords.**"

    "..."

    a "**Gabriel Andrews. He has a lot of information about him. All good stuff too. So why is it he doesn't want to investigate this? Let me try Melrose bank.**"

    a "**Hmm, the other officer was right. It looks like they were already digging into this. Possible gang activity. Suspicious money. I'm suprised the bank is still here.**"

    a "**Let me try something else... I wonder what pops up if I just type in snake, a common keyword that I believe is related to the bank.**"

    a "**What is this? A gangster nicknamed The Snake?**"

    a "**Wanted for embezzlement and money laundering. It this a person or a crew? It really doesn't say.**"

    #screen shake
    show bg apartment2 with vpunch
    play sound punch volume 0.2

    a "**Wait what's going on? Is someone attacking me? Oh no, it better not be I-504 again. Wait a minute. What's with this name. I can't read it. Is it someone else?**"

    a "**Wait... The Snake?! The Snake is contacting me?**"

    show snake at left
    with dissolve
    s "Looks like you're still at this, but no worries. In just a few minutes I will expose your location and everything will be taken care of."

    show adam talking
    a "Who are you!? And what do you mean taken care of? I have skills that you've never seen before."
    show adam neutral

    s "You're good but you're not that good. Watch this. Though, I can't get your exact location now, I can do this. This isn't the pinnacle of my power, but I'm sure it will give you some idea of what I'm capable of."

    #screen shakes
    show bg apartment2 with vpunch

    a "**What's this? Is my computer frozen? No, I still see stuff happening. The terminal is running but I can't do anything.**"

    a "**Did he freeze what I could do? What I can do? I can just unplug my computer right? My detection doesn't see anything else happening. No connections, no viruses.**"

    "..pulls plug"

    a "**What's this?**"

    s "You can't escape from me, Lucious. Or should I say, Adam."

    s "You should have just went home and stuck your nose into some books."

    s "It's like I told you. No matter what is out there, it can always be traced back."

    a "**Wait a minute... It can't be him right. But from what he's saying it has to be. Gabriel Andrews. He's behind this?**"

    hide snake
    show gabriel evil at left
    s "You may have figured out who I am, but there is no way you are going to stop me. I worked too long to get this far and be stopped by a child."

    s "This money is rightfully mine, and I will continue earning as long as I am alive and well. The bad news is that I'm about to get to you so you won't be able to tell anyone a thing."

    s "Even if you could, who is going are they going to believe? Me, a high ranking officer at the NISB or you, a teenage high school student on the verge of failing out."

    s "If you left it laone and returned the money back we wouldn't have had any problems."

    s "But it's okay. I could have hacked the money back but I'm leaving it in there as evidence that you stole from the bank. Have a wonderful life Adam, I'll see you soon."
    hide gabriel

    a "**This is not good...**"

    show bg apartment2 with vpunch

    play sound beep volume 0.2

    a "**Another message? What is this? Cleo? God damnit, I don't have time for this. I need to get out of here.**"

    show cleo at right
    c "For someone who is blooming in the hacking world, you sure are causing a lot of fires here. Looks like your system is still on lock down so you can't reply."

    c "Don't worry about who I am. Just go to Hyde Park."

    c "I made it so they can't see my messages, and if they do it's translated 3 times and comes out as a nursery rhyme. I am working on a new encryption hidden chat and you are my test dummy."

    c "There's no more time. They are about to find your location. At the park there is a bench with a small backpack under it. An associate of mine will place a laptop there. Open it and I will contact you."

    c "Hurry."

    a "**Normally, I wouldn't trust anyone. Especially a random person messaging me when my computer is acting up. But for now, I just need to get out of here alive.**"

    return
