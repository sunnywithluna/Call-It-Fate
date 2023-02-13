label intro:
    scene bg_room with dissolve
    play music "audio/dorm.mp3" fadein 1.0

    "It's the first day of my summer session class, and I'm only now looking at the syllabus."
    "My professor sent it a few weeks back before the spring semester had ended, but now is the first time I'm realizing what three months of work looks like crammed into three weeks."
    "This is going to suck."
    "I'm sitting in my dorm that has the distinct smell only dingy laundry in a poorly room could cause."
    "The place is a mess. The bed isn't made, the trash is overflowing, and the only cared-for items in the room are my GS5 and desktop."
    "Well, no time to clean now. I better get to class."
    jump intro_menu
    return

label intro_menu:
    "What should I do before I go?"
    menu:
        "Get dressed." if not get_dressed:
            jump get_dressed
        "Talk to Neko-Chan." if not intro_nc:
            jump intro_nc
        "Head out." if get_dressed:
            show neko
            nc "\"...\""
            jump school_day01
    return

label get_dressed:
    "What should I wear?"
    $get_dressed = True
    menu:
        "Sleek hoodie with joggers and white sneakers":
            "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
            $A = A + 1
        "Short-sleeved button down shirt with cuffed jeans and loafers":
            "I wish I was sophisticated enough to pull off this look."
            $B = B + 1
        "Bold colorblock shirt tucked into tapered pants and boots":
            "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
            $C = C + 1
        "Neko-Chan graphic tee with sweatpants and sandals":
            jump intro_menu
    jump intro_menu
    return

label intro_nc:
    show neko
    "What should I talk to Neko-Chan about?"
    $intro_nc = True
    menu: 
        "Confide in Neko-Chan." if not confide_nc:
            $confide_nc = True
            n "\"Hey, Neko-Chan. I'm kind of nervous about this class.\""
            n "\"It seems like a lot of work, and I don't know if I can handle it all.\""
            n "\"This is going to be a rough few weeks, isn't it?\""
            nc "\"...\""
            n "\"The only thing that could make this class even slightly bearable would be meeting a cute girl, but we both know how unlikely that is.\""
            n "\"Not that I'd ever be able to find a girl better than you, Neko-Chan.\""
            n "\"You were drawn with proportions real women need surgery to achieve.\""
            nc "\"...\""
            hide neko
            jump intro_menu
        "Say goodbye to Neko-Chan.": 
            jump goodbye_nc
    return

label goodbye_nc:
    if not get_dressed:
        $get_dressed = True
        "I should get dressed first..."
        "What should I wear?"
        menu:
            "Sleek hoodie with joggers and white sneakers":
                "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
                $A = A + 1
            "Short-sleeved button down shirt with cuffed jeans and loafers":
                "I wish I was sophisticated enough to pull off this look."
                $B = B + 1
            "Bold colorblock shirt tucked into tapered pants and boots":
                "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
                $C = C + 1
            "Neko-Chan graphic tee with sweatpants and sandals":
                "There's nothing like being comfortable. Now if only I could find my fedora, that would really complete this outfit."
    
    show neko
    n "\"Well, I better get going. Wish me luck, Neko-Chan!\""
    nc "\"...\""
    jump school_day01

    
label end_of_day:
    play music "audio/dorm.mp3" fadein 1.0
    scene bg_room_afterclass with dissolve

    "It's nice to be back at my dorm."
    "What should I do?"

    $text_flag = False 
    $body_flag = False 
    $game_flag = False
    $course_flag = False
    $gn_a_sent = False
    $gn_b_sent = False 
    $gn_c_sent = False
    $like_a_sent = False 
    $like_b_sent = False 
    $like_c_sent = False 
    $date_b_sent = False
    $hang_b_sent = False 
    $date_c_sent = False
    $hang_c_sent = False 
    $date_a_sent = False
    $hang_a_sent = False 
    $small_a_sent = False
    $small_b_sent = False
    $small_c_sent = False
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
    $course_flag = True
    #Change
    if day == 0 or day == 1 or day == 3 or day == 4:
        $course_counter = course_counter + 1
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
                            $grade = grade + 1
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
                            $grade = grade + 1
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
                            $grade = grade + 1
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

                    "John Locke was an English philosopher who once said, 'It is one thing to show a man that he is in error, and another to put him in possession of truth.'"
                    "Pointing out a person's mistakes only exalts yourself."

                    "According to John Locke, what would be more important?"

                    menu:
                        "Proving someone wrong":
                            "I hope I got that right..."
                            "There's nothing else to do on the class website, so I close out the page."
                            jump end_of_day_menu
                        "Showing someone the truth":
                            "Huh, I might actually pass this class."
                            $grade = grade + 1
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
    $game_flag = True
    $game_counter = game_counter + 1
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

label talk_nc1:
    $body_flag = True
    $max_amount = max(A,B,C)
    if max_amount == A:
        $max_string = "Maddie"
    elif max_amount == B:
        $max_string = "Anna"
    else:
        $max_string = "Erin"
    
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

label talk_nc:
    $body_flag = True
    "What should you talk about?"
    show neko

    menu:
        "Maddie":
            $girl_num = A
            $girl_string = 'Maddie'
        "Anna":
            $girl_num = B
            $girl_string = 'Anna'
        "Erin":
            $girl_num = C
            $girl_string = 'Erin'
        "The weather":
            jump talk_nc_d 
    
    if girl_num <= 0:
        n "\"I'm glad I get to come home to you, Neko-Chan. My day wasn't so great. I think [girl_string] really doesn't like me very much. I wonder what I did wrong...\""
        nc "\"...\""

    elif 0 < girl_num <= 3:
        n "\"Hey, Neko-Chan. Today was alright, but I would've stayed home with you if I could. [girl_string] is pretty cool. Not that she thinks of me in that way...Why don't girls ever like me...\""
        nc "\"...\""

    elif 3 < girl_num <= 6:
        n "\"Today wasn't so bad...I wonder what [girl_string] is doing right now.\""
        nc "\"...\""

    elif 6 < girl_num <= 9:
        n "\"It was a pretty good day, Neko-Chan. [girl_string] and I are really hitting it off I think.\""
        nc "\"...\""

    elif 9 < girl_num <= 12:
        n "\"I woke feeling kind of off this morning, but getting to see [girl_string] completely turned my day around.\""
        nc "\"...\""

    elif 12 < girl_num <= 15:
        n "\"I had a great day, Neko-Chan! I think [girl_string] might even like me. Who knows? Maybe I'll finally get a girlfriend.\""
        nc "\"...\""
        n "\"Don't look at me like that. You knew what this was.\"" 

    else:
        n "\"I'm sorry, Neko-Chan, but if this thing with [girl_string] and me is going to work, I think you and I should stop talking.\""
        nc "\"...\""
        n "\"I've never felt this way about anyone before...And I want to give a real relationship a shot.\"" 
        nc "\"...\""
    hide neko
    jump end_of_day_menu 
    return

label talk_nc_d:
    "We had a lovely talk about the weather."
    hide neko
    jump end_of_day_menu 
    return

label text_someone:
    $text_flag = True

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
    scene bg_room_dark with dissolve
    "I microwave some ramen for dinner before turning in for the night."
    stop music fadeout 1.0
    if eventaa_trigger and not maddie_hangout:
        jump maddie_hangout
    
    if eventab_trigger and not anna_hangout:
        jump anna_hangout
    
    if eventac_trigger and not erin_hangout:
        jump erin_hangout
    
    jump quick_calculations

label quick_calculations:
    stop music fadeout 1.0
    scene black with fade

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


label sick_day:
    $day = day + 1
    $max_amount = max(A,B,C)
    if max_amount == B:
        jump anna_sickday
    elif max_amount == C:
        jump erin_sickday 
    else:
        jump maddie_sickday 
    return 