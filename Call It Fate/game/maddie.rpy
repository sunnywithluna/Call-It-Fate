label maddie_hangout:
    $maddie_hangout = True
    scene maddie_hang with dissolve 
    play music "audio/event.mp3" fadein 1.0

    "The next day, I head to the school gym where Maddie is waiting, tying her hair into the usual ponytail."
    scene bg_gym with dissolve

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
            "I stand up and extend my hand to her."
            n "\"Of course.\""
            show maddie_2 flirty
            "She takes my hand, and I pull her up."
        "I don't forgive you.":
            n "\"I...don't know if I can yet.\""
            show maddie_2 uncomf
            a "\"You need time. I get it.\""
            "She stands up and extends her hand to me."
            show maddie_2 normal
            a "\"Until then, I'll try to prove that I mean it.\""
            "I take her hand, and she pulls me up."
    stop music fadeout 1.0
    scene black with fade
    jump quick_calculations
    return 

label maddie_date:
    $maddie_date = True
    $date_this_weekend = False
    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Maddie."
    a "\"Hey, Sam! Where were you thinking of going for our date?\""
    menu: 
        "Hiking trail":
            $A = A + 1
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
    scene maddie_date with dissolve

    "When I arrive, I find Maddie taking pictures of succulents planted at the entrance of the trail. It's a nice shaded area, full of greenery that dampens the sound of traffic in the distance."

    n "\"Hey!\""
    "Maddie turns to face me."
    scene bg_gymdate with dissolve

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
            $A = A + 2
            n "\"Let's do Death Row Ridge.\""
            show maddie_5 happy
            a "\"Alright, a challenge! This should be fun.\""
            "We start down the path, and within minutes, I'm already certain I'll be sore the next day."

        "Fluffy Bunny Hilltop":
            $A = A - 1
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
    hide jennifer
    show jennifer2 at trueright

    "Jennifer" "\"Oh, are you guys here...together?\""
    show maddie_5 normal
    a "\"Uh, yup. We're kind of on a date right now.\""

    "I try not to get offended as Jennifer's face scrunches up in disgust."
    hide jennifer2

    show jennifer at trueright

    "Jennifer" "\"Really, Maddie? Him?\""
    show maddie_5 angry at trueleft

    n "\"Ouch, okay, I'm right here.\""

    a "\"That's pretty rude, Jen.\""
    hide jennifer

    show jennifer2 at trueright

    "Jennifer" "\"What? I'm just surprised.\""
    show maddie_5 normal at trueleft

    a "\"You know what? I don't need your approval. Come on, Sam.\""
    hide jennifer2 with dissolve
    hide maddie_5 with dissolve
    scene black with fade
    "I feel Maddie's hand slip into mine as we push past Jennifer."
    scene bg_gymdate with dissolve

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
            $A = A + 1
            n "\"You didn't want to seem weak.\""
            show maddie_5 normal
            a "\"Yeah...\""

        "You wanted to belong":
            n "\"You wanted to fit in.\""
            show maddie_5 angry
            a "\"No, I just didn't want to seem weak.\""

        "You enjoyed hurting others":
            $A = A - 1
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

    scene bg_night with dissolve

    show maddie_5 flirty
    a "\"I had a lot of fun today, Sam.\""
    n "\"Yeah, me too. We should do it again sometime.\""
    "As I'm looking at her, I realize it's time to part ways."
    "How should I say goodbye?"

    menu:
        "Kiss her":
            if A >= A_mid3:
                scene black with dissolve

                $A = A + 1
                "I lean in."
                "And our lips meet."
                scene maddie_kiss with dissolve

                a "\"Bye, Sam.\""
                "She gets in her car and drives away."
                "And I can't wait until Tuesday when I get to see her again."
                jump quick_calculations
            else: 
                scene black with dissolve
                $A = A - 1
                "I lean in."
                scene bg_night with dissolve

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
        "Hug her":
            "I lean in for a hug."

            if A >= A_mid3:
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
        "Give her a high five":
            $A = A - 1
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

label maddie_sickday:
    scene maddie_dorm with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I open my door to find Maddie standing outside my room."
    scene bg_outside_dorm with dissolve

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
    scene bg_room with dissolve

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

    if A >= A_high2:
        $maddie_confessed = True
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
            "I like you too": 
                show maddie_2 normal
                n "\"Maddie, I--\""
                "A wave of dizziness overwhelms me."
                show maddie_2 sad
                a "\"Sam!\""
                "Maddie grabs me as I almost fall to the ground."
                a "\"I'm sorry. I should go so you can rest.\""
                scene maddie_dorm2 with dissolve
                "While leaving my room, she hesitates by the doorway."
                a "\"Call me later, okay? When you're feeling better.\""
                scene bg_room with dissolve
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
                scene maddie_dorm2 with dissolve
                "While leaving my room, she hesitates by the doorway."
                a "\"Call me later, okay? When you're feeling better.\""
                scene bg_room with dissolve
                "She rushes out, closing the door behind her before I have a chance to say anything else."
    else: 
        show maddie_2 uncomf
        a "\"I should probably go.\""
        n "\"Are you sure?\""
        a "\"Yeah, you need to rest. We'll see each other on Thursday, if you're not still sick.\""
        n "\"Alright. Talk to you later then.\""
        hide maddie_2 with dissolve
        "Maddie leaves, closing the door behind her, and I'm left standing in the middle of my dorm, alone."
        "I go to sleep with my fever induced headache and dream up a life with Neko-Chan...a perfect life."
    
    stop music fadeout 1.0
    scene black with fade
    jump ch3_schoolday2
    return

label maddie_roof: 
    scene bg_roof with dissolve
    play music "audio/rooftop.mp3" fadein 1.0

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    scene maddie_roof with dissolve
    "Maddie is standing with her hands on her hips, staring out into the horizon, steady as always."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    
    n "\"Hey.\""
    a "\"Hey, Sam.\""

    "She glances down at the gift in my hand."
    if maddie_gift:
        scene maddie_hoya with dissolve
        $A = A + 1
        a "\"A hoya kerrii plant! Is that for me?\""
        n "\"Yeah! Do you like it?\""
        if eventba_trigger:
            n "\"It reminded me of the ones from our hike.\""
        "She takes the potted plant from me, looking at it with admiration."
        a "\"I love it, Sam. Thank you.\""
        scene bg_roof with dissolve
    else:
        $A = A - 1
        n "\"Oh, this is for you.\""
        scene bg_roof with dissolve
        show maddie_1 uncomf
        "I hold out her present, and she takes it slowly, looking a little confused."
        a "\"Oh. Thanks.\""
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
                jump maddie_confessedending
            if A >= A_high3:
                jump maddie_perfectending
            elif A >= A_high:
                jump maddie_goodending
            else:
                jump maddie_badending
        "I've changed my mind":
            jump neko_ending
    return
