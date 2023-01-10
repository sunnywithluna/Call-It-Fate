label ch1_schoolday1:

    scene bg_class with fade
    play music "audio/class.mp3"

    "Right as I enter the classroom, I stop in my tracks."

    scene anna_intro with fade

    "There's a girl reading in the corner, so invested in her book that she doesn't even look up at the sound of the door closing behind me."
    "She curls a strand of hair behind her ear before turning a page."

    "I've seen her around campus but never actually worked up the courage to talk to her."
    "And how could I?"
    "She's way out of my league."
    "Besides, I hear she doesn't really date."

    scene bg_class with fade

    "I look away to avoid staring and pass the professor at his large wooden desk before taking a seat."

    "The only noise in the otherwise quiet room is the whirr of the air conditioner and the ticking of a clock that shows we have two minutes until class begins."

    "Soon, the door opens, and I glance up only to quickly look back down. With my elbow resting on my desk, I cup my hand above my eyes, hoping she doesn't notice me."

    "It's Maddie Geller."
    "We went to the same elementary, junior high, high school, and now, it would seem, we're at the same college too."

    scene maddie_intro with fade
    a "\"Sam? No way! I didn't know you went to LU.\""
    n "\"Maddie! Wow, yeah, you came here too I guess.\""
    "What are the chances…"
    p "\"Alright, everyone. Settle in, we're about to start class.\""
    "Maddie turns back to me, causing her ponytail to sway."
    scene bg_class with fade
    show maddie_1 flirty

    a "\"It's great to see you, Sam. Maybe we can catch up later.\""
    hide maddie_1
    "She drops down into her seat and starts digging through her backpack."
    "I'm a little shocked. No snide remarks? No teasing? She actually seemed pleasant for once."
    p "\"Let's get the ball rolling, shall we? My name is Dr. Paige and, as you already know, this is Intro to Philosophy.\""
    p "\"We'll be meeting here from one to four, Tuesday and Thursday for three weeks.\""
    p "\"Be aware that you'll be expected to use the days we don't meet to do assigned reading and respond to the quizzes I'll be posting on our class website.\""
    p "\"I will be available for correspondence via email. Any questions?\""
    "The wall clock ticks."
    p "\"Alright then, I'll take that as a 'no'. Now,  why don't we go around, introduce ourselves, and say at least one thing we're looking forward to learning over these next few weeks.\""
    "Dr. Paige nods to Maddie."
    p "\"Why don't you start us off?\""
    show maddie_1 normal
    a "\"Sure. My name is Maddie, and what I'm looking forward to most in this class is...\""
    "She scratches the back of her head while she thinks."
    show maddie_1 uncomf
    a "\"...the challenge of learning about a topic I don't know much about.\""
    hide maddie_1
    show anna_1 uncomf
    "The girl who was reading before class sits up tall in her chair with her book now closed on her desk."
    show anna_1 happy
    b "\"I'm Anna. I look forward to hearing about the great philosophers in history and what observations they made about our world.\""
    $ renpy.hide(custom_hide("anna"))

    scene erin_intro with fade

    "The classroom door swings open to reveal a girl who is clearly out of breath."
    c "\"Sorry I'm late. I got lost.\""
    p "\"No trouble. We were just going over introductions. Why don't you go next? Tell us your name and something you're excited about learning in this class.\""
   
    scene bg_class with fade

    $ renpy.show(custom_show("erin", "embarrassed"), [])
    c "\"Uh... I guess just...\""
    $ renpy.show(custom_show("erin", "uncomf"), [])
    c "\"...seeing things through new perspectives? Learning how to look at life in ways that I hadn't thought of before.\""
    $ renpy.show(custom_show("erin", "happy"), [])
    c "\"Oh, and my name's Erin.\""
    $ renpy.hide(custom_hide("erin"))
    "As Erin takes her seat, she wears a smile."

    "She has a genuine warmth and kindness about her that lights up the room. I've never seen someone look so happy before a lecture."

    "Finally, the professor turns to me."

    p "\"What about you? What are you looking forward to?\""

    menu:
        "The challenge":
            $ A = A + 2
            n "\"My name's Sam. And, I'm excited to push myself. I've heard this class can be pretty tough, but I think it'll be good for me.\""
            show maddie_1 normal
            a "\"...\""
            hide maddie_1
        "The philosophers":
            $ B = B + 2
            n "\"My name's Sam. And, I'm excited to learn from the philosophers we'll study and hopefully apply some of their wisdom to my life.\""
            show anna_1 normal
            b "\"...\""
            $ renpy.hide(custom_hide("anna"))
        "The perspectives":
            $ C = C + 2
            n "\"My name's Sam. And, I'm excited to hear different points of view. I'm just one person and the world's a big place. Maybe I'm missing something.\""
            $ renpy.show(custom_show("erin", "normal"), [])
            c "\"...\""
            $ renpy.hide(custom_hide("erin"))
        "The course credits":
            n "\"My name's Sam. And, honestly, I'm just here for the credits.\""

    p "\"Alright then. Now that we're all acquainted, let's get on with the lesson.\""

    scene black with fade
    stop music fadeout 1.0

    "Dr. Paige lectures for the remainder of the class period and then dismisses us for the day."
    scene bg_class_after with fade
    "I'm still packing up when the other students take off."
    "By the time I get outside, Maddie is already heading to the westside of campus towards the school gym."
    "Anna is heading to the northside of campus towards the library, and Erin is heading to the eastside of campus towards the art building."
    "I have some time to kill before dinner. What should I do?"
    jump after_class
    
    return

label ch1_schoolday2:
    $ day = day + 1
    scene bg_class with fade
    play music "audio/class.mp3"

    "On Thursday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."
    if 6 <= A <= 10:
        show maddie_2 happy
        a "\"Hey, Sam!\""
        hide maddie_2
    elif A > 10:
        show maddie_2 flirty
        a "\"Hey, Sam, sit with me!\""
        hide maddie_2
    if 6 <= B <= 10:
        show anna_2 happy
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > 10:
        show anna_2 flirty
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if 6 <= C <= 10:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > 10:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))

    "I take a seat and class begins."
    "Dr. Paige stands at the front of the room while he lectures, using grand hand movements to emphasize his words and occasionally writing key terms on the board."
    "What should I do?"

    menu:
        "Get out my grip strengthener":
            $A = A+1
            "If I have to sit here for a few hours, I might as well multitask."
            "I retrieve my grip strengthener from my backpack and practice squeezing the handles together, switching hands periodically."
            show maddie_2 normal
            "Out of the corner of my eye, I catch Maddie looking my way."
            hide maddie_2
        "Take notes diligently":
            $ B = B+1
            "What Dr. Paige is saying seems important. I should pay close attention."
            "I open my notebook and take down his main points."
            show anna_2 normal
            "Out of the corner of my eye, I catch Anna looking my way."
            $ renpy.hide(custom_hide("anna"))
        "Doodle":
            $C = C+1
            "While listening to Dr. Paige, I start sketching in my notebook."
            "Before I know it, a page intended for philosophy notes is covered in drawings."
            $ renpy.show(custom_show("erin", "normal"), [])
            "Out of the corner of my eye, I catch Erin looking my way."
            $ renpy.hide(custom_hide("erin"))
        "Sit back and wait for class to end":
            "I sit back in my chair and count down the hours to the end of class."

    scene black with fade
    stop music fadeout 1.0

    "Eventually, Dr. Paige dismisses us for the day."
    scene bg_class_after with fade
    "I have some time to kill before dinner. What should I do?"
    jump after_class
    return

label ch1_weekend:
    $ day = day + 1
    scene bg_room with fade
    play music "audio/dorm.mp3"

    if date == True:
        stop music fadeout 1.0
        "Finally, the week's over."
        "Usually, I'd just stay home--sleep in, watch TV, play some games, talk to Neko-Chan. But I actually have a reason to go out this weekend."
        play music "audio/event.mp3"
        if eventba_trigger and not maddie_date_over:
            jump event_ba
        elif eventbb_trigger and not anna_date_over:
            jump event_bb 
        elif eventbc_trigger and not erin_date_over:
            jump event_bc
    else: 
        "I can't believe it's already the weekend. I wish I had something to do…"
        "I laze around my dorm, playing games and watching TV, until the next school day."
        stop music fadeout 1.0
        scene bg black with fade
        jump ch2_schoolday1

label ch2_schoolday1:
    $ day = day + 1
    scene bg_class with fade
    play music "audio/class.mp3"

    "On Tuesday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."
    if 6 <= A <= 10:
        show maddie_3 happy
        a "\"Hey, Sam!\""
        hide maddie_3
    elif A > 10:
        show maddie_3 flirty
        a "\"Hey, Sam, sit with me!\""
        hide maddie_3
    if 6 <= B <= 10:
        show anna_3 happy
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > 10:
        show anna_3 flirty
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if 6 <= C <= 10:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > 10:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))


    "I take a seat and class begins."
    p "\"Alright, everyone. Today you'll be working on a group project. The assignment is simple. All you have to do is present information on three philosophers that we've learned about so far.\""
    p "\"You will be graded as a group on accuracy, creativity, and the extent of your collective knowledge. The project is due at the end of class.\""
    "Then, Dr. Paige sits down at his large wooden desk and starts a crossword."
    $ renpy.show(custom_show("maddie", "uncomf"), [trueleft])
    $ renpy.show(custom_show("anna", "uncomf"), [])
    $ renpy.show(custom_show("erin", "uncomf"), [trueright])

    "Maddie, Anna, Erin, and I look around at one another in slight confusion, slowly realizing those vague instructions are all we're going to be given."
    "We gather our things and move closer together."
    $ renpy.hide(custom_hide("maddie"))
    $ renpy.hide(custom_hide("anna"))
    $ renpy.hide(custom_hide("erin"))
    $ renpy.show(custom_show("anna", "normal"), [trueleft])
    b "\"I think we should keep it simple. We can make a diagram for each of the philosophers.\""
    $ renpy.show(custom_show("anna", "happy"), [trueleft])
    b "\"It's the easiest way to cover the most amount of information--their ideals, cultural impact, key events in their lives.\""
    $ renpy.show(custom_show("erin", "uncomf"), [trueright])
    c "\"Hm, I don't know. Dr. Paige said we'd be graded on creativity, not just our knowledge...\""
    c "\"What if we did a mosaic of each of the philosophers? And we can fill each of their portraits with words related to their work.\""
    $ renpy.show(custom_show("anna", "uncomf"), [trueleft])
    $ renpy.show(custom_show("erin", "sad"), [trueright])
    b "\"I'm not sure we'll have time to do something like that.\""
    $ renpy.show(custom_show("maddie", "happy"), [])
    a "\"What about a skit? We could write a script where three of us play the different philosophers, and one of us can be an interviewer that asks questions about their lives and beliefs and stuff.\""
    a "\"Then, we perform it at the end of class. That could be cool.\""
    $ renpy.show(custom_show("erin", "embarrassed"), [trueright])
    c "\"Oh, I have stage fright. Maybe we can do something else?\""
    $ renpy.show(custom_show("maddie", "angry"), [])
    a "\"It'd only be in front of Dr. Paige.\""
    $ renpy.show(custom_show("erin", "surprised"), [trueright])
    c "\"Yeah, I guess...\""
    $ renpy.show(custom_show("anna", "angry"), [trueleft])
    b "\"...\""
    $ renpy.show(custom_show("maddie", "flirty"), [])
    a "\"I know, why don't we let Sam pick? We have three ideas here, he can decide which one we go with.\""
    $ renpy.show(custom_show("anna", "flirty"), [trueleft])
    b "\"That seems fair.\""
    $ renpy.show(custom_show("erin", "flirty"), [trueright])
    c "\"Okay!\""
    $ renpy.hide(custom_hide("anna"))
    $ renpy.hide(custom_hide("erin"))
    $ renpy.show(custom_show("maddie", "happy"), [])
    a "\"So what do you think? What kind of project should we do?\""

    menu: 
        "Skit":

            $A = A+1
            $B = B-1
            n "\"I kind of like the skit idea. It sounds fun.\""
            $ renpy.show(custom_show("maddie", "flirty"), [])
            a "\"Awesome! It's settled then.\""
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "sad"), [])
            b "\"...\""
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "sad"), [])
            c "\"Aww...\""
            $ renpy.hide(custom_hide("erin"))
            "We spend the rest of the class period writing out a script, practicing our parts, and, finally, performing for Dr. Paige."
            p "\"Well, that was lively! It was like Descartes, Aristotle, and Hobbes were right here in front of me. Good work!\""

        "Diagram":
            $ renpy.hide(custom_hide("maddie"))
            $B = B+1
            n "\"I kind of like the diagram idea. It seems the most efficient.\""
            $ renpy.show(custom_show("anna", "flirty"), [])
            "Anna's disposition brightens as she pulls out her craft paper and colored pens."
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "sad"), [])
            c "\"Aww...\""
            $ renpy.hide(custom_hide("erin"))
            show maddie_3 sad
            a "\"Oh...\""
            $ renpy.hide(custom_hide("maddie"))
            "We spend the rest of the class period working on the diagrams before finally turning them in."
            p "\"Wow! This is one of the most thorough projects I've seen. Well done!\""

        "Mosaic":
            $ renpy.hide(custom_hide("maddie"))
            $C = C+1
            n "\"I kind of like the mosaic idea. It sounds interesting.\""
            $ renpy.show(custom_show("erin", "flirty"), [])
            c "\"Really? Thanks, Sam.\""
            $ renpy.hide(custom_hide("erin"))
            $ renpy.show(custom_show("maddie", "sad"), [])
            a "\"Oh...\""
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "sad"), [])
            b "\"...\""
            $ renpy.hide(custom_hide("anna"))
            "We spend the rest of the class period sketching out outlines for the mosaics, inking them, and then filling them in with words, phrases, and sayings associated with their respective philosophers."
            "We turn in the project just before four o'clock."
            p "\"How artistic! Beautifully done!\""

        "I can't decide, let's leave it to chance.":
            n "\"Why don't we just pick an idea at random? Since we can't decide.\""
            $ renpy.show(custom_show("maddie", "sad"), [])
            a "\"Yeah, I guess we can do that...\""
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "sad"), [])
            b "\"Okay...\""
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "sad"), [])
            c "\"Awww\""
            $ renpy.hide(custom_hide("erin"))
            "Maddie, Anna, and Erin all seem a little disappointed."
            "I write down \"diagram,\" \"mosaic,\" and \"skit\" on three separate sticky notes and fold them in half."
            "After shuffling the options, I select one."
            n "\"Looks like we're doing the skit.\""
            $ renpy.show(custom_show("maddie", "normal"), [])
            a "\"Awesome! It's settled then.\""
            $ renpy.hide(custom_hide("maddie"))
            "We spend the rest of the class period writing out a script, practicing our parts, and, finally, performing our skit for Dr. Paige."
            p "\"Well, that was lively! It was like Descartes, Aristotle, and Hobbes were right here in front of me. Good work!\""
    
    scene black with fade
    stop music fadeout 1.0
    "Dr. Paige dismisses us for the day"
    scene bg_class_after with fade
    "I have some time to kill before dinner. What should I do?"

    jump after_class
    return

label ch2_schoolday2:
    $ day = day + 1
    scene bg_class with fade
    play music "audio/class.mp3"

    "On Thursday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."
    if 6 <= A <= 10:
        show maddie_4 happy
        a "\"Hey, Sam!\""
        hide maddie_4
    elif A > 10:
        show maddie_4 flirty
        a "\"Hey, Sam, sit with me!\""
        hide maddie_4
    if 6 <= B <= 10:
        show anna_4 happy
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > 10:
        show anna_4 flirty
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if 6 <= C <= 10:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > 10:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))

    "I take a seat and class begins."
    p "\"I wanted to start class off a little differently today. Since we've been talking about different philosophies and worldviews, I would like to hear about your personal perspectives.\""
    p "\"What are some values or codes that you follow? By what mindset do you navigate the world?\""
    "The wall clock ticks as we think. Then, I raise my hand."
    p "\"Sam?\""

    menu:
        "I believe in discipline and hard work":
            $ A = A + 2
            n "\"I believe in working hard in all that I do. It's important for me to approach hurdles in life with discipline and endurance.\""
            p "\"That's a great answer, Sam. Anyone else?\""
            "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

            "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

            "My perspective on life was fickle, easily changing, and not always for the best."

            if A >= B and A >= C:
                $girl = "Maddie"
            if B >= A and B >= C:
                $girl = "Anna"
            if C >= A and C >= B:
                $girl = "Erin"

            "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


        "I believe in staying curious":
            $ B = B + 2
            n "\"I believe in trying to navigate the world with discernment and wisdom. I want to stay curious, applying the lessons I learn to the life I live.\""
            p "\"That's a great answer, Sam. Anyone else?\""
            "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

            "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

            "My perspective on life was fickle, easily changing, and not always for the best."

            if A >= B and A >= C:
                $girl = "Maddie"
            if B >= A and B >= C:
                $girl = "Anna"
            if C >= A and C >= B:
                $girl = "Erin"

            "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


        "I believe in learning from one another":
            $ C = C + 2
            n "\"I believe in learning as much as I can from those who know more than me. And, hopefully, becoming someone that others can learn from as well. I think that's the best way to grow.\""
            p "\"That's a great answer, Sam. Anyone else?\""
            "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

            "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

            "My perspective on life was fickle, easily changing, and not always for the best."

            if A >= B && A >= C:
                $girl = "Maddie"
            if B >= A && B >= C:
                $girl = "Anna"
            if C >= A && C >= B:
                $girl = "Erin"

            "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


        "I believe in doing whatever makes you happy":
            n "\"I believe in living a life that makes you happy. Happiness and money are the only things worth pursuing in this world.\""
            p "\"That's an…interesting thought, Sam. Anyone else?\""
            "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how none of this really matters."

            "Who cares about our outlooks or 'codes.'"

            "The truth is, the world is unfair and adding rules for yourself isn't going to help you get ahead. No one else is going to look out for you."

            "So do whatever you have to do to be happy."


    scene black with fade
    stop music fadeout 1.0
    "After he finishes going around the room, Dr. Paige continues on with the day's lesson, dismissing us, as always, at four o'clock."

    scene bg_class_after with fade

    "I have some time to kill before dinner. What should I do?"

    jump after_class
    return

label ch2_weekend:
    $ day = day + 1
    scene bg_room with fade
    play music "audio/dorm.mp3"

    if date == True:
        "Finally, the week's over."
        "Usually, I'd just stay home--sleep in, watch TV, play some games, talk to Neko-Chan. But I actually have a reason to go out this weekend."
        stop music fadeout 1.0
        play music "audio/event.mp3"
        if eventba_trigger:
            jump event_ba
        elif eventbb_trigger:
            jump event_bb 
        elif eventbc_trigger:
            jump event_bc

    else: 
        "I can't believe it's already the weekend. I wish I had something to do…"
        "I laze around my dorm, playing games and watching TV, until the next school day."
        stop music fadeout 1.0
        scene black with fade
        jump ch3_schoolday1
    return

label ch3_schoolday1:
    scene bg_room with fade
    play music "audio/dorm.mp3"
    $ day = day + 1

    "I wake up and my head feels heavy. There's a pulse at the front of my skull, a stuffiness in my ears. It's Tuesday, but I don't think I'll be able to go to class."
    "I get out my phone and write an email to Dr. Paige explaining the situation, and shortly after pressing send, I drift back to sleep."
    "When I wake up again, it's 3:30pm."
    n "\"Man, I can't believe I slept through the afternoon...\""
    "I put a palm to my forehead--it's a little warm. All around me are laundry and dishes that need cleaning, and I wonder how my dorm got so out of hand. Lying there in bed, I feel equally like a part of the mess."
    "What should I do?"
    menu: 
        "Go back to sleep, I need the rest":
            "I close my eyes again and feel the clutter around me grow increasingly distant until I've succumbed to my tired mind and fallen back asleep."
            "I wake up to the sound of knocking at my door, the time on my phone now reading 4:12pm."
        "Clean my room, it needs to be done":
            $ clean = True
            "I pick my dirty laundry off the floor and put it in the hamper. I take the scattered pieces of trash in my room and throw them away. I vacuum the carpet, wipe down my shelves, wash the dishes, and change my sheets."
            "Just as I've finished cleaning, I hear a knock at my door."
    stop music fadeout 1.0
    scene black with fade
    jump event_d
    return

label ch3_schoolday2:
    scene bg_class with fade
    play music "audio/class.mp3"
    $ day = day + 1
    "On Thursday, I walk into class where Dr. Paige, Maddie, Anna, and Erin are already inside."
    if 6 <= A <= 10:
        show maddie_1 happy
        a "\"Hey, Sam!\""
        hide maddie_1
    elif A > 10:
        show maddie_1 flirty
        a "\"Hey, Sam, sit with me!\""
        hide maddie_1
    if 6 <= B <= 10:
        show anna_1 happy
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > 10:
        show anna_1 flirty
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if 6 <= C <= 10:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > 10:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))
        
    "I take a seat and class begins."
    "Dr. Paige moves around the room, placing papers face down on our desks, and when he reaches me, he offers a nod."
    p "\"I'm glad to see you're feeling better, Sam. Ready for the final?\""
    
    menu:
        "Ha, no":
            $ A = A + 1
            n "\"Do I still have to take it if I'm not?\""
            p "\"Haha... yes.\""

        "Definitely":
            $ B = B + 1
            n "\"I wouldn't be here if I wasn't.\""
            p "\"That's what I like to hear.\""

        "Maybe":
            $ C = C + 1
            n "\"Eh, I'm prepared to try my best.\""
            p "\"Let's hope your best is good enough then, hm?\""

    "He returns to the front of the class and glances at the clock on the wall-- there's less than a minute until one."

    p "\"Before we begin, I just want to say it's been a pleasure having you all in this class. I hope we'll get the opportunity to cross paths again during your collegiate career.\""
    p "\"Though, not in Intro to Philosophy.\""
    p "\"I would like you to pass this class.\""

    "Dr. Paige clears his throat."
    
    p "\"I digress. You may now open your exam books and flip over the papers on your desks. The instructions for your final are written there. Good luck.\""
    scene black with fade
    stop music fadeout 1.0

    "We write in our booklets, racing against the ticking clock."

    "And by the time I finish the exam, I'm exhausted."
    scene bg_class_after with fade

    if grade >= 4:
        "Though I'm the last one to leave, I know it's just because I triple checked my answers."
        "I have a feeling I did pretty well."
    else:
        "It's a little embarrassing that I'm the last one to leave, but I guess that's what I get for not studying enough."
        "I can only hope that I passed."
    
    scene bg_room_afterclass with fade
    play music "audio/free.mp3"

    "I head back to my dorm, too drained to do anything else, and though I know I should be relieved that I'm done with Intro to Philosophy, I'm left with a bittersweet sentiment."

    python:
        if a_number_obtained_flag:
            if b_number_obtained_flag:
                if c_number_obtained_flag:
                    char_string = "Maddie, Anna, or Erin"
                else:
                    char_string = "Maddie or Anna"
            else:
                char_string = "Maddie"
        else:
            if b_number_obtained_flag:
                if c_number_obtained_flag:
                    char_string = "Anna or Erin"
                else:
                    char_string = "Anna"
            else:
                if c_number_obtained_flag:
                    char_string = "Erin"
                else:
                    char_string = "NONE"

    if char_string == "NONE":
        scene black with fade
        stop music fadeout 1.0
        $ d_ending_success = True
        "I think some people might see my life and assume I'm lonely. But I'm actually okay."
        "As I look at Neko-Chan, I think about how she is the only girl in my life who could never hurt me."
        "Real girls are too complicated."
        "Too confusing."
        "They expect too much."
        "Neko-Chan doesn't expect anything. She accepts me the way I am."
        "And that's enough for me."
        jump credits
        return
    else:
        "The LU campus is pretty big. There's no guarantee that I'll get a chance to see [char_string] again."
        "If there's something I need to say, I should say it now."
    
    menu:
        "Confess feelings to Maddie" if a_number_obtained_flag:
            $ a_ending = True
            jump event_ending
        "Confess feelings to Anna" if b_number_obtained_flag:
            $ b_ending = True
            jump event_ending
        "Confess feelings to Erin" if c_number_obtained_flag:
            $ c_ending = True
            jump event_ending
        "I have nothing to say":
            "I think some people might see my life and assume I'm lonely. But I'm actually okay."
            "As I look at Neko-Chan, I think about how she is the only girl in my life who could never hurt me."
            "Real girls are too complicated."
            "Too confusing."
            "They expect too much."
            "Neko-Chan doesn't expect anything. She accepts me the way I am."
            "And that's enough for me."
            $ d_ending_success = True
            jump credits

    stop music fadeout 1.0
    return

label event_ending:
    scene bg_room with fade
    play music "audio/event.mp3"

    "I take a deep breath."
    "I don't know much about this kind of thing, but if I'm really going to do this, I feel like I should bring a gift. Luckily, I have a couple hours before dusk to get something."
    scene options with fade
    "What should I give her?"

    menu:
        "A potted succulent":
            $ maddie_gift = True
            "I swing by the local nursery and pick up a succulent before heading back to campus."
        "A venus fly trap":
            $ anna_gift = True
            "I grab a venus fly trap at a pet shop before heading back to campus."
        "A bouquet of sunflowers":
            $ erin_gift = True
            "I pick up a bouquet of sunflowers from a flower shop before heading back to campus."
        "A single rose":
            "I buy a single rose from the grocery store before heading back to campus."
    
    if a_ending:
        jump event_ca
    elif b_ending:
        jump event_cb
    else:
        jump event_cc

    return
