
label eventBHang:
    scene event_hang_ba with dissolve
    play music "audio/event.mp3"  fadein 1.0
    $ eventBHangCompletedFlag = True
    $ eventBHangToday = True
    "I head to the library where Anna is waiting, her books and notes already spread out in front of her."
    n "\'Hey.\'"
    scene event_hang_bb with dissolve
    b "\'You made it.\'"
    "She looks up and puts her book away."
    scene bg_lib_a with dissolve
    $ renpy.show(custom_show("anna", "H"), [])
    n "\'Of course.\'"
    menu:
        "I wanted to see you.":
            n "\'Any excuse to see you is worth it.\'"
            if B >= B_mid2:
                $ renpy.show(custom_show("anna", "E"), [])
                $ B = B + 1
                b "\'...\'"
                $ renpy.show(custom_show("anna", "E2"), [])
            else:
                $ renpy.show(custom_show("anna", "U"), [])
                b "\'...\'"
        "I want to get an 'A'.":  
            n "\'I want to do well in this class.\'"
            $ renpy.show(custom_show("anna", "H"), [])
            b "\'...\'"

    $ renpy.hide(custom_hide("anna"))
    "We start the study session by working on our homework, moving through the short-answer questions quicker than I ever could alone."
    "It's strange to think that just a few weeks ago, I had trouble working up the nerve to even talk to Anna, and now we're studying together."

    "I feel lucky getting to spend time with her, though, it's also nerve-racking."

    "I'm terrified that I'll say something stupid or mess things up somehow. It's no secret that Anna's hard to impress."
    "I don't want to scare her off."

    "But as she looks up at me from her paper and smiles, I feel less tense."
    "After all, if she's here with me now, I must be doing something right."

    "When we finish the assignment, Anna hands me her nearly perfect notes, which I use to quiz her on the class material."

    "As I go through the questions, I start to notice that every time she gets an answer wrong, Anna will bite her lip or sigh."
    $ renpy.show(custom_show("anna", "E2"), [])
    n "\'It's okay not to know all the answers. That's why we're studying.\'"
    "Anna's gaze falls to the table in front of her, a disappointed look in her eyes."
    # $ renpy.show(custom_show("anna", "sigh"), [])

    b "\'I just...it's frustrating.\'"
    n "\'It's okay, you're still learning. If we knew all this stuff already, we wouldn't need to take the class.\'"
    $ renpy.show(custom_show("anna", "U"), [])
    b "\'...\'"
    n "\'I get that it's discouraging when you don't understand something right away. But it's also kind of exciting, right? Because that means we get the chance to learn something new.\'"
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'...Thank you, Sam...\'"
    b "\'Ask me another question, I'll be okay.\'"
    $ renpy.show(custom_show("anna", "N"), [])
    "We pick up where we left off, and Anna no longer seems bothered by her mistakes."
    jump event_calculation_a
    

label eventBDate:
    $ eventBDateCompletedFlag = True
    $ weekendDateFlag = False
    $ eventBDateToday = True
    
    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Anna."
    b "\'Did you have any ideas on where we should go today?\'"
    menu: 
        "Hiking trail":
            "In response, I write, \'I was thinking we could go on a hike. Is that okay?\'"
            b "\Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\'"
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
        "Interactive science museum":
            $ B = B + 1
            "In response, I write, \'I was thinking we could check out the science museum. Is that okay?\'"
            b "\'That's perfect. Let's meet there at 11am.\'"
        "Art gallery":
            "In response, I write, \'I was thinking we could go to this art gallery. Is that okay?\'"
            b "\'Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\'"
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
        "Ramen shop":
            "In response, I write, \'I was thinking we could grab some ramen. Is that okay?\'"
            b "\'Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\'"
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
    
    scene event_date_b with dissolve

    "When I arrive, I find Anna beside the ticket stand, thumbing through museum pamphlets."
    n "\'Hey!\'"
    "Anna turns to face me."
    scene bg_museum with dissolve
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'Good, you're here. I got us tickets.\'"
    n "\'Oh, really? I was planning on paying...\'"
    $ renpy.show(custom_show("anna", "F"), [])
    b "\'It's fine. You can get the next one.\'"
    n "\''The next one?'\'"
    $ renpy.show(custom_show("anna", "N"), [])
    b "\'So was there anything you really wanted to see? I have a map if you want to look.\'"
    "She pulls out the map and hands it to me. As I examine the creased, colorful illustration of the museum, I notice a couple exhibits that pique my interest."
    "What should we check out?"
    menu: 
        "Planetarium":
            $ B = B + 2
            n "\'Let's go to the planetarium.\'"
            $ renpy.show(custom_show("anna", "E"), [])
            b "\'I was thinking the same thing.\'"
            $ renpy.show(custom_show("anna", "E2"), [])
        "Bed of needles":
            $ B = B - 1
            n "\'Let's go to the bed of needles.\'"
            $ renpy.show(custom_show("anna", "U"), [])
            b "\'...Sure, we can do that. Would you mind if we went to the planetarium first though? There's a show starting soon.\'"

    $ renpy.hide(custom_hide("anna"))

    "As we head inside the museum, I look around at all the interesting interactive exhibits around us. I hear sounds of awe and laughter, the big, open room overflowing with energy."

    "It's much quieter in the planetarium though. The speakers play ethereal long tones to add to the space-like atmosphere as we stare up at a fake night sky and wait for the show to begin."

    "Soon the doors close, and the projected stars and planets start to move."

    "A deep, surrounding voice teaches us about the wonders of our galaxy, the mysteries of space, and I feel Anna's hand find mine."

    scene bg_stem_poster with dissolve

    "At the exit, we're handed flyers that read, \'GRANT OPPORTUNITIES FOR WOMEN IN STEM,\' followed by details on how to apply."

    n "\'Hey, I bet you'd qualify.\'"
    
    "I hold up the paper for Anna to see."
    scene bg_museum with dissolve

    $ renpy.show(custom_show("anna", "U"), [trueleft])

    b "\'I don't know if that's really for me...\'"

    "Isn't she in school for..."
    menu:
        "...Chemistry?":
            n "\'Sure it is, you're a chemistry student, right?\'"
            $ renpy.show(custom_show("anna", "E2"), [])
            b "\'Engineering actually. But that's not what I mean.\'"

        "...Engineering?":
            n "\'Sure it is, you're an engineering student, right?\'"
            $ renpy.show(custom_show("anna", "N"), [])
            b "\'Well, yes, but that's not what I mean.\'"

        "...Medicine?":
            n "\'Sure it is, you're a pre-med student, right?\'"
            $ renpy.show(custom_show("anna", "E2"), [])
            b "\'Engineering actually. But that's not what I mean.\'"

    $ renpy.show(custom_show("anna", "U"), [])

    b "\'I'm not sure I feel comfortable getting special treatment just because I'm a woman. If I get a grant, I want it to be because I earned it.\'"

    n "\'I wouldn't think of it like that…If you apply for the grant and get picked, that's you earning it. There's nothing noble about turning down a good opportunity.\'"

    if special_B_on:

        n "\'Besides, if you get the grant, you won't have to be so worried about losing your scholarship.\'"

    b "\'You make a fair point...\'"

    $ renpy.show(custom_show("anna", "N"), [])

    b "\'Okay, I'll do it. I'll apply.\'"

    n "\'Great! Let me know when you get it.\'"

    $ renpy.show(custom_show("anna", "F"), [])

    b "\'You mean 'if' I get it.\'"

    n "\'No, I mean 'when.'"

    $ renpy.hide(custom_hide("anna"))

    scene bg_museum with dissolve

    "We spend the rest of our time exploring the museum, laying on the bed of needles, disrupting the miniature tornado, poking all the venus flytraps in the gift shop to make their bristled mouths close."

    "Usually, when I'd see Anna around campus, she'd always be doing school work--reading, studying. Even in the cafeteria, she'd have a laptop or notebook out."

    "So, seeing her outside of school and actually letting loose...It's almost a little weird."

    "I'm taken by surprise at just how fun she is to hang around. How her eyes widen with wonder at all the gadgets and exhibits of the museum. How seeing something she doesn't understand and figuring out how it works seems to genuinely excite her."
    
    "But eventually, we run out of things to see, and it's time to leave the museum. So I walk Anna to her car."
    
    scene bg_after_date with dissolve 

    $ renpy.show(custom_show("anna", "H"), [])
    b "\'Today was nice.\'"


    if special_B_on:

        $ renpy.show(custom_show("anna", "F"), [])
        b "\'I think you were right, Sam. I really need to take breaks like this more often.\'"

    b "\'I'm glad you invited me out.\'"

    $ renpy.show(custom_show("anna", "N"), [])
    n "\'Me too.\'"
    "As I'm looking at her, I realize it's time to part ways."
    "How should I say goodbye?"

    menu:
        "Kiss her":
            if B >= B_high:
                scene black with dissolve

                $ B = B + 1
                "I lean in."
                "And our lips meet."
                scene event_kiss_b with dissolve

                "Smiling, she gets in her car and drives away."
                "And I can't wait until Tuesday when I get to see her again."
                jump event_calculation_a
            else:
                scene black with dissolve
                $ B = B - 1
                "I lean in."
                scene bg_after_date with dissolve 
                $ renpy.show(custom_show("anna", "U"), [])
                "And she leans away. I feel a wave of embarrassment wash over me."
                b "\'I should go. Bye, Sam.\'"
                $ renpy.hide(custom_hide("anna"))
                "Anna gets in her car and drives away."
                "And I'm left wondering what I did wrong."
                jump event_calculation_a
        "Hug her":
            $ renpy.hide(custom_hide("anna"))
            "I give Anna a hug goodbye before she gets in her car and drives away."
            "And I'm left wondering if there was a better way I could've done that."
            jump event_calculation_a
        "Give her a high five":
            "I hold up my hand to give her a high five."
            $ renpy.show(custom_show("anna", "A"), [])
            n "\'See you Tuesday.\'"
            "Anna stares blankly at my open palm"
            b "\'See you Tuesday.\'"
            $ renpy.hide(custom_hide("anna"))
            "She gets in her car and drives away."
            "And I awkwardly lower my hand, feeling a little embarrassed by the situation."
            jump event_calculation_a


label actB_scene3:
    scene event_dorm_b with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I open my door to find Anna standing outside my room."
    n "\'Anna! What are you doing here?\'"
    b "\'I brought you some papers from class and made you a copy of my notes.\'"
    n "\'Really? Thanks. You didn't have to do all that.\'"
    "She hands me a few pages, the passages already color-coded with highlighters."
    scene bg_room_outside_b with dissolve
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'The final's on Thursday. I wanted to make sure you'd be prepared.\'"
    n "\'Do you want to come in?\'"
    "I move to the side, and she walks into my dorm."
    scene bg_room_b with dissolve

    if clean:
        $ renpy.show(custom_show("anna", "F"), [])
        b "\'You have a nice dorm.\'"
        "She wanders over to my bookshelf, examining the collection of manga that sits there."
        $ renpy.show(custom_show("anna", "H"), [])
        b "\'And good taste.\'"

    else:
        $ renpy.show(custom_show("anna", "A"), [])
        n "\'Sorry for the mess. I've been meaning to clean.\'"
        "I catch Anna eyeing a dirty dish on my desk and instantly regret inviting her in."
        "She must think I'm disgusting."
        "I watch as she wanders over to my bookshelf, examining the collection of manga that sits there."

    $ renpy.show(custom_show("anna", "U"), [])

    b "\'I never owned any complete sets like these. I usually either check them out or buy second-hand.\'"

    n "\'You're welcome to borrow any of those if you like.\'"

    $ renpy.show(custom_show("anna", "H"), [])

    b "\'Do I get a 'Sam's Dorm' library card?\'"

    n "\'Sure. But if you're overdue, I'll have to charge you.\'"

    $ renpy.show(custom_show("anna", "F"), [])

    "She laughs."


    if B >= B_high:
        $ confessedFlagB = True
        stop music fadeout 1.0

        "We stand there for a moment in silence."
        $ renpy.show(custom_show("anna", "U"), [])
        b "\'There's something I want to tell you. But I'm a little nervous...\'"
        n "\'What is it? Is it bad?\'"
        "Anna shakes her head"
        $ renpy.show(custom_show("anna", "E"), [])
        b "\'No, nothing bad. It's just hard to say.\'"
        $ renpy.show(custom_show("anna", "E2"), [])
        "She looks away from me, and I wait, wondering what it could be."
        b "\'I have feelings for you. I thought I should tell you, even if you might not feel the same.\'"
        "Then, she looks up at me, and I know she's waiting for a response."

        menu:
            "I like you too": 
                n "\'Anna, I--\'"
                "A wave of dizziness overwhelms me."
                $ renpy.show(custom_show("anna", "E"), [])
                b "\'Sam!\'"
                "Anna grabs me, keeping me from losing my balance."
                $ renpy.show(custom_show("anna", "N"), [])
                b "\'I'm glad I came by.\'"
                n "\'Me too.\'"
                "I knew I had to reply to her confession, but I felt so weak."
                b "\'I'm going to leave now.\'"
                "My heart raced."
                n "\'What?\'"
                $ renpy.show(custom_show("anna", "U"), [])
                b "\'So you can rest. You're sick. I can't expect you to entertain a guest right now.\'"
                n "\'I guess you have a point.\'"
                $ renpy.show(custom_show("anna", "H"), [])
                b "\'Don't worry. We'll spend some time together...this weekend?\'"
                n "\'Sounds great.\'"
                $ renpy.hide(custom_hide("anna"))
                scene event_sick_b with dissolve
                "While leaving my room, she hesitates by the doorway."
                b "\'Goodbye, Sam. I hope you feel better in the morning.\'"
                scene bg_room_b with dissolve
                "Anna closes the door behind her, and I'm left lying in bed, wishing my headache away so I could go after her and ask her to stay a little longer."
                "But spending time with Anna would have to wait."
                "The second I lie down in my bed, I'm already drifting back to sleep."
                "I dream of a life with Anna. And though I know realistically it's probably just caused by the fever, I can't help but think it means something."
                "That these past two weeks are just the beginning."
                jump event_calculation_a
            "I don't think of you like that":
                n "\'Anna, I--\'"
                "A wave of dizziness overwhelms me."
                $ renpy.show(custom_show("anna", "E2"), [])
                b "\'Sam!\'"
                "Anna grabs me as I almost fall to the ground."
                b "\'I'm glad I came by.\'"
                n "\'Me too.\'"
                "I knew I had to reply to her confession, but I felt so weak."
                b "\'I'm going to leave now.\'"
                "My heart raced."
                n "\'What?\'"
                $ renpy.show(custom_show("anna", "U"), [])
                b "\'So you can rest. You're sick. I can't expect you to entertain a guest right now.\'"
                n "\'I guess you have a point.\'"
                $ renpy.hide(custom_hide("anna"))
                scene event_sick_b with dissolve
                "While leaving my room, she hesitates by the doorway."
                b "\'Don't worry. We'll spend some time together...this weekend?\'"
                n "\'Anna...\'"
                scene bg_room_b with dissolve
                "She leaves the room, closing the door behind her before I have a chance to say anything else."
                jump event_calculation_a

    else: 
        $ renpy.show(custom_show("anna", "U"), [])
        b "\'I'm going to go.\'"
        n "\'Are you sure?\'"
        b "\'You're sick. It's not good for you to entertain guests right now. I'll see you in class.\'"
        n "\'Alright. Talk to you later then.\'"
        $ renpy.hide(custom_hide("anna"))
        "Anna leaves, closing the door behind her, and I'm left standing in the middle of my dorm, alone."
        "I go to sleep with my fever-induced headache and dream of a life with Neko-Chan...a perfect life."
        jump event_calculation_a
    return

label eventRoofB:
    scene bg_roof with dissolve
    play music "audio/rooftop.mp3" fadein 1.0

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    scene event_roof_b with dissolve
    "Anna stands at a distance from the edge of the roof, even with the fencing in place. She seems...at peace. Relaxed."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    n "\'Hey.\'"
    b "\'I was just admiring the view.\'"
    "She looks back at the sunset, and I join her, watching the changing sky while I think of what to say."

    n "\'I got this for you.\'"

    if anna_gift:
        scene event_gift_b with dissolve
        $ B = B + 1
        $ renpy.show(custom_show("anna", "H"), [trueleft])
        "Anna looks down at the venus flytrap, and smiles."
        if eventBDateFlag:
            b "\'Like the ones at the museum.\'"
        "I hand it to her."
        b "I'll take good care of it. Thank you."
        $ renpy.hide(custom_hide("anna"))
    else:
        scene bg_roof with dissolve
        $ renpy.show(custom_show("anna", "U"), [])
        "Anna turns to face me and accepts the gift, the blank expression on her face only making me more nervous."
        n "\'Do you like it?\'"
        b "\'...I appreciate the thought.\'"
    scene bg_roof with dissolve
    $ renpy.show(custom_show("anna", "N"), [])
    "The air grows cooler as we stare out into the horizon."
    n "\'What are you thinking about?\'"
    $ renpy.show(custom_show("anna", "U"), [])
    b "\'I've never been up here before...I'll spend hours in the library. But I never once went on the roof...It's nice.\'"
    n "\'Well, I guess now you have a new spot for study breaks.\'"
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'I guess so...Thank you, Sam.\'"
    n "\'What for?\'"
    $ renpy.show(custom_show("anna", "F"), [])
    b "\'For inviting me here, for breaking me out of my comfort zone. I've been told I can be a little...closed off. I appreciate you being patient with me.\'"
    n "\'It's no trouble at all.\'"
    $ renpy.show(custom_show("anna", "H"), [])
    "She smiles."

    $ renpy.show(custom_show("anna", "N"), [])
    b "\'So what was it you wanted to talk about?\'"

    menu:
        "Confess my feelings":
            if confessedFlagB:
                jump endingB11
            if B >= B_high3:
                jump endingB10
            elif B >= B_high:
                jump endingB01
            else:
                jump endingB00
        "I've changed my mind":
            jump neko_ending