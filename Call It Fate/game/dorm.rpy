label act1_scene0:
    scene bg_room_a with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    "It's the first day of my summer session class, and I'm only now looking at the syllabus."
    "My professor sent it a few weeks back before the spring semester had ended, but now is the first time I'm realizing what three months of work looks like crammed into three weeks."
    "This is going to suck."
    "I'm sitting in my dorm that has the distinct smell only dingy laundry in a poorly ventilated room could cause."
    "The place is a mess. The bed isn't made, the trash is overflowing, and the only cared-for items in the room are my GS5 and desktop."
    "Well, no time to clean now. I better get to class."
    jump act1_scene0_menu1


label act1_scene0_menu1:
    "What should I do before I go?"
    menu:
        "Get dressed." if not act1_scene0_menu1_option1:
            jump act1_scene0_menu1_option1
        "Talk to Neko-Chan." if not act1_scene0_menu1_option2:
            jump act1_scene0_menu1_option2
        "Head out." if act1_scene0_menu1_option1:
            jump act1_scene0_menu1_option3


label act1_scene0_menu1_option1:
    "What should I wear?"
    $ act1_scene0_menu1_option1 = True
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
    jump act1_scene0_menu1


label act1_scene0_menu1_option2:
    scene bg_room_aa with dissolve
    show neko
    "What should I talk to Neko-Chan about?"
    $ act1_scene0_menu1_option2 = True
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
            jump act1_scene0_menu1
        "Say goodbye to Neko-Chan.": 
            if not act1_scene0_menu1_option1:
                "I should get dressed first..."
                jump act1_scene0_menu1_option1
            else:
                jump act1_scene0_menu1_option3


label act1_scene0_menu1_option3:
    scene bg_room_aa with dissolve
    show neko
    n "\'Well, I better get going. Wish me luck, Neko-Chan!\'"
    nc "\'...\'"
    jump act1_scene1


label end_of_act:
    scene bg_school_transition_b with longfade
    play sound "audio/door.mp3"
    with Pause (1)
    play music "audio/dorm.mp3" fadein 1.0
    scene bg_room_b with longfade

    "It's nice to be back at my dorm."
    "What should I do?"

    #  Resetting all daily variables
    $ end_of_act_menu1_flag4 = False 
    $ end_of_act_menu1_flag3 = False 
    $ end_of_act_menu1_flag2 = False
    $ end_of_act_menu1_flag1 = False
    $ gnSentA = False
    $ gnSentB = False 
    $ gnSentC = False
    $ dateSentFlagB = False
    $ hangSentFlagB = False 
    $ dateSentFlagC = False
    $ hangSentFlagC = False 
    $ dateSentFlagA = False
    $ hangSentFlagA = False 
    $ smallTalkFlagA = False
    $ smallTalkFlagB = False
    $ smallTalkFlagC = False
    jump end_of_act_menu1


label end_of_act_menu1:
    menu:
        "Check course website" if not end_of_act_menu1_flag1:
            jump end_of_act_menu1_option1
        "Play video games" if not end_of_act_menu1_flag2:
            jump end_of_act_menu1_option2
        "Talk to Neko-Chan" if not end_of_act_menu1_flag3:
            jump end_of_act_menu1_option3
        "Text someone" if not end_of_act_menu1_flag4:
            jump end_of_act_menu1_option4
        "Go to bed":
            jump end_of_act_menu1_option5


label end_of_act_menu1_option1:
    $ end_of_act_menu1_flag1 = True
    $ end_of_act_menu1_flag1_counter = end_of_act_menu1_flag1_counter + 1
    if end_of_act_menu1_flag1_counter == 1:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete homework":
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

            "Skip homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1

    elif end_of_act_menu1_flag1_counter == 2:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete homework":
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

            "Skip homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1
    
    elif end_of_act_menu1_flag1_counter == 3:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete homework":
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
                    
            "Skip homework":
                "I don't really feel like doing work right now..."
                jump end_of_act_menu1

    elif end_of_act_menu1_flag1_counter == 4:
        "It looks like Dr. Paige posted an assignment."
        menu:
            "Complete homework":
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

            "Skip homework":
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
    jump event_calculation_a

label act1_scene3:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_room_a with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    if weekendDateFlag:
        "Finally, the week's over."
        "Usually, I'd just stay home--sleep in, watch TV, play some games, talk to Neko-Chan. But I actually have a reason to go out this weekend."
        stop music fadeout 1.0
        play music "audio/event.mp3" fadein 1.0
        if eventADateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventADate
        elif eventBDateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventBDate 
        elif eventCDateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventCDate

    else: 
        "I can't believe the weekend is almost over. I wish I had something to do…"
        "I laze around my dorm, playing games and watching TV, until the next school day."
        jump event_calculation_a


label act2_scene3:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_room_a with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    if weekendDateFlag:
        "Finally, the week's over."
        "Usually, I'd just stay home--sleep in, watch TV, play some games, talk to Neko-Chan. But I actually have a reason to go out this weekend."
        stop music fadeout 1.0
        play music "audio/event.mp3" fadein 1.0
        if eventADateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventADate
        elif eventBDateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventBDate 
        elif eventCDateFlag:
            $ temp = day_counter
            $ temp_usage = True
            $ day_counter = 10
            jump eventCDate

    else: 
        "I can't believe the weekend is almost over. I wish I had something to do…"
        "I laze around my dorm, playing games and watching TV, until the next school day."
        jump event_calculation_a


label act3_scene1:
    scene bg_school_transition_a with dissolve
    play sound "audio/morning.mp3"
    with Pause (2)
    scene bg_room_a with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    "I wake up and my head feels heavy. There's a pulse at the front of my skull, a stuffiness in my ears. It's Tuesday, but I don't think I'll be able to go to class."
    "I get out my phone and write an email to Dr. Paige explaining the situation, and shortly after pressing send, I drift back to sleep."
    scene black with fade
    "When I wake up again, it's 3:30pm."
    scene bg_room_b with dissolve
    n "\'Man, I can't believe I slept through the afternoon...\'"
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
    # Calculating whose event is triggered
    $ max_amount = max(A,B,C)
    if max_amount == A:
        jump actA_scene3
    elif max_amount == B:
        jump actB_scene3 
    else:
        jump actC_scene3 


label event_ending_decision2_decision:
    scene bg_school_transition_b with longfade
    play sound "audio/door.mp3"
    with Pause (1)

    scene bg_room_b with dissolve
    play music "audio/free.mp3" fadein 1.0
    python:
        if phoneFlagA:
            if phoneFlagB:
                if phoneFlagC:
                    char_string = "Maddie, Anna, or Erin"
                else:
                    char_string = "Maddie or Anna"
            else:
                char_string = "Maddie"
        else:
            if phoneFlagB:
                if phoneFlagC:
                    char_string = "Anna or Erin"
                else:
                    char_string = "Anna"
            else:
                if phoneFlagC:
                    char_string = "Erin"
                else:
                    char_string = "NONE"

    if char_string == "NONE":
        $ nekochan = True
        "I head back to my dorm, too drained to do anything else, and though I didn't get to know the girls in my class as much as I'd hoped, I feel content."
        "I think some people might see my life and assume I'm lonely."
        "But I'm actually okay."
        "As I look at Neko-Chan, I think about how she is the only girl in my life who could never hurt me."
        "Real girls are too complicated."
        "Too confusing."
        "They expect too much."
        "Neko-Chan doesn't expect anything. She accepts me the way I am."
        "And that's enough for me."
        jump credits_1
    else:
        "I head back to my dorm, too drained to do anything else, and though I know I should be relieved that I'm done with Intro to Philosophy, I'm left with a bittersweet sentiment."
        "The LU campus is pretty big. There's no guarantee that I'll get a chance to see [char_string] again."
        "If there's something I need to say, I should say it now."
    
    menu:
        "Confess feelings to Maddie" if phoneFlagA:
            $ endingAFlag_Attempt = True
            "I can't just tell her something like that over text. It should be in person."
            "So I write and send a message that reads:"
            n "\'Hey, there's something I want to talk with you about. Do you think we could meet up?\'"
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Sounds serious. :o When did you want to meet?\'"
            "I type \'Meet me on top of the library, at sunset\' and hit send."
            jump event_ending_decision2
        "Confess feelings to Anna" if phoneFlagB:
            $ endingBFlag_Attempt = True
            "I can't just tell her something like that over text. It should be in person."
            "So I write and send a message that reads:"
            n "\'Hey, there's something I want to talk with you about. Do you think we could meet up?\'"
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'We can do that. Give me a time and place, and I'll be there.\'"
            "I type \'Meet me on top of the library, at sunset\' and hit send."
            jump event_ending_decision2
        "Confess feelings to Erin" if phoneFlagC:
            $ endingCFlag_Attempt = True
            "I can't just tell her something like that over text. It should be in person."
            "So I write and send a message that reads:"
            n "\'Hey, there's something I want to talk with you about. Do you think we could meet up?\'"
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Is everything okay?? We can talk. Where should I meet you?\'"
            "I type \'Meet me on top of the library, at sunset\' and hit send."
            jump event_ending_decision2
        "I have nothing to say":
            "I think some people might see my life and assume I'm lonely. But I'm actually okay."
            "As I look at Neko-Chan, I think about how she is the only girl in my life who could never hurt me."
            "Real girls are too complicated."
            "Too confusing."
            "They expect too much."
            "Neko-Chan doesn't expect anything. She accepts me the way I am."
            "And that's enough for me."
            $ nekochan = True
            jump credits_1
            

label event_ending_decision2:
    scene bg_room_b with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I take a deep breath."
    "I don't know much about this kind of thing, but if I'm really going to do this, I feel like I should bring a gift. Luckily, I have a couple hours before dusk to get something."
    scene bg_gift with dissolve
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
    
    if endingAFlag_Attempt:
        jump eventRoofA
    elif endingBFlag_Attempt:
        jump eventRoofB
    else:
        jump eventRoofC


label event_calculation_a:
    # day_counter calculation for outfits
    if eventADateCompletedFlag and eventADateToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventADateToday = False
        $ calendar_days_skipped = 2
    elif eventBDateCompletedFlag and eventBDateToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventBDateToday = False
        $ calendar_days_skipped = 2
    elif eventCDateCompletedFlag and eventCDateToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventCDateToday = False
        $ calendar_days_skipped = 2
    elif eventAHangCompletedFlag and eventAHangToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventAHangToday = False
        if day_counter == 11 or day_counter == 4:
            $ calendar_days_skipped = 2
        else:
            $ calendar_days_skipped = 1
    elif eventBHangCompletedFlag and eventBHangToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventBHangToday = False
        if day_counter == 11 or day_counter == 4:
            $ calendar_days_skipped = 2
        else:
            $ calendar_days_skipped = 1
    elif eventCHangCompletedFlag and eventCHangToday:
        scene bg_room_c with longfade
        play music "audio/dorm.mp3"
        "I get ready for bed after a long day."
        $ day_counter = temp
        $ temp_usage = False
        $ eventCHangToday = False
        if day_counter == 11 or day_counter == 4:
            $ calendar_days_skipped = 2
        else:
            $ calendar_days_skipped = 1
    elif not eventAHangCompletedFlag and eventAHangFlag:
        $ calendar_days_skipped = 1
    elif not eventBHangCompletedFlag and eventBHangFlag:
        $ calendar_days_skipped = 1
    elif not eventCHangCompletedFlag and eventCHangFlag:
        $ calendar_days_skipped = 1
    elif day_counter == 3 or day_counter == 10:
        $ calendar_days_skipped = 3
    else:
        $ calendar_days_skipped = 2

    stop music fadeout 1.0
    scene black with longfade
    play sound "audio/night.mp3"

    jump calendarAnimation_1


label calendarAnimation_1:
    if day_counter == 1: # Tuesday first day of class
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_01a with dissolve
            with Pause (1)
            show calendar_02 with dissolve
            with Pause (1)
            $ day_counter = 2
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_01a with dissolve
            with Pause (1)
            show calendar_02 with dissolve
            with Pause (1)
            show calendar_03 with dissolve
            with Pause (1)
            $ day_counter = 3
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_01a with dissolve
            with Pause (1)
            show calendar_02 with dissolve
            with Pause (1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            $ day_counter = 4
    elif day_counter == 2: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_02 with dissolve
            with Pause (1)
            show calendar_03 with dissolve
            with Pause (1)
            $ day_counter = 3
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_02 with dissolve
            with Pause (1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            $ day_counter = 4
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_02 with dissolve
            with Pause (1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            $ day_counter = 5
    elif day_counter == 3: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            $ day_counter = 4
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            $ day_counter = 5
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_03 with dissolve
            with Pause (1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            $ day_counter = 6
    elif day_counter == 4: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            $ day_counter = 5
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            $ day_counter = 6
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_04 with dissolve
            with Pause (1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            $ day_counter = 7
    elif day_counter == 5: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            $ day_counter = 6
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            $ day_counter = 7
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_05 with dissolve
            with Pause (1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            $ day_counter = 8
    elif day_counter == 6: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            $ day_counter = 7
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            $ day_counter = 8
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_06 with dissolve
            with Pause (1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            $ day_counter = 9
    elif day_counter == 7: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            $ day_counter = 8
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            $ day_counter = 9
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_07 with dissolve
            with Pause (1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            $ day_counter = 10
    elif day_counter == 8: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            $ day_counter = 9
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            $ day_counter = 10
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_08 with dissolve
            with Pause (1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            $ day_counter = 11
    elif day_counter == 9: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            $ day_counter = 10
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            show calendar_11 with dissolve
            with Pause (1)
            $ day_counter = 11
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_09 with dissolve
            with Pause (1)
            show calendar_10 with dissolve
            with Pause (1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            $ day_counter = 12
    elif day_counter == 10: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_10 with dissolve
            with Pause (1)
            show calendar_11 with dissolve
            with Pause (1)
            $ day_counter = 11
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_10 with dissolve
            with Pause (1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            $ day_counter = 12
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_10 with dissolve
            with Pause (1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            $ day_counter = 13
    elif day_counter == 11: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            $ day_counter = 12
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            $ day_counter = 13
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_11 with dissolve
            with Pause (1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            $ day_counter = 14
    elif day_counter == 12: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            $ day_counter = 13
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            $ day_counter = 14
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_12 with dissolve
            with Pause (1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            $ day_counter = 15
    elif day_counter == 13: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            $ day_counter = 14
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            $ day_counter = 15
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_13 with dissolve
            with Pause (1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            $ day_counter = 16
    elif day_counter == 14: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            $ day_counter = 15
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            $ day_counter = 16
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_14 with dissolve
            with Pause (1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 17
    elif day_counter == 15: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            $ day_counter = 16
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 17
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_15 with dissolve
            with Pause (1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 18
    elif day_counter == 16: 
        if calendar_days_skipped == 1:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 17
        elif calendar_days_skipped == 2:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 18
        elif calendar_days_skipped == 3:
            scene bg_school_transition_a with dissolve
            play sound "audio/morning.mp3"
            with Pause(1)
            show calendar_16 with dissolve
            with Pause (1)
            show calendar_17 with dissolve
            with Pause (1)
            show calendar_18 with dissolve
            with Pause (1)
            $ day_counter = 19
    jump event_calculation_b


label event_calculation_b:
    # day_counter calculation for outfits    
    if eventAHangFlag and not eventAHangCompletedFlag:
        scene bg_room_a with longfade
        play music "audio/dorm.mp3"
        "I get ready to see Maddie."
        $ temp = day_counter
        $ temp_usage = True
        $ day_counter = 2
        jump eventAHang
    elif eventBHangFlag and not eventBHangCompletedFlag:
        scene bg_room_a with longfade
        play music "audio/dorm.mp3"
        "I get ready to see Anna."
        $ temp = day_counter
        $ temp_usage = True
        $ day_counter = 1
        jump eventBHang
    elif eventCHangFlag and not eventCHangCompletedFlag:
        scene bg_room_a with longfade
        play music "audio/dorm.mp3"
        "I get ready to see Erin."
        $ temp = day_counter
        $ temp_usage = True
        $ day_counter = 4
        jump eventCHang

    if day_counter == 0: # Tuesday first day of class
        jump act1_scene2
    elif day_counter == 1: 
        jump act1_scene2
    elif day_counter == 2: 
        jump act1_scene2
    elif day_counter == 3: 
        jump act1_scene2
    elif day_counter == 4: 
        jump act1_scene3
    elif day_counter == 5: 
        jump act1_scene3
    elif day_counter == 6: 
        jump act1_scene3
    elif day_counter == 7: 
        jump act1_scene3
    elif day_counter == 8: 
        jump act2_scene1
    elif day_counter == 9: 
        jump act2_scene2
    elif day_counter == 10: 
        jump act2_scene2
    elif day_counter == 11: 
        jump act2_scene3
    elif day_counter == 12: 
        jump act2_scene3
    elif day_counter == 13: 
        jump act2_scene3
    elif day_counter == 14:
        jump act2_scene3
    elif day_counter == 15: 
        jump act3_scene1
    elif day_counter == 16: 
        jump act3_scene1
    else:
        jump act3_scene2
