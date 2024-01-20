
label library:
    scene bg_lib_a with dissolve
    play music "audio/free.mp3" fadein 1.0
    $ temp = day_counter
    $ lib_compliment = False
    if lib_counter == 1:
        "The high ceiling of the library is lined with fluorescent lights, half of them off, presumably to save energy during the break."
        "I skim the philosophy section, the age of each book easy to tell from the wear on the bindings. Below one of the books, 'J + K' has been scratched into the wood with a heart around it."

        "Though the library is always pretty quiet, I can usually at least hear the sounds of typing on laptop keys or the printer spitting out essay pages or even the occasional stress-induced sob during finals week."

        "But with the school year over, the place is completely silent."

        "Then, I hear a crinkling sound followed by a light pop."
        $ renpy.show(custom_show("anna", "N"), [])
        "I look out from behind the bookcase to investigate the noise and find Anna at a table, studying and snacking on a freshly opened bag of pretzels, a strand of hair lightly falling over her notes."
        jump library_main_menu
    elif lib_counter == 2:
        $ renpy.show(custom_show("anna", "N"), [])
        "Anna sits at the same table as last time, snacking on a bag of pretzels while she highlights passages in her book. I slide into a seat at a table one row over, across and to the right."
        jump library_main_menu
    elif lib_counter == 3:
        $ renpy.show(custom_show("anna", "N"), [])
        "In the library, Anna writes in a notebook, a variety of colored pens laid out on the table in front of her."
        "Distracted, I bump into a cart of books."
        "I quickly lurch forward to catch the falling cart, but the books still topple onto the ground with cascading thuds."
        $ renpy.show(custom_show("anna", "E"), [])
        "Anna's staring at the books with wide eyes, a hand over her mouth, and my face grows warm with embarrassment."
        "Then, her gaze moves to meet mine. She laughs, and my shoulders relax."
        b "\'Do you need help?\'"
        n "\'No, no. It's okay, I got it.\'"
        "I shove the books back into their cart with no concern for organization and take a seat."
        $ renpy.show(custom_show("anna", "H"), [])
        "Now, Anna's smiling at her notes."
        jump library_main_menu
    elif lib_counter == 4: 
        $ renpy.show(custom_show("anna", "N"), [])
        "When I go to sit down at my usual spot, there's a bag of pretzels waiting for me on the table with a little sticky note on it that reads, 'For Sam.'"
        n "\'Thanks for the pretzels.\'"
        $ renpy.show(custom_show("anna", "E"), [])
        "Anna glances over and smiles at me before returning to her notebook, her own pretzels beside it."
        jump library_main_menu
    else:
        n "..."

    jump library_main_menu
    return


label library_main_menu:
    "What should I do?"
    $ renpy.hide(custom_hide("anna"))
    menu:
        "Talk to Anna":
            # if not library_choice_1_a:
            jump library_1_talk
        "Study" if not library_choice_1_b:
            jump library_1_workout
        "Go Home":
            jump end_of_act
    return 


label library_1_talk:
    $ anna_unlocked = True
    $ library_choice_1_a = True
    if B < 0:
        $ renpy.show(custom_show("anna", "A"), [])
        b "\'I'm kind of in the middle of something...\'"
    elif 0 <= B <= 5:
        $ renpy.show(custom_show("anna", "U"), [])
        b "\'...\'"
    elif 6 <= B <=10:
        $ renpy.show(custom_show("anna", "N"), [])
        b "\'Good evening, Sam.\'"
    elif B >= 10:
        $ renpy.show(custom_show("anna", "H"), [])
        b "\'Sam. It's good to see you.\'"
    jump talking_to_anna


label talking_to_anna:
    menu:
        "Ask for her number" if not b_number_flag and not phoneFlagB:
            jump b_number
        "Small Talk" if not library_choice_2_a:
            jump library_choice_2_a
        "Ask her about herself" if library_choice_2_a and not library_choice_2_b and ii < day_counter:
            jump library_choice_2_b
        "Ask to study together" if library_choice_2_a and library_choice_2_b and not library_choice_2_c and jj < day_counter:
            jump library_choice_2_c
        "Compliment Her" if not lib_compliment:
            jump library_choice_2_d
        "Back":
            jump library_main_menu
    return 


label library_choice_2_a:
    $ renpy.show(custom_show("anna", "U"), [])
    n "\'It's so quiet in here.\'"
    $ renpy.show(custom_show("anna", "E"), [])
    b "\'Shouldn't it be?\'"
    $ renpy.show(custom_show("anna", "embarrassed2"), [])
    n "\'Well, yeah. But, you know, more than usual.\'"
    $ library_choice_2_a = True
    $ A = A + 1
    $ ii = day_counter
    jump talking_to_anna
    return


label library_choice_2_b:
    n "\'Tell me about yourself, Anna.\'"
    $ library_choice_2_b = True
    if B >= 5:
        $ renpy.show(custom_show("anna", "E"), [])
        b "\'What do you want to know?\'"
        $ renpy.show(custom_show("anna", "embarrassed2"), [])

        n "\'Well, do you have any hobbies?\'"

        $ renpy.show(custom_show("anna", "U"), [])

        "Anna looks away as she thinks."

        $ renpy.show(custom_show("anna", "N"), [])

        b "\'I like taking my telescope out on clear nights. Does that count?\'"

        n "\'So, you stargaze then.\'"

        $ renpy.show(custom_show("anna", "H"), [])

        b "\'You should try it sometime. Looking out into space really reminds you just how small we are--it's incredibly humbling.\'"

        $ renpy.show(custom_show("anna", "E"), [])

        b "\'I guess that's my hobby...That and manga.\'"
        $ renpy.show(custom_show("anna", "embarrassed2"), [])

        n "\'You read manga? We should exchange recommendation lists sometime.\'"

        if B >= special_B:
            $ special_B_on = True

            $ renpy.show(custom_show("anna", "A"), [])

            b "\'...\'"

            n "\'Is everything okay? It looks like something's on your mind.\'"

            $ renpy.show(custom_show("anna", "E2"), [])

            b "\'Nothing, it's just--nevermind.\'"

            n "\'What is it? You can talk to me.\'"

            $ renpy.show(custom_show("anna", "U"), [])

            b "\'I was just trying to remember the last time I actually took my telescope out...\'"
            b "\'And I never really set time aside to read manga anymore, unless you count the spare minutes between classes.\'"

            n "\'Well, why don't you do those things more then? It sounds like you miss them.\'"

            $ renpy.show(custom_show("anna", "E2"), [])

            b "\'I just don't have the time. I'm here on an engineering scholarship, I can't afford to let my grades drop.\'"
            b "\'That's why I'm always studying.\'"

            n "\'Anna, if you don't ever give yourself a break, you'll burn out.\'"
            n "\'You're not going to give your best work if you keep putting all this pressure on yourself.\'"

            b "\'I guess you have a point. I'm just worried that if I slow down, things will start slipping through the cracks.\'"

            n "\'Trust me. Letting yourself rest will help you do better, not worse.\'"

            $ renpy.show(custom_show("anna", "H"), [])

            b "\'You might be right...\'"
            $ renpy.show(custom_show("anna", "F"), [])

            b "\'Thank you, Sam. This gives me a lot to think about.\'" 

        else:
            $ renpy.show(custom_show("anna", "N"), [])

            b "\'We should. I'm always looking for something new to read.\'"

    else:
        $ B = B - 2
        $ renpy.show(custom_show("anna", "A"), [])
        b "\'I'd rather not.\'"

    $ jj = day_counter
    jump talking_to_anna
    return


label library_choice_2_c:
    n "\'Hey, I have an idea. Why don't we study together? I mean, we're in the same class. It might be helpful.\'"
    $ library_choice_2_c = True

    if B >= 4:
        $ renpy.show(custom_show("anna", "N"), [])

        b "\'Okay. That makes sense to me.\'"
        "I gather my things and move to a spot beside Anna, immediately wondering if I should have opted for a seat across from her instead so as to not encroach on her space. But she doesn't seem to mind."

        if study_counter >= 3:
            "We quiz each other on the class material, and I'm pleasantly surprised at how much I remember."
            $ renpy.show(custom_show("anna", "H"), [])
            b "\'Wow, Sam. You got nearly every answer right. That's amazing.\'"

        elif study_counter >= 1:
            "We quiz each other on the class material, and I'm a little disappointed. I only get about half of the answers right."
            $ renpy.show(custom_show("anna", "N"), [])
            b "\'Pretty good, but it wouldn't hurt for you to study more.\'"

        else:
            "We quiz each other on the class material, and I'm a little embarrassed. I barely get any answers right."
            $ renpy.show(custom_show("anna", "A"), [])
            b "\'Are you just guessing?\'"
            $ B = B-3

    else: 
        $ renpy.show(custom_show("anna", "U"), [])
        b "\'I study better alone.\'"
    $ B = B + 2
    $ kk = day_counter
    jump talking_to_anna
    return


label library_choice_2_d:
    $ library_choice_2_d = True 
    $ lib_compliment = True
    if lib_comp: 
        n "\'You look nice today!\'"
        $ renpy.show(custom_show("anna", "E"), [])
        b "\'...\'"
        $ renpy.show(custom_show("anna", "embarrassed2"), [])

        jump talking_to_anna
    else:
        $ lib_comp = True
        "Well, she's clearly very pretty, but hearing some of the things she says in class, it's obvious she's super smart too."
        "What should I compliment her on?"
        menu:
            "Beauty":
                jump library_choice_compliment_a
            "Intelligence":
                jump library_choice_compliment_b
    

label library_choice_compliment_a:
    "What should I say?"
    menu: 
        "You're really pretty":
            n "\'Just throwing it out there, but I think you're really pretty.\'"
            if B >= 7:
                $ renpy.show(custom_show("anna", "E"), [])
                $ A = A + 1
                b "\'I didn't realize I was being observed.\'"
                $ renpy.show(custom_show("anna", "embarrassed2"), [])

                n "\'Well, it's hard not to notice.\'"
                jump talking_to_anna
            else:
                $ renpy.show(custom_show("anna", "A"), [])
                $ B = B - 1
                b "\'Ok\'"
                jump talking_to_anna
        
        "You have a great body":
            $ B = B - 3
            n "\'I don't know how you eat all those pretzels and still have such a nice body.\'"
            n "\'You must have great genetics.\'"
            $ renpy.show(custom_show("anna", "A"), [])
            b "\'...\'"
            if day_counter == 1:
                "Anna takes a sweater out of her backpack and puts it on over her dress."
                $ temp = 1
                $ day_counter = 3
            if day_counter == 2:
                "Anna takes a sweater out of her backpack and puts it on over her dress."
                $ temp = 2
                $ day_counter = 4
            jump talking_to_anna
    return 


label library_choice_compliment_b:
    "What should I say?"

    menu: 
        "You're so smart":
            $ B = B + 2
            n "\'What you were saying in class today really got me thinking...\'"
            n "\'You're really insightful.\'"
            $ renpy.show(custom_show("anna", "H"), [])
            b "\'Thank you. If something I say has a positive impact on those around me, I know I'm doing something right.\'"
            jump talking_to_anna

        "You're pretty bright for a girl":
            n "\'You're really smart, you know that? I haven't met many girls with a brain.\'"
            if 3 <= B:
                $ renpy.show(custom_show("anna", "A"), [])
                b "\'You probably haven't met many girls then.\'"
            else:
                $ renpy.show(custom_show("anna", "A"), [])
                b "\'I'm guessing you weren't really paying that much attention to their brains.\'"
                n "\'What?\'"
                $ renpy.show(custom_show("anna", "U"), [])
                b "\'I'm saying maybe there were other...assets that kept you distracted.\'"
            $ B = B - 4
            jump talking_to_anna

        "Your notes look so much cleaner than mine":
            n "\'Are your notes color coded?\'"
            $ renpy.show(custom_show("anna", "E"), [])
            b "\'It makes it easier to study.\'"
            $ renpy.show(custom_show("anna", "embarrassed2"), [])
            n "\'Wow. I can't keep up with you.\'"

            if 4 <= B:
                $ renpy.show(custom_show("anna", "N"), [])
                $ A = A + 1
                b "\'I bet you could.\'"

            else:
                $ renpy.show(custom_show("anna", "U"), [])
                b "\'It's not that impressive really. They sell colored pens at the book store.\'"
            jump talking_to_anna 

    return


label library_1_workout:
    $ library_choice_1_b = True 
    $ study_counter = study_counter + 1
    $ B = B+1

    "I take out my philosophy book and start to read today's assigned pages, highlighting any sections that seem important."
    $ renpy.show(custom_show("anna", "N"), [])
    "I catch Anna looking in my direction."
    "What should I do?"

    menu:
        "Focus on studying":
            $ A = A + 1
            $ renpy.show(custom_show("anna", "N"), [])
            "I continue studying, and when I glance back at Anna, she looks impressed."
        "Wave":
            if B <= 4:
                $ B = B - 1
                "I wave at Anna."
                $ renpy.show(custom_show("anna", "A"), [])
                "She gives me a blank stare before returning to her studies."
            else:
                "I wave at Anna."
                $ renpy.show(custom_show("anna", "F"), [])
                "She smiles at me before returning to her studies."
                if B >= 7:
                    $ A = A + 1
    $ renpy.hide(custom_hide("anna"))

    "After I finish reading, I stretch my neck from side to side."
    scene bg_lib_b with dissolve

    "That's enough studying for now. I'm mentally exhausted, but I know I'm learning a lot."
    $ day_counter = temp
    menu: 
        "Talk to Anna":
            if not library_choice_1_a:
                $ renpy.show(custom_show("anna", "N"), [])
                jump library_1_talk
            if library_choice_1_a:
                "I say goodbye to Anna before heading out."
                $ A = A + 1
        
            stop music fadeout 1.0
            scene black with fade
            jump end_of_act
        "Go Home":
            "I've been out for a while. I think it's time to go home."
            
            stop music fadeout 1.0
            scene black with fade
            jump end_of_act
    return