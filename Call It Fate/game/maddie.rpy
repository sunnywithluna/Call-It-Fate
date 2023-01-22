label a_number:
    $ renpy.show(custom_show("maddie", "normal"), [])

    $ a_number_flag = True
    n "\"Hey, Maddie, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if A >= A_low:
        $ renpy.show(custom_show("maddie", "flirty"), [])        
        a "\"Or something?\""
        n "\"I didn't mean--\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"Haha, I'm just teasing. I think that's a great idea.\""
        "We exchange phone numbers."
        $ a_number_obtained_flag = True
        jump talking_to_maddie
    else:
        $ renpy.show(custom_show("maddie", "uncomf"), [])        
        a "\"Or something?\""
        n "\"I didn't mean--\""
        $ renpy.show(custom_show("maddie", "angry"), [])
        a "\"Listen, I know what you're trying to do. I'm not interested, okay?\""
        jump talking_to_maddie

label gym:
    scene bg_gym with fade
    play music "audio/free.mp3"
    $ gym_compliment = False

    if gym_counter == 1:
        "With most students home for the summer, the school gym is practically empty."

        "Motivational signs adorn the walls next to work out class schedules from the spring semester that have yet to be taken down."
        "Speakers hide in the high corners of the room but play no music, and the normal light clanking of weights coming together on the machines is replaced instead with silence."

        "Among all the empty workout equipment is the one person in the place besides myself."

        $ renpy.show(custom_show("maddie", "normal"), [])
        "Maddie's filling up a water bottle that looks comically large next to her short frame."
        "It's the same one she'd bring to high school every day that she and Jennifer would stick stickers to as they whispered in the back of class."

        "Only now, the stickers were gone and the white residue of the paper was all that remained."

        "When Maddie turns from the five-gallon dispenser, I look away, not wanting her to think I was staring."
        "Luckily, she doesn't seem to notice me as she heads for the leg press machine."
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)
    elif gym_counter == 2:
        $ renpy.show(custom_show("maddie", "happy"), [])
        "Upon entering the gym, I see Maddie increasing the weight on a shoulder press machine. She offers a wave before continuing with her workout."
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)

    elif gym_counter == 3:
        "I walk into an empty gym, and to my surprise, feel a slight sense of disappointment. I thought I'd see Maddie here again, but it seems she's taking the day off."
        $ renpy.show(custom_show("maddie", "normal"), [])
        a "\"Hey.\""
        "I turn to face Maddie who stands behind me at the entrance of the gym, taking a sip out of her ridiculous water bottle."
        $ renpy.show(custom_show("maddie", "flirty"), [])
        a "\"You beat me to the gym today. I guess I'll have to be faster next time.\""
        n "\"I didn't know it was a race.\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"Sure it is, a little healthy competition can be a great motivator.\""
        n "\"Then, what do I get if I win?\""
        $ renpy.show(custom_show("maddie", "uncomf"), [])
        a "\"The satisfaction of victory isn't enough? How about...\""
        if eventba_trigger:
            n "\"Another date?\""
        else:
            n "\"A date?\""
        $ renpy.show(custom_show("maddie", "flirty"), [])
        a "\"So forward! I was thinking more like...five bucks?\""
        n "\"That works. After our next class, the first one here wins. Deal?\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"Deal.\""
        "Maddie heads towards the machines to start her workout."
        $ renpy.hide(custom_hide("maddie"))
    elif gym_counter == 4:
        "I sprint to the gym, determined to get there before Maddie."
        $ renpy.show(custom_show("maddie", "normal"), [])
        "But as soon as I open the door, there she is, already at the leg press machine."
        $ renpy.show(custom_show("maddie", "flirty"), [])
        a "\"Took you long enough.\""
        n "\"What?! But I ran over here!\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"I guess I'm just faster than you then.\""
        n "\"Aagh, fine.\""
        "I pull out my wallet to hand her a five dollar bill."
        n "\"You win this time.\""
        $ renpy.show(custom_show("maddie", "flirty"), [])
        a "\"Is that a challenge for a rematch?\""
        n "\"No thanks. I think I'll keep what little money I have left.\""
        "I walk away to avoid any further gloating."
        $ renpy.hide(custom_hide("maddie"))
    else:
        n "\"...\""

    "What should I do?"
    jump gym_main_menu
    return

label gym_main_menu:
    menu:
        "Talk to Maddie":
            if not gym_choice_1_a:
                jump gym_1_talk
            else:
                "I say goodbye to Maddie before heading out."
                $ A = A + 1
                stop music fadeout 1.0
                scene black with longfade
                jump end_of_day
        "Work Out" if not gym_choice_1_b:
            jump gym_1_workout
        "Go Home":
            jump end_of_day
    return
        
label gym_1_talk:
    $ gym_choice_1_a = True
    if A < A_bad:
        $ renpy.show(custom_show("maddie", "uncomf"), [])
        a "\"What do you want?\""
    elif A_bad <= A <= A_mid:
        $ renpy.show(custom_show("maddie", "normal"), [])
        a "\"Hey, Sam. What's up?\""
    elif A_mid <= A <=A_mid3:
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"Hey, Sam! Great day to hit the gym, huh?\""
    else:
        $ renpy.show(custom_show("maddie", "flirty"), [])
        a "\"Hey, Sam! I was hoping you'd show up today.\""
    
    jump talking_to_maddie

label talking_to_maddie:
    menu:
        "Ask for number" if not a_number_flag and not a_number_obtained_flag:
            jump a_number
        "Engage in small talk" if not gym_choice_2_a:
            jump gym_choice_2_a
        "Get to know her" if gym_choice_2_a and not gym_choice_2_b and i < day:
            jump gym_choice_2_b
        "Ask her to spot you" if gym_choice_2_a and gym_choice_2_b and not gym_choice_2_c and j < day:
            jump gym_choice_2_c
        "Compliment" if not gym_compliment:
            jump gym_choice_2_d
        "Back":
            jump gym_main_menu
    return 

label gym_choice_2_a:
    n "\"It's so quiet in here.\""
    $ renpy.show(custom_show("maddie", "happy"), [])
    a "\"Yeah, the gym's always packed during the school year. It's kind of nice having the place to ourselves though.\""
    $ gym_choice_2_a = True
    $ A = A + 1
    $ i = day
    jump talking_to_maddie
    return

label gym_choice_2_b:
    n "\"So, what're you up to these days?\""
    $ gym_choice_2_b = True
    $ j = day
    if A > A_bad:
        $ renpy.show(custom_show("maddie", "normal"), [])
        $ A = A + 1
        a "\"Oh, you know, the usual. Hiking, climbing, anything that gets me outside and moving. What about you? You still play games?\""
        n "\"Yeah, I do. I'm trying some new things though. That's why I'm here instead of my dorm.\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"It's cool that you're taking an interest in fitness.\""
    
        if A >= A_mid:
            a "\"It can be hard to get into, but it's definitely rewarding if you stick with it.\""
            n "\"Any tips on how to stay motivated?\""
            "Maddie takes a sip of her water as she thinks."
            $ renpy.show(custom_show("maddie", "happy"), [])
            a "\"Envision the person you want to be. And remember why working out will help you get there.\""
            $ renpy.show(custom_show("maddie", "angry"), [])
            a "\"There are plenty of days I'd rather just stay at home in bed. It's tempting in the moment...but when I think about who I want to become, it isn't someone who takes the easy road just 'cause it's gratifying, you know?\""
            n "\"You want to be someone who's willing to put in the work, even when it's hard.\""
            $ renpy.show(custom_show("maddie", "embarrassed"), [])
            a "\"Exactly. That's what a strong person does. I don't want to be seen as weak just because of my height or because I'm a girl.\""
            $ renpy.show(custom_show("maddie", "uncomf"), [])
            a "\"I want to be strong.\""
            n "\"So are you almost the person you want to be?\""
            $ renpy.show(custom_show("maddie", "sad"), [])
            a "\"I don't know. But I'm a little closer every day.\""
            n "\"Well, I don't know if it means anything coming from me, but I've never thought of you as weak.\""
            $ renpy.show(custom_show("maddie", "flirty"), [])
            a "\"Thanks, Sam. Well, I guess I better keep at it then. So you don't change your mind about me.\""

        jump talking_to_maddie
    else:
        $ renpy.show(custom_show("maddie", "angry"), [])
        $ A = A - 1
        a "\"I'm not really here to make conversation. I just want to focus on my workout, okay?\""
        jump talking_to_maddie
    return

label gym_choice_2_c:
    $ k = day
    n "\"Hey, since we're both here, do you think you could spot me on the bench press?\""
    $ gym_choice_2_c = True

    if A >= A_mid:
        $ A = A + 2
        $ renpy.show(custom_show("maddie", "normal"), [])
        a "\"Yeah, of course!\""
        if workout_counter >= 3:
            "I do three sets, eight reps each." 
            $ renpy.show(custom_show("maddie", "flirty"), [])
            a "\"That's really impressive, Sam! Keep it up!\""
            $ A = A + 1 #extra point

        elif workout_counter >= 1:
            "I do three sets, five reps each."
            $ renpy.show(custom_show("maddie", "happy"), [])
            a "\"Not bad. Keep it up, Sam!\"" 

        else:
            $ A = A - 3
            "I do three sets, three reps each."
            $ renpy.show(custom_show("maddie", "uncomf"), [])
            n "\"You okay? You seem a bit out of breath...\""
    else:
        $ A = A - 2
        $ renpy.show(custom_show("maddie", "uncomf"), [])
        a "\"Eh, I think I'll pass. Sorry.\""
    jump talking_to_maddie

label gym_choice_2_d:
    $ gym_choice_2_d = True 
    $ gym_compliment = True

    if gym_comp: 
        n "\"You look nice today!\""
        $ renpy.show(custom_show("maddie", "happy"), [])
        a "\"Thanks, Sam!\""
        jump talking_to_maddie
    else:
        $ gym_comp = True
        "Well, she's obviously attractive, but seeing how much weight she has on the machine, she seems really strong too."
        "What should I compliment her on?"
        menu:
            "Beauty":
                jump beauty_comp_maddie
            "Strength":
                jump strength_comp_maddie
        return
    
label beauty_comp_maddie:
    "What should I say?"

    menu: 
        "You're really cute":

            n "\"I know this is kind of out of nowhere, but I just wanted to say, I think you're really cute.\""
            if A >= A_mid:
                $A = A + 1
                $ renpy.show(custom_show("maddie", "flirty"), [])
                a "\"Haha, really? That just gave me a confidence boost. Thanks, Sam.\""
                jump talking_to_maddie
            else:
                $A = A - 1
                $ renpy.show(custom_show("maddie", "uncomf"), [])
                a "\"Um...Okay? Thanks, I guess?\""
                jump talking_to_maddie

        "You have a great body":

            n "\"All this working out is really paying off. Your body looks great!\""
            $A = A - 3
            $ renpy.show(custom_show("maddie", "angry"), [])
            a "\"Sam, that's so weird. Don't say stuff like that, okay?\""
            jump talking_to_maddie
    return

label strength_comp_maddie:
    n "What should I say?"

    menu: 
        "You're really strong!":
            $A = A + 2
            n "\"You've nearly maxed out the machine! That's crazy!\""
            $ renpy.show(custom_show("maddie", "happy"), [])
            a "\"Really? I guess it is. I sometimes forget how far I've come.\""
            jump talking_to_maddie

        "I didn't know a girl could lift that much":
            n "\"Hey, you're pretty strong for a girl.\""
            if 3 <= A:
                $ renpy.show(custom_show("maddie", "angry"), [])
                a "\"And you're pretty annoying. Get lost, weeb.\""
            else:
                $ renpy.show(custom_show("maddie", "uncomf"), [])
                a "\"You could've just left off the 'for a girl' part...\""
            $A = A - 4
            jump talking_to_maddie

        "You're a lot stronger than me":
            n "\"Oh wow, that's impressive.\""
            $ renpy.show(custom_show("maddie", "embarrassed"), [])
            a "\"Really?\""
            n "\"Yeah!  I can't handle nearly that much weight!\""
            if 2 <= A:
                $A = A + 1
                $ renpy.show(custom_show("maddie", "flirty"), [])
                a "\"Haha, well, I couldn't always press this much! If you work at it, I bet you could do it too.\""
            else:
                $ renpy.show(custom_show("maddie", "uncomf"), [])
                a "\"Oh, maybe you just need to work out more then? I don't know what you want me to say...\""
            jump talking_to_maddie 
    return

label gym_1_workout:
    $ gym_choice_1_b = True 
    $ workout_counter = workout_counter + 1
    $ renpy.hide(custom_hide("maddie"))
    $ renpy.with_statement(dissolve)

    $ A = A + 1

    "I work my way through some of the gym equipment, doing three sets for every exercise and moving up in weight when it seems too easy."
    
    if day%2 == 0:
        "I catch Maddie looking in my direction."
        $ renpy.show(custom_show("maddie", "normal"), [])
        "What should I do?"

        menu:
            "Focus on working out":
                if A < A_mid2:
                    $ A = A + 1
                    "I continue with my workout, and when I glance back over at Maddie, she looks impressed."
                else:
                    "I continue with my workout, and when I glance back over at Maddie, she seems disappointed."
                    if A > A_high:
                        $ A = A - 1

            "Wave":
                if A < A_mid2:
                    $ A = A - 1
                    "I wave at Maddie."
                    $ renpy.show(custom_show("maddie", "uncomf"), [])
                    "She raises an eyebrow in confusion as she continues with her workout."

                else:
                    $ renpy.show(custom_show("maddie", "normal"), [])
                    "I wave at Maddie."
                    $ renpy.show(custom_show("maddie", "happy"), [])
                    a "\"Hey, Sam!\""
                    if A >= A_high: 
                        $ A = A + 1
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)

    scene bg_gym_night with fade
    "I finish a couple more sets before wiping down the equipment."
    "That was tiring, but I'm glad I pushed myself."
    
    menu: 
        "Talk to Maddie":
            if not gym_choice_1_a:
                jump gym_1_talk
            if gym_choice_1_a:
                $ renpy.show(custom_show("maddie", "normal"), [])
                "I say goodbye to Maddie before heading out."
                $ A = A + 1
            stop music fadeout 1.0
            scene black with longfade
            jump end_of_day
        "Go Home":
            "I've been out for a while. I think it's time to go home."
            stop music fadeout 1.0
            scene black with longfade
            jump end_of_day
    return 

label event_aa:
    $ maddie_hang_over = True
    scene maddie_hang with fade 
    play music "audio/event.mp3"

    "The next day, I head to the school gym where Maddie is waiting, tying her hair into the usual ponytail."
    scene bg_gym with fade

    show maddie_2 normal
    a "\"Hey, Sam. Ready for our workout?\""
    hide maddie_2 with dissolve

    "We walk over to the free weights and go through a few different exercises, Maddie talking me through my form for each of the movements."
    "I knew she played sports throughout high school, but I never realized just how knowledgeable she was about fitness."
    "She's able to answer all my questions and offer tips."
    "And though there's a lot I have to learn, she doesn't judge me for my inexperience."
    "It's nice. And surprising."

    "If this were a year ago, I'm sure she'd laugh at the amount of weight I could lift or make fun of my form. But I actually feel at ease working out with Maddie."

    "Every time she praises my progress or seems impressed by my ability, I'm only more motivated to keep pushing myself. And with her beside me, the minutes spent in exertion pass quickly."

    "By the end of our workout, we're blotting the sweat off our faces and sitting on the gym floor. I know my muscles will be sore tomorrow."
    show maddie_2 uncomf 
    a "\"Can I be honest with you for a second?\""
    "I look over at her, wiping the sweat from my brow."
    show maddie_2 normal
    a "\"I was really surprised when I saw you here. I didn't take you as the gym type back in high school.\""

    n "\"Well...I wasn't...\""
    n "\"The thing is, I realized recently that I never really push myself. I've always wanted to be stronger, but I had trouble taking that first step to start.\""
    n "\"I don't want to hold myself back anymore by not trying.\""
    show maddie_2 uncomf 
    a "\"It's definitely scary to take on a new challenge. Even when it's good for you.\""
    n "\"Can I say something too?\""
    show maddie_2 happy
    a "\"Go for it.\""
    n "\"I kind of thought you didn't like me. In high school, you were a little...intense.\""
    show maddie_2 sad 
    a "\"Yeah...I know. I'm sorry. I was such a jerk.\""
    a "\"I wish I could explain myself, but there's no excuse for the way I acted…Can you forgive me?\""
    menu:
        "I forgive you.":
            jump test
        "I don't forgive you.":
            jump test2
    return

label test:
    "I stand up and extend my hand to her."
    n "\"Of course.\""
    show maddie_2 flirty
    "She takes my hand, and I pull her up."
    stop music fadeout 1.0
    scene black with longfade
    jump quick_calculations
    return 

label test2:
    n "\"I...don't know if I can yet.\""
    show maddie_2 uncomf
    a "\"You need time. I get it.\""
    "She stands up and extends her hand to me."
    show maddie_2 normal
    a "\"Until then, I'll try to prove that I mean it.\""
    "I take her hand, and she pulls me up."
    stop music fadeout 1.0
    scene black with longfade
    jump quick_calculations
    return 


label event_ba:
    $ maddie_date_over = True
    $ date = False
    $ date_this_weekend = False
    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Maddie."
    a "\"Hey, Sam! Where were you thinking of going for our date?\""
    menu: 
        "Hiking trail":
            $ A = A + 1
            "In response, I write, \"I was thinking we could go on a hike. Is that okay?\""
            a "\"Yeah! That sounds fun! Send me the address, and I'll meet you there. :)\""
        "Interactive science museum":
            "In response, I write, \"I was thinking we could check out the science museum. Is that okay?\""
            a "\"Eh, to be honest, I'd rather do something different. Would you be up for a hike? I know a cool place.\""
            "Just the idea of hiking is already making my body feel heavy and tired, but I still agree to go. Besides, I probably need the exercise."
        "Art gallery":
            "In response, I write, \"I was thinking we could go to this art gallery. Is that okay?\""
            a "\"Eh, to be honest, I'd rather do something different. Would you be up for a hike? I know a cool place.\""
            "Just the idea of hiking is already making my body feel heavy and tired, but I still agree to go. Besides, I probably need the exercise."
        "Ramen shop":
            "In response, I write, \"I was thinking we could grab some ramen. Is that okay?\""
            a "\"Eh, to be honest, I'd rather do something different. Would you be up for a hike? I know a cool place.\""
            "Just the idea of hiking is already making my body feel heavy and tired, but I still agree to go. Besides, I probably need the exercise."
    scene maddie_date with fade

    "When I arrive, I find Maddie taking pictures of succulents planted at the entrance of the trail. It's a nice shaded area, full of greenery that dampens the sound of traffic in the distance."

    n "\"Hey!\""
    "Maddie turns to face me."
    scene bg_gymdate with fade

    show maddie_5 happy
    a "\"Hey, Sam!\""
    n "\"What're you doing?\""
    show maddie_5 normal
    a "\"I was just checking out the plants. I have a couple at home that look similar.\""
    n "\"Oh no, you're one of those plant-obsessed girls, aren't you?\""
    show maddie_5 embarrassed
    a "\"What's wrong with liking plants?\""
    "Maddie starts to head towards the trail signs, and I follow behind her, the sound of gravel crunching with every step."
    n "\"It's not just 'liking plants.' It's filling your room with plants to the point where you might as well just be outside.\""
    show maddie_5 happy
    a "\"Hey, I'd rather have a room full of plants than one full of Neko-Chan figurines.\""
    n "\"Wow.\""
    a "\"Haha, well, don't dish it out if you can't take it. Now, come on. Let's pick a trail. I'm ready to get moving.\""
    show maddie_5 normal
    "I look at the two wooden trail signs in front of us, both written in debossed black lettering."
    "Which trail should we go on?"

    menu:
        "Death Row Ridge":
            $ A = A + 2
            n "\"Let's do Death Row Ridge.\""
            show maddie_5 happy
            a "\"Alright, a challenge! This should be fun.\""
            "We start down the path, and within minutes, I'm already certain I'll be sore the next day."

        "Fluffy Bunny Hilltop":
            $ A = A - 1
            n "\"Let's do Fluffy Bunny Hilltop.\""
            show maddie_5 angry 
            a "\"Really? Alright. I guess there's nothing wrong with taking it easy.\""
            "We start down the leisurely path, and after a few minutes, I feel just the slightest bit of embarrassment as an elderly couple passes us by."
    
    hide maddie_5 with dissolve

    "But as we continue walking, I begin to really enjoy the hike. The light rustling of leaves in the wind accompanies the trickling of a nearby stream. The whole experience is surprisingly serene."

    "Then, I see a familiar figure approaching us."
    show jennifer at trueright

    "Jennifer" "\"Maddie? I haven't seen you since graduation! How've you been?\""

    show maddie_5 uncomf at trueleft

    "Maddie tenses up as Jennifer looks back and forth between us."

    "Jennifer" "\"Oh, are you guys here...together?\""
    show maddie_5 normal
    a "\"Uh, yup. We're kind of on a date right now.\""

    "I try not to get offended as Jennifer's face scrunches up in disgust."

    "Jennifer" "\"Really, Maddie? Him?\""
    show maddie_5 angry at trueleft

    n "\"Ouch, okay, I'm right here.\""

    a "\"That's pretty rude, Jen.\""

    "Jennifer" "\"What? I'm just surprised.\""
    show maddie_5 normal at trueleft

    a "\"You know what? I don't need your approval. Come on, Sam.\""
    hide jennifer with dissolve
    hide maddie_5 with dissolve
    scene black with longfade
    "I feel Maddie's hand slip into mine as we push past Jennifer."
    scene bg_gymdate with fade

    n "\"What was that about? I thought you guys were close.\""
    show maddie_5 angry 

    a "\"Not anymore. You saw how she was back there. Telling me who I should and shouldn't hang around.\""
    show maddie_5 normal 
    a "\"She's a total control freak.\""
    show maddie_5 uncomf 
    a "\"And judgemental.\""
    show maddie_5 sad

    a "\"And mean. Why would I want to be friends with someone like that?\""

    n "\"But...hasn't she always been like that?\""
    show maddie_5 sad

    "Maddie pauses before nodding her head."


    a "\"And I used to be just as bad.\""
    show maddie_5 uncomf 

    a "\"I hate who I was back then. It's just...\""

    menu:
        "You were afraid of seeming weak":
            $ A = A + 1
            n "\"You didn't want to seem weak.\""
            show maddie_5 normal
            a "\"Yeah...\""

        "You wanted to belong":
            n "\"You wanted to fit in.\""
            show maddie_5 angry
            a "\"No, I just didn't want to seem weak.\""

        "You enjoyed hurting others":
            $ A = A - 1
            n "\"You liked hurting people?\""
            show maddie_5 angry
            a "\"No! I just didn't want to seem weak.\""
    show maddie_5 uncomf
    a "\"And I'm not proud of it. I know it's not an excuse. But I am trying to be better...\""
    n "\"Hey, we all kind of sucked in high school, right? You can't beat yourself up about it forever.\""
    show maddie_5 normal
    a "\"Yeah...I guess that's true...\""
    hide maddie_5 with dissolve
    "Maddie wears a serious look on her face, her brows furrowed, her jaw clenched. I can tell she's sincere in wanting to change, but running into Jennifer seemed to resurface feelings of guilt and regret."

    "I squeeze her hand, and she looks at me with a softened expression."

    "As long as I've known her, Maddie has always wanted to seem strong, tough."
    "But, in that moment, I saw an unfamiliar vulnerability in her."
    "I saw a girl who knew she made mistakes, who knew she'd hurt others, and who, more than anything, wanted to right her wrongs."


    "At first, I'm worried our encounter with Jennifer might've ruined the day, but it seems the fresh air and sound of the creek are too soothing to remain tense."
    "The further we continue down the trail, the more Maddie relaxes again."

    "We let ourselves forget about the past and who we were before college, enjoying each other's company as we tackle the path in front of us."
    "When we reach the end of the loop, I walk Maddie to her car."

    scene bg_night with fade

    show maddie_5 flirty
    a "\"I had a lot of fun today, Sam.\""
    n "\"Yeah, me too. We should do it again sometime.\""
    "As I'm looking at her, I realize it's time to part ways."
    "How should I say goodbye?"

    menu:
        "Kiss her":
            jump kiss_maddie
        "Hug her":
            jump hug_maddie
        "Give her a high five":
            jump hand_maddie
    return

label kiss_maddie:
    if A >= A_high:
        scene black with fade

        $ A = A + 1
        "I lean in."
        "And our lips meet."
        scene maddie_kiss with fade

        a "\"Bye, Sam.\""
        "She gets in her car and drives away."
        "And I can't wait until Tuesday when I get to see her again."
        jump quick_calculations
    else: 
        scene black with fade
        $ A = A - 1
        "I lean in."
        scene bg_night with fade

        show maddie_5 angry
        a "\"Oh, no. Let's not do that.\""
        show maddie_5 uncomf
        "She's leaning away, and I feel a wave of embarrassment wash over me."
        n "\"Sorry...\""
        "She looks at me with pity."
        a "\"Don't worry about it, it's fine. Take care, okay?\""
        "She gets in her car and drives away."
        "And I'm left wondering what I did wrong."
        jump quick_calculations
    return 

label hug_maddie:
    "I lean in for a hug."

    if A >= A_high:
        $A = A - 1
        "Maddie feels stiff as she hugs me, and I wonder if I've done something wrong."
        show maddie_5 sad 
        a "\"Alright, Sam. Well, take care I guess.\""
        "She gets in her car and drives away. And I'm left with the impression that she was a little disappointed."
        jump quick_calculations
    else:
        $A = A + 1
        show maddie_5 normal
        "As she hugs me back, I'm reminded how much shorter she is than me. But even with our height difference, it's nice to just hold her."
        a "\"Bye, Sam.\""
        "She gets in her car and drives away."
        "And I can't wait until Tuesday when I get to see her again."
        jump quick_calculations
    return 

label hand_maddie:
    $ A = A - 1
    "I hold up my hand to give her a high five."
    n "\"See you Tuesday.\""
    show maddie_5 uncomf
    a "\"Okay...\""
    "She high fives me and laughs."
    show maddie_5 normal
    a "\"Bye, Sam.\""
    "Maddie gets in her car and leaves."
    "And I'm left wondering if there was a better way I could've done that."

    jump quick_calculations
    return 
    

label send_text_a:
    "What should I say?"

    menu:
        "Make small talk about her day" if not small_a_sent:
            jump text_small_a
        "Do you want to go on a date?" if not eventba_trigger and not date_a_sent and eventaa_trigger and maddie_hang_over:
            jump text_go_out_a
        "Let's hang out soon" if not eventaa_trigger and not hang_b_sent:
            jump text_buddy_a
        "Look at this cool video" if not video_a_sent:
            jump text_video_a
        "Goodnight" if not gn_a_sent:
            jump text_night_a
        "Put phone away":
            jump end_of_day_menu

label text_go_out_a:
    $ date_a_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else: 
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if A >= A_mid3:
            $ date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"Sure! Sounds fun. Does this weekend work for you?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $ eventba_trigger = True
            $ date = True
            jump send_text_a
        else:
            "After about thirty minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"I had a feeling this might happen. Listen, Sam, you're nice, but I'm not interested in you like that. Friends?\""
            jump send_text_a

label text_buddy_a:
    $ hang_a_sent = True
    "I send a text that reads, \"Hey, Maddie! I was thinking of hitting the gym tomorrow. You down?\""
    if A >= A_mid:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Totally! See you then!\""
        $ eventaa_trigger = True
        jump send_text_a
    else:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Tomorrow's actually a rest day for me.\""
        jump send_text_a
        
label text_video_a:
    $ video_a_sent = True
    "Which video should I send?"
    $ mvideo_counter = mvideo_counter + 1

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"Whoa! I wonder how many tries it takes to make those trickshots.\""
            jump send_text_a
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"What is this? Am I missing something?\""
            jump send_text_a
        "Test animation that features characters from a recently released, popular kid's film":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"What is this? Am I missing something?\""
            jump send_text_a
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"What is this? Am I missing something?\""
            jump send_text_a
    return

label text_small_a:
    $ small_a_sent = True
    "I ask Maddie about her day."

    if small_a_sent2 == False:
        $ small_a_sent2 = True
        if A >= A_low:
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            "We chat for a short while before I change the topic."
            jump send_text_a
        else:
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"I'm kind of busy right now.\""
            jump send_text_a   
    else:
        "We chat for a short while before I decide to change the topic."
        jump send_text_a 


label text_night_a:
    $ gn_a_sent = True
    "I send a simple goodnight message."

    if gn_a_sent2 == False:
        $ gn_a_sent2 = True
        if A >= A_low:
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"A goodnight text? If I didn't know any better, I'd think you like me. Lol, goodnight, Sam.\""
            jump send_text_a
        else:
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"Do you send all your friends goodnight texts?\""
            jump send_text_a   
    else:
        a "\"Goodnight, Sam!\""    
        jump send_text_a 

label text_roof_a:
    $ like_a_sent = True
    "I can't just tell her something like that over text. It should be in person."
    "So I write and send a message that reads:"
    n "\"Hey, there's something I want to talk with you about. Do you think we could meet up?\""
    if A >= 100:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Sounds serious. :o When did you want to meet?\""
        "I type \"Meet me on top of the library, at sunset,\" and hit send."
        $ eventca_trigger = True
        jump event_c
    else:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Right now? I don't know, Sam, I'm pretty tired. Unless it's an emergency, can we just save whatever it is for a different day?\""
        jump send_text_a
    return

    
label event_ca: 
    scene bg_roof with fade
    play music "audio/rooftop.mp3"

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    show maddie_1 normal
    "Maddie is standing with her hands on her hips, staring out into the horizon, steady as always."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    
    n "\"Hey.\""
    show maddie_1 happy
    a "\"Hey, Sam.\""

    "She glances down at the gift in my hand."
    if maddie_gift:
        scene maddie_hoya with fade
        $A = A + 1
        show maddie_1 flirty at trueleft
        a "\"A hoya kerrii plant! Is that for me?\""
        n "\"Yeah! Do you like it?\""
        if eventba_trigger:
            n "\"It reminded me of the ones from our hike.\""
        "She takes the potted plant from me, looking at it with admiration."
        a "\"I love it, Sam. Thank you.\""
    else:
        $ A = A - 1
        n "\"Oh, this is for you.\""
        show maddie_1 uncomf
        "I hold out her present, and she takes it slowly, looking a little confused."
        a "\"Oh. Thanks.\""
    scene bg_roof with fade
    show maddie_1 normal
    "We watch the sun slowly fall."
    a "\"I'm glad we ended up in Intro to Philosophy together.\""
    n "\"Is something on your mind?\""
    show maddie_1 happy
    a "\"I was just thinking about how nice it is being up here with you. And that...\""
    a "\"It's been cool getting to know you better.\""
    n "\"I think our high school selves would be shocked if they could see us now.\""
    a "\"Haha, definitely.\""
    a "\"So why did you want to meet up?\""
    n "\"Well...I actually had something I wanted to talk with you about.\""
    show maddie_1 flirty
    a "\"Yeah, you mentioned that in your text. What's up?\""

    menu:
        "Confess my feelings":
            if maddie_confessed:
                jump maddie_confessed

            if A >= A_high3:
                jump maddie_perfectending
            elif A >= A_high:
                jump maddie_goodending
            else:
                jump maddie_badending
        "I've changed my mind":
            jump neko_ending
    return

label maddie_goodending:
    $ maddie = True
    n "\"Alright, well, I guess I'll just say it. I know we only just started hanging out, but…I really like you, and I was wondering if maybe...you felt the same way?\""
    "Another breeze blows past us as I wait for her to respond."
    show maddie_1 flirty
    a "\"I like you too.\""
    "It takes a moment before what she's saying sinks in."
    n "\"Really?! I mean, that's great!\""
    "She smiles, then takes my hand."
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with longfade
    jump epi_start
    return 

label maddie_greatending:
    $ maddie = True
    show maddie_1 angry
    a "\"Are you serious, Sam?\""
    n "\"Sorry, nevermind, forget I said anything.\""
    a "\"No! That's not what I mean.\""
    n "\"What?\""
    show maddie_1 happy
    a "\"Of course I like you! I wasn't trying to be subtle, could you really not tell?\""
    n "\"I had no idea.\""
    "Maddie sighs dramatically, jokingly."
    show maddie_1 flirty
    a "\"Well, now you do.\""
    "She smiles, then takes my hand."
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with longfade
    jump epi_start
    return 

label maddie_badending:
    $ d_ending_success = True
    show maddie_1 sad
    a "\"Oh...Sam, I'm so sorry.\""
    "It takes a moment before what she's saying sinks in."
    n "\"Huh...I guess I misread things...I'll see you around.\""
    scene black with longfade
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    scene bg_room_dark with fade
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    show neko
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black
    jump credits
    return

label event_da:
    scene maddie_dorm with fade
    play music "audio/event.mp3"

    "I open my door to find Maddie standing outside my room."
    scene bg_outside_dorm with fade

    show maddie_2 normal
    a "\"Hey, Sam. Feeling better?\""
    n "\"A little. What're you doing here?\""
    show maddie_2 uncomf
    a "\"I came by to bring you some handouts from class.\""
    "She holds up a few pages."
    a "\"Dr. Paige wanted to make sure you got these.\""
    n "\"Oh, thanks. Do you want to come in?\""
    show maddie_2 normal
    "I move to the side, and she walks into my dorm, handing me the papers as she looks around the room."
    scene bg_room with fade

    if clean:
        show maddie_2 happy
        a "\"Wow, Sam. Your dorm is so clean. So much nicer than most guys' rooms.\""
        n "\"How many guys' dorms have you been in?\""
        show maddie_2 embarrassed
        a "\"Uh, forget I said that.\""
    else:
        show maddie_2 angry
        a "\"Did a tornado come through here? This place is a mess.\""
        n "\"Hey, you have to be nice to me. I'm sick.\""
        a "\"Fine, fine. I'll cut you some slack.\""
        
    show maddie_2 flirty
    "She gestures to Neko-Chan on my bed."
    a "\"Still a fan of 2D girls, huh?\""
    n "\"2D girls don't talk so much.\""
    show maddie_2 embarrassed
    "Maddie's jaw drops in jest."
    show maddie_2 happy
    a "\"She's not even fully human!\""
    n "\"Fifty-percent woman, fifty-percent cat. One hundred percent my type.\""
    show maddie_2 uncomf
    a "\"I'm remembering why I picked on you in high school...\""

    if A >= A_high:
        $ maddie_confessed = True
        show maddie_2 uncomf
        a "\"Listen, there's actually something I wanted to talk to you about.\""
        n "\"Yeah? What is it?\""
        n "\"Maddie scratches the back of her head. She almost seems...nervous.\""
        show maddie_2 normal
        a "\"Well...I know this might seem a bit sudden, but, I like you, Sam.\""
        a "\"And the only reason I'm even saying this is because I'd rather know how you feel now than get my hopes up, you know?\""
        show maddie_2 uncomf
        a "\"So, what do you think?\""

        menu:
            "I like you too": #CHANGE
                show maddie_2 normal
                n "\"Maddie, I--\""
                "A wave of dizziness overwhelms me."
                show maddie_2 sad
                a "\"Sam!\""
                "Maddie grabs me as I almost fall to the ground."
                a "\"I'm sorry. I should go so you can rest.\""
                "While leaving my room, she hesitates by the doorway."
                a "\"Call me later, okay? When you're feeling better.\""
                hide maddie_2 with dissolve
                "Maddie closes the door behind her, and I'm left standing in the middle of my dorm, wishing my headache away so I could go after her and ask her to stay a little longer."
                "But spending time with Maddie would have to wait."
                "The second I lie down in my bed, I'm already drifting back to sleep."
                "I dream of a life with Maddie. And though I know realistically it's probably just caused by the fever, I can't help but think it means something."
                "That these past two weeks are just the beginning."

            "I don't think of you like that":
                show maddie_2 normal
                n "\"Maddie, I--\""
                "A wave of dizziness overwhelms me."
                show maddie_2 sad
                a "\"Sam!\""
                "Maddie grabs me as I almost fall to the ground."
                a "\"I'm sorry. I should go so you can rest.\""
                "While leaving my room, she hesitates by the doorway."
                a "\"Call me later, okay? When you're feeling better.\""
                hide maddie_2 with dissolve
                "She rushes out, closing the door behind her before I have a chance to say anything else."
    else: 
        #Change
        show maddie_2 uncomf
        a "\"I should probably go.\""
        n "\"Are you sure?\""
        a "\"Yeah, you need to rest. We'll see each other on Thursday, if you're not still sick.\""
        n "\"Alright. Talk to you later then.\""
        hide maddie_2 with dissolve
        "Maddie leaves, closing the door behind her, and I'm left standing in the middle of my dorm, alone."
        "I go to sleep with my fever induced headache and dream up a life with Neko-Chan...a perfect life."
    
    stop music fadeout 1.0
    scene black with longfade
    jump ch3_schoolday2
    return

label maddie_confessed:
    $ maddie = True
    show maddie_1 normal
    n "\"The other day, when I was sick, you said something to me.\""
    show maddie_1 uncomf

    a "\"You mean that I like you?\""

    n "\"Yeah, that...\""

    n "\"I-I didn't get a chance to respond before, but...\""
    show maddie_1 embarrassed

    n "\"I feel the same way.\""

    "Another breeze blows past us."
    show maddie_1 happy

    "Then, she smiles."
    show maddie_1 flirty

    a "\"Good.\""

    "She takes my hand, and leans on my shoulder."

    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with longfade
    jump epi_start
    return
