define nisb = Character("NISB Worker")
define bw = Character("Bank Worker")
define bm = Character("Bank Manager")

# The game starts here.

label a2s2:

    #play lobby music
    play music badSequential

    #transition to the nisb office
    scene bg office
    with fade

    show nisb
    nisb "Hello there, due to security you must have an appointment to enter the premises."

    show adam talking at left
    a "Hi, my name is Finn and no. I would like to speak to someone in charge of the county's network security here."
    show adam neutral

    a "** I think I am wanted but I want to make sure I don't get caught before I get to the bottom of this. **"

    nisb "I don't think I can squeeze you in for someone like that. What would be the purpose?"

    show adam talking
    a "I'm not at liberty to say but a friend of mine told me about some security flaws for some places in the area and they found something interesting."
    show adam neutral

    nisb "And that is?"

    show adam talking
    a "A money laundering front for a criminal organizaion that is terrorizing our city. Haha..."
    show adam neutral

    nisb "Are you joking? We take these kind of things very seriously."

    show adam talking
    a "I'm not! I even have the name of the bank that might be in trouble. Melrose Bank."
    show adam neutral

    nisb "Melrose Bank? Why does that sound so familiar. "

    nisb "That isn't too far from here. Maybe I can stop by. Let me log this in but you're coming with me. "

    nisb "If I found out you are kidding around, I don't think calling your parents will help you at this point."

    show adam talking
    a "I swear I'm not. My friend is a good computer whiz and he's working onn a computer projcet that requires mapping out different netweork routes of our city."
    a "He's sort of building a network map similar to our subway system."
    show adam neutral

    nisb "Is that so? Sounds like a smart kid. Well let's get going, my car is over there."

    #hide people
    scene bg bank
    with fade

    #show bank worker, nisb and Adam
    show banker at right
    bw "Hello there, is there anything I can help you with?"
    show nisb
    show adam neutral at left
    nisb "Yes, is it okay if I can speak to your manager, as well as someone who helps run your IT department here?"

    bw "For any particular reason?"

    nisb "Excuse me, I'm from the NISB and I'm here to make sure everything is up to code here. I'm not here to see client information, I'm just making sure that everything is all connected and running smoothly."

    nisb "Have you experienced anything weird lately?"

    bw "Not to my knowledge, no. But excuse me while I fetch them."
    hide banker

    a "**I wonder if my dad was working with NISB before. Internet police sounds really cool.**"

    #sounds of door opening
    #enter new characters
    "A figure approaches."

    show gabriel neutral at right
    "???" "So you must be the kid that's inquiring about this bank. Allow me to introduce myself. My name is Gabriel Andrews."

    nisb "Ahh sir, what brings you out here?"

    ga "I saw the inquiry report and I decided to take over. Actually, I worked with this bank to get them connected so I figured I would come by and take over since I'm familiar with their infrastructure."

    ga "So officially, I am here to relieve you from your duty. I can take it from here with the kid."

    nisb "Ah thank you sir. I already asked for their manager and their IT department but I will make a note of this as soon as I get to the office."

    ga "You're doing fine work, and thanks for filling out the report."

    hide nisb
    "The NISB Worker leaves."
    show gabriel at center
    ga "Excuse me, are you the manager?"

    show bankMan at right
    bm "Yes, I was told someone needed me and th-.."

    ga "Sorry to cut you off, but we figured out what happened and it looked like a clerical error on our end. I am sorry to have bothered you."

    ga "Come now, we have to get you back to the office so you can finish your report, son."
    hide bankMan

    show adam talking
    a "Hey what are you doing? Shouldn't we ask them some questions? And I don't have a report to do."
    show adam neutral

    ga "Are you the one my office has been trying to locate?"

    ga "Adam right? But if I recall correctly the report mentioned a Finn. But I believe they already have been to Finn's house."

    ga "What are you up to?"

    show adam talking
    a "I'm not up to anything. I just wanted to explain to them about their weak security.."
    show adam neutral

    ga "And? That can't be all."

    show adam talking
    a "I don't know what you are talking about, but my friend told me this bank is a front for a criminal organization."
    show adam neutral

    ga "That can't be true, but I will make note of that in my report."

    ga "Listen here, Finn. Let me do my work and I will report any findings regarding a criminal network here. I am good at my job Finn, or whoever you are."

    ga "The network is a complex place and can be dangerous. No matter what happens out there, it can always be traced. And if there are traces of criminal activity here I will find it."

    ga "Now run along home and I will deal with this."

    hide gabriel
    with dissolve
    "Gabriel walks away."

    a "**There's something about him that I can't shake.**"

    a "**He has a menacing aura around him and he just came out of nowhere. What's more is he didn't want to complete the inquiry.**"

    a "**What is his plan?**"

    "..."

    a "**Why is he shaking everyone's hand here?**"

    a "**Wait a minute. What is that near his sleeve?**"

    a "**I can't believe it! It looks like a tongue of a snake. There's no way. A coincidental tattoo? I don't think so.**"

    a "**Who is this Gabriel Andrews really? I wonder how thick the NISB network really is.**"

    return
