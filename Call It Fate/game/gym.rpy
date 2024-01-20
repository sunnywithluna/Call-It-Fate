label gym:
    scene bg_gym_a with dissolve
    play music "audio/free.mp3" fadein 1.0
    $ gym_compliment = False

    if gym_counter == 1:
        "With most students home for the summer, the school gym is practically empty."

        "Motivational signs adorn the walls next to work out class schedules from the spring semester that have yet to be taken down."
        "Speakers hide in the high corners of the room but play no music, and the normal light clanking of weights coming together on the machines is replaced instead with silence."

        "Among all the empty workout equipment is the one person in the place besides myself."

        $ renpy.show(custom_show("maddie", "N"), [])
        "Maddie's filling up a water bottle that looks comically large next to her short frame."
        "It's the same one she'd bring to high school every day that she and Jennifer would stick stickers to as they whispered in the back of class."

        "Only now, the stickers were gone and the white residue of the paper was all that remained."

        "When Maddie turns from the five-gallon dispenser, I look away, not wanting her to think I was staring."
        "Luckily, she doesn't seem to notice me as she heads for the leg press machine."
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)
    elif gym_counter == 2:
        $ renpy.show(custom_show("maddie", "H"), [])
        "Upon entering the gym, I see Maddie increasing the weight on a shoulder press machine. She offers a wave before continuing with her workout."
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)

    elif gym_counter == 3:
        "I walk into an empty gym, and to my surprise, feel a slight sense of disappointment. I thought I'd see Maddie here again, but it seems she's taking the day off."
        $ renpy.show(custom_show("maddie", "N"), [])
        a "\'Hey.\'"
        "I turn to face Maddie who stands behind me at the entrance of the gym, taking a sip out of her ridiculous water bottle."
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'You beat me to the gym today. I guess I'll have to be faster next time.\'"
        n "\'I didn't know it was a race.\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Sure it is, a little healthy competition can be a great motivator.\'"
        n "\'Then, what do I get if I win?\'"
        $ renpy.show(custom_show("maddie", "U"), [])
        a "\'The satisfaction of victory isn't enough? How about...\'"
        if eventADateFlag:
            n "\'Another date?\'"
        else:
            n "\'A date?\'"
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'So forward! I was thinking more like...five bucks?\'"
        n "\'That works. After our next class, the first one here wins. Deal?\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Deal.\'"
        "Maddie heads towards the machines to start her workout."
        $ renpy.hide(custom_hide("maddie"))
    elif gym_counter == 4:
        "I sprint to the gym, determined to get there before Maddie."
        $ renpy.show(custom_show("maddie", "N"), [])
        "But as soon as I open the door, there she is, already at the leg press machine."
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Took you long enough.\'"
        n "\'What?! But I ran over here!\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'I guess I'm just faster than you then.\'"
        n "\'Aagh, fine.\'"
        "I pull out my wallet to hand her a five dollar bill."
        n "\'You win this time.\'"
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Is that a challenge for a rematch?\'"
        n "\'No thanks. I think I'll keep what little money I have left.\'"
        "I walk away to avoid any further gloating."
        $ renpy.hide(custom_hide("maddie"))
    else:
        n "\'...\'"

    "What should I do?"
    jump gym_main_menu


label gym_main_menu:
    menu:
        "Talk to Maddie" if not gym_choice_1_a:
            jump gym_1_talk
        "Work out" if not gym_choice_1_b:
            jump gym_1_workout
        "Say bye":
            $ renpy.show(custom_show("maddie", "N"), [])
            "I say goodbye to Maddie before heading out."
            $ A = A + 1
            stop music fadeout 1.0
            scene black with fade
            jump end_of_act
        "Go home":
            jump end_of_act
        

label gym_1_talk:
    $ maddie_unlocked = True
    $ gym_choice_1_a = True
    if A < A_bad:
        $ renpy.show(custom_show("maddie", "U"), [])
        a "\'What do you want?\'"
    elif A_bad <= A <= A_mid:
        $ renpy.show(custom_show("maddie", "N"), [])
        a "\'Hey, Sam. What's up?\'"
    elif A_mid <= A <=A_mid3:
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Hey, Sam! Great day to hit the gym, huh?\'"
    else:
        $ renpy.show(custom_show("maddie", "F"), [])
        a "\'Hey, Sam! I was hoping you'd show up today.\'"
    jump talking_to_maddie


label talking_to_maddie:
    menu:
        "Ask for her number" if not numberFlagA and not phoneFlagA:
            jump a_number
        "Engage in small talk" if not gym_choice_2_a:
            jump gym_choice_2_a
        "Get to know her" if gym_choice_2_a and not gym_choice_2_b and i < day_counter:
            jump gym_choice_2_b
        "Ask her to spot you" if gym_choice_2_a and gym_choice_2_b and not gym_choice_2_c and j < day_counter:
            jump gym_choice_2_c
        "Compliment her" if not gym_compliment:
            jump gym_choice_2_d
        "Back":
            jump gym_main_menu


label gym_choice_2_a:
    n "\'It's so quiet in here.\'"
    $ renpy.show(custom_show("maddie", "H"), [])
    a "\'Yeah, the gym's always packed during the school year. It's kind of nice having the place to ourselves though.\'"
    $ gym_choice_2_a = True
    $ A = A + 1
    $ i = day_counter
    jump talking_to_maddie


label gym_choice_2_b:
    n "\'So, what're you up to these days?\'"
    $ gym_choice_2_b = True
    $ j = day_counter
    if A > A_bad:
        $ renpy.show(custom_show("maddie", "N"), [])
        $ A = A + 1
        a "\'Oh, you know, the usual. Hiking, climbing, anything that gets me outside and moving. What about you? You still play games?\'"
        n "\'Yeah, I do. I'm trying some new things though. That's why I'm here instead of my dorm.\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'It's cool that you're taking an interest in fitness.\'"
    
        if A >= A_mid:
            a "\'It can be hard to get into, but it's definitely rewarding if you stick with it.\'"
            $ renpy.show(custom_show("maddie", "N"), [])
            n "\'Any tips on how to stay motivated?\'"
            "Maddie takes a sip of her water as she thinks."
            $ renpy.show(custom_show("maddie", "H"), [])
            a "\'Envision the person you want to be. And remember why working out will help you get there.\'"
            $ renpy.show(custom_show("maddie", "A"), [])
            a "\'There are plenty of days I'd rather just stay at home in bed. It's tempting in the moment...but when I think about who I want to become, it isn't someone who takes the easy road just 'cause it's gratifying, you know?\'"
            n "\'You want to be someone who's willing to put in the work, even when it's hard.\'"
            $ renpy.show(custom_show("maddie", "E"), [])
            a "\'Exactly. That's what a strong person does. I don't want to be seen as weak just because of my height or because I'm a girl.\'"
            $ renpy.show(custom_show("maddie", "U"), [])
            a "\'I want to be strong.\'"
            n "\'So are you almost the person you want to be?\'"
            $ renpy.show(custom_show("maddie", "S"), [])
            a "\'I don't know. But I'm a little closer every day.\'"
            n "\'Well, I don't know if it means anything coming from me, but I've never thought of you as weak.\'"
            $ renpy.show(custom_show("maddie", "H"), [])
            a "\'Thanks, Sam. Well, I guess I better keep at it then. So you don't change your mind about me.\'"

        jump talking_to_maddie
    else:
        $ renpy.show(custom_show("maddie", "A"), [])
        $ A = A - 1
        a "\'I'm not really here to make conversation. I just want to focus on my workout, okay?\'"
        jump talking_to_maddie


label gym_choice_2_c:
    $ k = day_counter
    n "\'Hey, since we're both here, do you think you could spot me on the bench press?\'"
    $ gym_choice_2_c = True

    if A >= A_mid:
        $ A = A + 2
        $ renpy.show(custom_show("maddie", "N"), [])
        a "\'Yeah, of course!\'"
        if workout_counter >= 3:
            "I do three sets, eight reps each." 
            $ renpy.show(custom_show("maddie", "F"), [])
            a "\'That's really impressive, Sam! Keep it up!\'"
            $ A = A + 1 # extra point

        elif workout_counter >= 1:
            "I do three sets, five reps each."
            $ renpy.show(custom_show("maddie", "H"), [])
            a "\'Not bad. Keep it up, Sam!\'" 

        else:
            $ A = A - 3
            "I do three sets, three reps each."
            $ renpy.show(custom_show("maddie", "U"), [])
            n "\'You okay? You seem a bit out of breath...\'"
    else:
        $ A = A - 2
        $ renpy.show(custom_show("maddie", "U"), [])
        a "\'Eh, I think I'll pass. Sorry.\'"
    jump talking_to_maddie


label gym_choice_2_d:
    $ gym_choice_2_d = True 
    $ gym_compliment = True

    if gym_comp: 
        n "\'You look nice today!\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Thanks, Sam!\'"
        jump talking_to_maddie
    else:
        $ gym_comp = True
        "Well, she's obviously attractive, but seeing how much weight she has on the machine, she seems really strong too."
        "What should I compliment her on?"
        menu:
            "Beauty":
                jump gym_choice_compliment_a
            "Strength":
                jump gym_choice_compliment_b
    

label gym_choice_compliment_a:
    "What should I say?"

    menu: 
        "You're really cute":

            n "\'I know this is kind of out of nowhere, but I just wanted to say, I think you're really cute.\'"
            if A >= A_mid:
                $ A = A + 1
                $ renpy.show(custom_show("maddie", "F"), [])
                a "\'Haha, really? That just gave me a confidence boost. Thanks, Sam.\'"
                jump talking_to_maddie
            else:
                $ A = A - 1
                $ renpy.show(custom_show("maddie", "U"), [])
                a "\'Um...Okay? Thanks, I guess?\'"
                jump talking_to_maddie

        "You have a great body":

            n "\'All this working out is really paying off. Your body looks great!\'"
            $ A = A - 3
            $ renpy.show(custom_show("maddie", "A"), [])
            a "\'Sam, that's so weird. Don't say stuff like that, okay?\'"
            jump talking_to_maddie


label gym_choice_compliment_b:
    "What should I say?"

    menu: 
        "You're really strong!":
            $ A = A + 2
            n "\'You've nearly maxed out the machine! That's crazy!\'"
            $ renpy.show(custom_show("maddie", "H"), [])
            a "\'Really? I guess it is. I sometimes forget how far I've come.\'"
            jump talking_to_maddie

        "I didn't know a girl could lift that much":
            n "\'Hey, you're pretty strong for a girl.\'"
            if 3 <= A:
                $ renpy.show(custom_show("maddie", "A"), [])
                a "\'And you're pretty annoying. Get lost, weeb.\'"
            else:
                $ renpy.show(custom_show("maddie", "U"), [])
                a "\'You could've just left off the 'for a girl' part...\'"
            $ A = A - 4
            jump talking_to_maddie

        "You're a lot stronger than me":
            n "\'Oh wow, that's impressive.\'"
            $ renpy.show(custom_show("maddie", "E"), [])
            a "\'Really?\'"
            n "\'Yeah!  I can't handle nearly that much weight!\'"
            if 2 <= A:
                $ A = A + 1
                $ renpy.show(custom_show("maddie", "F"), [])
                a "\'Haha, well, I couldn't always press this much! If you work at it, I bet you could do it too.\'"
            else:
                $ renpy.show(custom_show("maddie", "U"), [])
                a "\'Oh, maybe you just need to work out more then? I don't know what you want me to say...\'"
            jump talking_to_maddie 


label gym_1_workout:
    $ gym_choice_1_b = True 
    $ workout_counter = workout_counter + 1
    $ renpy.hide(custom_hide("maddie"))
    $ renpy.with_statement(dissolve)

    $ A = A + 1

    "I work my way through some of the gym equipment, doing three sets for every exercise and moving up in weight when it seems too easy."
    $  randnotice = renpy.random.choice(['notice', 'or not'])
    if randnotice == 'notice':
        "I catch Maddie looking in my direction."
        $ renpy.show(custom_show("maddie", "N"), [])
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
                    $ renpy.show(custom_show("maddie", "U"), [])
                    "She raises an eyebrow in confusion as she continues with her workout."

                else:
                    $ renpy.show(custom_show("maddie", "N"), [])
                    "I wave at Maddie."
                    $ renpy.show(custom_show("maddie", "H"), [])
                    a "\'Hey, Sam!\'"
                    if A >= A_high: 
                        $ A = A + 1
        $ renpy.hide(custom_hide("maddie"))
        $ renpy.with_statement(dissolve)

    scene bg_gym_b with dissolve
    "I finish a couple more sets before wiping down the equipment."
    "That was tiring, but I'm glad I pushed myself."

    jump gym_main_menu