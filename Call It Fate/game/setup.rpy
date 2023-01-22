# AFTER SCHOOL BELOW:
label after_class:

    $ a_number_flag = False 
    $ b_number_flag = False 
    $ c_number_flag = False 
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
            jump gym
        "Go to the library.":
            "I'll go to the library. If I want to do well in this class, I better study."
            $ lib_counter = lib_counter + 1
            jump library
        "Go to the art room.":
            "I'll go to the art room. I have to practice if I want to improve."
            $ art_counter = art_counter + 1
            jump art
        "Go to my dorm.":
            "I'm feeling pretty tired. I think I'll just head home."
            jump end_of_day
    stop music fadeout 1.0
    return

# END OF DAY BELOW:
label end_of_day:
    play music "audio/dorm.mp3"
    scene bg_room_afterclass with fade

    "It's nice to be back at my dorm."
    "What should I do?"

    $ text_flag = False 
    $ body_flag = False 
    $ game_flag = False
    $ course_flag = False
    #$ video_a_sent = False 
    #$ video_b_sent = False 
    #$ video_c_sent = False 
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
    jump end_of_day_menu
    return

label end_of_day_menu:
    menu:
        "Check Course Website" if not course_flag:
            jump check_course_website
        "Play video games" if not game_flag:
            jump play_video_games
        "Talk to Neko-Chan" if not body_flag:
            jump talk_nc
        "Text someone" if not text_flag:
            jump text_someone
        "Go to bed":
            jump goodnight_sam
    return

label check_course_website:
    $ course_flag = True
    #Change
    if day == 0 or day == 1 or day == 3 or day == 4:
        $ course_counter = course_counter + 1
        if course_counter == 1:
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
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Authoritarianism":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Freedom":
                            "Huh, I might actually pass this class."
                            $ grade = grade + 1
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu

                "Skip Homework":
                    "I don't really feel like doing work right now..."
                    jump end_of_day_menu

        elif course_counter == 2:
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
                            $ grade = grade + 1
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "We are too dumb":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "We are too biased":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu

                "Skip Homework":
                    "I don't really feel like doing work right now..."
                    jump end_of_day_menu
        
        elif course_counter == 3:
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
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Ignorance":
                            "Huh, I might actually pass this class."
                            $ grade = grade + 1
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Pride":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        
                "Skip Homework":
                    "I don't really feel like doing work right now..."
                    jump end_of_day_menu

        elif course_counter == 4:
            "It looks like Dr. Paige posted an assignment."
            menu:
                "Complete Homework":
                    "A pop-up appears on the page:"

                    "John Locke was an English philosopher who once said, 'It is one thing to show a man that he is in error, and another to put him in possession of truth'"
                    "Pointing out a person's mistakes only exalts yourself."

                    "According to John Locke, what would be more important?"

                    menu:
                        "Proving someone wrong":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Showing someone the truth":
                            "Huh, I might actually pass this class."
                            $ grade = grade + 1
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu

                "Skip Homework":
                    "I don't really feel like doing work right now..."
                    jump end_of_day_menu
        jump end_of_day_menu
    else:
        "There isn't anything new posted."
        jump end_of_day_menu

    return


label play_video_games:
    $ game_flag = True
    $ game_counter = game_counter + 1
    if game_counter == 1:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I like how many different choices it gives you and how the decisions you make change the story."
    elif game_counter == 2:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "The villagers in the game are being terrorized by a vicious dragon. They ask for my help."
    elif game_counter == 3:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I craft armor and level up until I'm confident I can take on the dragon."
    elif game_counter == 4:
        "I turn on my GS5 and TV, the blue light blinding in the dark room, and play my favorite RPG."
        "I awake the dragon who sits on a hoard of gold and jewels. As we battle, I wonder if I should've prepared more for this fight..."
        "I emerge victorious from the dragon's hideout and return the gold to the villagers. They rejoice."
    else:
        "I already beat the game."
    jump end_of_day_menu 
    return

label talk_nc:
    $ body_flag = True
    $ max_amount = max(A,B,C)
    if max_amount == A:
        $ max_string = "Maddie"
    elif max_amount == B:
        $ max_string = "Anna"
    else:
        $ max_string = "Erin"
    
    show neko
    
    if max_amount <= 0:
        n "\"I'm glad I get to come home to you, Neko-Chan. My day wasn't so great. I think [max_string] really doesn't like me very much. I wonder what I did wrong...\""
        nc "\"...\""

    elif 0 < max_amount <= 3:
        n "\"Hey, Neko-Chan. Today was alright, but I would've stayed home with you if I could. [max_string] is pretty cool. Not that she thinks of me in that way...Why don't girls ever like me...\""
        nc "\"...\""

    elif 3 < max_amount <= 6:
        n "\"Today wasn't so bad...I wonder what [max_string] is doing right now.\""
        nc "\"...\""

    elif 6 < max_amount <= 9:
        n "\"It was a pretty good day, Neko-Chan. [max_string] and I are really hitting it off I think.\""
        nc "\"...\""

    elif 9 < max_amount <= 12:
        n "\"I woke feeling kind of off this morning, but getting to see [max_string] completely turned my day around.\""
        nc "\"...\""

    elif 12 < max_amount <= 15:
        n "\"I had a great day, Neko-Chan! I think [max_string] might even like me. Who knows? Maybe I'll finally get a girlfriend.\""
        nc "\"...\""
        n "\"Don't look at me like that. You knew what this was.\"" 

    else:
        n "\"I’m sorry, Neko-Chan, but if this thing with [max_string] and me is going to work, I think you and I should stop talking.\""
        nc "\"...\""
        n "\"I’ve never felt this way about anyone before...And I want to give a real relationship a shot.\"" 
        nc "\"...\""
    hide neko
    jump end_of_day_menu 
    return

label text_someone:
    $ text_flag = True

    if not a_number_obtained_flag and not b_number_obtained_flag and not c_number_obtained_flag:
        n "\"Oh, it looks like I don't have anyone to text...\""
        jump end_of_day_menu 
        return

    else:
        "Who should I text?"
        menu:
            "Text Maddie" if a_number_obtained_flag:
                jump send_text_a
            "Text Anna" if b_number_obtained_flag:
                jump send_text_b
            "Text Erin" if c_number_obtained_flag:
                jump send_text_c
    return

label goodnight_sam:
    scene bg_room_dark with fade
    "I microwave some ramen for dinner before turning in for the night."
    stop music fadeout 1.0
    if eventaa_trigger and not maddie_hang_over:
        jump event_aa
    
    if eventab_trigger and not anna_hang_over:
        jump event_ab
    
    if eventac_trigger and not erin_hang_over:
        jump event_ac
    
    jump quick_calculations

label quick_calculations:
    stop music fadeout 1.0
    scene black with longfade

    if day == 0:
        jump ch1_schoolday2
    else:
        if day == 1:
            jump ch1_weekend
        else:
            if day == 2:
                jump ch2_schoolday1
            else:
                if day == 3:
                    jump ch2_schoolday2
                else:
                    if day == 4:
                        jump ch2_weekend
                    else:
                        if day == 5:
                            # event d
                            jump ch3_schoolday1
                        else:
                            if day == 6:
                                jump ch3_schoolday2
                            else:
                                jump ch3_schoolday2
                                return



label event_c:
    scene bg_room_afterclass with fade
    play music "audio/event.mp3"

    "I take a deep breath."
    "I don't know much about this kind of thing, but if I'm really going to do this, I feel like I should bring a gift."
    "Luckily, I have a couple hours before dusk to get something."
    "What should I give her?"

    menu:
        "A potted succulent":
            $ maddie_gift = True
            scene black with longfade
            "I swing by the local nursery and pick up a succulent before heading back to campus."
        "A venus fly trap":
            $ anna_gift = True
            scene black with longfade
            "I grab a venus fly trap at a pet shop before heading back to campus."
        "A bouquet of sunflowers":
            $ erin_gift = True
            scene black with longfade
            "I pick up a bouquet of sunflowers from a flower shop before heading back to campus."
        "A single rose":
            scene black with longfade
            "I buy a single rose from the grocery store before heading back to campus."

    if eventca_trigger:
        jump event_ca
    elif eventcb_trigger:
        jump event_cb 
    elif eventcc_trigger:
        jump event_cc 
    return

label neko_ending:
    stop music fadeout 1.0
    "And in that moment, it hits me."
    "I've made the wrong choice."
    "I shouldn't be here."
    "She isn't the girl I want to be with."
    n "\"Um...sorry...I have to go.\""
    
    scene bg_room with fade
    play music "audio/event.mp3"

    "I leave the roof and head back to my dorm where Neko-Chan sits on her usual spot on my bed."
    n "\"Oh thank God you're still here.\""
    show neko
    nc "\"...\""
    n "\"Listen, on the roof I realized something.\""
    n "I realized that you're the only girl who's always been there for me. The only one who liked me the way I was and never expected me to change...\""
    n "\"I'm sorry I didn't realize it sooner, Neko-Chan, but I want to be with you. What do you say?\""
    nc "\"...\""
    n "\"I'm so happy you feel the same.\""
    "I hold Neko-Chan in my arms and smile, knowing that for now on, it's just going to be me and her."
    "Forever."
    scene black with longfade
    jump credits
    return 

label event_d:
    $ day = day + 1
    $ max_amount = max(A,B,C)
    if max_amount == B:
        jump event_db
    elif max_amount == C:
        jump event_dc 
    else:
        jump event_da 
    return 