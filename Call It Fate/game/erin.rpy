
label eventCHang:
    scene erin_hang with dissolve
    $ eventCHangCompletedFlag = True
    $ eventCHangToday = True
    play music "audio/event.mp3" fadein 1.0

    "The next day, I head to the art room where Erin is waiting."
    c "\'Hi, Sam! I brought the pizza--\'"
    scene bg_art_a with dissolve
    $ renpy.show(custom_show("erin", "surprised"), [])

    c "\'Oh.\'"
    "I'm in the doorway with a pizza box in my hands, looking at Erin holding a cardboard box of her own."
    n "\'I guess we should have coordinated this better.\'"
    $ renpy.show(custom_show("erin", "A"), [])
    c "\'Oh well. I guess we'll just have to eat two whole pizzas.\'"
    n "\'Haha, or maybe just have leftovers?\'"
    "Erin feigns a dramatic sigh."
    $ renpy.show(custom_show("erin", "F"), [])

    c "\'I guess that's an option too.\'"
    $ renpy.hide(custom_hide("erin"))
    "We eat our pizza, barely making a dent in the two boxes, then, we start drawing."
    "It's oddly relaxing to work with Erin beside me."

    "When I draw alone, it's easy to get frustrated at little mistakes or feel like I'm not progressing fast enough, but her presence is so calming, and her focus is contagious--not once do I reach for my phone to distract myself."

    "Instead, I feel motivated."

    "I'm sketching a fake potted plant that's in the room, the smell of cheap cheese and crust still strong in the air, and when I look over at Erin's page, I see that it's completely covered in pizza illustrations."

    "At the top of the paper, she's written, 'Pizza Emotional Poses.'"
    n "\'Are you drawing pizza with different expressions?\'"
    $ renpy.show(custom_show("erin", "N"), []) 
    c "\'Oh, haha, yeah. I guess I got inspired.\'"
    "She holds up her sketchbook for me to see."
    "Oddly enough, it's easy to tell what emotion the delicious food is emitting in most of the mini sketches."
    $ renpy.show(custom_show("erin", "E"), [])
    c "\'What do you think?\'"
    "The drawings are..."
    menu:
        "Weird":
            $ renpy.show(custom_show("erin", "S"), [])
            n "\'A little strange maybe.\'"
        "Cool":
            $ C = C + 1
            $ renpy.show(custom_show("erin", "F"), [])
            n "\'Cool!\'"

    n "\'What's that one supposed to be?\'"
    "I point to a pizza that seems expressionless, just a normal slice."
    $ renpy.show(custom_show("erin", "A"), [])
    c "\'Despair.\'"
    n "\'Wow, so edgy.\'"
    $ renpy.hide(custom_hide("erin"))
    "We soon move on to drawing other food items with various emotions, and I only get stuck once when trying to decide how a hamburger might look when in love."
    jump event_calculation_a


label eventCDate:
    $ eventCDateCompletedFlag = True
    $ date_this_weekend = False
    $ eventCDateToday = True
    
    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Erin."
    c "\'So, where are we gonna go today?\'"
    menu: 
        "Hiking trail":
            "In response, I write, \'I was thinking we could go on a hike. Is that okay?\'"
            a "\'Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\'"
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
        "Interactive science museum":
            "In response, I write, \'I was thinking we could check out the science museum. Is that okay?\'"
            a "\'Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\'"
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
        "Art gallery":
            $ C = C + 1
            "In response, I write, \'I was thinking we could go to this art gallery. Is that okay?\'"
            c "\'Oo, that sounds really cool! Text me the address so I know where to meet you. :)\'"
        "Ramen shop":
            "In response, I write, \'I was thinking we could grab some ramen. Is that okay?\'"
            a "\'Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\'"
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
    scene eventCDateCompletedFlag with dissolve
    "When I arrive, I find Erin already inside, staring at a painting."
    "I walk towards the colors of yellow, green, and blue on the canvas, my footsteps loud against the concrete floors, until I'm standing beside her."
    scene bg_art_gallery with dissolve
    $ renpy.show(custom_show("erin", "N"), [])
    c "\'Hi, Sam.\'"
    "I see now that the painting depicts a sunflower field with all flowers but one facing the sun."
    scene sunflowers with dissolve
    c "\'What do you think of it?\'"

    menu:
        "I think it's about paving your own path":
            n "\'I think it's about finding your own way, even if everyone else doesn't get it.\'"
            $ renpy.show(custom_show("erin", "F"), [trueleft])
            c "\'That's nice. I like that.\'"
        "I think it's about how it's better to follow what others are doing":
            n "\'I think it's showing why it's important to pay attention to what others are doing and follow their example.\'"
            $ renpy.show(custom_show("erin", "S"), [trueleft])
            c "\'Hm, you really think so?\'"
            n "\'Yeah, I mean, that sunflower isn't going to grow very well if it's not facing the sun. It needs to turn around.\'"          
            $ renpy.show(custom_show("erin", "U"), [trueleft])
            c "\'That's an interesting interpretation.\'"
        "That sunflower isn't going to grow very well":
            n "\'That's one dumb sunflower. Can't even find the sun.\'"
            $ renpy.show(custom_show("erin", "S"), [trueleft])
            c "\'Maybe it doesn't want to face the sun.\'"

    $ renpy.show(custom_show("erin", "N"), [trueleft])

    c "\'Come on, let's look at some others.\'"
    scene bg_art_gallery with dissolve

    $ renpy.hide(custom_hide("erin"))

    "We move throughout the art gallery, admiring the different paintings displayed on the white walls and pondering on what the artists might've been trying to say with every brush stroke."

    "It's easy to listen to Erin as she talks about art."

    "She speaks with passion and considers every word carefully."

    "Even the way she approaches each painting is intriguing, like she's truly trying to understand the artist through their work. Like she's getting to know a friend."

    $ renpy.show(custom_show("erin", "surprised"), [])

    "Suddenly, Erin's phone rings, and everyone in the gallery turns to see who's guilty of causing the disturbance."

    "Her eyes grow wide as she checks the screen."

    c "\'I'm sorry, I have to take this.\'"

    $ renpy.hide(custom_hide("erin"))

    "She walks off and out of the room, leaving me the sole victim of glares and headshakes from the art snobs."

    "I continue to move from painting to painting, but it's significantly less fun without Erin. Luckily, it isn't too long before she returns."

    $ renpy.show(custom_show("erin", "E"), [])

    c "You'll never guess who that was."

    n "\'Why? Was it...\'"
    menu:
        "Your mom?":
            n "\'...your mom or something?\'"
            if special_C_on:
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'Remember that internship I told you about? Well, I got it! I can't believe it!\'"
            else:
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'I applied for an internship at this local game company, and that was them. I got it! I can't believe it!\'"
        "Your doctor?":
            n "\'...your doctor or something?\'"
            if special_C_on:
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'Remember that internship I told you about? Well, I got it! I can't believe it!\'"
            else:
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'I applied for an internship at this local game company, and that was them. I got it! I can't believe it!\'"
        "The game company?" if special_C_on:
            $ C = C + 1
            $ renpy.show(custom_show("erin", "F"), [])
            n "\'...the internship?\'"
            c "\'Yes!! Sam, I got it! I can't believe it!\'"

    n "\'Oh! Wow! Congratulations!\'"

    if believe_in_her:
        $ renpy.show(custom_show("erin", "F"), [])
        c "\'Thanks for believing in me, Sam.\'"

    $ renpy.show(custom_show("erin", "U"), [])
    c "\'...I didn't realize it until now, but I think waiting to hear back about the whole thing was really starting to wear on me. I try not to care what people think...But...\'"
    $ renpy.show(custom_show("erin", "S"), [])

    c "\'It was really important to me that they liked my art. I guess I've been wondering if I really have what it takes to do game art professionally and landing this internship is so reassuring.\'"
    $ renpy.show(custom_show("erin", "F"), [])
    c "\'It makes me feel like I'm not crazy for picking this as a career path.\'"

    n "\'Choosing art as your career isn't crazy. What would be crazy is being as good as you are and not choosing it.\'"

    "She looks up at me with warmth, and I take her hand."
    $ renpy.hide(custom_hide("erin"))

    "We stop in front of each painting as we make our way through the gallery, but I'm no longer paying much attention to the art. All my focus is on Erin, her comforting presence and bright disposition."

    "Despite my best efforts to walk slowly, we eventually find ourselves at the end of the exhibition room and back outside."

    "I walk Erin to her car."

    scene bg_after_date with dissolve
    
    $ renpy.show(custom_show("erin", "F"), [])
    c "\'Thanks for inviting me out today, Sam.\'"
    n "\'Of course. I'm glad you could make it.\'"
    "As I'm looking at her, I realize it's time to part ways."
    n "\'How should I say goodbye?\'"

    menu:
        "Kiss her":
            if C >= 9:
                scene black with dissolve

                "I lean in."
                "And our lips meet."
                c "\'So, I'll see you in class?\'"
                n "\'Yeah, I'll see you then.\'"
                scene event_kiss_c with dissolve
                "She gets in her car and drives away."
                "And I can't wait until Tuesday when I get to see her again."
                jump event_calculation_a

            else:
                scene black with dissolve
                $ C = C - 2
                "I lean in."
                scene bg_after_date with dissolve

                $ renpy.show(custom_show("erin", "U"), [])
                c "\'Uh, well, I gotta go.\'"
                "She's leaning away, and I feel a wave of embarrassment wash over me."
                c "\'Thanks again.\'"
                $ renpy.hide(custom_hide("erin"))
                "Erin gets in her car and drives away. And I'm left wondering what I did wrong."
                jump event_calculation_a
        "Hug her":
            $ renpy.show(custom_show("erin", "F"), [])
            $ C = C + 1
            "I give her a hug goodbye, and she holds me tightly."
            c "\'This was a great day.\'"
            $ renpy.hide(custom_hide("erin"))
            "She gets in her car and drives away."
            "And I can't wait until Tuesday when I get to see her again."
            jump event_calculation_a
        "Give her a high five":
            if C >= 9:
                $ C = C - 1
                $ renpy.show(custom_show("erin", "U"), [])
                "She cocks her head and slowly raises her hand to meet mine."
                c "\'Uh, okay. See you then I guess.\'"
                $ renpy.hide(custom_hide("erin"))
                "Erin gets in her car and drives away."
                "And I'm wondering if there was a better way I could've done that."
                jump event_calculation_a

            else:
                $ C = C + 1
                "I hold up my hand to give her a high five."
                n "\'See you Tuesday.\'"
                "Her hand bounces off mine."
                c "\'See ya!\'"
                $ renpy.hide(custom_hide("erin"))
                "She gets in her car and drives away."
                "And I can't wait until I get to see her again."
                jump event_calculation_a
    return
    

label actC_scene3:
    scene event_dorm_c with dissolve
    play music "audio/event.mp3" fadein 1.0

    "I open my door to find Erin standing outside my room."
    c "\'Hi, Sam. How're you feeling? I heard you were sick.\'"
    n "\'Eh, I'm okay, could always be worse though.\'"
    c "\'That's the spirit. I'm here because Dr. Paige asked me to drop off some handouts. So you don't get behind.\'"
    "I see a few papers in her hand."
    scene bg_room_outside_b with dissolve
    $ renpy.show(custom_show("erin", "H"), [])

    n "\'Oh, thanks. Do you want to come in?\'"
    c "\'Sure!\'"
    "I move to the side, and she walks into my dorm, handing me the papers as she looks around the room."
    scene bg_room_b with dissolve

    if clean:
        $ renpy.show(custom_show("erin", "F"), [])
        c "\'Whoa, your room is so clean!\'"
        n "\'Well, you know. I don't like clutter.\'"
        "While her back is turned, I kick a stray piece of trash under my bed."
        "She goes over to my desk and examines my PC, from my keyboard and mouse to my headset and dual monitors."
        $ renpy.show(custom_show("erin", "H"), [])
        c "\'Nice setup!\'"

    else:
        $ renpy.show(custom_show("erin", "U"), [])
        n "\'Sorry for the mess. I've been meaning to clean.\'"
        c "\'Eh, that's alright. You're sick, you get to be a little messy today.\'"
        "Despite what she says, I can tell by her expression that she's at least a little grossed out by the state of my room."

    "I watch her eyes move across my shelves over every trinket on display."

    $ renpy.show(custom_show("erin", "N"), [])

    c "\'You have quite the merch collection.\'"

    n "\'Yeah, most of them are from conventions. That's where you get the best deals.\'"
    $ renpy.show(custom_show("erin", "surprised"), [])

    c "\'Really? I didn't know that. I've never been.\'"

    n "\'Well, maybe I can take you sometime.\'"

    if special_C:
        $ renpy.show(custom_show("erin", "F"), [])
        "She smiles at me."
    else:
        $ renpy.show(custom_show("erin", "U"), [])
        "We stand there for a moment in awkward silence."

    if C >= 16:
        $ erin_confessed = True
        stop music fadeout 1.0

        $ renpy.show(custom_show("erin", "E"), [])
        c "\'Sam? Can I tell you something?\'"
        n "\'Sure. What's up?\'"
        "She pauses as she thinks."
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Uh, well, I don't know how to say this, but...I think I like you. I'm sorry, did I make things weird?\'"

        menu:
            "I like you too": 
                n "\'Erin, I--\'"
                "We stand there in a moment of content silence before I start getting dizzy."
                $ renpy.show(custom_show("erin", "S"), [])
                c "\'Sam!\'"
                "Erin grabs me as I almost fall to the ground."
                "I know I need to respond to her confession, but my head hurts so much..."
                n "\'Let's go out this weekend. I should be feeling better by then.\'"
                $ renpy.show(custom_show("erin", "F"), [])
                c "\'Yeah! That'd be fun.\'"
                $ renpy.show(custom_show("erin", "A"), [])
                c "\'Oh but...I should let you rest then! Or you won't heal in time for our date.\'"
                $ renpy.hide(custom_hide("erin"))
                scene event_sick_c with dissolve
                "While leaving my room, she hesitates by the doorway."
                c "\'I'm glad we talked, Sam. Rest up, okay?\'"
                scene bg_room_b with dissolve
                "Erin closes the door behind her, and I'm left standing in the middle of my dorm, wishing my headache away so I could go after her and ask her to stay a little longer."
                "But spending time with Erin would have to wait."
                "The second I lie down in my bed, I'm already drifting back to sleep."
                "I dream of a life with Erin. And though I know realistically it's probably caused by the fever, I can't help but think it means something."
                "That these past two weeks are just the beginning."

            "I don't think of you like that":
                n "\'Erin, I--\'"
                "A wave of dizziness overwhelms me."
                $ renpy.show(custom_show("erin", "S"), [])
                c "\'Sam!\'"
                "Erin grabs me as I almost fall to the ground."
                "I know I need to respond to her confession, but my head hurts so much..."
                $ renpy.hide(custom_hide("erin"))
                scene event_sick_c with dissolve
                "While leaving my room, she hesitates by the doorway."
                c "\'I'll head out...let's talk later okay?\'"
                scene bg_room_b with dissolve
                "She heads out, closing the door behind her before I have a chance to say anything else."
                $ renpy.hide(custom_hide("erin"))
                n "\'Erin...\'"
    else: 
        $ renpy.show(custom_show("erin", "S"), [])
        c "\'Is it alright if I head out? I know I just got here, but I have some stuff I should probably take care of.\'"
        n "\'Are you sure?\'"
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Yeah, I think it's for the best. Plus, you're not feeling well.\'"
        $ renpy.hide(custom_hide("erin"))
        n "\'Alright. Talk to you later then.\'"
        c "\'Bye, Sam.\'"
        "Erin leaves, closing the door behind her, and I'm left standing in the middle of my dorm, alone."
        "I go to sleep with my fever induced headache and dream up a life with Neko-Chan...a perfect life."
    stop music fadeout 1.0
    scene black with fade
    jump event_calculation_a


label event_roof_c:
    scene bg_roof with dissolve
    play music "audio/rooftop.mp3" fadein 1.0

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    $ renpy.show(custom_show("erin", "N"), [])
    "Erin sits cross legged as she stares up at the sky, the clouds drifting above. Her apparent contentment makes me wonder what she's thinking about.."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    
    n "\'Hey.\'"
    c "\'Hi, Sam.\'"
    "She glances down at the gift in my hand."

    if erin_gift:
        $ C = C + 1
        scene event_gift_c with dissolve
        $ renpy.show(custom_show("erin", "F"), [])
        "Her eyebrows shoot up in excitement."
        c "\'Hey! Sunflowers!\'"
        n "\'I brought them for you.\'"
        if eventCDateFlag:
            n "\'They made me think of that painting we saw.\'"
        "When I hand her the bouquet, she closes her eyes and brings the flowers to her nose."
        c "\'Thanks, Sam. This made my day.\'"
        scene bg_roof with dissolve
    else:
        $ C = C - 1
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Whatcha got there?\'"
        n "\'It's for you.\'"
        "As I hand Erin her present, she looks a little confused."
        c "\'Uh, cool. Thanks.\'"

    $ renpy.show(custom_show("erin", "N"), [])
    "We watch the sun slowly fall."
    c "\'It's a great view, huh?\'"
    n "\'Yeah...\'"
    $ renpy.show(custom_show("erin", "A"), [])
    c "\'No matter how many times I come up here, I never get tired of it...I want to find more things like that.\'"
    n "\'Things you won't get tired of?\'"
    $ renpy.show(custom_show("erin", "F"), [])
    c "\'Things that are always just as fun, exciting, and beautiful as the first time I experience them.\'"
    n "\'I'm not sure that's possible.\'"
    $ renpy.show(custom_show("erin", "N"), [])
    c "\'Maybe for some people. It takes effort to notice beautiful things--not everyone pauses long enough to watch sunsets.\'"
    $ renpy.show(custom_show("erin", "H"), [])
    c "\'Anyway, you wanted to talk about something?\'"

    menu:
        "Confess my feelings":
            if erin_confessed:
                jump endingC11
            if C == 20:
                jump endingC10
            elif C >= 16:
                jump endingC01
            else:
                jump endingC00
        "I've changed my mind":
            jump neko_ending
    return
