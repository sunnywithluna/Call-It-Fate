﻿
label epilogueScene:
    scene bg_room_a with dissolve
    play music "audio/event.mp3" fadein 1.0

    "It's been three weeks since my Intro to Philosophy class ended, and Dr. Paige is only now updating the final grades."
    "He sent out an email last night, saying they'd be posted at noon today, so I wait and watch the 11:59 AM on my computer turn into 12:00 PM and hit refresh on my student portal."

    if class_score >= 4 and study_counter >= 3:
        "I got an A+!"
        "I let out a sigh of relief."
    elif class_score >= 4:
        "I passed!"
        "I let out a sigh of relief."
    else:
        "I failed..."
        "I let out a tired sigh. I guess I'll just have to retake the class next year..."

    "A knock at my door pulls me away from my computer."
    scene bg_room_outside_a with dissolve

    if endingAFlag:
        jump epi_maddie
    if endingBFlag:
        jump epi_anna
    if endingCFlag:
        jump epi_erin


label epi_maddie:
    scene event_epi_a with dissolve
    "Standing outside is Maddie, holding up a large plastic bag in her hand."

    a "\"Ready for lunch?\""

    n "\"Oh, wow, you didn't have to do that.\""
    scene bg_room_outside_a with dissolve

    $ renpy.show(custom_show("maddie", "H"), []) 
    a "\"I know, I wanted to.\""

    "She walks in and starts pulling Styrofoam containers out of the bag."

    scene bg_room_a with dissolve
    n "\"Did you check your Philosophy grade yet?\""
    $ renpy.show(custom_show("maddie", "N"), []) 

    a "\"Nah, I'll look later. It's not like I can go back and change anything, might as well pay attention to what's ahead.\""

    n "\"And what's that?\""
    $ renpy.show(custom_show("maddie", "H"), []) 

    a "\"Sushi.\""

    "She holds up a container and chopsticks, taking a seat on the floor."

    n "\"You don't care how you did? We had to do a ton of work for that class. Don't you want to know if you passed?\""

    "Maddie looks off into the corner of the room as she chews, thinking."
    $ renpy.show(custom_show("maddie", "U"), []) 

    a "\"There's this quote I heard in Psych class, \'Until you make the unconscious conscious, it will direct your life and you will call it fate.\'\""

    n "\"What's that mean?\""
    $ renpy.show(custom_show("maddie", "F"), []) 

    a "\"I'm getting to that, Sam. Please.\""

    "She laughs, and I join her on the floor, grabbing chopsticks from the bag."
    $ renpy.show(custom_show("maddie", "H"), []) 

    a "\"If you don't make an honest effort to change the way you do things, you'll end up doing them the way you always do and blame some outside force like fate or God or whatever when you get a bad outcome.\""
    $ renpy.show(custom_show("maddie", "N"), []) 
    a "\"I worked really hard in that class. Probably harder than I have in any class this year. I could've done what I normally do, procrastinate and put in the minimum amount of work, but I decided to try.\""
    $ renpy.show(custom_show("maddie", "A"), []) 
    a "\"So, if I didn't pass, it's not because I didn't put the work in. I made the unconscious conscious. I took control.\""

    n "\"I don't get it then. Wouldn't you want to see if your hard work paid off?\""
    $ renpy.show(custom_show("maddie", "H"), []) 

    a "\"Today, I just want to celebrate that I worked hard at something I don't normally work hard at. I can worry about the grade later."
    $ renpy.show(custom_show("maddie", "F"), []) 
    a "\"Now hurry up before I eat all the food.\""

    "She kisses me on the cheek, and I pick up a roll from the Styrofoam box."
    $ renpy.hide(custom_hide("maddie"))

    "As we eat our lunch, I think on Maddie's words and all the ways I've tried to work on myself this summer."
    "I'm exercising more, eating better."
    "I'm trying to be more confident--even just telling Maddie how I feel was a huge step for me."

    "For a long time, I let my patterns control me."

    "I felt like the world was against me when, in reality, I had every ability to improve my life."

    "I don't want to let my unconscious direct my life or control my behavior."

    "I worked for the person I am. I worked for the relationship I have with Maddie."
    scene black with fade
    "And I won't call it fate."
    jump credits_1
    return


label epi_anna:

    $ renpy.show(custom_show("anna", "N"), [])

    "Standing outside is Anna, holding up a large plastic bag in her hand."

    $ renpy.show(custom_show("anna", "H"), [])

    b "\"I brought sushi.\""

    n "\"Oh, wow, you didn't have to do that.\""

    $ renpy.show(custom_show("anna", "E"), [])

    b "\"Did you already eat?\""
    $ renpy.show(custom_show("anna", "E2"), [])

    n "\"No, it's just--I didn't expect it.\""

    $ renpy.show(custom_show("anna", "F"), [])

    b "\"That's what makes it a surprise.\""

    "She walks in and starts pulling Styrofoam containers out of the bag."
    scene bg_room_a 
    with dissolve

    n "\"Did you check your Philosophy grade yet?\""

    $ renpy.show(custom_show("anna", "N"), [])
    $ renpy.with_statement(Dissolve(0.25))

    b "\"No.\""

    n "\"Really? I thought you'd want to know right away.\""

    $ renpy.show(custom_show("anna", "F"), [])

    b "\"I do. I want to know, but I always make myself wait a day after the grade's posted to check.\""

    n "\"Why?\""

    "She takes a seat on my bed, holding a take-out box and chopsticks."

    $ renpy.show(custom_show("anna", "U"), [])

    b "\"I used to have pretty bad study habits.\""

    n "\"I can't imagine that.\""
    $ renpy.show(custom_show("anna", "E"), [])

    b "\"Well, bad for me at least. I used to get mostly \'B\'s, a few \'C\'s.\""
    $ renpy.show(custom_show("anna", "E2"), [])

    "I gasp and she laughs as I sit next to her on the bed, grabbing chopsticks from the bag."
    $ renpy.show(custom_show("anna", "H"), [])

    b "\"Anyway, I knew I could do better.\""
    b "\"Then, I heard this Carl Jung quote, \'Until you make the unconscious conscious, it will direct your life and you will call it fate.\'\""
    b "\"You have to put in effort to resist bad habits, and if you do, you can improve your life. Otherwise, your habits will dictate everything.\""
    b "\"So that's when I started to make changes.\""
    $ renpy.show(custom_show("anna", "N"), [])
    b "\"When I got done with class, instead of procrastinating, I'd do my homework right away.\""
    b "\"If I had a test coming up, I'd schedule out times to study in advance. Do you get what I'm saying?\""

    n "\"I guess...? But I don't get why you'd wait to check your grade.\""
    $ renpy.show(custom_show("anna", "A"), [])

    b "\"That's one of the changes.\""
    b "\"I used to check my grades as soon as they were posted. But all that did was make me value the letter more than what I actually learned.\""
    $ renpy.show(custom_show("anna", "F"), [])

    b "\"I want to take the time to reflect on how much more I know now than I did before taking the class. Then, I can check my grade.\""

    n "\"You probably got an \'A\' though, right?\""
    $ renpy.show(custom_show("anna", "N"), [])

    b "\"Probably. Are you not hungry?\""

    "I kiss her on her forehead before picking up a roll from the Styrofoam box."
    $ renpy.hide(custom_hide("anna"))

    "As we eat our lunch, I think on Anna's words and all the ways I've tried to work on myself this summer."
    "I'm getting more organized and trying to learn something new every day."
    "I'm trying to be more confident--even just telling Anna how I feel was a huge step for me."

    "For a long time, I let my patterns control me."

    "I felt like the world was against me when, in reality, I had every ability to improve my life."

    "I don't want to let my unconscious direct my life or control my behavior."

    "I worked for the person I am. I worked for the relationship I have with Anna."
    scene black with fade

    "And I won't call it fate."

    jump credits_1
    return


label epi_erin:
    "Standing outside is Erin, holding up a large plastic bag in her hand."
    $ renpy.show(custom_show("erin", "N"), [])

    c "\"I thought I'd surprise you with lunch today.\""

    n "\"Wow! You didn't have to do that.\""

    c "\"I know, but I wanted to.\""

    "She walks in and starts pulling Styrofoam containers out of the bag."
    scene bg_room_a with dissolve

    n "\"Did you check your Philosophy grade yet?\""
    $ renpy.show(custom_show("erin", "surprised"), [])

    c "\"Are they posted?\""

    n "\"Yeah, Dr. Paige emailed us last night. You didn't see?\""

    "She shrugs before grabbing a container and chopsticks, taking a seat on the floor."
    $ renpy.show(custom_show("erin", "F"), [])

    c "\"I'll check later. I took the class and tried my best. So, I give myself an 'A+' for effort.\""
    n "\"Yeah, but don't you want to know…the actual grade?\""
    c "\"I don't think I have to be too worried. I finished my homework every night and studied even when I didn't feel like it. That's enough, right?\""
    c "\"There's this quote I heard once, \'Until you make the unconscious conscious, it will direct your life and you will call it fate.\'\""

    n "\"Make the unconscious conscious?\""
    "I join her on the floor, grabbing chopsticks from the bag."
    $ renpy.show(custom_show("erin", "N"), [])

    c "\"It means that you have to purposely change your patterns and behaviors if you want to improve.\""

    n "\"And you did that?\""
    $ renpy.show(custom_show("erin", "F"), [])

    c "\"I did. So, I can rest easy. Now, let's eat! I'm starving.\""

    "She kisses me on the cheek, and I pick up a roll from the Styrofoam box."
    $ renpy.hide(custom_hide("erin"))

    "As we eat our lunch, I think on Erin's words and all the ways I've tried to work on myself this summer."
    "I'm drawing more and working on myself."
    "I'm trying to be more confident--even just telling Erin how I feel was a huge step for me."

    "For a long time, I let my patterns control me."

    "I felt like the world was against me when, in reality, I had every ability to improve my life."

    "I don't want to let my unconscious direct my life or control my behavior."

    "I worked for the person I am. I worked for the relationship I have with Erin."
    scene black with fade

    "And I won't call it fate."

    jump credits_1
    return


label credits_1:

    if endingAFlag:
        $ persistent.endingAFlag = True
        # scene black with fade
        # play music "audio/rooftop.mp3" fadein 1.0
        
        # scene credits_a_1 with dissolve
        # with Pause(3)

        # show credits_a_2 with dissolve
        # with Pause(3)

        # show credits_a_3 with dissolve
        # with Pause(3)

        # show credits_a_4 with dissolve
        # with Pause(3)

        # show credits_a_5 with dissolve
        # with Pause(3)

        # show credits_a_6 with dissolve
        # with Pause(3)

        # show credits_a_7 with dissolve
        # with Pause(4)

    elif endingBFlag:
        $ persistent.endingBFlag = True
        scene black with fade
        # play music "audio/rooftop.mp3" fadein 1.0
        # "ended up with anna"
        # "Kim Jang Kris Gathman Nick Gathman Etc"
    elif endingCFlag:
        $ persistent.endingCFlag = True
        scene black with fade
        # play music "audio/rooftop.mp3" fadein 1.0
        # "ended up with erin"
        # "Kim Jang Kris Gathman Nick Gathman Etc"
    elif nekochan:
        $ persistent.d_ending_success = True
        scene black with fade
        # play music "audio/rooftop.mp3" fadein 1.0
        # "ended up with neko"
        # "Kim Jang Kris Gathman Nick Gathman Etc"
    else:
        scene black with fade
        # play music "audio/end.mp3" fadein 1.0
        # "You somehow didn't end up with anyone"
        # "Kim Jang Kris Gathman Nick Gathman Etc"
    
    jump persistent_check


label persistent_check:
    # current credit test
    scene black with fade
    show text "Credits" with dissolve

    $ renpy.pause(2.0)
    show text "Writer: Kris Gathman\n\nProgrammer & Artist: Kim Jang\n\nComposer: Nicholas Gathman"

    $ renpy.pause(4.0)
    show text "Thank you for playing Call it Fate\n\nA Jang Jang Productions Game\n\nPowered by Ren\'Py"
    $ renpy.pause(4.0)

    if persistent.endingAFlag == True:
        if persistent.endingCFlag == True:
            if persistent.endingBFlag == True:
                $ persistent.titleScreenCounter = 7 #  111 - all
            else:
                $ persistent.titleScreenCounter = 6 #  110 -- no anna
        else:
            if persistent.endingCFlag == True:
                $ persistent.titleScreenCounter = 5 #  101 -- no erin
            else:
                $ persistent.titleScreenCounter = 4 #  100 -- only maddie
    else:
        if persistent.endingBFlag == True:
            if persistent.endingCFlag == True:
                $ persistent.titleScreenCounter = 3 #  011 -- no maddie
            else:
                $ persistent.titleScreenCounter = 2 #  010 -- only anna
        else:
            if persistent.endingCFlag == True:
                $ persistent.titleScreenCounter = 1 #  001 -- only erin
            else:
                $ persistent.titleScreenCounter = 0 #  000 -- no one
    return