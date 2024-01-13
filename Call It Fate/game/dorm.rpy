label act1_scene1:
    scene bg_room_a with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    "It's the first day of my summer session class, and I'm only now looking at the syllabus."
    "My professor sent it a few weeks back before the spring semester had ended, but now is the first time I'm realizing what three months of work looks like crammed into three weeks."
    "This is going to suck."
    "I'm sitting in my dorm that has the distinct smell only dingy laundry in a poorly ventilated room could cause."
    "The place is a mess. The bed isn't made, the trash is overflowing, and the only cared-for items in the room are my GS5 and desktop."
    "Well, no time to clean now. I better get to class."
    
    jump act1_scene1_menu1
    return


label act1_scene1_menu1:
    "What should I do before I go?"
    menu:
        "Get dressed." if not act1_scene1_menu1_option1:
            jump act1_scene1_menu1_option1
        "Talk to Neko-Chan." if not act1_scene1_menu1_option2:
            jump act1_scene1_menu1_option2
        "Head out." if act1_scene1_menu1_option1:
            jump act1_scene1_menu1_option3
    return


label act1_scene1_menu1_option1:
    "What should I wear?"
    $ act1_scene1_menu1_option1 = True
    menu:
        "Sleek hoodie with joggers and white sneakers":
            "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
            $ A = A + 1
        "Short-sleeved button down shirt with cuffed jeans and loafers":
            "I wish I was sophisticated enough to pull off this look."
            $ B = B + 1
        "Bold colorblock shirt tucked into tapered pants and boots":
            "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
            $ C = C + 1
        "Neko-Chan graphic tee with sweatpants and sandals":
            "There's nothing like being comfortable. Now if only I could find my fedora, that would really complete this outfit."
    jump act1_scene1_menu1


label act1_scene1_menu1_option2:
    scene bg_room_aa with dissolve
    show neko
    "What should I talk to Neko-Chan about?"
    $ act1_scene1_menu1_option2 = True
    menu: 
        "Confide in Neko-Chan.":
            n "\'Hey, Neko-Chan. I'm kind of nervous about this class.\'"
            n "\'It seems like a lot of work, and I don't know if I can handle it all.\'"
            n "\'This is going to be a rough few weeks, isn't it?\'"
            nc "\'...\'"
            n "\'The only thing that could make this class even slightly bearable would be meeting a cute girl, but we both know how unlikely that is.\'"
            n "\'Not that I'd ever be able to find a girl better than you, Neko-Chan.\'"
            n "\'You were drawn with proportions real women need surgery to achieve.\'"
            nc "\'...\'"
            hide neko
            scene bg_room_a with dissolve
            jump act1_scene1_menu1
        "Say goodbye to Neko-Chan.": 
            if not act1_scene1_menu1_option1:
                "I should get dressed first..."
                jump act1_scene1_menu1_option1
            else:
                jump act1_scene1_menu1_option3


label act1_scene1_menu1_option3:
    scene bg_room_aa with dissolve
    show neko
    n "\'Well, I better get going. Wish me luck, Neko-Chan!\'"
    nc "\'...\'"
    jump act1_scene2


label end_of_act:
    scene bg_school_transition_b with longfade

    play music "audio/dorm.mp3" fadein 1.0
    scene bg_room_b with longfade

    "It's nice to be back at my dorm."
    "What should I do?"

    #  Resetting all daily variables
    $ end_of_act_menu1_flag4 = False 
    $ end_of_act_menu1_flag3 = False 
    $ end_of_act_menu1_flag2 = False
    $ end_of_act_menu1_flag1 = False
    $ gn_a_sent = False
    $ gn_b_sent = False 
    $ gn_c_sent = False
    $ like_a_sent = False 
    $ like_b_sent = False 
    $ like_c_sent = False 
    $ date_b_sent = False
    $ hang_b_sent = False 
    $ date_c_sent = False
    $ hang_c_sent = False 
    $ date_a_sent = False
    $ hang_a_sent = False 
    $ small_a_sent = False
    $ small_b_sent = False
    $ small_c_sent = False
    jump end_of_act_menu1


label end_of_act_menu1:
    menu:
        "Check Course Website" if not end_of_act_menu1_flag1:
            jump end_of_act_menu1_option1
        "Play video games" if not end_of_act_menu1_flag2:
            jump end_of_act_menu1_option2
        "Talk to Neko-Chan" if not end_of_act_menu1_flag3:
            jump end_of_act_menu1_option3
        "Text someone" if not end_of_act_menu1_flag4:
            jump end_of_act_menu1_option4
        "Go to bed":
            jump end_of_act_menu1_option5
    return


label end_of_act_menu1_option1:
    $ end_of_act_menu1_flag1 = True
    # DELETE if day_counter == 0 or day_counter == 1 or day_counter == 3 or day_counter == 4:
    $ end_of_act_menu1_flag1_counter = end_of_act_menu1_flag1_counter + 1
    if end_of_act_menu1_flag1_counter == 1:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete Homework":
                "A pop-up appears on the page:"

                "Aristotle, the Greek philosopher, once said, 'Through discipline comes freedom.'"
                "Discipline prevents us from becoming slaves to our every impulse and allows us to work towards worthwhile goals."

                "According to Aristotle, what does discipline bring about?"

                menu:
                    "Misery":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "Authoritarianism":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "Freedom":
                        "Huh, I might actually pass this class."
                        $ class_score = class_score + 1
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1

            "Skip Homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1

    elif end_of_act_menu1_flag1_counter == 2:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete Homework":
                "A pop-up appears on the page:"

                "The philosopher and theologian St. Augustine once said, 'We are too weak to discover the truth by reason alone.'"
                "We, as humans, are limited in our knowledge and should not rely purely on our own minds for answers about the universe or ourselves."

                "According to St. Augustine, why do we need more than reason to discover the truth?"

                menu:
                    "We are too weak":
                        "Huh, I might actually pass this class."
                        $ class_score = class_score + 1
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "We are too dumb":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "We are too biased":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1

            "Skip Homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1
    
    elif end_of_act_menu1_flag1_counter == 3:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete Homework":
                "A pop-up appears on the page:"

                "The Greek philosopher Socrates once said, 'There is only one good, knowledge, and one evil, ignorance.'"
                "Those who possess knowledge can discern from wise decisions and foolish ones."

                "According to Socrates, what is the 'one evil'?"

                menu:
                    "Greed":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "Ignorance":
                        "Huh, I might actually pass this class."
                        $ class_score = class_score + 1
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "Pride":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    
            "Skip Homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1

    elif end_of_act_menu1_flag1_counter == 4:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete Homework":
                "A pop-up appears on the page:"

                "John Locke was an English philosopher who once said, 'It is one thing to show a man that he is in error, and another to put him in possession of truth.'"
                "Pointing out a person's mistakes only exalts yourself."

                "According to John Locke, what would be more important?"

                menu:
                    "Proving someone wrong":
                        "I hope I got that right..."
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1
                    "Showing someone the truth":
                        "Huh, I might actually pass this class."
                        $ class_score = class_score + 1
                        "There's nothing else to do on the class website, so I close out of the page."
                        jump end_of_act_menu1

            "Skip Homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1
    else:
        "There's nothing new on the class website, so I close out of the page."
    jump end_of_act_menu1


label end_of_act_menu1_option2:
    $ end_of_act_menu1_flag2 = True
    $ end_of_act_menu1_flag2_counter = end_of_act_menu1_flag2_counter + 1
    if end_of_act_menu1_flag2_counter == 1:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I like how many different choices it gives you and how the decisions you make change the story."
    elif end_of_act_menu1_flag2_counter == 2:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "The villagers in the game are being terrorized by a vicious dragon. They ask for my help."
    elif end_of_act_menu1_flag2_counter == 3:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I craft armor and level up until I'm confident I can take on the dragon."
    elif end_of_act_menu1_flag2_counter == 4:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I awake the dragon who sits on a hoard of gold and jewels. As we battle, I wonder if I should've prepared more for this fight..."
        "I emerge victorious from the dragon's hideout and return the gold to the villagers. They rejoice."
    else:
        "I already beat the game."
    jump end_of_act_menu1 


label end_of_act_menu1_option3:
    $ end_of_act_menu1_flag3 = True

    #  Calculating string for below
    $ max_amount = max(A,B,C)
    if max_amount == A:
        $ max_string = "Maddie"
    elif max_amount == B:
        $ max_string = "Anna"
    else:
        $ max_string = "Erin"

    scene bg_room_bb with dissolve
    show neko
    
    if max_amount <= 0:
        n "\'I'm glad I get to come home to you, Neko-Chan. My day wasn't so great. I think [max_string] really doesn't like me very much. I wonder what I did wrong...\'"
        nc "\'...\'"

    elif 0 < max_amount <= 3:
        n "\'Hey, Neko-Chan. Today was alright, but I would've stayed home with you if I could. [max_string] is pretty cool. Not that she thinks of me in that way...Why don't girls ever like me...\'"
        nc "\'...\'"

    elif 3 < max_amount <= 6:
        n "\'Today wasn't so bad...I wonder what [max_string] is doing right now.\'"
        nc "\'...\'"

    elif 6 < max_amount <= 9:
        n "\'It was a pretty good day, Neko-Chan. [max_string] and I are really hitting it off I think.\'"
        nc "\'...\'"

    elif 9 < max_amount <= 12:
        n "\'I woke feeling kind of off this morning, but getting to see [max_string] completely turned my day around.\'"
        nc "\'...\'"

    elif 12 < max_amount <= 15:
        n "\'I had a great day, Neko-Chan! I think [max_string] might even like me. Who knows? Maybe I'll finally get a girlfriend.\'"
        nc "\'...\'"
        n "\'Don't look at me like that. You knew what this was.\'" 

    else:
        n "\'I'm sorry, Neko-Chan, but if this thing with [max_string] and me is going to work, I think you and I should stop talking.\'"
        nc "\'...\'"
        n "\'I've never felt this way about anyone before...And I want to give a real relationship a shot.\'" 
        nc "\'...\'"
    hide neko
    scene bg_room_b with dissolve

    jump end_of_act_menu1 


label end_of_act_menu1_option3:
    $ end_of_act_menu1_flag3 = True
    "What should I talk to Neko-Chan about?"
    scene bg_room_bb with dissolve
    show neko

    menu:
        "Maddie" if maddie_unlocked:
            $ love_points = A
            $ love_interest = 'Maddie'
        "Anna" if anna_unlocked:
            $ love_points = B
            $ love_interest = 'Anna'
        "Erin" if erin_unlocked:
            $ love_points = C
            $ love_interest = 'Erin'
        "Neko-Chan":
            $ neko_counter = neko_counter + 1
            if neko_counter == 1:
                n "It's crazy Mom wanted me to leave you at home. I couldn't imagine coming to college without you here."
                nc "..."
            elif neko_counter == 2:
                n "I don't care what my family says. It's not weird to have a body pillow."
                nc "..."
            elif neko_counter == 3:
                n "Plenty of people hold pillows when they fall asleep, but sure, it's 'concerning' when a pciture of a half girl, half cat in a bikini is on it. If anything, that's MORE normal."
                nc "..."
            elif neko_counter == 4:
                n "Okay. FINE. So MOST people don't have anime body pillows. They're the ones missing out."
                nc "..."
            else:
                "We had a lovely talk about the weather."
            hide neko
            scene bg_room_b with dissolve

            jump end_of_act_menu1 
    
    if love_points <= 0:
        n "\'I'm glad I get to come home to you, Neko-Chan. My day wasn't so great. I think [love_interest] really doesn't like me very much. I wonder what I did wrong...\'"
        nc "\'...\'"

    elif 0 < love_points <= 3:
        n "\'Hey, Neko-Chan. Today was alright, but I would've stayed home with you if I could. [love_interest] is pretty cool. Not that she thinks of me in that way...Why don't girls ever like me...\'"
        nc "\'...\'"

    elif 3 < love_points <= 6:
        n "\'Today wasn't so bad...I wonder what [love_interest] is doing right now.\'"
        nc "\'...\'"

    elif 6 < love_points <= 9:
        n "\'It was a pretty good day, Neko-Chan. [love_interest] and I are really hitting it off I think.\'"
        nc "\'...\'"

    elif 9 < love_points <= 12:
        n "\'I woke feeling kind of off this morning, but getting to see [love_interest] completely turned my day around.\'"
        nc "\'...\'"

    elif 12 < love_points <= 15:
        n "\'I had a great day, Neko-Chan! I think [love_interest] might even like me. Who knows? Maybe I'll finally get a girlfriend.\'"
        nc "\'...\'"
        n "\'Don't look at me like that. You knew what this was.\'" 

    else:
        n "\'I'm sorry, Neko-Chan, but if this thing with [love_interest] and me is going to work, I think you and I should stop talking.\'"
        nc "\'...\'"
        n "\'I've never felt this way about anyone before...And I want to give a real relationship a shot.\'" 
        nc "\'...\'"
    
    hide neko
    scene bg_room_b with dissolve
    jump end_of_act_menu1 


label end_of_act_menu1_option4:
    $ end_of_act_menu1_flag4 = True

    if not phoneFlagA and not phoneFlagB and not phoneFlagC:
        n "\'Oh, it looks like I don't have anyone to text...\'"
        jump end_of_act_menu1 
    else:
        "Who should I text?"
        menu:
            "Text Maddie" if phoneFlagA:
                jump actA_sceneText
            "Text Anna" if phoneFlagB:
                jump actB_sceneText
            "Text Erin" if phoneFlagC:
                jump actC_sceneText


label end_of_act_menu1_option5:
    scene bg_room_c with dissolve
    "I microwave some ramen for dinner before turning in for the night."
    
    stop music fadeout 1.0
    if eventAHangFlag and not eventAHangCompletedFlag:
        jump eventAHang
    elif eventBHangFlag and not eventBHangCompletedFlag:
        jump eventBHang
    elif eventCHangFlag and not eventCHangCompletedFlag:
        jump eventCHang
    else:
        jump event_calculation_1


label event_calculation_1:
    # day_counter calculation for outfits

    stop music fadeout 1.0

    if day_counter == 0:
        scene black with longfade
        with Pause(1)
        show calendar_02 with dissolve
        with Pause (1)
        show calendar_03 with dissolve
        with Pause (1)
        scene black with longfade
        jump act1_scene2
    elif day_counter == 1:
        scene black with longfade
        with Pause(1)
        show calendar_04 with dissolve
        with Pause (1)
        show calendar_05 with dissolve
        with Pause (1)
        scene black with longfade
        jump act1_scene3
    elif day_counter == 2:
        scene black with longfade
        with Pause(1)
        show calendar_06 with dissolve
        with Pause (1)
        show calendar_07 with dissolve
        with Pause (1)
        show calendar_08 with dissolve
        scene black with longfade
        with Pause (1)
        jump act2_scene1
    elif day_counter == 3:
        scene black with longfade
        with Pause(1)
        show calendar_09 with dissolve
        with Pause (1)
        show calendar_10 with dissolve
        with Pause (1)
        scene black with longfade
        jump act2_scene2
    elif day_counter == 4:
        scene black with longfade
        with Pause(1)
        show calendar_11 with dissolve
        with Pause (1)
        show calendar_12 with dissolve
        with Pause (1)
        scene black with longfade
        jump act2_scene3
    elif day_counter == 5:
        scene black with longfade
        with Pause(1)
        show calendar_13 with dissolve
        with Pause (1)
        show calendar_14 with dissolve
        with Pause (1)
        show calendar_15 with dissolve
        with Pause (1)
        scene black with longfade
        jump act3_scene1
    elif day_counter == 6:
        scene black with longfade
        with Pause(1)
        show calendar_16 with dissolve
        with Pause (1)
        show calendar_17 with dissolve
        with Pause (1)
        scene black with longfade
        jump act3_scene2
    else:
        scene black with longfade
        with Pause(1)
        show calendar_16 with dissolve
        with Pause (1)
        show calendar_17 with dissolve
        with Pause (1)
        scene black with longfade
        jump act3_scene2


label event_calculation_2:
    # Calculating whose event is triggered
    $ day_counter = day_counter + 1
    $ max_amount = max(A,B,C)
    if max_amount == A:
        jump actA_scene3
    elif max_amount == B:
        jump actB_scene3 
    else:
        jump actC_scene3 