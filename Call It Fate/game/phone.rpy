label send_text_a:
    "What should I say?"

    menu:
        "Make small talk about her day" if not small_a_sent:
            jump text_small_a
        "Do you want to go on a date?" if not eventba_trigger and not date_a_sent and eventaa_trigger and maddie_hangout:
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
    $date_a_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else: 
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if A >= A_mid2:
            $date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"Sure! Sounds fun. Does this weekend work for you?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $eventba_trigger = True
            jump send_text_a
        else:
            "After about thirty minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"I had a feeling this might happen. Listen, Sam, you're nice, but I'm not interested in you like that. Friends?\""
            jump send_text_a

label text_buddy_a:
    $hang_a_sent = True
    "I send a text that reads, \"Hey, Maddie! I was thinking of hitting the gym tomorrow. You down?\""
    if A >= A_mid:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Totally! See you then!\""
        $eventaa_trigger = True
        jump send_text_a
    else:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\"Tomorrow's actually a rest day for me.\""
        jump send_text_a
        
label text_video_a:
    $video_a_sent = True
    "Which video should I send?"

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            $A = A + 1
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
    $small_a_sent = True
    "I ask Maddie about her day."

    if small_a_sent2 == False:
        $small_a_sent2 = True
        if A >= A_low:
            $A = A + 1
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

label text_small_b:
    $small_b_sent = True
    "I ask Anna about her day."

    if small_b_sent2 == False:
        $small_b_sent2 = True
        if B >= B_low:
            $B = B + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            "We chat for a short while before I change the topic."
            jump send_text_b
        else:
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I'm kind of busy right now.\""
            jump send_text_b   
    else:
        "We chat for a short while before I decide to change the topic."
        jump send_text_b

label text_small_c:
    $small_c_sent = True
    "I ask Erin about her day."

    if small_c_sent2 == False:
        $small_c_sent2 = True
        if C >= C_low:
            $C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            "We chat for a short while before I change the topic."
            jump send_text_c
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"I'm kind of busy right now.\""
            jump send_text_c 
    else:
        "We chat for a short while before I decide to change the topic."
        jump send_text_c

label text_night_a:
    $gn_a_sent = True
    "I send a simple goodnight message."

    if gn_a_sent2 == False:
        $gn_a_sent2 = True
        if A >= A_low:
            $A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"A goodnight text? If I didn't know any better, I'd think you like me. Lol, goodnight, Sam.\""
            jump end_of_day_menu
        else:
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\"Do you send all your friends goodnight texts?\""
            jump end_of_day_menu   
    else:
        a "\"Goodnight, Sam!\""    
        jump end_of_day_menu 

label send_text_b:
    "What should I say?"
    menu:
        "Do you want to go on a date?" if not eventbb_trigger and not date_b_sent:
            jump text_go_out_b
        "Let's hang out soon" if not eventab_trigger and not hang_b_sent:
            jump text_buddy_b
        "Look at this cool video" if not video_b_sent:
            jump text_video_b
        "Goodnight" if not gn_b_sent:
            jump text_night_b
        "Put phone away":
            jump end_of_day_menu
    return

label text_go_out_b:
    $date_b_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if B >= 6:
            $date_this_weekend = True
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I was hoping you'd ask. How's this weekend sound?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $eventbb_trigger = True
            jump send_text_b
        else:
            "After waiting for some time, I realize Anna isn't going to respond. I guess she isn't interested."
            jump send_text_b
        return

label text_buddy_b:
    $hang_b_sent = True
    "I send a text that reads, \"Hey, Anna! I'm planning to study in the library tomorrow if you want to join\""
    if B >= 4:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"Good thinking. I'll be there.\""
        $eventab_trigger = True
        jump send_text_b
    else:
        "After waiting for some time, I realize Anna isn't going to respond. Maybe she's busy?"
        jump send_text_b
    return
        
label text_video_b:
    "Which video should I send?"
    $video_b_sent = True

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I don't get it. Why'd you send this to me?\""
            $B = B - 1
            jump send_text_b
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"Neat video.\""
            $B = B + 1
            jump send_text_b
        "Test animation that features characters from a recently released, popular kid's film":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I don't get it. Why'd you send this to me?\""
            jump send_text_b
        "A cute kitten grooms a bunny":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I don't get it. Why'd you send this to me?\""
            jump send_text_b
    return 

label text_night_b:
    $gn_b_sent = True
    "I send a simple goodnight message."

    if gn_b_sent2 == False:
        $gn_b_sent2 = True
        if B >= 5:
            $B = B + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I hope you had a good day, Sam. Sleep well.\""
            jump end_of_day_menu
        else:
            "After waiting for some time, I realize Anna isn't going to respond. Maybe she's already asleep."
            jump end_of_day_menu        
    else:
        b "\"Goodnight\""
        jump end_of_day_menu        
    return

label text_roof_b:
    $like_b_sent = True
    "I can't just tell her something like that over text. It should be in person."
    "So I write and send a message that reads:"
    n "\"Hey, there's something I want to talk with you about. Do you think we could meet up?\""

    if B >= 100:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"We can do that. Give me a time and place, and I'll be there.\""
        "I type \"Meet me on top of the library, at sunset\" and hit send."
        $eventcb_trigger = True
        jump confession
    else:
        "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"Now's not a great time. Raincheck?\""
        jump send_text_b

label send_text_c:
    "What should I say?"
    menu:
        "Do you want to go on a date?" if not eventbc_trigger and not date_c_sent:
            jump text_go_out_c
        "Let's hang out soon" if not eventac_trigger and not hang_c_sent:
            jump text_buddy_c
        "Look at this cool video" if not video_c_sent:
            jump text_video_c
        "Goodnight" if not gn_c_sent:
            jump text_night_c
        "Put phone away":
            jump end_of_day_menu
    return 

label text_go_out_c:
    $date_c_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if C >= 6:
            $date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Erin shows on the screen:"
            c "\"Hi, Sam! I'd love to go out! Are you free this weekend?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $eventbc_trigger = True
            jump send_text_c
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, uh, I don't really feel like I know you that well. I wouldn't be comfortable. Sorry.\""
            jump send_text_c
        return 
                
label text_buddy_c:
    $hang_c_sent = True
    "I send a text that reads, \"Hey, Erin! I'm going to the art room tomorrow to draw. Do you want to join me? We could order pizza or something while we're there.\""
    if C >= 4:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\"Yeah! I'm down! See you tomorrow. :)\""
        $eventac_trigger = True
        jump send_text_c
    else:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\"I can't tomorrow, but I hope you have fun!\""
        jump send_text_c
    return
                        
label text_video_c:
    $video_c_sent = True
    "Which video should I send?"
    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, did you send this to me by accident?\""
            jump send_text_c
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, did you send this to me by accident?\""
            jump send_text_c
        "Test animation that features characters from a recently released, popular kid's film":
            $C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"I love animation tests. They really show you how much hard work goes into a project.\""
            jump send_text_c
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, did you send this to me by accident?\""
            jump send_text_c
    return
            
label text_night_c:
    $gn_c_sent = True
    "I send a simple goodnight message."
    
    if gn_c_sent2 == False:
        $gn_c_sent2 = True
        if C >= 5:
            $C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Goodnight!! :)\""
            jump end_of_day_menu
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Uh, goodnight?\""
            jump end_of_day_menu   
    else:
        c "\"Goodnight :)\""
        jump end_of_day_menu
    return

