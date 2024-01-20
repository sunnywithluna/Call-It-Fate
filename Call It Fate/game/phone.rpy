label a_number:
    $ renpy.show(custom_show("maddie", "N"), [])

    $ numberFlagA = True
    n "\'Hey, Maddie, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if A >= A_low:
        $ renpy.show(custom_show("maddie", "F"), [])        
        a "\'Or something?\'"
        n "\'I didn't mean--\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Haha, I'm just teasing. I think that's a great idea.\'"
        "We exchange phone numbers."
        $ phoneFlagA = True
    else:
        $ renpy.show(custom_show("maddie", "U"), [])        
        a "\'Or something?\'"
        n "\'I didn't mean--\'"
        $ renpy.show(custom_show("maddie", "A"), [])
        a "\'Listen, I know what you're trying to do. I'm not interested, okay?\'"
    jump talking_to_maddie
        

label b_number:
    $ numberFlagB = True
    n "\'Hey, Anna, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if B >= B_low:
        $ renpy.show(custom_show("anna", "H"), [])
        b "\'Good thinking.\'"
        "We exchange phone numbers."
        $ phoneFlagB = True
    else:
        $ renpy.show(custom_show("anna", "A"), [])
        b "\'I won't need help.\'"
    jump talking_to_anna


label c_number:
    $ numberFlagC = True
    n "\'Hey, Erin, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if C >= C_low:
        $ renpy.show(custom_show("erin", "N"), [])
        c "\'Yeah okay! I could probably use the help.\'"
        "We exchange phone numbers."
        $ phoneFlagC = True
    else:
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Oh, sorry. I don't really give my number out...\'"
    jump talking_to_erin


label actA_sceneText:
    "What should I say?"

    menu:
        "How are you?" if not smallTalkFlagA:
            jump actA_sceneText_smallTalk
        "Do you want to go on a date?" if not eventADateFlag and not dateSentFlagA and eventAHangFlag and eventAHangCompletedFlag:
            jump actA_sceneText_date
        "Let's hang out soon" if not eventAHangFlag and not hangSentFlagA:
            jump actA_sceneText_hang
        "Look at this cool video" if not videoSentA:
            jump actA_sceneText_video
        "Goodnight" if not gnSentA:
            jump actA_sceneText_gn
        "Put phone away":
            jump end_of_act_menu1


label actA_sceneText_date:
    $ dateSentFlagA = True
    if weekendDateFlag:
        "I already have a date this weekend. I shouldn't overbook myself."
    else: 
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if A >= A_mid2:
            $ weekendDateFlag = True
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Sure! Sounds fun. Does this weekend work for you?\'"
            "As if I ever have plans."
            "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventADateFlag = True
        else:
            "After about thirty minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'I had a feeling this might happen. Listen, Sam, you're nice, but I'm not interested in you like that. Friends?\'"
    jump actA_sceneText


label actA_sceneText_hang:
    $ hangSentFlagA = True
    "I send a text that reads, \'Hey, Maddie! I was thinking of hitting the gym tomorrow. You down?\'"
    if A >= A_mid:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\'Totally! See you then!\'"
        $ eventAHangFlag = True
    else:
        "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
        a "\'Tomorrow's actually a rest day for me.\'"
    jump actA_sceneText
        

label actA_sceneText_video:
    $ videoSentA = True
    "Which video should I send?"

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Whoa! I wonder how many tries it takes to make those trickshots.\'"
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
        "Test animation that features characters from a recently released, popular kid's film":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'What is this? Am I missing something?\'"
    jump actA_sceneText


label actA_sceneText_smallTalk:
    $ smallTalkFlagA = True
    "I send a message asking about her night."
    "After a few minutes, she replies and we text for a short while."
    if A >= A_low:
        $ A = A + 1
        "She seemed happy to hear from me."
    else:
        "She seemed to be in a bad mood."
    jump actA_sceneText   


label actB_sceneText_smallTalk:
    $ smallTalkFlagB = True
    "I ask Anna about her day."

    if smallTalkFlagB == False:
        $ smallTalkFlagB = True
        if B >= B_low:
            $ B = B + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            "We chat for a short while before I change the topic."
        else:
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I'm kind of busy right now.\'"
    else:
        "We chat for a short while before I decide to change the topic."
    jump actB_sceneText


label actC_sceneText_smallTalk:
    $ smallTalkFlagC = True
    "I ask Erin about her day."

    if smallTalkFlagC == False:
        $ smallTalkFlagC = True
        if C >= C_low:
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            "We chat for a short while before I change the topic."
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'I'm kind of busy right now.\'"
    else:
        "We chat for a short while before I decide to change the topic."
    jump actC_sceneText


label actA_sceneText_gn:
    $ gnSentA = True
    "I send a simple goodnight message."

    if gnSentA == False:
        $ gnSentA = True
        if A >= A_mid:
            $ A = A + 1
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'A goodnight text? If I didn't know any better, I'd think you like me. Lol, goodnight, Sam.\'"
        else:
            "After a few minutes, my phone chimes and a response from Maddie shows on the screen."
            a "\'Do you send all your friends goodnight texts?\'"
    else:
        a "\'Goodnight, Sam!\'"    
    jump end_of_act_menu1 


label actB_sceneText:
    "What should I say?"
    menu:
        "How are you?" if not smallTalkFlagB:
            jump actB_sceneText_smallTalk
        "Do you want to go on a date?" if not eventBDateFlag and not dateSentFlagB and eventBHangFlag and eventBHangCompletedFlag:
            jump actB_sceneText_date
        "Let's hang out soon" if not eventBHangFlag and not hangSentFlagB:
            jump actB_sceneText_hang
        "Look at this cool video" if not videoSentB:
            jump actB_sceneText_video
        "Goodnight" if not gnSentB:
            jump actB_sceneText_gn
        "Put phone away":
            jump end_of_act_menu1
    return


label actB_sceneText_date:
    $ dateSentFlagB = True
    if weekendDateFlag:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if B >= B_mid:
            $ weekendDateFlag = True
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I was hoping you'd ask. How's this weekend sound?\'"
            "As if I ever have plans."
            "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventBDateFlag = True
        else:
            "After waiting for some time, I realize Anna isn't going to respond. I guess she isn't interested."
    jump actB_sceneText


label actB_sceneText_hang:
    $ hangSentFlagB = True
    "I send a text that reads, \'Hey, Anna! I'm planning to study in the library tomorrow if you want to join.\'"
    if B >= B_low:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\'Good thinking. I'll be there.\'"
        $ eventBHangFlag = True
    else:
        "After waiting for some time, I realize Anna isn't going to respond. Maybe she's busy?"
    jump actB_sceneText
        

label actB_sceneText_video:
    "Which video should I send?"
    $ videoSentB = True

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
            $ B = B - 1
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'Neat video.\'"
            $ B = B + 1
        "Test animation that features characters from a recently released, popular kid's film":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
        "A cute kitten grooms a bunny":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I don't get it. Why'd you send this to me?\'"
    jump actB_sceneText


label actB_sceneText_gn:
    $ gnSentB = True
    "I send a simple goodnight message."

    if gnSentB == False:
        $ gnSentB = True
        if B >= B_mid:
            $ B = B + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\'I hope you had a good day, Sam. Sleep well.\'"
        else:
            "After waiting for some time, I realize Anna isn't going to respond. Maybe she's already asleep."
    else:
        b "\'Goodnight\'"
    jump end_of_act_menu1        


label actC_sceneText:
    "What should I say?"
    menu:
        "How are you?" if not smallTalkFlagC:
            jump actC_sceneText_smallTalk
        "Do you want to go on a date?" if not eventCDateFlag and not dateSentFlagC and eventCHangFlag and eventCHangCompletedFlag:
            jump actC_sceneText_date
        "Let's hang out soon" if not eventCHangFlag and not hangSentFlagC:
            jump actC_sceneText_hang
        "Look at this cool video" if not videoSentC:
            jump actC_sceneText_video
        "Goodnight" if not gnSentC:
            jump actC_sceneText_gn
        "Put phone away":
            jump end_of_act_menu1


label actC_sceneText_date:
    $ dateSentFlagC = True
    if weekendDateFlag:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \'Hey, I was wondering, do you want to go out sometime?\'"
        if C >= C_mid:
            $ weekendDateFlag = True
            "After a few minutes, my phone chimes and a response from Erin shows on the screen:"
            c "\'Hi, Sam! I'd love to go out! Are you free this weekend?\'"
            "As if I ever have plans."
            "\'This weekend sounds great,\' I reply, beaming, though I doubt she can tell over text."
            $ eventCDateFlag = True
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, uh, I don't really feel like I know you that well. I wouldn't be comfortable. Sorry.\'"
    jump actC_sceneText
                

label actC_sceneText_hang:
    $ hangSentFlagC = True
    "I send a text that reads, \'Hey, Erin! I'm going to the art room tomorrow to draw. Do you want to join me? We could order pizza or something while we're there.\'"
    if C >= C_mid:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\'Yeah! I'm down! See you tomorrow. :)\'"
        $ eventCHangFlag = True
    else:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\'I can't tomorrow, but I hope you have fun!\'"
    jump actC_sceneText
                        

label actC_sceneText_video:
    $ videoSentC = True
    "Which video should I send?"
    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
        "Test animation that features characters from a recently released, popular kid's film":
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'I love animation tests. They really show you how much hard work goes into a project.\'"
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Oh, did you send this to me by accident?\'"
    jump actC_sceneText
            

label actC_sceneText_gn:
    $ gnSentC = True
    "I send a simple goodnight message."
    
    if gnSentC == False:
        $ gnSentC = True
        if C >= C_mid:
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Goodnight!! :)\'"
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\'Uh, goodnight?\'"
    else:
        c "\'Goodnight :)\'"
    jump end_of_act_menu1