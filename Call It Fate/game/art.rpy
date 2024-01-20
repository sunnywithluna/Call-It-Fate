
label art:
    scene bg_art_a with dissolve
    play music "audio/free.mp3" fadein 1.0
    $ art_compliment = False
    if art_counter == 1:
        "I peek in through the door window at the nearly empty studio, easels abandoned and scattered throughout the space, the adjacent prop room closed off."

        "The only person inside is Erin, who sits near the front, drawing on a tablet."

        "When I walk in, she turns to see who opened the door."
        $ renpy.show(custom_show("erin", "N"), [])
        n "\'Oh, um, is it alright if I work here too?\'"
        $ renpy.show(custom_show("erin", "H"), [])

        c "\'Go for it! I don't mind the company.\'"

        n "\'Awesome. I thought it might be easier to practice away from my dorm--too many distractions there.\'"
        $ renpy.show(custom_show("erin", "F"), [])

        c "\'I'll try not to disturb you then.\'"
        $ renpy.hide(custom_hide("erin"))

        "She smiles and turns back to her tablet, an illustration of a griffin on the screen, which I immediately recognize from the student gallery where an earlier version of the painting sits on display."

        "I'm a little surprised."

        "Usually, the most skilled art students tend to carry themselves with a sort of withdrawn self-importance."
        "But Erin seems so affable and easygoing."
        "It's refreshing."
    elif art_counter == 2:
        $ renpy.show(custom_show("erin", "N"), [])
        "As I enter the room, Erin looks back and waves."
        $ renpy.hide(custom_hide("erin"))
        "It's nice being here in the summer."
        "During the school year, I never felt quite comfortable working in the art room, always paranoid that students and professors were silently judging my sketches."
        "But the place doesn't seem so intimidating now."
    elif art_counter == 3:
        "I stare at the blank page in front of me, wondering what I should draw, tapping my pencil against the edge of my sketchbook."
        "The cursor blinks in an open browser on my laptop, waiting for me to search for reference photos once I decide on a subject."
        $ renpy.show(custom_show("erin", "N"), [])
        "Then, I look up and see Erin drawing on her tablet. And I start sketching."
        $ renpy.hide(custom_hide("erin"))
        "The illustration that forms on my page isn't half bad. I might even ink this one."
        $ renpy.show(custom_show("erin", "H"), [])
        c "\'I'm going to the vending machine. Do you want anything?\'"
        "Erin is standing above me, and I instinctively cover my sketchbook. I'd been so focused on cleaning my lines, I didn't catch her getting up."
        $ renpy.show(custom_show("erin", "N"), []) 
        c "\'Whatcha drawing?\'"
        "I feel my face flush as I move my hand from the page."
        n "\'I needed to practice people. I--\'"
        $ renpy.show(custom_show("erin", "E"), [])
        c "\'Hey, that's me!\'"
        "She examines the drawing with squinted eyes."
        $ renpy.show(custom_show("erin", "A"), [])
        c "\'It's not a bad start. Maybe try breaking the subject up into smaller shapes next time.\'"
        "\'Don't try to draw a person, just draw the shapes that make up the person, does that make sense?\'"
        n "\'Yeah...I think so.\'"
        $ renpy.show(custom_show("erin", "H"), [])
        c "\'Great! So, vending machine?\'"
        n "\'I'm okay.\'"
        $ renpy.hide(custom_hide("erin"))
        "As soon as she leaves, I take a deep breath. At least she doesn't seem to think I'm weird."
        "Soon, Erin returns with a bag of potato chips and continues to work on her tablet."
    elif art_counter == 4:
        "When I walk into the art room, Erin doesn't look back to see who it is."
        $ renpy.show(custom_show("erin", "A"), [])
        c "\'I used to be the same way with my art, you know, scared of what people thought.\'"
        c "\'But then, I realized it didn't matter.\'" 
        c "\'The important thing was that I kept drawing.\'"
        c "\'That I kept getting better.\'"
        n "\'What?\'"
        "Erin turns towards me, a serious look on her face."
        c "\'The other day, you hid your sketchbook from me.\'"
        c "\'You don't have to do that.\'"
        n "\'I was embarrassed. Because I was drawing you.\'"
        $ renpy.show(custom_show("erin", "U"), [])
        "She shrugs."
        c "\'I draw people all the time.\'"
        n "\'So you don't care?\'"
        "Erin turns back to her tablet before sliding out of her seat and walking up to me."
        $ renpy.show(custom_show("erin", "E"), [])
        "Then, she holds up the device, a drawing of myself in our class on the screen."
        c "\'We'll call it even.\'"
        "She returns to her seat."

    jump art_main_menu
    return


label art_main_menu:
    hide girl C
    "What should I do?"
    menu:
        "Talk to Erin" if not art_choice_1_a:
            jump art_1_talk
        "Draw" if not art_choice_1_b:
            jump art_1_workout
        "Say bye":
            $ renpy.show(custom_show("Erin", "N"), [])
            "I say goodbye to Erin before heading out."
            $ C = C + 1
            jump end_of_act
        "Go home":
            jump end_of_act


label art_1_talk:
    $ erin_unlocked = True
    $ renpy.show(custom_show("erin", "N"), [])
    $ art_choice_1_a = True
    if C < 0:
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Oh, did you need something?\'"
    elif 0 <= C <= 5:
        $ renpy.show(custom_show("erin", "N"), [])
        c "\'Hi, Sam.\'"
    elif 6 <= C <=10:
        $ renpy.show(custom_show("erin", "H"), [])
        c "\'Hi, Sam! What can I do for you?\'"
    elif C >= 10:
        $ renpy.show(custom_show("erin", "F"), [])
        c "\'Hi, Sam! Let me know if you need anything, okay?\'"
    
    jump talking_to_erin


label talking_to_erin:
    menu:
        "Ask for her number" if not numberFlagC and not phoneFlagC:
            jump c_number
        "Engage in small talk" if not art_choice_2_a:
            jump art_choice_2_a
        "Get to know her" if art_choice_2_a and not art_choice_2_b and iii < day_counter:
            jump art_choice_2_b
        "Ask for feedback on your art" if art_choice_2_a and art_choice_2_b and not art_choice_2_c and jjj < day_counter:
            jump art_choice_2_c
        "Compliment her" if not art_compliment:
            jump art_choice_2_d
        "Back":
            jump art_main_menu
    return


label art_choice_2_a:
    $ art_choice_2_a = True
    $ C = C + 1
    $ iii = day_counter
    $ renpy.show(custom_show("erin", "N"), [])
    n "\'It's so quiet on campus right now.\'"
    $ renpy.show(custom_show("erin", "S"), [])
    c "\'Yeah...At first I kind of missed everyone, but I'm starting to enjoy the peace.\'"

    jump talking_to_erin
    return


label art_choice_2_b:
    $ renpy.show(custom_show("erin", "N"), [])
    $ jjj = day_counter
    n "\'So, do you have any hobbies? Other than drawing, I mean.\'"

    if 2 <= C < special_C:
        $ renpy.show(custom_show("erin", "H"), [])
        c "\'Hm, well, I like games. It's a nice way to relax after a long day.\'"

        n "\'That's cool, have you ever thought about doing game art professionally? After you graduate?\'"

        $ renpy.show(custom_show("erin", "F"), [])
        c "\'That's actually a big reason I started drawing in the first place. I'd love to be a character artist or work on illustrations for deck-building games or something. No pressure though.\'"
        $ renpy.show(custom_show("erin", "N"), [])

        c "\'Right now, I'm just refining my skills as best I can.\'"
    if C >= special_C:
        $ special_C_on = True
        $ renpy.show(custom_show("erin", "S"), [])
        c "\'Hm, well, I like games. It's a nice way to relax after a long day.\'"

        n "\'That's cool, have you ever thought about doing game art professionally? After you graduate?\'"

        $ renpy.show(custom_show("erin", "F"), [])
        c "\'That's actually a big reason I started drawing in the first place. I'd love to be a character artist or work on illustrations for deck-building games or something. No pressure though.\'"
    
        c "\'Well...Actually, there is a little pressure.\'"

        n "\'There is?\'"

        $ renpy.show(custom_show("erin", "U"), [])

        c "\'I probably shouldn't even be saying this in case I jinx it or something. But I'm kind of waiting to hear back from this internship opportunity. It's for a local game company.\'"

        n "\'Whoa, really?! That's awesome!\'"

        $ renpy.show(custom_show("erin", "S"), [])

        c "\'Yeah! I mean, it would be…But I probably won't get it. They get a lot of applications, and I'm just a freshman, you know?\'"

        menu:
            "Yeah, you're probably right":
                $ C = C + 1
                n "\'I guess it is a bit of a long shot...\'"
            "Of course you'll get it!":
                $ believe_in_her = True
                n "\'Are you kidding? I've seen some of your art in the student gallery, and you're way better than most of the seniors.\'"
                $ renpy.show(custom_show("erin", "surprised"), [])

                c "\'You really think so? They're all so amazing though...\'"

        c "\'It's just, this has been a dream of mine for so long now. And I'm scared I won't be good enough.\'"

        n "\'Erin, whether or not you get it, you're good enough. Trust me.\'"

        $ renpy.show(custom_show("erin", "F"), [])

        c "\'Thanks, Sam.\'"
    
    else: 
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Uh, I don't know. Not really I guess.\'"

    $ art_choice_2_b = True
    $ C = C + 1
    jump talking_to_erin
    return


label art_choice_2_c:
    $ renpy.show(custom_show("erin", "N"), [])
    $ kkk = day_counter
    n "\'Do you think you could give me feedback on some of my sketches? I feel like I've hit a wall.\'"
    if C>=2:
        $ renpy.show(custom_show("erin", "F"), [])
        c "\'Yeah, I can take a look!\'"
        "I hand her my sketchbook."
        $ renpy.show(custom_show("erin", "N"), [])
        "She flips through the pages, and though I'm a little nervous, I know I need to get used to criticism if I want to improve."
        if arting_counter >= 3:
            $ renpy.show(custom_show("erin", "F"), [])
            c "\'You have a great eye. Maybe try inking some of the sketches--that'd give you a chance to experiment outside of graphite. Other than that, I really like what you've done so far!\'"
            $ C = C + 1
        elif arting_counter >=1:
            $ renpy.show(custom_show("erin", "H"), [])
            c "\'Hm, your shading could use some work. Try to add more contrast, the values are a little...flat.\'"
        else: 
            $ renpy.show(custom_show("erin", "E"), [])
            c "\'Uh, there aren't really enough sketches here for me to give too much feedback...Maybe I can look again when you've practiced a bit more?\'"
            $ C = C - 3
    else:
        $ renpy.show(custom_show("erin", "E"), [])
        c "\'Maybe some other time...\'"
        $ C = C - 3

    $ art_choice_2_c = True
    $ C = C + 2
    jump talking_to_erin
    return


label art_choice_2_d:
    $ art_choice_2_d = True 
    $ art_compliment = True
    if art_comp: 
        n "\'You look nice today!\'"
        $ renpy.show(custom_show("erin", "F"), [])

        c "\'Aw, thanks!\'"
        jump talking_to_erin
    else:
        $ art_comp = True
        $ renpy.show(custom_show("erin", "N"), [])
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
            n "\'You have such a cool style, Erin.\'"

            if C >= 2:
                $ C = C + 1
                $ renpy.show(custom_show("erin", "F"), [])
                c "\'You like my style?\'"
                n "\'Yeah! I think it's really unique.\'"
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'Thanks, Sam. I like your style too!\'"
                jump talking_to_erin
            else:
                $ C = C - 1
                $ renpy.show(custom_show("erin", "U"), [])
                c "\'Oh, uh, thank you?\'"
                jump talking_to_erin

        "More girls should dress like you":
            n "\'You have such a cool style, Erin. Most girls dress in really boring clothes.\'"
            $ renpy.show(custom_show("erin", "S"), [])
            c "\'Maybe that's just what they like...\'"
            $ C = C - 3
            jump talking_to_erin
    return 


label art_choice_compliment_b:
    $ renpy.show(custom_show("erin", "N"), [])
    "What should I say?"

    menu: 
        "You're such a great artist":
            $ C = C + 2
            n "\'Wow! Your line art is so clean!\'"
            $ renpy.show(custom_show("erin", "F"), [])
            c "\'Really? Thanks, Sam. I think I needed the encouragement!\'"   
            jump talking_to_erin

        "I wish I was naturally gifted like you":
            n "\'I wish I could draw like that. Some people are just born talented I guess...\'"

            if 3 <= C:
                $ renpy.show(custom_show("erin", "U"), [])
                c "\'Maybe you just need to practice more then...\'"
            else:
                $ renpy.show(custom_show("erin", "S"), [])
                c "\'It actually took me a lot of practice to get where I am...\'"

            $ C = C - 4
            jump talking_to_erin

        "How'd you get so good at art?":
            n "\'Hey, I'm still pretty new to drawing. Do you have any tips for a beginner?\'"

            if 4 <= C:
                $ C = C + 1
                $ renpy.show(custom_show("erin", "F"), [])
                c "\'Of course! What do you need help with?\'"
                n "\'I feel like my drawings kind of lack...depth?\'"
                $ renpy.show(custom_show("erin", "H"), [])
                c "\'Ah, I had that issue early on too. Try paying more attention to the values on a subject--where light's coming from and where shadows are being cast. It'll look a lot better than just focusing on the outline of whatever you're drawing. Does that make sense?\'"
                n "\'Yeah! That makes a lot of sense. Thanks!\'"
                $ renpy.show(custom_show("erin", "N"), [])

                c "\'No problem! Always happy to help.\'"

            else:
                $ renpy.show(custom_show("erin", "S"), [])
                c "\'Hm, there aren't really any shortcuts to improving. You kind of just have to experiment and practice consistently. Sorry if that isn't really helpful.\'"
            jump talking_to_erin 

    return 


label art_1_workout:
    $ art_choice_1_b = True 
    $ arting_counter = arting_counter + 1
    $ C = C + 1
    "The pencil scratches against the page of my sketchbook, the lines light in case they'll need erasing."
    
    $  randnotice = renpy.random.choice(['notice', 'or not'])
    if randnotice == 'notice':
        $ renpy.show(custom_show("erin", "N"), []) 
        "I catch Erin looking in my direction."
        "What should I do?"

        menu:
            "Focus on drawing":
                "I continue drawing, and when I glance back at Erin, her attention has already returned to her tablet."

            "Wave":
                if C < 0:
                    $ renpy.show(custom_show("erin", "N"), [])
                    $ C = C - 2
                    "I wave at Erin."
                    "She looks away."
                    $ renpy.hide(custom_hide("erin"))
                else: 
                    "I wave at Erin."
                    $ renpy.show(custom_show("erin", "H"), [])
                    "She waves back at me before returning to her drawing."
                    $ renpy.hide(custom_hide("erin"))
                    if C >=2:
                        $ C = C + 1
        
    scene bg_art_b with dissolve
    "After I've filled the page, I close the sketchbook and stretch my wrist."
    "That's enough drawing for now. My hand's a little tired, but the sketches turned out great."
    
    jump art_main_menu