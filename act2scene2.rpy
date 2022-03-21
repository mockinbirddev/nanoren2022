define nisb = Character("NISB Worker")
define bw = Character("Bank Worker")
define bm = Character("Bank Manager")

# The game starts here.

label a2s2:

    #play lobby music

    #transition to the nisb office
    scene bgroom
    with fade

    nisb "Hello there, due to security you must have an appointment to enter the premises."

    a "Hi, my name is Finn and no. I would like to speak to someone in charge of the county's network security here."

    a "** I think I am wanted but I want to make sure I don't get caught before I get to the bottom of this. **"

    nisb "I don't think I can squeeze you in for someone like that. What would be the purpose?"

    a "I'm not at liberty to say but a friend of mine told me about some security flaws for some places in the area and they found something interesting."

    nisb "And that is?"

    a "A money laundering front for a criminal organizaion that is terrorizing our city. Haha..."

    nisb "Are you joking? We take these kind of things very seriously."

    a "I'm not! I even have the name of the bank that might be in trouble. Melrose Bank."

    nisb "Melrose Bank? Why does that sound so familiar. "

    nisb "That isn't too far from here. Maybe I can stop by. Let me log this in but you're coming with me. "

    nisb "If I found out you are kidding around, I don't think calling your parents will help you at this point."

    a "I swear I'm not. My friend is a good computer whiz and he's working onn a computer projcet that requires mapping out different netweork routes of our city."

    a "He's sort of building a network map similar to our subway system."

    nisb "Is that so? Sounds like a smart kid. Well let's get going, my car is over there."

    #hide people
    #load bank scene

    #show bank worker, nisb and Adam

    bw "Hello there, is there anything I can help you with?"

    nisb "Yes, is it okay if I can speak to your manager, as well as someone who helps run your IT department here?"

    bw "For any particular reason?"

    nisb "Excuse me, I'm from the NISB and I'm here to make sure everything is up to code here. I'm not here to see client information, I'm just making sure that everything is all connected and running smoothly."

    nisb "Have you experienced anything weird lately?"

    bw "Not to my knowledge, no. But excuse me while I fetch them."

    a "**I wonder if my dad was working with NISB before. Internet police sounds really cool.**"

    #sounds of door opening
    #enter new characters
    "A figure approaches."

    "???" "So you must be the kid that's inquiring about this bank. Allow me to introduce myself. My name is Gabriel Andrews."

    nisb "Ahh sir, what brings you out here?"

    g "I saw the inquiry report and I decided to take over. Actually, I worked with this bank to get them connected so I figured I would come by and take over since I'm familiar with their infrastructure."

    g "So officially, I am here to relieve you from your duty. I can take it from here with the kid."

    nisb "Ah thank you sir. I already asked for their manager and their IT department but I will make a note of this as soon as I get to the office."

    g "You're doing fine work, and thanks for filling out the report."

    #hide NISB
    "The NISB Worker leaves."

    g "Excuse me, are you the manager?"

    bm "Yes, I was told someone needed me and th-.."

    g "Sorry to cut you off, but we figured out what happened and it looked like a clerical error on our end. I am sorry to have bothered you."

    g "Come now, we have to get you back to the office so you can finish your report, son."

    a "Hey what are you doing? Shouldn't we ask them some questions? And I don't have a report to do."

    g "Are you the one my office has been trying to locate?"

    g "Adam right? But if I recall correctly the report mentioned a Finn. But I believe they already have been to Finn's house."

    g "What are you up to?"

    a "I'm not up to anything. I just wanted to explain to them about their weak security.."

    g "And? That can't be all."

    a "I don't know what you are talking about, but my friend told me this bank is a front for a criminal organization."

    g "That can't be true, but I will make note of that in my report."

    g "Listen here, Finn. Let me do my work and I will report any findings regarding a criminal network here. I am good at my job Finn, or whoever you are."

    g "The network is a complex place and can be dangerous. No matter what happens out there, it can always be traced. And if there are traces of criminal activity here I will find it."

    g "Now run along home and I will deal with this."

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
