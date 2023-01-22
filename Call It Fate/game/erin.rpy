label c_number:
    $ c_number_flag = True
    n "\"Hey, Erin, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if C >= 1:
        $ renpy.show(custom_show("erin", "normal"), [])
        c "\"Yeah okay! I could probably use the help.\""
        "We exchange phone numbers."
        $ c_number_obtained_flag = 1
        jump talking_to_erin
    else:
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Oh, sorry. I don't really give my number out...\""
        jump talking_to_erin
    return 

label art:
    scene bg_art with fade
    play music "audio/free.mp3"
    $ art_compliment = False
    if art_counter == 1:
        "I peek in through the door window at the nearly empty studio, easels abandoned and scattered throughout the space, the adjacent prop room closed off."

        "The only person inside is Erin, who sits near the front, drawing on a tablet."

        "When I walk in, she turns to see who opened the door."
        $ renpy.show(custom_show("erin", "normal"), [])
        n "\"Oh, um, is it alright if I work here too?\""
        $ renpy.show(custom_show("erin", "happy"), [])

        c "\"Go for it! I don't mind the company.\""

        n "\"Awesome. I thought it might be easier to practice away from my dorm--too many distractions there.\""
        $ renpy.show(custom_show("erin", "flirty"), [])

        c "\"I'll try not to disturb you then.\""
        $ renpy.hide(custom_hide("erin"))

        "She smiles and turns back to her tablet, an illustration of a griffin on the screen, which I immediately recognize from the student gallery where an earlier version of the painting sits on display."

        "I'm a little surprised."

        "Usually, the most skilled art students tend to carry themselves with a sort of withdrawn self-importance."
        "But Erin seems so affable and easygoing."
        "It's refreshing."
    elif art_counter == 2:
        $ renpy.show(custom_show("erin", "normal"), [])
        "As I enter the room, Erin looks back and waves."
        $ renpy.hide(custom_hide("erin"))
        "It's nice being here in the summer."
        "During the school year, I never felt quite comfortable working in the art room, always paranoid that students and professors were silently judging my sketches."
        "But the place doesn't seem so intimidating now."
    elif art_counter == 3:
        "I stare at the blank page in front of me, wondering what I should draw, tapping my pencil against the edge of my sketchbook."
        "The cursor blinks in an open browser on my laptop, waiting for me to search for reference photos once I decide on a subject."
        $ renpy.show(custom_show("erin", "normal"), [])
        "Then, I look up and see Erin drawing on her tablet. And I start sketching."
        $ renpy.hide(custom_hide("erin"))
        "The illustration that forms on my page isn't half bad. I might even ink this one."
        $ renpy.show(custom_show("erin", "happy"), [])
        c "\"I'm going to the vending machine. Do you want anything?\""
        "Erin is standing above me, and I instinctively cover my sketchbook. I'd been so focused on cleaning my lines, I didn't catch her getting up."
        $ renpy.show(custom_show("erin", "normal"), []) 
        c "\"Whatcha drawing?\""
        "I feel my face flush as I move my hand from the page."
        n "\"I needed to practice people. I--\""
        $ renpy.show(custom_show("erin", "embarrassed"), [])
        c "\"Hey, that's me!\""
        "She examines the drawing with squinted eyes."
        $ renpy.show(custom_show("erin", "angry"), [])
        c "\"It's not a bad start. Maybe try breaking the subject up into smaller shapes next time.\""
        "\"Don't try to draw a person, just draw the shapes that make up the person, does that make sense?\""
        n "\"Yeah...I think so.\""
        $ renpy.show(custom_show("erin", "happy"), [])
        c "\"Great! So, vending machine?\""
        n "\"I'm okay.\""
        $ renpy.hide(custom_hide("erin"))
        "As soon as she leaves, I take a deep breath. At least she doesn't seem to think I'm weird."
        "Soon, Erin returns with a bag of potato chips and continues to work on her tablet."
    elif art_counter == 4:
        "When I walk into the art room, Erin doesn't look back to see who it is."
        $ renpy.show(custom_show("erin", "angry"), [])
        c "\"I used to be the same way with my art, you know, scared of what people thought.\""
        c "\"But then, I realized it didn't matter.\"" 
        c "\"The important thing was that I kept drawing.\""
        c "\"That I kept getting better.\""
        n "\"What?\""
        "Erin turns towards me, a serious look on her face."
        c "\"The other day, you hid your sketchbook from me.\""
        c "\"You don't have to do that.\""
        n "\"I was embarrassed. Because I was drawing you.\""
        $ renpy.show(custom_show("erin", "uncomf"), [])
        "She shrugs."
        c "\"I draw people all the time.\""
        n "\"So you don't care?\""
        "Erin turns back to her tablet before sliding out of her seat and walking up to me."
        $ renpy.show(custom_show("erin", "embarrassed"), [])
        "Then, she holds up the device, a drawing of myself in our class on the screen."
        c "\"We'll call it even.\""
        "She returns to her seat."

    jump art_main_menu
    return

label art_main_menu:
    hide girl C
    "What should I do?"
    menu:
        "Talk to Erin":
            #if not art_choice_1_a:
            jump art_1_talk
        "Draw" if not art_choice_1_b:
            jump art_1_workout
        "Go Home":
            jump end_of_day
    return 
            
label art_1_talk:
    $ renpy.show(custom_show("erin", "normal"), [])
    $ art_choice_1_a = True
    if C < 0:
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Oh, did you need something?\""
    elif 0 <= C <= 5:
        $ renpy.show(custom_show("erin", "normal"), [])
        c "\"Hi, Sam.\""
    elif 6 <= C <=10:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "\"Hi, Sam! What can I do for you?\""
    elif C >= 10:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"Hi, Sam! Let me know if you need anything, okay?\""
    
    jump talking_to_erin

label talking_to_erin:
    menu:
        "Ask for her number" if not c_number_flag and not c_number_obtained_flag:
            jump c_number
        "Small Talk" if not art_choice_2_a:
            jump art_choice_2_a
        "Ask her about herself" if art_choice_2_a and not art_choice_2_b and iii < day:
            jump art_choice_2_b
        "Ask for feedback on your art" if art_choice_2_a and art_choice_2_b and not art_choice_2_c and jjj < day:
            jump art_choice_2_c
        "Compliment Her" if not art_compliment:
            jump art_choice_2_d
        "Back":
            jump art_main_menu
    return

label art_choice_2_a:
    $ art_choice_2_a = True
    $ C = C + 1
    $ iii = day
    $ renpy.show(custom_show("erin", "normal"), [])
    n "\"It's so quiet on campus right now.\""
    $ renpy.show(custom_show("erin", "sad"), [])
    c "\"Yeah...At first I kind of missed everyone, but I'm starting to enjoy the peace.\""

    jump talking_to_erin
    return

label art_choice_2_b:
    $ renpy.show(custom_show("erin", "normal"), [])
    $ jjj = day
    n "\"So, do you have any hobbies? Other than drawing, I mean.\""

    if 2 <= C < special_C:
        $ renpy.show(custom_show("erin", "happy"), [])
        c "\"Hm, well, I like games. It's a nice way to relax after a long day.\""

        n "\"That's cool, have you ever thought about doing game art professionally? After you graduate?\""

        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"That's actually a big reason I started drawing in the first place. I'd love to be a character artist or work on illustrations for deck-building games or something. No pressure though.\""
        $ renpy.show(custom_show("erin", "normal"), [])

        c "\"Right now, I'm just refining my skills as best I can.\""
    if C >= special_C:
        $ special_C_on = True
        $ renpy.show(custom_show("erin", "sad"), [])
        c "\"Hm, well, I like games. It's a nice way to relax after a long day.\""

        n "\"That's cool, have you ever thought about doing game art professionally? After you graduate?\""

        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"That's actually a big reason I started drawing in the first place. I'd love to be a character artist or work on illustrations for deck-building games or something. No pressure though.\""
    
        c "\"Well...Actually, there is a little pressure.\""

        n "\"There is?\""

        $ renpy.show(custom_show("erin", "uncomf"), [])

        c "\"I probably shouldn't even be saying this in case I jinx it or something. But I'm kind of waiting to hear back from this internship opportunity. It's for a local game company.\""

        n "\"Whoa, really?! That's awesome!\""

        $ renpy.show(custom_show("erin", "sad"), [])

        c "\"Yeah! I mean, it would be…But I probably won't get it. They get a lot of applications, and I'm just a freshman, you know?\""

        menu:
            "Yeah, you're probably right":
                $ C = C + 1
                n "\"I guess it is a bit of a long shot...\""
            "Of course you'll get it!":
                $ believe_in_her = True
                n "\"Are you kidding? I've seen some of your art in the student gallery, and you're way better than most of the seniors.\""
                $ renpy.show(custom_show("erin", "surprised"), [])

                c "\"You really think so? They're all so amazing though...\""

        c "\"It's just, this has been a dream of mine for so long now. And I'm scared I won't be good enough.\""

        n "\"Erin, whether or not you get it, you're good enough. Trust me.\""

        $ renpy.show(custom_show("erin", "flirty"), [])

        c "\"Thanks, Sam.\""
    
    else: 
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Uh, I don't know. Not really I guess.\""

    $ art_choice_2_b = True
    $ C = C + 1
    jump talking_to_erin
    return

label art_choice_2_c:
    $ renpy.show(custom_show("erin", "normal"), [])
    $ kkk = day
    n "\"Do you think you could give me feedback on some of my sketches? I feel like I've hit a wall.\""
    if C>=2:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"Yeah, I can take a look!\""
        "I hand her my sketchbook."
        $ renpy.show(custom_show("erin", "normal"), [])
        "She flips through the pages, and though I'm a little nervous, I know I need to get used to criticism if I want to improve."
        if arting_counter >= 3:
            $ renpy.show(custom_show("erin", "flirty"), [])
            c "\"You have a great eye. Maybe try inking some of the sketches--that'd give you a chance to experiment outside of graphite. Other than that, I really like what you've done so far!\""
            $ C = C + 1
        elif arting_counter >=1:
            $ renpy.show(custom_show("erin", "happy"), [])
            c "\"Hm, your shading could use some work. Try to add more contrast, the values are a little...flat.\""
        else: 
            $ renpy.show(custom_show("erin", "embarrassed"), [])
            c "\"Uh, there aren't really enough sketches here for me to give too much feedback...Maybe I can look again when you've practiced a bit more?\""
            $ C = C - 3
    else:
        $ renpy.show(custom_show("erin", "embarrassed"), [])
        c "\"Maybe some other time...\""
        $ C = C - 3

    $ art_choice_2_c = True
    $ C = C + 2
    jump talking_to_erin
    return

label art_choice_2_d:
    $ art_choice_2_d = True 
    $ art_compliment = True
    if art_comp: 
        n "\"You look nice today!\""
        $ renpy.show(custom_show("erin", "flirty"), [])

        c "\"Aw, thanks!\""
        jump talking_to_erin
    else:
        $ art_comp = True
        $ renpy.show(custom_show("erin", "normal"), [])
        "Well, she's obviously got a great sense of style, but I remember seeing her art in the student gallery, and she's really talented too."
        "What should I compliment her on?"

        menu:
            "Style":
                jump art_choice_compliment_a
            "Talent":
                jump art_choice_compliment_b
        return
                    
label art_choice_compliment_a:
    "What should I say?"
    menu: 
        "That's a cool outfit":
            n "\"You have such a cool style, Erin.\""

            if C >= 2:
                $C = C + 1
                $ renpy.show(custom_show("erin", "flirty"), [])
                c "\"You like my style?\""
                n "\"Yeah! I think it's really unique.\""
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"Thanks, Sam. I like your style too!\""
                jump talking_to_erin
            else:
                $C = C - 1
                $ renpy.show(custom_show("erin", "uncomf"), [])
                c "\"Oh, uh, thank you?\""
                jump talking_to_erin

        "More girls should dress like you":
            n "\"You have such a cool style, Erin. Most girls dress in really boring clothes.\""
            $ renpy.show(custom_show("erin", "sad"), [])
            c "\"Maybe that's just what they like...\""
            $C = C - 3
            jump talking_to_erin
    return 

label art_choice_compliment_b:
    $ renpy.show(custom_show("erin", "normal"), [])
    "What should I say?"

    menu: 
        "You're such a great artist":
            $C = C + 2
            n "\"Wow! Your line art is so clean!\""
            $ renpy.show(custom_show("erin", "flirty"), [])
            c "\"Really? Thanks, Sam. I think I needed the encouragement!\""   
            jump talking_to_erin

        "I wish I was naturally gifted like you":
            n "\"I wish I could draw like that. Some people are just born talented I guess...\""

            if 3 <= C:
                $ renpy.show(custom_show("erin", "uncomf"), [])
                c "\"Maybe you just need to practice more then...\""
            else:
                $ renpy.show(custom_show("erin", "sad"), [])
                c "\"It actually took me a lot of practice to get where I am...\""

            $C = C - 4
            jump talking_to_erin

        "How'd you get so good at art?":
            n "\"Hey, I'm still pretty new to drawing. Do you have any tips for a beginner?\""

            if 4 <= C:
                $C = C + 1
                $ renpy.show(custom_show("erin", "flirty"), [])
                c "\"Of course! What do you need help with?\""
                n "\"I feel like my drawings kind of lack...depth?\""
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"Ah, I had that issue early on too. Try paying more attention to the values on a subject-where light's coming from and where shadows are being cast. It'll look a lot better than just focusing on the outline of whatever you're drawing. Does that make sense?\""
                n "\"Yeah! That makes a lot of sense. Thanks!\""
                $ renpy.show(custom_show("erin", "normal"), [])

                c "\"No problem! Always happy to help.\""

            else:
                $ renpy.show(custom_show("erin", "sad"), [])
                c "\"Hm, there aren't really any shortcuts to improving. You kind of just have to experiment and practice consistently. Sorry if that isn't really helpful.\""
            jump talking_to_erin 

    return 

label art_1_workout:
    $ art_choice_1_b = True 
    $ arting_counter = arting_counter + 1
    $ C = C + 1
    "The pencil scratches against the page of my sketchbook, the lines light in case they'll need erasing."
    $ renpy.show(custom_show("erin", "normal"), []) 
    "I catch Erin looking in my direction."
    "What should I do?"

    menu:
        "Focus on drawing":
            "I continue drawing, and when I glance back at Erin, her attention has already returned to her tablet."

        "Wave":
            if C < 0:
                $ renpy.show(custom_show("erin", "normal"), [])
                $ C = C - 2
                "I wave at Erin."
                "She looks away."
                $ renpy.hide(custom_hide("erin"))
            else: 
                "I wave at Erin."
                $ renpy.show(custom_show("erin", "happy"), [])
                "She waves back at me before returning to her drawing."
                $ renpy.hide(custom_hide("erin"))
                if C >=2:
                    $ C = C + 1
    
    scene bg_art_night with fade
    "After I've filled the page, I close the sketchbook and stretch my wrist."
    "That's enough drawing for now. My hand's a little tired, but the sketches turned out great."
    
    menu: 
        "Talk to Erin":
            if not art_choice_1_a:
                $ renpy.show(custom_show("erin", "normal"), [])
                jump art_1_talk
            if art_choice_1_a:
                $ renpy.show(custom_show("erin", "normal"), [])
                "I say goodbye to Erin before heading out."
                $ C = C + 1
            stop music fadeout 1.0
            scene black with longfade

            jump end_of_day
        "Go Home":
            "I've been out for a while. I think it's time to go home."
            stop music fadeout 1.0
            scene black with longfade

            jump end_of_day
    stop music fadeout 1.0
    return

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
    $ date_c_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if C >= 6:
            $ date_this_weekend = True
            "After a few minutes, my phone chimes and a response from Erin shows on the screen:"
            c "\"Hi, Sam! I'd love to go out! Are you free this weekend?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $ eventbc_trigger = True
            $ date = True
            jump send_text_c
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, uh, I don't really feel like I know you that well. I wouldn't be comfortable. Sorry.\""
            jump send_text_c
        return 
                
label text_buddy_c:
    $ hang_c_sent = True
    "I send a text that reads, \"Hey, Erin! I'm going to the art room tomorrow to draw. Do you want to join me? We could order pizza or something while we're there.\""
    if C >= 4:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\"Yeah! I'm down! See you tomorrow. :)\""
        $ eventac_trigger = True
        jump send_text_c
    else:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\"I can't tomorrow, but I hope you have fun!\""
        jump send_text_c
    return
                        
label text_video_c:
    $ video_c_sent = True
    "Which video should I send?"
    $ evideo_counter = evideo_counter + 1

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
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"I love animation tests. They really show you how much hard work goes into a project.\""
            jump send_text_c
        "A cute kitten grooms a bunny":
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Oh, did you send this to me by accident?\""
            jump send_text_c
    return
            
label text_night_c:
    $ gn_c_sent = True
    "I send a simple goodnight message."
    
    if gn_c_sent2 == False:
        $ gn_c_sent2 = True
        if C >= 5:
            $ C = C + 1
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Goodnight!! :)\""
            jump send_text_c
        else:
            "After a few minutes, my phone chimes and a response from Erin shows on the screen."
            c "\"Uh, goodnight?\""
            jump send_text_c   
    else:
        c "\"Goodnight :)\""
        jump send_text_c
    return

label text_roof_c:
    $ like_c_sent = True
    "I can't just tell her something like that over text. It should be in person."
    "So I write and send a message that reads:"
    n "\"Hey, there's something I want to talk with you about. Do you think we could meet up?\""
    if C >= 100:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen:"
        c "\"Is everything okay?? We can talk. Where should I meet you?\""
        "I type \"Meet me on top of the library, at sunset,\" and hit send."
        $ eventcc_trigger = True
        jump event_c
    else:
        "After a few minutes, my phone chimes and a response from Erin shows on the screen."
        c "\"Oh, I can't right now. Maybe we can talk some other time?\""
        jump end_of_day_menu
    return

label event_ac:
    scene erin_hang with fade
    $ erin_hang_over = True
    play music "audio/event.mp3"
    $temp = day 
    $day = 1

    "The next day, I head to the art room where Erin is waiting."
    c "\"Hi, Sam! I brought the pizza--\""
    scene bg_art with fade
    $ renpy.show(custom_show("erin", "surprised"), [])

    c "\"Oh.\""
    "I'm in the doorway with a pizza box in my hands, looking at Erin holding a cardboard box of her own."
    n "\"I guess we should have coordinated this better.\""
    $ renpy.show(custom_show("erin", "angry"), [])
    c "\"Oh well. I guess we'll just have to eat two whole pizzas.\""
    n "\"Haha, or maybe just have leftovers?\""
    "Erin feigns a dramatic sigh."
    $ renpy.show(custom_show("erin", "flirty"), [])

    c "\"I guess that's an option too.\""
    $ renpy.hide(custom_hide("erin"))
    "We eat our pizza, barely making a dent in the two boxes, then, we start drawing."
    "It's oddly relaxing to work with Erin beside me."

    "When I draw alone, it's easy to get frustrated at little mistakes or feel like I'm not progressing fast enough, but her presence is so calming, and her focus is contagious--not once do I reach for my phone to distract myself."

    "Instead, I feel motivated."

    "I'm sketching a fake potted plant that's in the room, the smell of cheap cheese and crust still strong in the air, and when I look over at Erin's page, I see that it's completely covered in pizza illustrations."

    "At the top of the paper, she's written, 'Pizza Emotional Poses.'"
    n "\"Are you drawing pizza with different expressions?\""
    $ renpy.show(custom_show("erin", "normal"), []) 
    c "\"Oh, haha, yeah. I guess I got inspired.\""
    "She holds up her sketchbook for me to see."
    "Oddly enough, it's easy to tell what emotion the delicious food is emitting in most of the mini sketches."
    $ renpy.show(custom_show("erin", "embarrassed"), [])
    c "\"What do you think?\""
    "The drawings are..."
    menu:
        "Weird":
            $ renpy.show(custom_show("erin", "sad"), [])
            n "\"A little strange maybe.\""
        "Cool":
            $ C = C + 1
            $ renpy.show(custom_show("erin", "flirty"), [])
            n "\"Neat!\""

    n "\"What's that one supposed to be?\""
    "I point to a pizza that seems expressionless, just a normal slice."
    $ renpy.show(custom_show("erin", "angry"), [])
    c "\"Despair.\""
    n "\"Wow, so edgy.\""
    $ renpy.hide(custom_hide("erin"))
    "We soon move on to drawing other food items with various emotions, and I only get stuck once when trying to decide how a hamburger might look when in love."
    stop music fadeout 1.0
    scene black with longfade

    jump quick_calculations

label event_bc:
    $ erin_date_over = True
    $ date = False
    $ date_this_weekend = False
    $ temp = day 
    $ day = 10

    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Erin."
    c "\"So, where are we gonna go today?\""
    menu: 
        "Hiking trail":
            "In response, I write, \"I was thinking we could go on a hike. Is that okay?\""
            a "\"Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\""
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
        "Interactive science museum":
            "In response, I write, \"I was thinking we could check out the science museum. Is that okay?\""
            a "\"Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\""
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
        "Art gallery":
            $ C = C + 1
            "In response, I write, \"I was thinking we could go to this art gallery. Is that okay?\""
            c "\"Oo, that sounds really cool! Text me the address so I know where to meet you. :)\""
        "Ramen shop":
            "In response, I write, \"I was thinking we could grab some ramen. Is that okay?\""
            a "\"Hm, I don't really feel like doing that. But I saw some flyers for an art gallery nearby, maybe we could go?\""
            "I like practicing art a lot more than I like looking at it, but studying other people's work will probably help me improve too."
    scene erin_date with fade
    "When I arrive, I find Erin already inside, staring at a painting."
    "I walk towards the colors of yellow, green, and blue on the canvas, my footsteps loud against the concrete floors, until I'm standing beside her."
    scene bg_artdate with fade
    $ renpy.show(custom_show("erin", "normal"), [])
    c "\"Hi, Sam.\""
    "I see now that the painting depicts a sunflower field with all flowers but one facing the sun."
    scene sunflowers with fade
    c "\"What do you think of it?\""

    menu:
        "I think it's about paving your own path":
            n "\"I think it's about finding your own way, even if everyone else doesn't get it.\""
            $ renpy.show(custom_show("erin", "flirty"), [trueleft])
            c "\"That's nice. I like that.\""
        "I think it's about how it's better to follow what others are doing":
            n "\"I think it's showing why it's important to pay attention to what others are doing and follow their example.\""
            $ renpy.show(custom_show("erin", "sad"), [trueleft])
            c "\"Hm, you really think so?\""
            n "\"Yeah, I mean, that sunflower isn't going to grow very well if it's not facing the sun. It needs to turn around.\""          
            $ renpy.show(custom_show("erin", "uncomf"), [trueleft])
            c "\"That's an interesting interpretation.\""
        "That sunflower isn't going to grow very well":
            n "\"That's one dumb sunflower. Can't even find the sun.\""
            $ renpy.show(custom_show("erin", "sad"), [trueleft])
            c "\"Maybe it doesn't want to face the sun.\""

    $ renpy.show(custom_show("erin", "normal"), [trueleft])

    c "\"Come on, let's look at some others.\""
    scene bg_artdate with fade

    $ renpy.hide(custom_hide("erin"))

    "We move throughout the art gallery, admiring the different paintings displayed on the white walls and pondering on what the artists might've been trying to say with every brush stroke."

    "It's easy to listen to Erin as she talks about art."

    "She speaks with passion and considers every word carefully."

    "Even the way she approaches each painting is intriguing, like she's truly trying to understand the artist through their work. Like she's getting to know a friend."

    $ renpy.show(custom_show("erin", "surprised"), [])

    "Suddenly, Erin's phone rings, and everyone in the gallery turns to see who's guilty of causing the disturbance."

    "Her eyes grow wide as she checks the screen."

    c "\"I'm sorry, I have to take this.\""

    $ renpy.hide(custom_hide("erin"))

    "She walks off and out of the room, leaving me the sole victim of glares and headshakes from the art snobs."

    "I continue to move from painting to painting, but it's significantly less fun without Erin. Luckily, it isn't too long before she returns."

    $ renpy.show(custom_show("erin", "embarrassed"), [])

    c "You'll never guess who that was."

    n "\"Why? Was it...\""
    menu:
        "Your mom?":
            n "\"...your mom or something?\""
            if special_C_on:
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"Remember that internship I told you about? Well, I got it! I can't believe it!\""
            else:
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"I applied for an internship at this local game company, and that was them. I got it! I can't believe it!\""
        "Your doctor?":
            n "\"...your doctor or something?\""
            if special_C_on:
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"Remember that internship I told you about? Well, I got it! I can't believe it!\""
            else:
                $ renpy.show(custom_show("erin", "happy"), [])
                c "\"I applied for an internship at this local game company, and that was them. I got it! I can't believe it!\""
        "The game company?" if special_C_on:
            $ C = C + 1
            $ renpy.show(custom_show("erin", "flirty"), [])
            n "\"...the internship?\""
            c "\"Yes!! Sam, I got it! I can't believe it!\""

    n "\"Oh! Wow! Congratulations!\""

    if believe_in_her:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"Thanks for believing in me, Sam.\""

    $ renpy.show(custom_show("erin", "uncomf"), [])
    c "\"...I didn't realize it until now, but I think waiting to hear back about the whole thing was really starting to wear on me. I try not to care what people think...But...\""
    $ renpy.show(custom_show("erin", "sad"), [])

    c "\"It was really important to me that they liked my art. I guess I've been wondering if I really have what it takes to do game art professionally and landing this internship is so reassuring.\""
    $ renpy.show(custom_show("erin", "flirty"), [])
    c "\"It makes me feel like I'm not crazy for picking this as a career path.\""

    n "\"Choosing art as your career isn't crazy. What would be crazy is being as good as you are and not choosing it.\""

    "She looks up at me with warmth, and I take her hand."
    $ renpy.hide(custom_hide("erin"))

    "We stop in front of each painting as we make our way through the gallery, but I'm no longer paying much attention to the art. All my focus is on Erin, her comforting presence and bright disposition."

    "Despite my best efforts to walk slowly, we eventually find ourselves at the end of the exhibition room and back outside."

    "I walk Erin to her car."

    #change to outside
    scene bg_night with fade
    
    $ renpy.show(custom_show("erin", "flirty"), [])
    c "\"Thanks for inviting me out today, Sam.\""
    n "\"Of course. I'm glad you could make it.\""
    "As I'm looking at her, I realize it's time to part ways."
    n "\"How should I say goodbye?\""

    menu:
        "Kiss her":
            jump kiss_erin
        "Hug her":
            jump hug_erin
        "Give her a high five":
            jump hand_erin
    return

label kiss_erin:
    if C >= 9:
        scene black with fade

        "I lean in."
        "And our lips meet."
        c "\"So, I'll see you in class?\""
        n "\"Yeah, I'll see you then.\""
        scene erin_kiss with fade
        "She gets in her car and drives away."
        "And I can't wait until Tuesday when I get to see her again."
        $day = temp
        jump quick_calculations

    else:
        scene black with fade
        $ C = C - 2
        "I lean in."
        scene bg_night with fade

        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Uh, well, I gotta go.\""
        "She's leaning away, and I feel a wave of embarrassment wash over me."
        c "\"Thanks again.\""
        $ renpy.hide(custom_hide("erin"))
        "Erin gets in her car and drives away. And I'm left wondering what I did wrong."
    
        $day = temp
        jump quick_calculations
    return 

label hug_erin:
    $ renpy.show(custom_show("erin", "flirty"), [])
    $ C = C + 1
    "I give her a hug goodbye, and she holds me tightly."
    c "\"This was a great day.\""
    $ renpy.hide(custom_hide("erin"))
    "She gets in her car and drives away."
    "And I can't wait until Tuesday when I get to see her again."
    $day = temp
    jump quick_calculations
    return

label hand_erin:
    if C >= 9:
        $ C = C - 1
        $ renpy.show(custom_show("erin", "uncomf"), [])
        "She cocks her head and slowly raises her hand to meet mine."
        c "\"Uh, okay. See you then I guess.\""
        $ renpy.hide(custom_hide("erin"))
        "Erin gets in her car and drives away."
        "And I'm wondering if there was a better way I could've done that."
        $day = temp
        jump quick_calculations

    else:
        $ C = C + 1
        "I hold up my hand to give her a high five."
        n "\"See you Tuesday.\""
        "Her hand bounces off mine."
        c "\"See ya!\""
        $ renpy.hide(custom_hide("erin"))
        "She gets in her car and drives away."
        "And I can't wait until I get to see her again."
        $day = temp
        jump quick_calculations
    return

    
label event_cc:
    scene bg_roof with fade
    play music "audio/rooftop.mp3"

    $temp = day 
    $day = 0

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    $ renpy.show(custom_show("erin", "normal"), [])
    "Erin sits cross legged as she stares up at the sky, the clouds drifting above. Her apparent contentment makes me wonder what she's thinking about.."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    
    n "\"Hey.\""
    c "\"Hi, Sam.\""
    "She glances down at the gift in my hand."

    if erin_gift:
        $C = C + 1
        scene sunflowers with fade
        $ renpy.show(custom_show("erin", "flirty"), [])
        "Her eyebrows shoot up in excitement."
        c "\"Hey! Sunflowers!\""
        n "\"I brought them for you.\""
        if eventbc_trigger:
            n "\"They made me think of that painting we saw.\""
        "When I hand her the bouquet, she closes her eyes and brings the flowers to her nose."
        c "\"Thanks, Sam. This made my day.\""
    else:
        $ C = C - 1
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Whatcha got there?\""
        n "\"It's for you.\""
        "As I hand Erin her present, she looks a little confused."
        c "\"Uh, cool. Thanks.\""

    $ renpy.show(custom_show("erin", "normal"), [])
    "We watch the sun slowly fall."
    c "\"It's a great view, huh?\""
    n "\"Yeah...\""
    $ renpy.show(custom_show("erin", "angry"), [])
    c "\"No matter how many times I come up here, I never get tired of it...I want to find more things like that.\""
    n "\"Things you won't get tired of?\""
    $ renpy.show(custom_show("erin", "flirty"), [])
    c "\"Things that are always just as fun, exciting, and beautiful as the first time I experience them.\""
    n "\"I'm not sure that's possible.\""
    $ renpy.show(custom_show("erin", "normal"), [])
    c "\"Maybe for some people. It takes effort to notice beautiful things--not everyone pauses long enough to watch sunsets.\""
    $ renpy.show(custom_show("erin", "happy"), [])
    c "\"Anyway, you wanted to talk about something?\""

    menu:
        "Confess my feelings":
            if erin_confessed:
                jump erin_confessed
            if C == 20:
                jump erin_perfectending
            elif C >= 16:
                jump erin_goodending
            else:
                jump erin_badending
        "I've changed my mind":
            jump neko_ending
    return

label erin_goodending:
    $ erin = True
    n "\"Um, right. Okay, I guess I should just say it then. I really like you, Erin. I know we haven't known each other for very long, but I like you, and I was wondering if maybe...you felt the same way?\""
    "Another breeze blows past us as I wait for her to respond."
    $ renpy.show(custom_show("erin", "normal"), [])
    c "\"You're pretty great, you know that?\""
    n "\"Does that mean...?\""
    $ renpy.show(custom_show("erin", "flirty"), [])
    c "\"I like you too.\""
    n "\"Really?! I mean, that's great!\""
    n "\"She smiles and takes my hand.\""
    "And we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with longfade
    jump epi_start
    return 

label erin_perfectending:
    $ erin = True
    $ renpy.show(custom_show("erin", "flirty"), [])
    c "\"I'm surprised you don't already know.\""
    n "\"Does that mean...?\""
    $ renpy.show(custom_show("erin", "happy"), [])
    c "\"I feel the same. I like you too.\""
    n "\"Really?\""
    $ renpy.show(custom_show("erin", "normal"), [])
    c "\"Really.\""
    "She smiles and takes my hand."
    "Then, we finish watching the sun disappear."
    stop music fadeout 1.0
    scene black with longfade
    $ day = temp
    jump epi_start
    return

label erin_badending:
    $ d_ending_success = True
    $ renpy.show(custom_show("erin", "sad"), [])
    c "\"Uh, sorry. I don't know how to say this. I'm happy we met, and you're a good friend. But...I don't like you in that way.\""
    "It takes a moment before what she's saying sinks in."
    n "\"Huh...I guess I misread things...I'll see you around.\""
    $ renpy.hide(custom_hide("erin"))
    stop music fadeout 1.0
    scene black with longfade
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    scene bg_room_dark
    show neko    
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black with longfade
    $day = temp
    jump credits
    return 

label event_dc:
    scene erin_dorm with fade
    play music "audio/event.mp3"
    $temp = day 
    $day = 3


    "I open my door to find Erin standing outside my room."
    c "\"Hi, Sam. How're you feeling? I heard you were sick.\""
    n "\"Eh, I'm okay, could always be worse though.\""
    c "\"That's the spirit. I'm here because Dr. Paige asked me to drop off some handouts. So you don't get behind.\""
    "I see a few papers in her hand."
    scene bg_outside_dorm with fade
    $ renpy.show(custom_show("erin", "happy"), [])

    n "\"Oh, thanks. Do you want to come in?\""
    c "\"Sure!\""
    "I move to the side, and she walks into my dorm, handing me the papers as she looks around the room."
    scene bg_room with fade

    if clean:
        $ renpy.show(custom_show("erin", "flirty"), [])
        c "\"Whoa, your room is so clean!\""
        n "\"Well, you know. I don't like clutter.\""
        "While her back is turned, I kick a stray piece of trash under my bed."
        "She goes over to my desk and examines my PC, from my keyboard and mouse to my headset and dual monitors."
        $ renpy.show(custom_show("erin", "happy"), [])
        c "\"Nice setup!\""

    else:
        $ renpy.show(custom_show("erin", "uncomf"), [])
        n "\"Sorry for the mess. I've been meaning to clean.\""
        c "\"Eh, that's alright. You're sick, you get to be a little messy today.\""
        "Despite what she says, I can tell by her expression that she's at least a little grossed out by the state of my room."

    "I watch her eyes move across my shelves over every trinket on display."

    $ renpy.show(custom_show("erin", "normal"), [])

    c "\"You have quite the merch collection.\""

    n "\"Yeah, most of them are from conventions. That's where you get the best deals.\""
    $ renpy.show(custom_show("erin", "surprised"), [])

    c "\"Really? I didn't know that. I've never been.\""

    n "\"Well, maybe I can take you sometime.\""

    if special_C:
        $ renpy.show(custom_show("erin", "flirty"), [])
        "She smiles at me."
    else:
        $ renpy.show(custom_show("erin", "uncomf"), [])
        "We stand there for a moment in awkward silence."

    if C >= 16:
        $ erin_confessed = True
        $ renpy.show(custom_show("erin", "embarrassed"), [])
        c "\"Sam? Can I tell you something?\""
        n "\"Sure. What's up?\""
        "She pauses as she thinks."
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Uh, well, I don't know how to say this, but...I think I like you. I'm sorry, did I make things weird?\""

        menu:
            "I like you too": #CHANGE
                n "\"Erin, I--\""
                "We stand there in a moment of content silence before I start getting dizzy."
                $ renpy.show(custom_show("erin", "sad"), [])
                c "\"Sam!\""
                "Erin grabs me as I almost fall to the ground."
                "I know I need to respond to her confession, but my head hurts so much..."
                n "\"Let's go out this weekend. I should be feeling better by then.\""
                $ renpy.show(custom_show("erin", "flirty"), [])
                c "\"Yeah! That'd be fun.\""
                $ renpy.show(custom_show("erin", "angry"), [])
                c "\"Oh but...I should let you rest then! Or you won't heal in time for our date.\""
                "While leaving my room, she hesitates by the doorway."
                $ renpy.show(custom_show("erin", "normal"), [])
                c "\"I'm glad we talked, Sam. Rest up, okay?\""
                $ renpy.hide(custom_hide("erin"))
                "Erin closes the door behind her, and I'm left standing in the middle of my dorm, wishing my headache away so I could go after her and ask her to stay a little longer."
                "But spending time with Erin would have to wait."
                "The second I lie down in my bed, I'm already drifting back to sleep."
                "I dream of a life with Erin. And though I know realistically it's probably caused by the fever, I can't help but think it means something."
                "That these past two weeks are just the beginning."

            "I don't think of you like that":
                n "\"Erin, I--\""
                "We stand there in a moment of content silence before I start getting dizzy."
                $ renpy.show(custom_show("erin", "sad"), [])
                c "\"Sam!\""
                "Erin grabs me as I almost fall to the ground."
                "I know I need to respond to her confession, but my head hurts so much..."
                c "\"I'll head out...let's talk later okay?\""
                "She heads out, closing the door behind her before I have a chance to say anything else."
                $ renpy.hide(custom_hide("erin"))
                n "\"Erin...\""
    else: 
        #Change
        $ renpy.show(custom_show("erin", "sad"), [])
        c "\"Is it alright if I head out? I know I just got here, but I have some stuff I should probably take care of.\""
        n "\"Are you sure?\""
        $ renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Yeah, I think it's for the best. Plus, you're not feeling well.\""
        $ renpy.hide(custom_hide("erin"))
        n "\"Alright. Talk to you later then.\""
        c "\"Bye, Sam.\""
        "Erin leaves, closing the door behind her, and I'm left standing in the middle of my dorm, alone."
        "I go to sleep with my fever induced headache and dream up a life with Neko-Chan...a perfect life."
    $ day = temp
    stop music fadeout 1.0
    scene black with longfade
    jump ch3_schoolday2
    return

label erin_confessed:
    $erin = True
    $ renpy.show(custom_show("erin", "normal"), [])
    n "\"The other day, when I was sick, you said you liked me?\""
    $ renpy.show(custom_show("erin", "embarrassed"), [])
    c "\"Ahh! That was so embarrassing. Can you just forget I said anything?\""

    n "\"No, you don't understand!\""
    $ renpy.show(custom_show("erin", "surprised"), [])

    n "\"I-I didn't get a chance to respond before, but...\""
    n "\"I feel the same way.\""

    
    "Another breeze blows past us."
    $ renpy.show(custom_show("erin", "happy"), [])
    c "\"Really?\""

    n "\"Really.\""
    $ renpy.show(custom_show("erin", "flirty"), [])
    "She smiles as I take her hand."

    "And we finish watching the sun disappear."
    $ day = temp
    stop music fadeout 1.0
    scene black with longfade
    jump epi_start
    return