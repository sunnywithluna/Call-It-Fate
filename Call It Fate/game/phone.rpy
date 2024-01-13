
label actA_sceneText:
    "What should I say?"

    menu:
        "How are you?" if not small_a_sent:
            jump text_small_a
        "Do you want to go on a date?" if not eventADateFlag and not date_a_sent and eventAHangFlag and eventAHangCompletedFlag:
            jump text_go_out_a
        "Let's hang out soon" if not eventAHangFlag and not hang_b_sent:
            jump text_buddy_a
        "Look at this cool video" if not video_a_sent:
            jump text_video_a
        "Goodnight" if not gn_a_sent:
            jump text_night_a
        "Put phone away":
            jump end_of_act_menu1


label text_go_out_a:
    $ date_a_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else: 
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if A >= A_mid2:
            $ date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Sure! Sounds fun. Does this weekend work for you?\'"
            "As if I ever have plans."
            n "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventADateFlag = True
            jump actA_sceneText
        else:
            "After about thirty minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'I had a feeling this might happen. Listen, Sam, you're nice, but I'm not interested in you like that. Friends?\'"
            jump actA_sceneText


label text_buddy_a:
    $ hang_a_sent = True
    "I send a text that reads, \'Hey, Maddie! I was thinking of hitting the gym tomorrow. You down?\'"
    if A >= A_mid:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\'Totally! See you then!\'"
        $ eventAHangFlag = True
        jump actA_sceneText
    else:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\'Tomorrow's actually a rest day for me.\'"
        jump actA_sceneText
        

label text_video_a:
    $ video_a_sent = True
    "Which video should I send?"

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            $ B = B + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Whoa! I wonder how many tries it takes to make those trickshots.\'"
            jump actA_sceneText
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
            jump actA_sceneText
        "Test animation that features characters from a recently released, popular kid's film":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
            jump actA_sceneText
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
            jump actA_sceneText
    return


label text_small_a:
    $ small_a_sent = True
    "I send a message asking about her night."
    "After a few minutes, she replies and we text for a short while."
    if A >= A_low:
        $ B = B + 1
        "She seemed happy to hear from me."
        jump actA_sceneText
    else:
        "She seemed to be in a bad mood."
        jump actA_sceneText   


label text_small_b:
    $ small_b_sent = True
    "I ask Anna about her day."

    if small_b_sent2 == False:
        $ small_b_sent2 = True
        if D >= B_low:
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            "We chat for a short while before I change the topic."
            jump actB_sceneText
        else:
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I'm kind of busy right now.\'"
            jump actB_sceneText   
    else:
        "We chat for a short while before I decide to change the topic."
        jump actB_sceneText


label text_small_c:
    $ small_c_sent = True
    "I ask Erin about her day."

    if small_c_sent2 == False:
        $ small_c_sent2 = True
        if C >= C_low:
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            "We chat for a short while before I change the topic."
            jump actC_sceneText
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'I'm kind of busy right now.\'"
            jump actC_sceneText 
    else:
        "We chat for a short while before I decide to change the topic."
        jump actC_sceneText


label text_night_a:
    $ gn_a_sent = True
    "I send a simple goodnight message."

    if gn_a_sent2 == False:
        $ gn_a_sent2 = True
        if A >= A_low:
            $ B = B + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'A goodnight text? If I didn't know any better, I'd think you like me. Lol, goodnight, Sam.\'"
            jump end_of_act_menu1
        else:
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Do you send all your friends goodnight texts?\'"
            jump end_of_act_menu1   
    else:
        a "\'Goodnight, Sam!\'"    
        jump end_of_act_menu1 


label actB_sceneText:
    "What should I say?"
    menu:
        "Do you want to go on a date?" if not eventBDateFlag and not date_b_sent:
            jump text_go_out_b
        "Let's hang out soon" if not eventBHangFlag and not hang_b_sent:
            jump text_buddy_b
        "Look at this cool video" if not video_b_sent:
            jump text_video_b
        "Goodnight" if not gn_b_sent:
            jump text_night_b
        "Put phone away":
            jump end_of_act_menu1
    return


label text_go_out_b:
    $ date_b_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if D >= 6:
            $ date_this_weekend = True
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I was hoping you'd ask. How's this weekend sound?\'"
            "As if I ever have plans."
            n "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventBDateFlag = True
            jump actB_sceneText
        else:
            "After waiting for some time, I realize Anna isn't going to respond. I guess she isn't interested."
            jump actB_sceneText
        return


label text_buddy_b:
    $ hang_b_sent = True
    "I send a text that reads, \'Hey, Anna! I'm planning to study in the library tomorrow if you want to join\'"
    if D >= 4:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\'Good thinking. I'll be there.\'"
        $ eventBHangFlag = True
        jump actB_sceneText
    else:
        "After waiting for some time, I realize Anna isn't going to respond. Maybe she's busy?"
        jump actB_sceneText
    return
        

label text_video_b:
    "Which video should I send?"
    $ video_b_sent = True

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
            $ B = B - 1
            jump actB_sceneText
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'Neat video.\'"
            $ A = A + 1
            jump actB_sceneText
        "Test animation that features characters from a recently released, popular kid's film":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
            jump actB_sceneText
        "A cute kitten grooms a bunny":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
            jump actB_sceneText
    return 


label text_night_b:
    $ gn_b_sent = True
    "I send a simple goodnight message."

    if gn_b_sent2 == False:
        $ gn_b_sent2 = True
        if D >= 5:
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I hope you had a good day, Sam. Sleep well.\'"
            jump end_of_act_menu1
        else:
            "After waiting for some time, I realize Anna isn't going to respond. Maybe she's already asleep."
            jump end_of_act_menu1        
    else:
        b "\'Goodnight\'"
        jump end_of_act_menu1        
    return


label text_roof_b:
    $ like_b_sent = True
    "I can't just tell her something like that over text. It should be in person."
    "So I write and send a message that reads:"
    n "\'Hey, there's something I want to talk with you about. Do you think we could meet up?\'"

    if D >= 100:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\'We can do that. Give me a time and place, and I'll be there.\'"
        "I type \'Meet me on top of the library, at sunset\' and hit send."
        $ eventcb_trigger = True
        jump confession
    else:
        "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
        b "\'Now's not a great time. Raincheck?\'"
        jump actB_sceneText


label actC_sceneText:
    "What should I say?"
    menu:
        "Do you want to go on a date?" if not eventCDateFlag and not date_c_sent:
            jump text_go_out_c
        "Let's hang out soon" if not eventCHangFlag and not hang_c_sent:
            jump text_buddy_c
        "Look at this cool video" if not video_c_sent:
            jump text_video_c
        "Goodnight" if not gn_c_sent:
            jump text_night_c
        "Put phone away":
            jump end_of_act_menu1
    return 


label text_go_out_c:
    $ date_c_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if C >= 6:
            $ date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Erin shows on the screen:"
            c "\'Hi, Sam! I'd love to go out! Are you free this weekend?\'"
            "As if I ever have plans."
            n "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventCDateFlag = True
            jump actC_sceneText
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, uh, I don't really feel like I know you that well. I wouldn't be comfortable. Sorry.\'"
            jump actC_sceneText
        return 
                

label text_buddy_c:
    $ hang_c_sent = True
    "I send a text that reads, \'Hey, Erin! I'm going to the art room tomorrow to draw. Do you want to join me? We could order pizza or something while we're there.\'"
    if C >= 4:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\'Yeah! I'm down! See you tomorrow. :)\'"
        $ eventCHangFlag = True
        jump actC_sceneText
    else:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\'I can't tomorrow, but I hope you have fun!\'"
        jump actC_sceneText
    return
                        

label text_video_c:
    $ video_c_sent = True
    "Which video should I send?"
    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
            jump actC_sceneText
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
            jump actC_sceneText
        "Test animation that features characters from a recently released, popular kid's film":
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'I love animation tests. They really show you how much hard work goes into a project.\'"
            jump actC_sceneText
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
            jump actC_sceneText
    return
            

label text_night_c:
    $ gn_c_sent = True
    "I send a simple goodnight message."
    
    if gn_c_sent2 == False:
        $ gn_c_sent2 = True
        if C >= 5:
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Goodnight!! :)\'"
            jump end_of_act_menu1
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Uh, goodnight?\'"
            jump end_of_act_menu1   
    else:
        c "\'Goodnight :)\'"
        jump end_of_act_menu1
    return

