define e = Character("Crystal")
define p = Character("You")

image title_video = Movie(play="images/Title.webm", loop=True)

transform zoom_out:
    zoom 0.8
    xalign 0.5
    yalign 0.5
transform zoom_in: 
    zoom 3.0
    xalign 0.5 
    yalign 0.5
transform zoom_more: 
    zoom 4.0
    xalign 0.5 
    yalign 0.5

image Sadaura_video = Movie(play="images/SadAura.webm", loop=True)
image FishShirt = "images/FishShirt.jpg"
image CatShirt = "images/CatShirt.jpg"
image Hoodie = "images/Hoodie.jpg"

#BACKGROUNDS
image intropage = "images/Intro.jpg"
image entercrystal = "images/Crystal.jpg"
image enteryou = "images/You.jpg"
image Chat1 = "images/Dumplings.jpg"
image Final = "images/Final.jpg"
image 4thChat = "images/4thChat.jpg"
image 3rdChat = "images/Chat3.jpg"
image Chat2 = "images/2ndChat.jpg"
image FloralDress = "images/FloralDress.jpg"

init python:
    style.unread_text = Style(style.default)
    style.unread_text.size = 100
    style.unread_text.color = "#370a0a"
    style.unread_text.outlines = [(2, "#000000", 0, 0)]

# Variables
default tone = "neutral"
default chats_saved = 0


label start:

    scene black
    
    play music "audio/Hardtimes.mp3" fadein 1.0

    show title_video at zoom_out
    with dissolve

    show expression Text("UNREAD", style="unread_text") at truecenter
    with dissolve

    pause 6

    hide expression Text("UNREAD", style="unread_text")
    hide title_video

    scene black
    with fade
    jump intro 

label intro:
    
    scene intropage at zoom_more
    with fade 
    pause 1.0 
    "There are messages you don't forget."
    pause 1.5 
    "Not because they mattered but because you keep wondering what would have happened if they were different. "
    pause 2.0 
    "You tell yourself a different word, tone, or moment could have changed everything."
    pause 1.5 
    "Maybe it could have."
    pause 1.0 
    "Or maybe....."
    pause 1.5 
    "It was always going to end this way."
    pause 2.5 
    scene black 
    with dissolve 
    scene entercrystal at zoom_in
    with fade 
    "Crystal."
    pause 1.0 
    "She was easy to talk to."
    pause 1.0 
    "At least, at first."
    pause 1.5
    scene enteryou at zoom_in
    "You."
    pause 1.0 
    "You learned how to say the right things."
    pause 1.5

    "Even when they weren’t yours."

    pause 2.0

    "This is not a story about what went wrong."

    pause 1.5

    "It’s about when it started to."

    pause 2.5

    "And everything that was left…"

    pause 1.5

    "unread."

    pause 3.0
    stop music fadeout 2.0
    

    jump chat_1
    


# -------------------------
# CHAT 1
# -------------------------
label chat_1:
    scene Chat1 at zoom_more
    with dissolve
    play music "audio/Televangelism.mp3" fadein 1.0
    "March 3rd, 11:42 PM"
    show FishShirt:
        zoom 1.5
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.1

    e "Hey, are you still up?"
    p "Yeah :) what's up?"
    e "I just got back, went to that dumpling place on 5th with my mom."
    p "Oh yeah? Was it good?"
    e "It was okay. You would not have liked it LOL, pretty spicy. The vibe also just wasn't really cute. People were being so loud and obnoxious."
    pause 0.5
    e "You would have been complaining about it the whole time."
    menu: 
        "How do you respond?"
        "Play along":
            $ tone = "warm"
            p "LOL yea, I would have gotten up and left halfway through."
        "Get defensive":
            $ tone = "cold"
            p "I would have been fine, I am not that picky."
        "Brush it off":
            $ tone = "neutral"
            p "Cool"
    e "Hm"
    pause 0.5
    e "I dont know, I just feel like you don't do that anymore."
    p "Do what?"
    e "Have opinions"
    pause 1.0 
    e "You just kind of go along with whatever I say now."
    stop music fadeout 2.0

    jump chat_saved_1


# -------------------------
# CHAT SAVED 1
# -------------------------
label chat_saved_1:

    $ chats_saved += 1

    scene black
    with fade

    centered "Chat saved."

    pause 1.5

    jump chat_2


# -------------------------
# CHAT 2
# -------------------------
label chat_2:
    scene Chat2 at zoom_more
    with dissolve
    "March 8th, 12:10 AM"
    play music "audio/EthelStrangers.mp3" fadein 1.0

    
    show CatShirt:
        zoom 1.5
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.1

    e "Can i ask you something?"
    p "Yeah"
    e "Why did you say you liked the movie?"
    p "What do you mean?"
    e "You told me you loved it, but when I asked what your favorite part was, you just said 'the ending'"
    pause 0.5
    e "I don't get it. You obviously did not like that movie...."


    pause 0.5
    menu:
        "Your response:"
        "Admit it":
            p "I didn't want to ruin it for you."
        "Defend":
            p "I did like it, I just don't have a favorite part."
        "Avoid":
            p "You're reading too much into it."
    e "I'm not trying to catch you in a lie, I just want to understand you better."
    if tone == "warm":
        e "It just feels like you're trying really hard to match me."
    elif tone == "neutral":
        e "I just don't know what you actually think anymore."
    else: 
        e "It doesn't feel honest."
    pause 0.5 

    e "Like... when we first met, you argued with me about everything. You had your own opinions, and I loved that about you. We were always actively getting to know one another. "
    pause 1.0 
    e "Now it's just easy."
    e "not in a good way."
    stop music fadeout 2.0
    jump chat_saved_2


# -------------------------
# CHAT SAVED 2
# -------------------------
label chat_saved_2:

    $ chats_saved += 1

    scene black
    with fade

    centered "Chat saved."

    pause 1.5

    jump chat_3

# -------------------------
# CHAT 3
# -------------------------
label chat_3:
    scene 3rdChat at zoom_in 
    play music "audio/FamilyTree.mp3" fadein 1.0
    "March 11th, 11:27 PM"
    show FloralDress:
        xalign 0.5 
        yalign 0.5
        zoom 3.0
    e "Sorry I didn't text for a bit."
    p "It's okay."
    e "I was out with some people from class."
    p "Oh nice :)"
    pause 0.5 
    e "Yea"
    pause 1.0 
    e "You would've liked them."
    menu: 
        "Your response:"
        "Show interest":
            p "Yea? What were they like?"
        "Be neutral":
            p "Cool"
        "Withdraw":
            p "You don't know that."
    e "I dont know, they just felt really easy to talk to...."
    pause 1.0 
    e "Like I didn't have to to think about what I was saying"
    pause 0.5 
    e "or how it would land."
    if tone == "warm":
        p "You dont' have to do that with me."
        e "I know but it still feels like I do sometimes"
    elif tone == "neutral":
        p "I mean that's pretty normal."
        e "Maybe"
        e "I don't know"
    else: 
        p "So I guess you just feel really uncomfortable with me them."
        e "That's not what I meant"
    pause 1.0 
    e "I just feel like something changed"
    e "and I can't tell when it did."
    stop music fadeout 2.0
    jump chat_saved_3

# -------------------------
# CHAT SAVED 3
# -------------------------
label chat_saved_3:

    $ chats_saved += 1

    scene black
    with fade

    centered "Chat saved."

    pause 1.5

    jump chat_4



# -------------------------
# CHAT 4
# -------------------------
label chat_4:
    scene 4thChat at zoom_more
    play music "audio/WesternNights.mp3" fadein 1.0

    "March 14th, 1:03 AM"
    show Hoodie:
        zoom 1.5
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.1

    e "This is what i mean......"
    e "earlier today......"
    e "I said I was stressed about my presentation and you said 'you'll do great'"
    p "Yeah because you will????"
    e "That's not the point."
    pause 0.5 
    e "You didn't even ask what it was about bruh"
    e "or why I was even stressed."
    pause 0.5 
    menu:
        "Your response:"

        "Try to explain":
            p "I didn’t know what else to say. I thought it would help."
        "Get frustrated":
            p "What do you want from me?"
        "Pull away":
            p "I was just trying to be supportive"

    e "I don't want the right response. I want a real one. I want to know that you care enough to actually listen to me and understand what I am going through. I want to have real conversations with you, not just surface level ones where you say what you think I want to hear."
    pause 1.0 
    e "It feels like I am talking to someone who is trying to pass a test"
    if tone == "cold":
        e "and honestly it's really exhausting."
    else: 
        e "and it makes me feel really alone."
    stop music fadeout 2.0

    jump chat_saved_4


# -------------------------
# CHAT SAVED 4
# -------------------------
label chat_saved_4:

    $ chats_saved += 1

    scene black
    with fade

    centered "Chat saved."

    pause 1.5

    jump final_chat



# -------------------------
# FINAL CHAT
# -------------------------
label final_chat:
    scene Final at zoom_more
    play music "audio/HouseInNebraska.mp3" fadein 1.0
    show FishShirt:
        zoom 1.5
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.1

    e "I’ve been thinking about this for a while"

    pause 1.0

    e "I don’t think this is working"

    p "What?"

    e "I don’t know who you are when you’re talking to me"

    e "and i don’t think you do either"

    pause 1.5

    "You start typing a message."

    "You stop."

    "You delete it."

    "You try again."

    menu:
        "Final message:"

        "Be honest":
            p "I thought if I was easier to love you’d stay"
        "Hold back":
            p "I didn’t know what you wanted me to be"
        "Say nothing":
            pass

    pause 1.0

    e "…"

    e "That’s the first real thing you’ve said in a while"

    pause 1.5

    e "I just wish it didn’t come this late"

    "Message read."

    pause 2.0

    "No reply."

    scene black
    with fade

    if chats_saved == 4:
        "5 chats saved."
    else:
        "Chats saved."

    "Chat archived."
    

    return