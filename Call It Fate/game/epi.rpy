label epi_start:
    scene bg_room with dissolve
    play music "audio/event.mp3" fadein 1.0

    "It's been three weeks since my Intro to Philosophy class ended, and Dr. Paige is only now updating the final grades."
    "He sent out an email last night, saying they'd be posted at noon today, so I wait and watch the 11:59 AM on my computer turn into 12:00 PM and hit refresh on my student portal."

    if grade >= 4:
        "I passed!"
        "I let out a sigh of relief."
    else:
        "I failed..."
        "I let out a tired sigh. I guess I'll just have to retake the class next year..."

    "A knock at my door pulls me away from my computer."
    scene bg_outside_dorm with dissolve

    if maddie:
        jump epi_maddie
    if anna:
        jump epi_anna
    if erin:
        jump epi_erin

label epi_maddie:
    scene maddie_epi with dissolve
    "Standing outside is Maddie, holding up a large plastic bag in her hand."

    a "\"Ready for lunch?\""

    n "\"Oh, wow, you didn't have to do that.\""
    scene bg_outside_dorm with dissolve

    $renpy.show(custom_show("maddie", "happy"), []) 
    a "\"I know, I wanted to.\""

    "She walks in and starts pulling styrofoam containers out of the bag."

    scene bg_room with dissolve
    n "\"Did you check your Philosophy grade yet?\""
    $renpy.show(custom_show("maddie", "normal"), []) 

    a "\"Nah, I'll look later. It's not like I can go back and change anything, might as well pay attention to what's ahead.\""

    n "\"And what's that?\""
    $renpy.show(custom_show("maddie", "happy"), []) 

    a "\"Sushi.\""

    "She holds up a container and chopsticks, taking a seat on the floor."

    n "\"You don't care how you did? We had to do a ton of work for that class. Don't you want to know if you passed?\""

    "Maddie looks off into the corner of the room as she chews, thinking."
    $renpy.show(custom_show("maddie", "uncomf"), []) 

    a "\"There's this quote I heard in Psych class, 'Until you make the unconscious conscious, it will direct your life and you will call it fate.'\""

    n "\"What's that mean?\""
    $renpy.show(custom_show("maddie", "flirty"), []) 

    a "\"I'm getting to that, Sam. Please.\""

    "She laughs, and I join her on the floor, grabbing chopsticks from the bag."
    $renpy.show(custom_show("maddie", "happy"), []) 

    a "\"If you don't make an honest effort to change the way you do things, you'll end up doing them the way you always do and blame some outside force like fate or God or whatever when you get a bad outcome.\""
    $renpy.show(custom_show("maddie", "normal"), []) 
    a "\"I worked really hard in that class. Probably harder than I have in any class this year. I could've done what I normally do, procrastinate and put in the minimum amount of work, but I decided to try.\""
    $renpy.show(custom_show("maddie", "angry"), []) 
    a "\"So, if I didn't pass, it's not because I didn't put the work in. I made the unconscious conscious. I took control.\""

    n "\"I don't get it then. Wouldn't you want to see if your hard work paid off?\""
    $renpy.show(custom_show("maddie", "happy"), []) 

    a "\"Today, I just want to celebrate that I worked hard at something I don't normally work hard at. I can worry about the grade later."
    $renpy.show(custom_show("maddie", "flirty"), []) 
    a "\"Now hurry up before I eat all the food.\""

    "She kisses me on the cheek, and I pick up a roll from the styrofoam box."
    $renpy.hide(custom_hide("maddie"))

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

    $renpy.show(custom_show("anna", "normal"), [])

    "Standing outside is Anna, holding up a large plastic bag in her hand."

    $renpy.show(custom_show("anna", "happy"), [])

    b "\"I brought sushi.\""

    n "\"Oh, wow, you didn't have to do that.\""

    $renpy.show(custom_show("anna", "embarrassed"), [])

    b "\"Did you already eat?\""
    $renpy.show(custom_show("anna", "embarrassed2"), [])

    n "\"No, it's just--I didn't expect it.\""

    $renpy.show(custom_show("anna", "flirty"), [])

    b "\"That's what makes it a surprise.\""

    "She walks in and starts pulling styrofoam containers out of the bag."
    scene bg_room with dissolve

    n "\"Did you check your Philosophy grade yet?\""

    $renpy.show(custom_show("anna", "normal"), [])

    b "\"No.\""

    n "\"Really? I thought you'd want to know right away.\""

    $renpy.show(custom_show("anna", "flirty"), [])

    b "\"I do. I want to know, but I always make myself wait a day after the grade's posted to check.\""

    n "\"Why?\""

    "She takes a seat on my bed, holding a take out box and chopsticks."

    $renpy.show(custom_show("anna", "angry"), [])

    b "\"I used to have pretty bad study habits.\""

    n "\"I can't imagine that.\""
    $renpy.show(custom_show("anna", "embarrassed"), [])

    b "\"Well, bad for me at least. I used to get mostly “B”s, a few “C”s.\""
    $renpy.show(custom_show("anna", "embarrassed2"), [])

    "I gasp and she laughs as I sit next to her on the bed, grabbing chopsticks from the bag."
    $renpy.show(custom_show("anna", "happy"), [])

    b "\"Anyway, I knew I could do better.\""
    b "\"Then, I heard this Carl Jung quote, 'Until you make the unconscious conscious, it will direct your life and you will call it fate.'\""
    b "\"You have to put in effort to resist bad habits, and if you do, you can improve your life. Otherwise, your habits will dictate everything.\""
    b "\"So that's when I started to make changes.\""
    $renpy.show(custom_show("anna", "normal"), [])
    b "\"When I got done with class, instead of procrastinating, I'd do my homework right away.\""
    b "\"If I had a test coming up, I'd schedule out times to study in advance. Do you get what I'm saying?\""

    n "\"I guess...? But I don't get why you'd wait to check your grade.\""
    $renpy.show(custom_show("anna", "angry"), [])

    b "\"That's one of the changes.\""
    b "\"I used to check my grades as soon as they were posted. But all that did was make me value the letter more than what I actually learned.\""
    $renpy.show(custom_show("anna", "flirty"), [])

    b "\"I want to take the time to reflect on how much more I know now than I did before taking the class. Then, I can check my grade.\""

    n "\"You probably got an 'A' though, right?\""
    $renpy.show(custom_show("anna", "normal"), [])

    b "\"Probably. Are you not hungry?\""

    "I kiss her on her forehead before picking up a roll from the styrofoam box."
    $renpy.hide(custom_hide("anna"))

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
    $renpy.show(custom_show("erin", "normal"), [])

    c "\"I thought I'd surprise you with lunch today.\""

    n "\"Wow! You didn't have to do that.\""

    c "\"I know, but I wanted to.\""

    "She walks in and starts pulling styrofoam containers out of the bag."
    scene bg_room with dissolve

    n "\"Did you check your Philosophy grade yet?\""
    $renpy.show(custom_show("erin", "surprised"), [])

    c "\"Are they posted?\""

    n "\"Yeah, Dr. Paige emailed us last night. You didn't see?\""

    "She shrugs before grabbing a container and chopsticks, taking a seat on the floor."
    $renpy.show(custom_show("erin", "flirty"), [])

    c "\"I'll check later. I took the class and tried my best. So, I give myself an 'A+' for effort.\""
    n "\"Yeah, but don't you want to know…the actual grade?\""
    c "\"I don't think I have to be too worried. I finished my homework every night and studied even when I didn't feel like it. That's enough, right?\""
    c "\"There's this quote I heard once, 'Until you make the unconscious conscious, it will direct your life and you will call it fate.'\""

    n "\"Make the unconscious conscious?\""
    "I join her on the floor, grabbing chopsticks from the bag."
    $renpy.show(custom_show("erin", "normal"), [])

    c "\"It means that you have to purposely change your patterns and behaviors if you want to improve.\""

    n "\"And you did that?\""
    $renpy.show(custom_show("erin", "flirty"), [])

    c "\"I did. So I can rest easy. Now, let's eat! I'm starving.\""

    "She kisses me on the cheek, and I pick up a roll from the styrofoam box."
    $renpy.hide(custom_hide("erin"))

    "As we eat our lunch, I think on Erin's words and all the ways I've tried to work on myself this summer."
    "I'm drawing more, and working on myself."
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

    if maddie:
        $persistent.a_ending_success = True
        scene black with fade
        play music "audio/roof.mp3" fadein 1.0
        
        scene perfectm1 with dissolve
        with Pause(3)

        show perfectm2 with dissolve
        with Pause(3)

        show perfectm3 with dissolve
        with Pause(3)

        show perfectm4 with dissolve
        with Pause(3)

        show perfectm5 with dissolve
        with Pause(3)

        show perfectm6 with dissolve
        with Pause(3)

        show perfectm7 with dissolve
        with Pause(4)

    elif anna:
        $persistent.b_ending_success = True
        scene black with fade
        play music "audio/end.mp3" fadein 1.0
        "ended up with anna"
        "Kim Jang Kris Gathman Nick Gathman Etc"
    elif erin:
        $persistent.c_ending_success = True
        scene black with fade
        play music "audio/end.mp3" fadein 1.0
        "ended up with erin"
        "Kim Jang Kris Gathman Nick Gathman Etc"
    elif nekochan:
        $persistent.d_ending_success = True
        scene black with fade
        play music "audio/end.mp3" fadein 1.0
        "ended up with neko"
        "Kim Jang Kris Gathman Nick Gathman Etc"
    else:
        scene black with fade
        play music "audio/end.mp3" fadein 1.0
        "You somehow didn't end up with anyone"
        "Kim Jang Kris Gathman Nick Gathman Etc"
    
    jump persistent_check

label persistent_check:
    if persistent.a_ending_success == True:
        if persistent.b_ending_success == True:
            if persistent.c_ending_success == True:
                $persistent.score = 7
            else:
                $persistent.score = 4
        else:
            if persistent.c_ending_success == True:
                $persistent.score = 5
            else:
                $persistent.score = 4
    elif persistent.b_ending_success == True:
        if persistent.a_ending_success == True:
            if persistent.c_ending_success == True:
                $persistent.score = 7
            else:
                $persistent.score = 6
        else:
            if persistent.c_ending_success == True:
                $persistent.score = 3
            else:
                $persistent.score = 1
    elif persistent.c_ending_success == True:
        if persistent.b_ending_success == True:
            if persistent.a_ending_success == True:
                $persistent.score = 7
            else:
                $persistent.score = 3
        else:
            if persistent.a_ending_success == True:
                $persistent.score = 6
            else:
                $persistent.score = 2
    else:
        $persistent.score = 0
    return
