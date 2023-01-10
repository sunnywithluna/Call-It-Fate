label b_number:
    $ b_number_flag = True
    n "\"Hey, Anna, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if B >= 1:
        $ renpy.show(custom_show("anna", "happy"), [])
        b "\"Good thinking.\""
        "We exchange phone numbers."
        $ b_number_obtained_flag = 1
        jump talking_to_anna
    else:
        $ renpy.show(custom_show("anna", "angry"), [])
        b "\"I won't need help.\""
        jump talking_to_anna
    return

label library:
    scene bg_lib with fade
    play music "audio/free.mp3"
    $ temp = day
    $ lib_compliment = False
    if lib_counter == 1:
        "The high ceiling of the library is lined with fluorescent lights, half of them off, presumably to save energy during the break."
        "I skim the philosophy section, the age of each book easy to tell from the wear on the bindings. Below one of the books, 'J + K' has been scratched into the wood with a heart around it."

        "Though the library is always pretty quiet, I can usually at least hear the sounds of typing on laptop keys or the printer spitting out essay pages or even the occasional stress-induced sob during finals week."

        "But with the school year over, the place is completely silent."

        "Then, I hear a crinkling sound followed by a light pop."
        $ renpy.show(custom_show("anna", "normal"), [])
        "I look out from behind the bookcase to investigate the noise and find Anna at a table, studying and snacking on a freshly opened bag of pretzels, a strand of hair lightly falling over her notes."
        jump library_main_menu
    elif lib_counter == 2:
        $ renpy.show(custom_show("anna", "normal"), [])
        "Anna sits at the same table as last time, snacking on a bag of pretzels while she highlights passages in her book. I slide into a seat at a table one row over, across and to the right."
        jump library_main_menu
    elif lib_counter == 3:
        $ renpy.show(custom_show("anna", "normal"), [])
        "In the library, Anna writes in a notebook, a variety of colored pens laid out on the table in front of her."
        "Distracted, I bump into a cart of books."
        "I quickly lurch forward to catch the falling cart, but the books still topple onto the ground with cascading thuds."
        $ renpy.show(custom_show("anna", "embarrassed"), [])
        "Anna's staring at the books with wide eyes, a hand over her mouth, and my face grows warm with embarrassment."
        "Then, her gaze moves to meet mine. She laughs, and my shoulders relax."
        b "\"Do you need help?\""
        n "\"No, no. It's okay, I got it.\""
        "I shove the books back into their cart with no concern for organization and take a seat."
        $ renpy.show(custom_show("anna", "happy"), [])
        "Now, Anna's smiling at her notes."
        jump library_main_menu
    elif lib_counter == 4: 
        $ renpy.show(custom_show("anna", "normal"), [])
        "When I go to sit down at my usual spot, there's a bag of pretzels waiting for me on the table with a little sticky note on it that reads, 'For Sam.'"
        n "\"Thanks for the pretzels.\""
        $ renpy.show(custom_show("anna", "embarrassed"), [])
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
            #if not library_choice_1_a:
            jump library_1_talk
        "Study" if not library_choice_1_b:
            jump library_1_workout
        "Go Home":
            jump end_of_day
    return 

label library_1_talk:
    $ library_choice_1_a = True
    if B < 0:
        $ renpy.show(custom_show("anna", "angry"), [])
        b "\"I'm kind of in the middle of something...\""
    elif 0 <= B <= 5:
        $ renpy.show(custom_show("anna", "uncomf"), [])
        b "\"...\""
    elif 6 <= B <=10:
        $ renpy.show(custom_show("anna", "normal"), [])
        b "\"Good evening, Sam.\""
    elif B >= 10:
        $ renpy.show(custom_show("anna", "happy"), [])
        b "\"Sam. It's good to see you.\""
    jump talking_to_anna

label talking_to_anna:
    menu:
        "Ask for her number" if not b_number_flag and not b_number_obtained_flag:
            jump b_number
        "Small Talk" if not library_choice_2_a:
            jump library_choice_2_a
        "Ask her about herself" if library_choice_2_a and not library_choice_2_b and ii < day:
            jump library_choice_2_b
        "Ask to study together" if library_choice_2_a and library_choice_2_b and not library_choice_2_c and jj < day:
            jump library_choice_2_c
        "Compliment Her" if not lib_compliment:
            jump library_choice_2_d
        "Back":
            jump library_main_menu
    return 

label library_choice_2_a:
    $ renpy.show(custom_show("anna", "uncomf"), [])
    n "\"It's so quiet in here.\""
    $ renpy.show(custom_show("anna", "embarrassed"), [])
    b "\"Shouldn't it be?\""
    $ renpy.show(custom_show("anna", "embarrassed2"), [])
    n "\"Well, yeah. But, you know, more than usual.\""
    $ library_choice_2_a = True
    $ B = B + 1
    $ ii = day
    jump talking_to_anna
    return

label library_choice_2_b:
    n "\"Tell me about yourself, Anna.\""
    $ library_choice_2_b = True
    if B >= 5:
        $ renpy.show(custom_show("anna", "embarrassed"), [])
        b "\"What do you want to know?\""
        $ renpy.show(custom_show("anna", "embarrassed2"), [])

        n "\"Well, do you have any hobbies?\""

        $ renpy.show(custom_show("anna", "uncomf"), [])

        "Anna looks away as she thinks."

        $ renpy.show(custom_show("anna", "normal"), [])

        b "\"I like taking my telescope out on clear nights. Does that count?\""

        n "\"So, you stargaze then.\""

        $ renpy.show(custom_show("anna", "happy"), [])

        b "\"You should try it sometime. Looking out into space really reminds you just how small we are-- it's incredibly humbling.\""

        $ renpy.show(custom_show("anna", "embarrassed"), [])

        b "\"I guess that's my hobby... That and manga.\""
        $ renpy.show(custom_show("anna", "embarrassed2"), [])

        n "\"You read manga? We should exchange recommendation lists sometime.\""

        if B >= special_B:
            $ special_B_on = True

            $ renpy.show(custom_show("anna", "angry"), [])

            b "\"...\""

            n "\"Is everything okay? It looks like something's on your mind.\""

            $ renpy.show(custom_show("anna", "sad"), [])

            b "\"Nothing, it's just-- nevermind.\""

            n "\"What is it? You can talk to me.\""

            $ renpy.show(custom_show("anna", "uncomf"), [])

            b "\"I was just trying to remember the last time I actually took my telescope out...\""
            b "\"And I never really set time aside to read manga anymore, unless you count the spare minutes between classes.\""

            n "\"Well, why don't you do those things more then? It sounds like you miss them.\""

            $ renpy.show(custom_show("anna", "sad"), [])

            b "\"I just don't have the time. I'm here on an engineering scholarship, I can't afford to let my grades drop.\""
            b "\"That's why I'm always studying.\""

            n "\"Anna, if you don't ever give yourself a break, you'll burn out.\""
            n "\"You're not going to give your best work if you keep putting all this pressure on yourself.\""

            b "\"I guess you have a point. I'm just worried that if I slow down, things will start slipping through the cracks.\""

            n "\"Trust me. Letting yourself rest will help you do better, not worse.\""

            $ renpy.show(custom_show("anna", "happy"), [])

            b "\"You might be right...\""
            $ renpy.show(custom_show("anna", "flirty"), [])

            b "\"Thank you, Sam. This gives me a lot to think about.\"" 

        else:
            $ renpy.show(custom_show("anna", "normal"), [])

            b "\"We should. I'm always looking for something new to read.\""

    else:
        $ B = B - 2
        $ renpy.show(custom_show("anna", "angry"), [])
        b "\"I'd rather not.\""

    $ jj = day
    jump talking_to_anna
    return

label library_choice_2_c:
    n "\"Hey, I have an idea. Why don't we study together? I mean, we're in the same class. It might be helpful.\""
    $ library_choice_2_c = True

    if B >= 4:
        $ renpy.show(custom_show("anna", "normal"), [])

        b "\"Okay. That makes sense to me.\""
        "I gather my things and move to a spot beside Anna, immediately wondering if I should have opted for a seat across from her instead so as to not encroach on her space. But she doesn't seem to mind."

        if study_counter >= 3:
            "We quiz each other on the class material, and I'm pleasantly surprised at how much I remember."
            $ renpy.show(custom_show("anna", "happy"), [])
            b "\"Wow, Sam. You got nearly every answer right. That's amazing.\""

        elif study_counter >= 1:
            "We quiz each other on the class material, and I'm a little disappointed. I only get about half of the answers right."
            $ renpy.show(custom_show("anna", "normal"), [])
            b "\"Pretty good, but it wouldn't hurt for you to study more.\""

        else:
            "We quiz each other on the class material, and I'm a little embarrassed. I barely get any answers right."
            $ renpy.show(custom_show("anna", "angry"), [])
            b "\"Are you just guessing?\""
            $ B = B-3

    else: 
        $ renpy.show(custom_show("anna", "uncomf"), [])
        b "\"I study better alone.\""
    $ B = B + 2
    $ kk = day
    jump talking_to_anna
    return

label library_choice_2_d:
    $ library_choice_2_d = True 
    $ lib_compliment = True
    if lib_comp: 
        n "\"You look nice today!\""
        $ renpy.show(custom_show("anna", "embarrassed"), [])
        b "\"...\""
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
            n "\"Just throwing it out there, but I think you're really pretty.\""
            if B >= 7:
                $ renpy.show(custom_show("anna", "embarrassed"), [])
                $B = B + 1
                b "\"I didn't realize I was being observed.\""
                $ renpy.show(custom_show("anna", "embarrassed2"), [])

                n "\"Well, it's hard not to notice.\""
                jump talking_to_anna
            else:
                $ renpy.show(custom_show("anna", "angry"), [])
                $B = B - 1
                b "\"Ok\""
                jump talking_to_anna
        
        "You have a great body":
            $B = B - 3
            n "\"I don't know how you eat all those pretzels and still have such a nice body.\""
            n "\"You must have great genetics.\""
            $ renpy.show(custom_show("anna", "angry"), [])
            b "\"...\""
            if day == 1:
                "Anna takes a sweater out of her backpack and puts it on over her dress."
                $temp = 1
                $day = 3
            if day == 2:
                "Anna takes a sweater out of her backpack and puts it on over her dress."
                $temp = 2
                $day = 4
            jump talking_to_anna
    return 

label library_choice_compliment_b:
    n "What should I say?"

    menu: 
        "You're so smart":
            $B = B + 2
            n "\"What you were saying in class today really got me thinking...\""
            n "\"You're really insightful.\""
            $ renpy.show(custom_show("anna", "happy"), [])
            b "\"Thank you. If something I say has a positive impact on those around me, I know I'm doing something right.\""
            jump talking_to_anna

        "You're pretty bright for a girl":
            n "\"You're really smart, you know that? I haven't met many girls with a brain.\""
            if 3 <= B:
                $ renpy.show(custom_show("anna", "angry"), [])
                b "\"You probably haven't met many girls then.\""
            else:
                $ renpy.show(custom_show("anna", "angry"), [])
                b "\"I'm guessing you weren't really paying that much attention to their brains.\""
                n "\"What?\""
                $ renpy.show(custom_show("anna", "uncomf"), [])
                b "\"I'm saying maybe there were other... assets that kept you distracted.\""
            $B = B - 4
            jump talking_to_anna

        "Your notes look so much cleaner than mine":
            n "\"Are your notes color coded?\""
            $ renpy.show(custom_show("anna", "embarrassed"), [])
            b "\"It makes it easier to study.\""
            $ renpy.show(custom_show("anna", "embarrassed2"), [])
            n "\"Wow. I can't keep up with you.\""

            if 4 <= B:
                $ renpy.show(custom_show("anna", "normal"), [])
                $B = B + 1
                b "\"I bet you could.\""

            else:
                $ renpy.show(custom_show("anna", "uncomf"), [])
                b "\"It's not that impressive really. They sell colored pens at the book store.\""
            jump talking_to_anna 

    return

label library_1_workout:
    $ library_choice_1_b = True 
    $ study_counter = study_counter + 1
    $ B = B+1

    "I take out my philosophy book and start to read today's assigned pages, highlighting any sections that seem important."
    $ renpy.show(custom_show("anna", "normal"), [])
    "I catch Anna looking in my direction."
    "What should I do?"

    menu:
        "Focus on studying":
            $ B = B + 1
            $ renpy.show(custom_show("anna", "normal"), [])
            "I continue studying, and when I glance back at Anna, she looks impressed."
        "Wave":
            if B <= 4:
                $ B = B - 1
                "I wave at Anna."
                $ renpy.show(custom_show("anna", "angry"), [])
                "She gives me a blank stare before returning to her studies."
            else:
                "I wave at Anna."
                $ renpy.show(custom_show("anna", "flirty"), [])
                "She smiles at me before returning to her studies."
                if B >= 7:
                    $ B = B + 1
    $ renpy.hide(custom_hide("anna"))

    "After I finish reading, I stretch my neck from side to side."
    scene bg_lib_night with fade

    "That's enough studying for now. I'm mentally exhausted, but I know I'm learning a lot."
    $ day = temp
    menu: 
        "Talk to Anna":
            if not library_choice_1_a:
                $ renpy.show(custom_show("anna", "normal"), [])
                jump library_1_talk
            if library_choice_1_a:
                "I say goodbye to Anna before heading out."
                $ B = B + 1
        
            stop music fadeout 1.0
            scene black with fade
            jump end_of_day
        "Go Home":
            "I've been out for a while. I think it's time to go home."
            
            stop music fadeout 1.0
            scene black with fade
            jump end_of_day
    return

label send_text_b:
    n "What should I say?"
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
    $ date_b_sent = True
    if date_this_weekend:
        "I already have a date this weekend. I shouldn't overbook myself."
    else:
        "I send a text that reads, \"Hey, I was wondering, do you want to go out sometime?\""
        if B >= 6:
            $ date_this_weekend = True
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I was hoping you'd ask. How's this weekend sound?\""
            "As if I ever have plans."
            n "\"This weekend sounds great,\" I reply, beaming, though I doubt she can tell over text."
            $ eventbb_trigger = True
            $ date = True
            jump send_text_b
        else:
            "After waiting for some time, I realize Anna isn't going to respond. I guess she isn't interested."
            jump send_text_b
        return

label text_buddy_b:
    $ hang_b_sent = True
    "I send a text that reads, \"Hey, Anna! I'm planning to study in the library tomorrow if you want to join\""
    if B >= 4:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"Good thinking. I'll be there.\""
        $ eventab_trigger = True
        jump send_text_b
    else:
        "After waiting for some time, I realize Anna isn't going to respond. Maybe she's busy?"
        jump send_text_b
    return
        
label text_video_b:
    "Which video should I send?"
    $ avideo_counter = avideo_counter + 1
    $ video_b_sent = True

    menu:
        "A guy bounces a ping pong ball off five surfaces before landing it perfectly in a cup":
            "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I don't get it. Why'd you send this to me?\""
            $ B = B - 1
            jump send_text_b
        "A man on a podcast talks about dark matter":
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"Neat video.\""
            $ B = B + 1
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
    $ gn_b_sent = True
    "I send a simple goodnight message."

    if gn_b_sent2 == False:
        $ gn_b_sent2 = True
        if B >= 5:
            $ B = B + 1
            "After a few minutes, my phone chimes and a response from Anna shows on the screen."
            b "\"I hope you had a good day, Sam. Sleep well.\""
            jump send_text_b
        else:
            "After waiting for some time, I realize Anna isn't going to respond. Maybe she's already asleep."
            jump send_text_b        
    else:
        b "\"Goodnight\""
        jump send_text_b        
    return

label text_roof_b:
    $ like_b_sent = True
    "I can't just tell her something like that over text. It should be in person."
    "So I write and send a message that reads:"
    n "\"Hey, there's something I want to talk with you about. Do you think we could meet up?\""

    if B >= 100:
        "After a few minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"We can do that. Give me a time and place, and I'll be there.\""
        "I type \"Meet me on top of the library, at sunset\" and hit send."
        $ eventcb_trigger = True
        jump event_c
    else:
        "After about thirty minutes, my phone chimes and a response from Anna shows on the screen."
        b "\"Now's not a great time. Raincheck?\""
        jump send_text_b


label event_ab:
    scene anna_hang with fade
    play music "audio/event.mp3"
    $ anna_hang_over = True
    $ temp = day
    $ day = 1

    "The next day, I head to the library where Anna is waiting, her attention so focused on the book in front of her, she doesn't even notice when I arrive."
    n "\"Hey.\""
    scene bg_lib with fade

    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"You made it.\""
    "She looks up and puts her book away."
    
    n "\"Of course.\""
    menu:
        "I wanted to see you.":
            n "\"Any excuse to see you is worth it.\""
            if B >= 5:
                $ renpy.show(custom_show("anna", "embarrassed"), [])
                $B = B + 1
                b "\"...\""
                $ renpy.show(custom_show("anna", "embarrassed2"), [])
            else:
                $ renpy.show(custom_show("anna", "uncomf"), [])
                b "\"...\""
        "I want to get an 'A'.":  
            n "\"I want to do well in this class.\""
            $ renpy.show(custom_show("anna", "happy"), [])
            b "\"...\""

    $ renpy.hide(custom_hide("anna"))
    "We start the study session by working on our homework, moving through the short-answer questions quicker than I ever could alone."
    "It's strange to think that just a few weeks ago, I had trouble working up the nerve to even talk to Anna, and now we're studying together."

    "I feel lucky getting to spend time with her, though, it's also nerve-racking."

    "I'm terrified that I'll say something stupid or mess things up somehow. It's no secret that Anna's hard to impress."
    "I don't want to scare her off."

    "But as she looks up at me from her paper and smiles, I feel less tense."
    "After all, if she's here with me now, I must be doing something right."

    "When we finish the assignment, Anna hands me her nearly perfect notes, which I use to quiz her on the class material."

    "As I go through the questions, I start to notice that every time she gets an answer wrong, Anna will bite her lip or sigh."
    $ renpy.show(custom_show("anna", "sad"), [])
    n "\"It's okay not to know all the answers. That's why we're studying.\""
    "Anna's gaze falls to the table in front of her, a disappointed look in her eyes."
    #$ renpy.show(custom_show("anna", "sigh"), [])

    b "\"I just... it's frustrating.\""
    n "\"It's okay, you're still learning. If we knew all this stuff already, we wouldn't need to take the class.\""
    $ renpy.show(custom_show("anna", "uncomf"), [])
    b "\"...\""
    n "\"I get that it's discouraging when you don't understand something right away. But it's also kind of exciting, right? Because that means we get the chance to learn something new.\""
    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"...Thank you, Sam...\""
    b "\"Ask me another question, I'll be okay.\""
    $ renpy.show(custom_show("anna", "normal"), [])
    "We pick up where we trueleft off, and Anna no longer seems bothered by her mistakes."
    stop music fadeout 1.0
    scene black with fade
    $ day = temp
    jump quick_calculations
    return

label event_bb:
    $ anna_date_over = True
    $ date = False
    $ date_this_weekend = False
    
    $temp = day 
    $day = 10

    "Because I have a date!"
    "My phone chimes, and when I check it, there's a new text from Anna."
    b "\"Did you have any ideas on where we should go today?\""
    menu: 
        "Hiking trail":
            "In response, I write, \"I was thinking we could go on a hike. Is that okay?\""
            b "\Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\""
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
        "Interactive science museum":
            $ B = B + 1
            "In response, I write, \"I was thinking we could check out the science museum. Is that okay?\""
            b "\"That's perfect. Let's meet there at 11am.\""
        "Art gallery":
            "In response, I write, \"I was thinking we could go to this art gallery. Is that okay?\""
            b "\"Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\""
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
        "Ramen shop":
            "In response, I write, \"I was thinking we could grab some ramen. Is that okay?\""
            b "\"Actually, could we go to the Revelation Science Museum? They have some new exhibits that I've been meaning to check out.\""
            "I usually avoid museums, thinking they'll be boring, but I still agree to go. Maybe this will be a chance for me to learn something new."
    
    scene anna_date with fade

    "When I arrive, I find Anna beside the ticket stand, thumbing through museum pamphlets."
    n "\"Hey!\""
    "Anna turns to face me."
    scene bg_libdate with fade
    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"Good, you're here. I got us tickets.\""
    n "\"Oh, really? I was planning on paying...\""
    $ renpy.show(custom_show("anna", "flirty"), [])
    b "\"It's fine. You can get the next one.\""
    n "\"'The next one?'\""
    $ renpy.show(custom_show("anna", "normal"), [])
    b "\"So was there anything you really wanted to see? I have a map if you want to look.\""
    "She pulls out the map and hands it to me. As I examine the creased, colorful illustration of the museum, I notice a couple exhibits that pique my interest."
    n "\"What should we check out?\""
    menu: 
        "Planetarium":
            $ B = B + 2
            n "\"Let's go to the planetarium.\""
            $ renpy.show(custom_show("anna", "embarrassed"), [])
            b "\"I was thinking the same thing.\""
            $ renpy.show(custom_show("anna", "embarrassed2"), [])
        "Bed of needles":
            $ B = B - 1
            n "\"Let's go to the bed of needles.\""
            $ renpy.show(custom_show("anna", "uncomf"), [])
            b "\"...Sure, we can do that. Would you mind if we went to the planetarium first though? There's a show starting soon.\""

    $ renpy.hide(custom_hide("anna"))

    "As we head inside the museum, I look around at all the interesting interactive exhibits around us. I hear sounds of awe and laughter, the big, open room overflowing with energy."

    "It's much quieter in the planetarium though. The speakers play ethereal long tones to add to the space--like atmosphere as we stare up at a fake night sky and wait for the show to begin."

    "Soon the doors close, and the projected stars and planets start to move."

    "A deep, surrounding voice teaches us about the wonders of our galaxy, the mysteries of space, and I feel Anna's hand find mine."

    scene stem_poster with fade

    "At the exit, we're handed flyers that read, \"GRANT OPPORTUNITIES FOR WOMEN IN STEM,\" followed by details on how to apply."

    n "\"Hey, I bet you'd qualify.\""
    
    "I hold up the paper for Anna to see."

    $ renpy.show(custom_show("anna", "uncomf", "trueleft"), [])

    b "\"I don't know if that's really for me...\""

    "Isn't she in school for..."
    menu:
        "...Chemistry?":
            n "\"Sure it is, you're a chemistry student, right?\""
            $ renpy.show(custom_show("anna", "sad"), [])
            b "\"Engineering actually. But that's not what I mean.\""

        "...Engineering?":
            n "\"Sure it is, you're an engineering student, right?\""
            $ renpy.show(custom_show("anna", "normal"), [])
            b "\"Well, yes, but that's not what I mean.\""

        "...Medicine?":
            n "\"Sure it is, you're a pre-med student, right?\""
            $ renpy.show(custom_show("anna", "sad"), [])
            b "\"Engineering actually. But that's not what I mean.\""

    $ renpy.show(custom_show("anna", "uncomf"), [])

    b "\"I'm not sure I feel comfortable getting special treatment just because I'm a woman. If I get a grant, I want it to be because I earned it.\""

    n "\"I wouldn't think of it like that…If you apply for the grant and get picked, that's you earning it. There's nothing noble about turning down a good opportunity.\""

    if special_B_on:

        n "\"Besides, if you get the grant, you won't have to be so worried about losing your scholarship.\""

    b "\"You make a fair point...\""

    $ renpy.show(custom_show("anna", "normal"), [])

    b "\"Okay, I'll do it. I'll apply.\""

    n "\"Great! Let me know when you get it.\""

    $ renpy.show(custom_show("anna", "flirty"), [])

    b "\"You mean 'if' I get it.\""

    n "\"No, I mean 'when.'"

    $ renpy.hide(custom_hide("anna"))

    scene bg_libdate with fade

    "We spend the rest of our time exploring the museum, laying on the bed of needles, disrupting the miniature tornado, poking all the venus flytraps in the gift shop to make their bristled mouths close."

    "Usually, when I'd see Anna around campus, she'd always be doing school work--reading, studying. Even in the cafeteria, she'd have a laptop or notebook out."

    "So, seeing her outside of school and actually letting loose... It's almost a little weird."

    "I'm taken by surprise at just how fun she is to hang around. How her eyes widen with wonder at all the gadgets and exhibits of the museum. How seeing something she doesn't understand and figuring out how it works seems to genuinely excite her."
    
    "But eventually, we run out of things to see, and it's time to leave the museum. So I walk Anna to her car."
    
    scene bg_night with fade 

    $ renpy.show(custom_show("anna", "flirty"), [])
    b "\"Today was nice.\""


    if special_B_on:

        $ renpy.show(custom_show("anna", "flirty"), [])
        b "\"I think you were right, Sam. I really need to take breaks like this more often.\""

    b "\"I'm glad you invited me out.\""

    $ renpy.show(custom_show("anna", "flirty"), [])
    n "\"Me too.\""
    "As I'm looking at her, I realize it's time to part ways."
    "How should I say goodbye?"

    menu:
        "Kiss her":
            jump kiss_anna
        "Hug her":
            jump hug_anna
        "Give her a high five":
            jump hand_anna
    return

label kiss_anna:
    if B >= 8:
        scene anna_kiss with fade

        $ B = B + 1
        "I lean in."
        "And our lips meet."
        scene black

        "Smiling, she gets in her car and drives away."
        "And I can't wait until Tuesday when I get to see her again."
        $ day = temp
        jump quick_calculations
    else:
        $ B = B - 1
        "I lean in."
        $ renpy.show(custom_show("anna", "uncomf"), [])
        "And she leans away. I feel a wave of embarrassment wash over me."
        b "\"I should go. Bye, Sam.\""
        $ renpy.hide(custom_hide("anna"))
        "Anna gets in her car and drives away."
        "And I'm trueleft wondering what I did wrong."
        $ day = temp
        jump quick_calculations
    return 

label hug_anna:
    $ renpy.hide(custom_hide("anna"))
    "I give Anna a hug goodbye before she gets in her car and drives away."
    "And I'm trueleft wondering if there was a better way I could've done that."
    $ day = temp
    jump quick_calculations
    return 

label hand_anna:
    "I hold up my hand to give her a high five."
    $ renpy.show(custom_show("anna", "angry"), [])
    n "\"See you Tuesday.\""
    "Anna stares blankly at my open palm"
    b "\"See you Tuesday.\""
    $ renpy.hide(custom_hide("anna"))
    "She gets in her car and drives away."
    "And I awkwardly lower my hand, feeling a little embarrassed by the situation."
    $ day = temp
    jump quick_calculations
    return

label event_cb:
    $temp = day 
    $day = 0
    scene bg_roof with fade
    play music "audio/rooftop.mp3"

    "The sky is just beginning to turn a faded orange as I climb onto the roof of the library. A cool breeze rushes through my hair."
    "As my heart picks up pace, I realize just how nervous I am."
    $ renpy.show(custom_show("anna", "normal"), [])
    "Anna stands at a distance from the edge of the roof, even with the fencing in place. She seems...at peace. Relaxed."
    "When I walk towards her, the sound of my footsteps gives me away, and she turns around."
    n "\"Hey.\""
    b "\"I was just admiring the view.\""
    $ renpy.show(custom_show("anna", "happy"), [])
    "She looks back at the sunset, and I join her, watching the changing sky while I think of what to say."

    n "\"I got this for you.\""

    if anna_gift:
        scene anna_venus_flytraps with fade
        $B = B + 1
        "Anna looks down at the venus flytrap, and smiles."
        if eventbb_trigger:
            b "\"Like the ones at the museum.\""
        "I hand it to her."
        b "I'll take good care of it. Thank you."
    else:
        $ renpy.show(custom_show("anna", "uncomf"), [])
        "Anna turns to face me and accepts the gift, the blank expression on her face only making me more nervous."
        n "\"Do you like it?\""
        b "\"...I appreciate the thought.\""
    scene bg_roof with fade
    $ renpy.show(custom_show("anna", "normal"), [])
    "The air grows cooler as we stare out into the horizon."
    n "\"What are you thinking about?\""
    $ renpy.show(custom_show("anna", "uncomf"), [])
    b "\"I've never been up here before...I'll spend hours in the library. But I never once went on the roof... It's nice.\""
    n "\"Well, I guess now you have a new spot for study breaks.\""
    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"I guess so...Thank you, Sam.\""
    n "\"What for?\""
    $ renpy.show(custom_show("anna", "flirty"), [])
    b "\"For inviting me here, for breaking me out of my comfort zone. I've been told I can be a little...closed off. I appreciate you being patient with me.\""
    n "\"It's no trouble at all.\""
    $ renpy.show(custom_show("anna", "happy"), [])
    "She smiles."

    $ renpy.show(custom_show("anna", "normal"), [])
    b "\"So what was it you wanted to talk about?\""

    menu:
        "Confess my feelings":
            if anna_confessed:
                jump anna_confessed
            if B == 20:
                jump anna_perfectending
            elif B >= 14:
                jump anna_goodending
            else:
                jump anna_badending
        "I've changed my mind":
            jump neko_ending
    return

label anna_goodending:
    $ anna = True
    n "\"I really like you, Anna. I know we haven't known each other for very long, but I like you, and I was wondering if maybe... you felt the same way?\""
    "Another breeze blows past us as I wait for her to respond."
    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"I do.\""
    "It takes a moment before what she's saying sinks in."
    n "\"You...feel the same?\""
    $ renpy.show(custom_show("anna", "normal"), [])
    "She nods."
    n "\"Really?! I mean, that's great!\""
    "Despite the chilled air, I feel warm."
    "She takes my hand."
    "And we finish watching the sun disappear."
    $day = temp 
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 

label anna_perfectending:
    $ anna = True
    $ renpy.show(custom_show("anna", "flirty"), [])
    b "\"Of course I feel the same way.\""
    n "\"Really?! I mean, that's great!\""
    $ renpy.show(custom_show("anna", "normal"), [])

    "Despite the chilled air, I feel warm."
    "And we finish watching the sun disappear."
    $day = temp
    stop music fadeout 1.0
    scene black with fade
    jump epi_start
    return 

label anna_badending:
    $ d_ending_success = True
    $ renpy.show(custom_show("anna", "angry"), [])
    b "\"You're a good guy, so I'm sorry if I've misled you. But I don't feel that way about you.\""
    "It takes a moment before what she's saying sinks in."
    n "\"Huh... I guess I misread things... I'll see you around.\""
    "I have nothing else to say, so I leave the roof and head back to my dorm."
    $day = temp
    stop music fadeout 1.0
    scene black with fade

    scene bg_room_dark
    "Neko-Chan sits on her usual spot on my bed, and I realize, looking at her, that she is the only girl in my life who could never hurt me."
    "I'm done putting myself out there just to get rejected."
    "For now on, it's just going to be me and Neko-Chan."
    "And I guess I'm okay with that."
    stop music fadeout 1.0
    scene black with fade
    jump credits
    return 

label event_db:
    scene anna_dorm with fade
    play music "audio/event.mp3"
    $temp = day 
    $day = 3

    "I open my door to find Anna standing outside my room."
    n "\"Anna! What are you doing here?\""
    b "\"I brought you some papers from class and made you a copy of my notes.\""
    n "\"Really? Thanks. You didn't have to do all that.\""
    "She hands me a few pages, the passages already color-coded with highlighters."
    scene bg_outside_dorm with fade
    $ renpy.show(custom_show("anna", "happy"), [])
    b "\"The final's on Thursday. I wanted to make sure you'd be prepared.\""
    n "\"Do you want to come in?\""
    "I move to the side, and she walks into my dorm."
    scene bg_room with fade

    if clean:
        $ renpy.show(custom_show("anna", "flirty"), [])
        b "\"You have a nice dorm.\""
        "She wanders over to my bookshelf, examining the collection of manga that sits there."
        $ renpy.show(custom_show("anna", "happy"), [])
        b "\"And good taste.\""

    else:
        $ renpy.show(custom_show("anna", "angry"), [])
        n "\"Sorry for the mess. I've been meaning to clean.\""
        "I catch Anna eyeing a dirty dish on my desk and instantly regret inviting her in."
        "She must think I'm disgusting."
        "I watch as she wanders over to my bookshelf, examining the collection of manga that sits there."

    $ renpy.show(custom_show("anna", "uncomf"), [])

    b "\"I never owned any complete sets like these. I usually either check them out or buy second-hand.\""

    n "\"You're welcome to borrow any of those if you like.\""

    $ renpy.show(custom_show("anna", "happy"), [])

    b "\"Do I get a 'Sam's Dorm' library card?\""

    n "\"Sure. But if you're overdue, I'll have to charge you.\""

    $ renpy.show(custom_show("anna", "flirty"), [])

    "She laughs."


    if B >= 14:
        $ anna_confessed = True
        "We stand there for a moment in silence."
        $ renpy.show(custom_show("anna", "uncomf"), [])
        b "\"There's something I want to tell you. But I'm a little nervous...\""
        n "\"What is it? Is it bad?\""
        "Anna shakes her head"
        $ renpy.show(custom_show("anna", "embarrassed"), [])
        b "\"No, nothing bad. It's just hard to say.\""
        $ renpy.show(custom_show("anna", "embarrassed2"), [])
        "She looks away from me, and I wait, wondering what it could be."
        b "\"I have feelings for you. I thought I should tell you, even if you might not feel the same.\""
        "Then, she looks up at me, and I know she's waiting for a response."

        menu:
            "I like you too": #CHANGE
                n "\"Anna, I--\""
                "A wave of dizziness overwhelms me."
                $ renpy.show(custom_show("anna", "embarrassed"), [])
                b "\"Sam!\""
                "Anna grabs me, keeping me from losing my balance."
                $ renpy.show(custom_show("anna", "normal"), [])
                b "\"I'm glad I came by.\""
                n "\"Me too.\""
                "I knew I had to reply to her confession, but I felt so weak."
                b "\"I'm going to leave now.\""
                "My heart raced."
                n "\"What?\""
                $ renpy.show(custom_show("anna", "uncomf"), [])
                b "\"So you can rest. You're sick. I can't expect you to entertain a guest right now.\""
                n "\"I guess you have a point.\""
                $ renpy.show(custom_show("anna", "happy"), [])
                b "\"Don't worry. We'll spend some time together...this weekend?\""
                n "\"Sounds great.\""
                "While leaving my room, she hesitates by the doorway."
                $ renpy.show(custom_show("anna", "embarrassed2"), [])
                b "\"Goodbye, Sam. I hope you feel better in the morning.\""
                $ renpy.hide(custom_hide("anna"))
                "Anna closes the door behind her, and I'm trueleft lying in bed, wishing my headache away so I could go after her and ask her to stay a little longer."
                "But spending time with Anna would have to wait."
                "The second I lie down in my bed, I'm already drifting back to sleep."
                "I dream of a life with Anna. And though I know realistically it's probably just caused by the fever, I can't help but think it means something."
                "That these past two weeks are just the beginning."
                $ day = temp
                jump quick_calculations
            "I don't think of you like that":
                n "\"Anna, I--\""
                "We stand there in a moment of content silence before I start getting dizzy."
                $ renpy.show(custom_show("anna", "sad"), [])
                b "\"Sam!\""
                "Anna grabs me as I almost fall to the ground. Anna helps me get into bed as I become too dizzy to stand"
                b "\"I'm glad I came by.\""
                n "\"Me too.\""
                "I knew I had to reply to her confession, but I felt so weak."
                b "\"I'm going to leave now.\""
                "My heart raced."
                n "\"What?\""
                $ renpy.show(custom_show("anna", "uncomf"), [])
                b "\"So you can rest. You're sick. I can't expect you to entertain a guest right now.\""
                n "\"I guess you have a point.\""
                $ renpy.show(custom_show("anna", "happy"), [])
                b "\"Don't worry. We'll spend some time together...this weekend?\""
                n "\"Anna...\""
                $ renpy.hide(custom_hide("anna"))
                "She leaves the room, closing the door behind her before I have a chance to say anything else."
                $ day = temp
                jump quick_calculations

    else: 
        #Change
        $ renpy.show(custom_show("anna", "uncomf"), [])
        b "\"I'm going to go.\""
        n "\"Are you sure?\""
        b "\"You're sick. It's not good for you to entertain guests right now. I'll see you in class.\""
        n "\"Alright. Talk to you later then.\""
        $ renpy.hide(custom_hide("anna"))
        "Anna leaves, closing the door behind her, and I'm trueleft standing in the middle of my dorm, alone."
        "I go to sleep with my fever induced headache and dream up a life with Neko-Chan... a perfect life."
        $ day = temp
        jump quick_calculations
    return

label anna_confessed:
    $ anna = True
    n "\"The other day, when I was sick, you said something to me.\""
    $ renpy.show(custom_show("anna", "embarrassed"), [])

    b "\"I was hoping you'd forgotten that...\""
    $ renpy.show(custom_show("anna", "embarrassed2"), [])

    n "\"Why?\""
    $ renpy.show(custom_show("anna", "sad"), [])

    b "\"Because... you don't feel the same.\""

    n "\"No, but I do! I didn't get a chance to respond before, but-\""

    "Anna interrupts me with a kiss."

    "Despite the chilled air, I feel warm."

    "And we finish watching the sun disappear."
    $day = temp
    stop music fadeout 1.0
    scene black with fade
    jump epi_start

    return
