label act1_scene1:
    stop music fadeout 1.0
    scene black with dissolve
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause(1)
    show calendar_01a with dissolve
    with Pause (1)
    show calendar_01b with dissolve
    with Pause (2)
    scene bg_class_a with dissolve
    play music "audio/class.mp3" fadein 1.0
    "Right as I enter the classroom, I stop in my tracks."

    scene event_intro_b with dissolve
    "There's a girl reading in the corner, so invested in her book that she doesn't even look up at the sound of the door closing behind me."
    "She curls a strand of hair behind her ear before turning a page."
    "I've seen her around campus but never actually worked up the courage to talk to her."
    "And how could I?"
    "She's way out of my league."
    "Besides, I hear she doesn't really date."

    scene bg_class_a with dissolve
    "I look away to avoid staring and pass the professor at his large wooden desk before taking a seat."
    "The only noise in the otherwise quiet room is the whirr of the air conditioner and the ticking of a clock that shows we have two minutes until class begins."
    "Soon, the door opens, and I glance up only to quickly look back down. With my elbow resting on my desk, I cup my hand above my eyes, hoping she doesn't notice me."
    "It's Maddie Geller."
    "We went to the same elementary, junior high, high school, and now, it would seem, we're at the same college too."

    scene event_intro_a with dissolve
    a "\'Sam? No way! I didn't know you went to LU.\'"
    n "\'Maddie! Wow, yeah, you came here too I guess.\'"
    "What are the chances…"
    p "\'Alright, everyone. Settle in, we're about to start class.\'"
    "Maddie turns back to me, causing her ponytail to sway."

    scene bg_class_a with dissolve
    $ renpy.show(custom_show("maddie", "F"), [])
    a "\'It's great to see you, Sam. Maybe we can catch up later.\'"

    $ renpy.hide(custom_hide("maddie")) 
    "She drops down into her seat and starts digging through her backpack."
    "I'm a little shocked. No snide remarks? No teasing? She actually seemed pleasant for once."
    p "\'Let's get the ball rolling, shall we? My name is Dr. Paige and, as you already know, this is Intro to Philosophy.\'"
    p "\'We'll be meeting here from one to four, Tuesday and Thursday for three weeks.\'"
    p "\'Be aware that you'll be expected to use the days we don't meet to do assigned reading and respond to the quizzes I'll be posting on our class website.\'"
    p "\'I will be available for correspondence via email. Any questions?\'"
    "The wall clock ticks."
    p "\'Alright then, I'll take that as a 'no.' Now,  why don't we go around, introduce ourselves, and say at least one thing we're looking forward to learning over these next few weeks.\'"
    "Dr. Paige nods to Maddie."
    p "\'Why don't you start us off?\'"

    $ renpy.show(custom_show("maddie", "N"), [])
    a "\'Sure. My name is Maddie, and what I'm looking forward to most in this class is...\'"
    "She scratches the back of her head while she thinks."

    $ renpy.show(custom_show("maddie", "U"), [])
    a "\'...the challenge of learning about a topic I don't know much about.\'"

    $ renpy.hide(custom_hide("maddie")) 
    $ renpy.show(custom_show("anna", "U"), [])
    "The girl who was reading before class sits up tall in her chair with her book now closed on her desk."
    
    $ renpy.show(custom_show("anna", "H"), [])
    b "\'I'm Anna. I look forward to hearing about the great philosophers in history and what observations they made about our world.\'"
    
    $ renpy.hide(custom_hide("anna"))

    scene event_intro_c with dissolve
    "The classroom door swings open to reveal a girl who is clearly out of breath."
    c "\'Sorry I'm late. I got lost.\'"
    p "\'No trouble. We were just going over introductions. Why don't you go next? Tell us your name and something you're excited about learning in this class.\'"
   
    scene bg_class_a with dissolve
    $ renpy.show(custom_show("erin", "E"), [])
    c "\'Uh...I guess just...\'"

    $ renpy.show(custom_show("erin", "U"), [])
    c "\'...seeing things through new perspectives? Learning how to look at life in ways that I hadn't thought of before.\'"
    
    $ renpy.show(custom_show("erin", "H"), [])
    c "\'Oh, and my name's Erin.\'"
    
    $ renpy.hide(custom_hide("erin"))
    "As Erin takes her seat, she wears a smile."
    "She has a genuine warmth and kindness about her that lights up the room. I've never seen someone look so happy before a lecture."
    "Finally, the professor turns to me."
    p "\'What about you? What are you looking forward to?\'"

    menu:
        "The challenge":
            $ A = A + 2
            n "\'My name's Sam. And, I'm excited to push myself. I've heard this class can be pretty tough, but I think it'll be good for me.\'"
            $ renpy.show(custom_show("maddie", "N"), [])
            a "\'...\'"
            $ renpy.hide(custom_hide("maddie"))

        "The philosophers":
            $ B = B + 2
            n "\'My name's Sam. And, I'm excited to learn from the philosophers we'll study and hopefully apply some of their wisdom to my life.\'"
            $ renpy.show(custom_show("anna", "N"), [])
            b "\'...\'"
            $ renpy.hide(custom_hide("anna"))

        "The perspectives":
            $ C = C + 2
            n "\'My name's Sam. And, I'm excited to hear different points of view. I'm just one person and the world's a big place. Maybe I'm missing something.\'"
            $ renpy.show(custom_show("erin", "N"), [])
            c "\'...\'"
            $ renpy.hide(custom_hide("erin"))

        "The course credits":
            n "\'My name's Sam. And, honestly, I'm just here for the credits.\'"

    p "\'Alright then. Now that we're all acquainted, let's get on with the lesson.\'"

    scene black with fade
    stop music fadeout 1.0
    "Dr. Paige lectures for the remainder of the class period and then dismisses us for the day."
    
    scene bg_class_b with dissolve
    "I'm still packing up when the other students take off."
    "By the time I get outside, Maddie is already heading to the westside of campus towards the school gym."
    "Anna is heading to the northside of campus towards the library, and Erin is heading to the eastside of campus towards the art building."
    "I have some time to kill before dinner. What should I do?"
    
    jump after_class
    

label act1_scene2:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_class_a with dissolve
    play music "audio/class.mp3" fadein 1.0
    "On Thursday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."

    if A_mid <= A <= A_mid3:
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Hey, Sam!\'"
        $ renpy.hide(custom_hide("maddie"))
    elif A >= A_high:
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Hey, Sam, sit with me!\'"
        $ renpy.hide(custom_hide("maddie"))
    if B_mid <= B <= B_mid3:
        $ renpy.show(custom_show("anna", "H"), [])
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > B_high:
        $ renpy.show(custom_show("anna", "H"), [])
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if C_mid <= C <= C_mid3:
        $ renpy.show(custom_show("erin", "H"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > C_high:
        $ renpy.show(custom_show("erin", "F"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))

    "I take a seat and class begins."
    "Dr. Paige stands at the front of the room while he lectures, using grand hand movements to emphasize his words and occasionally writing key terms on the board."
    "What should I do?"

    # $  randnotice = renpy.random.choice(['notice', 'or not'])
    menu:
        "Get out my grip strengthener":
            $ A = A+1
            "If I have to sit here for a few hours, I might as well multitask."
            "I retrieve my grip strengthener from my backpack and practice squeezing the handles together, switching hands periodically."
            # if randnotice == 'notice':
            $ renpy.show(custom_show("maddie", "N"), [])
            "Out of the corner of my eye, I catch Maddie looking my way."
            $ renpy.hide(custom_hide("maddie"))

        "Take notes diligently":
            $ B = B+1
            "What Dr. Paige is saying seems important. I should pay close attention."
            "I open my notebook and take down his main points."
            # if randnotice == 'notice':
            $ renpy.show(custom_show("anna", "N"), [])
            "Out of the corner of my eye, I catch Anna looking my way."
            $ renpy.hide(custom_hide("anna"))

        "Doodle":
            $ C = C+1
            "While listening to Dr. Paige, I start sketching in my notebook."
            "Before I know it, a page intended for philosophy notes is covered in drawings."
            # if randnotice == 'notice':
            $ renpy.show(custom_show("erin", "N"), [])
            "Out of the corner of my eye, I catch Erin looking my way."
            $ renpy.hide(custom_hide("erin"))

        "Sit back and wait for class to end":
            "I sit back in my chair and count down the hours to the end of class."

    scene black with fade
    stop music fadeout 1.0
    "Eventually, Dr. Paige dismisses us for the day."

    scene bg_class_b with dissolve
    "I have some time to kill before dinner. What should I do?"
    
    jump after_class


label act2_scene1:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_class_a with dissolve
    play music "audio/class.mp3" fadein 1.0

    "On Tuesday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."
    if A_mid <= A <= A_mid3:
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Hey, Sam!\'"
        $ renpy.hide(custom_hide("maddie"))
    elif A >= A_high:
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Hey, Sam, sit with me!\'"
        $ renpy.hide(custom_hide("maddie"))
    if B_mid <= B <= B_mid3:
        $ renpy.show(custom_show("anna", "H"), [])
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > B_high:
        $ renpy.show(custom_show("anna", "H"), [])
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if C_mid <= C <= C_mid3:
        $ renpy.show(custom_show("erin", "H"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > C_high:
        $ renpy.show(custom_show("erin", "F"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))

    "I take a seat and class begins."
    p "\'Alright, everyone. Today you'll be working on a group project. The assignment is simple. All you have to do is present information on three philosophers that we've learned about so far.\'"
    p "\'You will be graded as a group on accuracy, creativity, and the extent of your collective knowledge. The project is due at the end of class.\'"
    "Then, Dr. Paige sits down at his large wooden desk and starts a crossword."
    $ renpy.show(custom_show("maddie", "U"), [trueleft])
    with dissolve
    $ renpy.show(custom_show("anna", "U"), [])
    with dissolve
    $ renpy.show(custom_show("erin", "U"), [trueright])
    with dissolve

    "Maddie, Anna, Erin, and I look around at one another in slight confusion, slowly realizing those vague instructions are all we're going to be given."
    "We gather our things and move closer together."
    $ renpy.hide(custom_hide("maddie"))
    $ renpy.hide(custom_hide("anna"))
    $ renpy.hide(custom_hide("erin"))
    $ renpy.show(custom_show("anna", "N"), [trueleft])
    b "\'I think we should keep it simple. We can make a diagram for each of the philosophers.\'"
    $ renpy.show(custom_show("anna", "H"), [trueleft])
    b "\'It's the easiest way to cover the most amount of information--their ideals, cultural impact, key events in their lives.\'"
    $ renpy.show(custom_show("erin", "U"), [trueright])
    c "\'Hm, I don't know. Dr. Paige said we'd be graded on creativity, not just our knowledge...\'"
    c "\'What if we did a mosaic of each of the philosophers? And we can fill each of their portraits with words related to their work.\'"
    $ renpy.show(custom_show("anna", "U"), [trueleft])
    $ renpy.show(custom_show("erin", "S"), [trueright])
    b "\'I'm not sure we'll have time to do something like that.\'"
    $ renpy.show(custom_show("maddie", "H"), [])
    a "\'What about a skit? We could write a script where three of us play the different philosophers, and one of us can be an interviewer that asks questions about their lives and beliefs and stuff.\'"
    a "\'Then, we perform it at the end of class. That could be cool.\'"
    $ renpy.show(custom_show("erin", "E"), [trueright])
    c "\'Oh, I have stage fright. Maybe we can do something else?\'"
    $ renpy.show(custom_show("maddie", "A"), [])
    a "\'It'd only be in front of Dr. Paige.\'"
    $ renpy.show(custom_show("erin", "E"), [trueright])
    c "\'Yeah, I guess...\'"
    $ renpy.show(custom_show("anna", "A"), [trueleft])
    b "\'...\'"
    $ renpy.show(custom_show("maddie", "F"), [])
    a "\'I know, why don't we let Sam pick? We have three ideas here, he can decide which one we go with.\'"
    $ renpy.show(custom_show("anna", "F"), [trueleft])
    b "\'That seems fair.\'"
    $ renpy.show(custom_show("erin", "F"), [trueright])
    c "\'Okay!\'"
    $ renpy.hide(custom_hide("anna"))
    $ renpy.hide(custom_hide("erin"))
    $ renpy.show(custom_show("maddie", "H"), [])
    a "\'So what do you think? What kind of project should we do?\'"

    menu: 
        "Skit":

            $ A = A+1
            $ B = B-1
            n "\'I kind of like the skit idea. It sounds fun.\'"
            $ renpy.show(custom_show("maddie", "F"), [])
            a "\'Awesome! It's settled then.\'"
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "E2"), [])
            b "\'...\'"
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "S"), [])
            c "\'Aww...\'"
            $ renpy.hide(custom_hide("erin"))
            "We spend the rest of the class period writing out a script, practicing our parts, and, finally, performing for Dr. Paige."
            p "\'Well, that was lively! It was like Descartes, Aristotle, and Hobbes were right here in front of me. Good work!\'"

        "Diagram":
            $ renpy.hide(custom_hide("maddie"))
            $ B = B+1
            n "\'I kind of like the diagram idea. It seems the most efficient.\'"
            $ renpy.show(custom_show("anna", "F"), [])
            "Anna's disposition brightens as she pulls out her craft paper and colored pens."
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "S"), [])
            c "\'Aww...\'"
            $ renpy.hide(custom_hide("erin"))
            $ renpy.show(custom_show("maddie", "S"), [])
            a "\'Oh...\'"
            $ renpy.hide(custom_hide("maddie"))
            "We spend the rest of the class period working on the diagrams before finally turning them in."
            p "\'Wow! This is one of the most thorough projects I've seen. Well done!\'"

        "Mosaic":
            $ renpy.hide(custom_hide("maddie"))
            $ C = C+1
            n "\'I kind of like the mosaic idea. It sounds interesting.\'"
            $ renpy.show(custom_show("erin", "F"), [])
            c "\'Really? Thanks, Sam.\'"
            $ renpy.hide(custom_hide("erin"))
            $ renpy.show(custom_show("maddie", "S"), [])
            a "\'Oh...\'"
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "E2"), [])
            b "\'...\'"
            $ renpy.hide(custom_hide("anna"))
            "We spend the rest of the class period sketching out outlines for the mosaics, inking them, and then filling them in with words, phrases, and sayings associated with their respective philosophers."
            "We turn in the project just before four o'clock."
            p "\'How artistic! Beautifully done!\'"

        "I can't decide, let's leave it to chance.":
            n "\'Why don't we just pick an idea at random? Since we can't decide.\'"
            $ renpy.show(custom_show("maddie", "S"), [])
            a "\'Yeah, I guess we can do that...\'"
            $ renpy.hide(custom_hide("maddie"))
            $ renpy.show(custom_show("anna", "E2"), [])
            b "\'Okay...\'"
            $ renpy.hide(custom_hide("anna"))
            $ renpy.show(custom_show("erin", "S"), [])
            c "\'Awww\'"
            $ renpy.hide(custom_hide("erin"))
            "Maddie, Anna, and Erin all seem a little disappointed."
            "I write down \'diagram,\' \'mosaic,\' and \'skit\' on three separate sticky notes and fold them in half."
            "After shuffling the options, I select one."
            n "\'Looks like we're doing the skit.\'"
            $ renpy.show(custom_show("maddie", "N"), [])
            a "\'Awesome! It's settled then.\'"
            $ renpy.hide(custom_hide("maddie"))    
            "We spend the rest of the class period writing out a script, practicing our parts, and, finally, performing our skit for Dr. Paige."
            p "\'Well, that was lively! It was like Descartes, Aristotle, and Hobbes were right here in front of me. Good work!\'"
    
    scene black with fade
    stop music fadeout 1.0
    "Dr. Paige dismisses us for the day."
    scene bg_class_b with dissolve
    "I have some time to kill before dinner. What should I do?"

    jump after_class


label act2_scene2:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_class_a with dissolve
    play music "audio/class.mp3" fadein 1.0

    "On Thursday, I walk into class and find Dr. Paige, Maddie, Anna, and Erin already inside."

    "I take a seat and class begins."
    p "\'I wanted to start class off a little differently today. Since we've been talking about different philosophies and worldviews, I would like to hear about your personal perspectives.\'"
    p "\'What are some values or codes that you follow? By what mindset do you navigate the world?\'"

    $ max_amount = max(A,B,C)
    if A == max_amount:
        $ girl = "Maddie"
    if B == max_amount:
        $ girl = "Anna"
    if C == max_amount:
        $ girl = "Erin"

    if max_amount > 5:
        "The wall clock ticks as we think. Then, I raise my hand."
        p "\'Sam?\'"

        menu:
            "I believe in discipline and hard work":
                $ A = A + 2
                n "\'I believe in working hard in all that I do. It's important for me to approach hurdles in life with discipline and endurance.\'"
                p "\'That's a great answer, Sam. Anyone else?\'"
                "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

                "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

                "My perspective on life was fickle, easily changing, and not always for the best."

                "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


            "I believe in staying curious":
                $ B = B + 2
                n "\'I believe in trying to navigate the world with discernment and wisdom. I want to stay curious, applying the lessons I learn to the life I live.\'"
                p "\'That's a great answer, Sam. Anyone else?\'"
                "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

                "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

                "My perspective on life was fickle, easily changing, and not always for the best."

                "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


            "I believe in learning from one another":
                $ C = C + 2
                n "\'I believe in learning as much as I can from those who know more than me. And, hopefully, becoming someone that others can learn from as well. I think that's the best way to grow.\'"
                p "\'That's a great answer, Sam. Anyone else?\'"
                "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how much I've changed over these past couple weeks."

                "When I first started this class, I'm not sure I would've been able to clearly talk about my outlook or values."

                "My perspective on life was fickle, easily changing, and not always for the best."

                "I don't know why, maybe it's the class. Maybe it's [girl]. But I'm a lot happier with the person I've been lately."


            "I believe in doing whatever makes you happy":
                n "\'I believe in living a life that makes you happy. Happiness and money are the only things worth pursuing in this world.\'"
                p "\'That's an…interesting thought, Sam. Anyone else?\'"
                "As Dr. Paige moves his attention to Maddie, Anna, and Erin, listening to them each talk about their personal worldviews, I can't help but think about how none of this really matters."

                "Who cares about our outlooks or 'codes.'"

                "The truth is, the world is unfair and adding rules for yourself isn't going to help you get ahead. No one else is going to look out for you."

                "So do whatever you have to do to be happy."

        scene black with fade
        stop music fadeout 1.0
        "After he finishes going around the room, Dr. Paige continues on with the day's lesson, dismissing us, as always, at four o'clock."
    else:
        "As Dr. Paige makes his way around the room, Maddie, Anna, and Erin each talk about their personal worldviews while I rack my brain for something to say."
        "What do I believe? What are the guiding values in my life?"
        p "\'Alright, last one. What do you think, Sam?\'"

        "By what mindset do I navigate the world?"

        menu:
            "I believe in discipline and hard work":
                $ A = A + 2
                n "\'I believe in working hard in all that I do. It's important for me to approach hurdles in life with discipline and endurance.\'"
                p "\'That's a great answer, Sam.\'"

            "I believe in staying curious":
                $ B = B + 2
                n "\'I believe in trying to navigate the world with discernment and wisdom. I want to stay curious, applying the lessons I learn to the life I live.\'"
                p "\'That's a great answer, Sam.\'"

            "I believe in learning from one another":
                $ C = C + 2
                n "\'I believe in learning as much as I can from those who know more than me. And, hopefully, becoming someone that others can learn from as well. I think that's the best way to grow.\'"
                p "\'That's a great answer, Sam. \'"

            "I believe in doing whatever makes you happy":
                n "\'I believe in living a life that makes you happy. Happiness and money are the only things worth pursuing in this world.\'"
                p "\'That's an…interesting thought, Sam.\'"
                "As Dr. Paige starts lecturing, I can't help but think about how none of this really matters."

                "Who cares about our outlooks or 'codes.'"

                "The truth is, the world is unfair and adding rules for yourself isn't going to help you get ahead. No one else is going to look out for you."

                "So do whatever you have to do to be happy."

        scene black with fade
        stop music fadeout 1.0
        "Dr. Paige continues on with the day's lesson, dismissing us, as always, at four o'clock."

    scene bg_class_b with dissolve

    "I have some time to kill before dinner. What should I do?"

    jump after_class


label act3_scene2:
    scene bg_class_a with dissolve
    play music "audio/class.mp3" fadein 1.0
    "On Thursday, I walk into class where Dr. Paige, Maddie, Anna, and Erin are already inside."
    if A_mid <= A <= A_mid3:
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Hey, Sam!\'"
        $ renpy.hide(custom_hide("maddie"))
    elif A >= A_high:
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Hey, Sam, sit with me!\'"
        $ renpy.hide(custom_hide("maddie"))
    if B_mid <= B <= B_mid3:
        $ renpy.show(custom_show("anna", "H"), [])
        b "Anna smiles at me before returning to her book."
        $ renpy.hide(custom_hide("anna"))
    elif B > B_high:
        $ renpy.show(custom_show("anna", "F"), [])
        b "Anna smiles at me."
        $ renpy.hide(custom_hide("anna"))
    if C_mid <= C <= C_mid3:
        $ renpy.show(custom_show("erin", "H"), [])
        c "Erin waves at me."
        $ renpy.hide(custom_hide("erin"))
    elif C > C_high:
        $ renpy.show(custom_show("erin", "F"), [])
        c "Erin waves at me, beaming."
        $ renpy.hide(custom_hide("erin"))

    "I take a seat and class begins."
    "Dr. Paige moves around the room, placing papers face down on our desks, and when he reaches me, he offers a nod."
    p "\'I'm glad to see you're feeling better, Sam. Ready for the final?\'"
    
    menu:
        "Ha, no":
            $ A = A + 1
            n "\'Do I still have to take it if I'm not?\'"
            p "\'Haha...yes.\'"

        "Definitely":
            $ B = B + 1
            n "\'I wouldn't be here if I wasn't.\'"
            p "\'That's what I like to hear.\'"

        "Maybe":
            $ C = C + 1
            n "\'Eh, I'm prepared to try my best.\'"
            p "\'Let's hope your best is good enough then, hm?\'"

    "He returns to the front of the class and glances at the clock on the wall--there's less than a minute until one."

    p "\'Before we begin, I just want to say it's been a pleasure having you all in this class. I hope we'll get the opportunity to cross paths again during your collegiate career.\'"
    p "\'Though, not in Intro to Philosophy.\'"
    p "\'I would like you to pass this class.\'"

    "Dr. Paige clears his throat."
    
    p "\'I digress. You may now open your exam books and flip over the papers on your desks. The instructions for your final are written there. Good luck.\'"
    scene black with fade
    stop music fadeout 1.0

    "We write in our booklets, racing against the ticking clock."

    "And by the time I finish the exam, I'm exhausted."
    scene bg_class_b with dissolve

    if class_score >= 4:
        "Though I'm the last one to leave, I know it's just because I triple checked my answers."
        "I have a feeling I did pretty well."
    else:
        "It's a little embarrassing that I'm the last one to leave, but I guess that's what I get for not studying enough."
        "I can only hope that I passed."
    scene black with dissolve
    jump event_ending_decision2_decision


label after_class:
    $ numberFlagA = False 
    $ numberFlagB = False 
    $ numberFlagC = False 
    $ gym_choice_1_a = False
    $ gym_choice_1_b = False 
    $ library_choice_1_a = False 
    $ library_choice_1_b = False 
    $ art_choice_1_a = False 
    $ art_choice_1_b = False 
    $ library_choice_2_c = False
    $ art_choice_2_c = False
    $ gym_choice_2_c = False
    
    menu:
        "Go to the gym.":
            "I'll go to the gym. It's important that I prioritize my health."
            $ gym_counter = gym_counter + 1
            stop music fadeout 1.0
            jump gym
        "Go to the library.":
            "I'll go to the library. If I want to do well in this class, I better study."
            $ lib_counter = lib_counter + 1
            stop music fadeout 1.0
            jump library
        "Go to the art room.":
            "I'll go to the art room. I have to practice if I want to improve."
            $ art_counter = art_counter + 1
            stop music fadeout 1.0
            jump art
        "Go to my dorm.":
            "I'm feeling pretty tired. I think I'll just head home."
            stop music fadeout 1.0
            jump end_of_act