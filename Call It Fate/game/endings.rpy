label endingA0:
    $ maddie = True
    n "\'Alright, well, I guess I'll just say it. I know we only just started hanging out, but…I really like you, and I was wondering if maybe...you felt the same way?\'"
    "Another breeze blows past us as I wait for her to respond."
    $ renpy.show(custom_show("maddie", "F"), [])
    a "\'I like you too.\'"
    "It takes a moment before what she's saying sinks in."
    n "\'Really?! I mean, that's great!\'"
    "She smiles, then takes my hand."
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 


label endingA1:
    $ maddie = True
    $ renpy.show(custom_show("maddie", "A"), [])
    a "\'Are you serious, Sam?\'"
    n "\'Sorry, nevermind, forget I said anything.\'"
    a "\'No! That's not what I mean.\'"
    n "\'What?\'"
    $ renpy.show(custom_show("maddie", "H"), [])
    a "\'Of course I like you! I wasn't trying to be subtle, could you really not tell?\'"
    n "\'I had no idea.\'"
    "Maddie sighs dramatically, jokingly."
    $ renpy.show(custom_show("maddie", "F"), [])
    a "\'Well, now you do.\'"
    "She smiles, then takes my hand."
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 


label maddie_badending:
    $ nekochan = True
    $ renpy.show(custom_show("maddie", "S"), [])
    a "\'Oh...Sam, I'm so sorry.\'"
    "It takes a moment before what she's saying sinks in."
    n "\'Huh...I guess I misread things...I'll see you around.\'"
    scene black with fade
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    scene bg_room_c with dissolve
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    scene bg_room_cc with dissolve

    show neko
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black
    jump credits_1
    return


label maddie_confessedending:
    $ maddie = True
    $ renpy.show(custom_show("maddie", "N"), [])
    n "\'The other day, when I was sick, you said something to me.\'"
    $ renpy.show(custom_show("maddie", "U"), [])

    a "\'You mean that I like you?\'"

    n "\'Yeah, that...\'"

    n "\'I-I didn't get a chance to respond before, but...\'"
    $ renpy.show(custom_show("maddie", "E"), [])

    n "\'I feel the same way.\'"

    "Another breeze blows past us."
    $ renpy.show(custom_show("maddie", "H"), [])

    "Then, she smiles."
    $ renpy.show(custom_show("maddie", "F"), [])

    a "\'Good.\'"

    "She takes my hand, and leans on my shoulder."

    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return



label anna_goodending:
    $ anna = True
    n "\'I really like you, Anna. I know we haven't known each other for very long, but I like you, and I was wondering if maybe...you felt the same way?\'"
    "Another breeze blows past us as I wait for her to respond."
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'I do.\'"
    "It takes a moment before what she's saying sinks in."
    n "\'You...feel the same?\'"
    $ renpy.show(custom_show("anna", "N"), [])
    "She nods."
    n "\'Really?! I mean, that's great!\'"
    "Despite the chilled air, I feel warm."
    "She takes my hand."
    "And we finish watching the sun disappear."
    $ day_counter = temp 
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 


label anna_perfectending:
    $ anna = True
    $ renpy.show(custom_show("anna", "F"), [])
    b "\'Of course I feel the same way.\'"
    n "\'Really?! I mean, that's great!\'"
    $ renpy.show(custom_show("anna", "N"), [])

    "Despite the chilled air, I feel warm."
    "And we finish watching the sun disappear."
    $ day_counter = temp
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 


label anna_badending:
    $ nekochan = True
    $ renpy.show(custom_show("anna", "A"), [])
    b "\'You're a good guy, so I'm sorry if I've misled you. But I don't feel that way about you.\'"
    "It takes a moment before what she's saying sinks in."
    n "\'Huh...I guess I misread things...I'll see you around.\'"
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    $ day_counter = temp
    stop music fadeout 1.0
    scene black with fade

    scene bg_room_c
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black with fade
    jump credits_1
    return 


label anna_confessedending:
    $ anna = True
    n "\'The other day, when I was sick, you said something to me.\'"
    $ renpy.show(custom_show("anna", "E"), [])

    b "\'I was hoping you'd forgotten that...\'"
    $ renpy.show(custom_show("anna", "embarrassed2"), [])

    n "\'Why?\'"
    $ renpy.show(custom_show("anna", "E2"), [])

    b "\'Because...you don't feel the same.\'"

    n "\'No, but I do! I didn't get a chance to respond before, but-\'"

    "Anna interrupts me with a kiss."

    "Despite the chilled air, I feel warm."

    "And we finish watching the sun disappear."
    $ day_counter = temp
    stop music fadeout 1.0
    scene black with fade
    jump epi_start

    return



label erin_goodending:
    $ erin = True
    n "\'Um, right. Okay, I guess I should just say it then. I really like you, Erin. I know we haven't known each other for very long, but I like you, and I was wondering if maybe...you felt the same way?\'"
    "Another breeze blows past us as I wait for her to respond."
    $ renpy.show(custom_show("erin", "N"), [])
    c "\'You're pretty great, you know that?\'"
    n "\'Does that mean...?\'"
    $ renpy.show(custom_show("erin", "F"), [])
    c "\'I like you too.\'"
    n "\'Really?! I mean, that's great!\'"
    n "\'She smiles and takes my hand.\'"
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 


label erin_perfectending:
    $ erin = True
    $ renpy.show(custom_show("erin", "F"), [])
    c "\'I'm surprised you don't already know.\'"
    n "\'Does that mean...?\'"
    $ renpy.show(custom_show("erin", "H"), [])
    c "\'I feel the same. I like you too.\'"
    n "\'Really?\'"
    $ renpy.show(custom_show("erin", "N"), [])
    c "\'Really.\'"
    "She smiles and takes my hand."
    "Then, we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with fade
    $ day_counter = temp
    jump epi_start
    return


label erin_badending:
    $ nekochan = True
    $ renpy.show(custom_show("erin", "S"), [])
    c "\'Uh, sorry. I don't know how to say this. I'm happy we met, and you're a good friend. But...I don't like you in that way.\'"
    "It takes a moment before what she's saying sinks in."
    n "\'Huh...I guess I misread things...I'll see you around.\'"
    $ renpy.hide(custom_hide("erin"))
    stop music fadeout 1.0
    scene black with fade
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    scene bg_room_cc with dissolve

    show neko
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black with fade
    $ day_counter = temp
    jump credits_1
    return 


label erin_confessedending:
    $ erin = True
    $ renpy.show(custom_show("erin", "N"), [])
    n "\'The other day, when I was sick, you said you liked me?\'"
    $ renpy.show(custom_show("erin", "E"), [])
    c "\'Ahh! That was so embarrassing. Can you just forget I said anything?\'"

    n "\'No, you don't understand!\'"
    $ renpy.show(custom_show("erin", "surprised"), [])

    n "\'I-I didn't get a chance to respond before, but...\'"
    n "\'I feel the same way.\'"

    
    "Another breeze blows past us."
    $ renpy.show(custom_show("erin", "H"), [])
    c "\'Really?\'"

    n "\'Really.\'"
    $ renpy.show(custom_show("erin", "F"), [])
    "She smiles as I take her hand."

    "And we finish watching the sun disappear."
    $ day_counter = temp
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return


label neko_ending:
    stop music fadeout 1.0
    "And in that moment, it hits me."
    "I've made the wrong choice."
    "I shouldn't be here."
    "She isn't the girl I want to be with."
    n "\'Um...sorry...I have to go.\'"
    
    scene bg_room_c with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I leave the roof and head back to my dorm where Neko-Chan sits on her usual spot on my bed."
    n "\'Oh thank God you're still here.\'"
    scene bg_room_cc with dissolve

    show neko
    nc "\'...\'"
    n "\'Listen, on the roof I realized something.\'"
    n "I realized that you're the only girl who's always been there for me. The only one who liked me the way I was and never expected me to change...\'"
    n "\'I'm sorry I didn't realize it sooner, Neko-Chan, but I want to be with you. What do you say?\'"
    nc "\'...\'"
    n "\'I'm so happy you feel the same.\'"
    "I hold Neko-Chan in my arms and smile, knowing that for now on, it's just going to be me and her."
    "Forever."
    scene black with fade
    jump credits_1
    return 


label confession:
    scene bg_room_b with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I take a deep breath."
    "I don't know much about this kind of thing, but if I'm really going to do this, I feel like I should bring a gift."
    "Luckily, I have a couple hours before dusk to get something."
    "What should I give her?"

    menu:
        "A potted succulent":
            $ maddie_gift = True
            scene black with fade
            "I swing by the local nursery and pick up a succulent before heading back to campus."
        "A venus fly trap":
            $ anna_gift = True
            scene black with fade
            "I grab a venus fly trap at a pet shop before heading back to campus."
        "A bouquet of sunflowers":
            $ erin_gift = True
            scene black with fade
            "I pick up a bouquet of sunflowers from a flower shop before heading back to campus."
        "A single rose":
            scene black with fade
            "I buy a single rose from the grocery store before heading back to campus."

    if eventca_trigger:
        jump event_roof_a
    elif eventcb_trigger:
        jump event_roof_b 
    elif eventcc_trigger:
        jump event_roof_c 
    return
