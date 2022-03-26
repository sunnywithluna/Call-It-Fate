# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Girl A")
define b = Character("Girl B")
define c = Character("Girl C")
define nc = Character("Neko-Chan")

define n = Character("Narrator")

# The game starts here.

init:
    image girl A = Image("girl_A.png")
    image girl B = Image("girl_B.png")
    image girl C = Image("girl_C.png")

# Points
#default book = False
default A = 0
default B = 0
default C = 0
default day = 0
default D = 0

# Flags
default a_number_flag = False
default a_number_obtained_flag = False 
default a_small_talk_flag = False
default a_ask_more_flag = False 
default a_workout_flag = False 

default b_number_flag = False
default b_number_obtained_flag = False 
default b_small_talk_flag = False
default b_ask_more_flag = False 
default b_workout_flag = False 

default c_number_flag = False
default c_number_obtained_flag = False 
default c_small_talk_flag = False
default c_ask_more_flag = False 
default c_workout_flag = False 

# day 0 flags
default day_0_choice_1_a = False 
default day_0_choice_1_b = False

default gym_choice_1_a = False 
default gym_choice_1_b = False 

default gym_choice_2_a = False 
default gym_choice_2_b = False 
default gym_choice_2_c = False
default gym_choice_2_d = False

default library_choice_1_a = False 
default library_choice_1_b = False 

default library_choice_2_a = False 
default library_choice_2_b = False 
default library_choice_2_c = False
default library_choice_2_d = False

default art_choice_1_a = False 
default art_choice_1_b = False 

default art_choice_2_a = False 
default art_choice_2_b = False 
default art_choice_2_c = False
default art_choice_2_d = False

default text_flag = False
default body_flag = False 
default game_flag = False

default event_AA = False
default event_AB = False
default event_AC = False

default event_BA = False
default event_BB = False
default event_BC = False

label start:

    scene bg_bedroom
    n "Yawn I sure am tired"
    n "Today is the first day of my summer session. I can't be late!"
    n "You look around your room"
    n "You have a gaming console and body pillow."
    n "Room is kind of messy."
    n "Oh well..."
    
    jump day_0

    label day_0:
        n "What now?"
        menu:
            "Pick outfit." if not day_0_choice_1_a:
                jump s_2_1
            "Talk to Neko-Chan." if not day_0_choice_1_b:
                jump s_2_2
            "Head out." if day_0_choice_1_a and day_0_choice_1_b:
                jump s_3

        label s_2_1:

            n "Hmm what should I wear?"
            $ day_0_choice_1_a = True

            menu:
                "A sporty look.":
                    n "Maybe I'll go to the gym today..."
                    $ A = A + 1
                    jump day_0
                "A chic look.":
                    n "Does it look like I'm trying too hard?"
                    $ B = B + 1
                    jump day_0
                "An artsy look.":
                    n "I feel creative!"
                    $ C = C + 1
                    jump day_0
                "My usual.":
                    n "Nothing like being comfortable!"
                    jump day_0

        label s_2_2:

            $ day_0_choice_1_b = True


            menu: 
                "Confide in Neko-Chan.":
                    jump s_2_2_1
                "Say goodbye to Neko-Chan.":
                    jump s_2_2_2

            label s_2_2_1:
                
                n "I'm really nervous about the summer session, Neko-Chan."
                n "Sigh"
                n "I should get going soon..."
                jump day_0
            
            label s_2_2_2:
                n "Goodbye..."
                jump day_0

        label s_3:
            scene bg_classroom
            n "It's the first day of the summer school semester!"
            n "You are taking oral communications"
            n "There are people from all types of majors in this class since its general education!"
            n "I hope I make friends"
            n "Maybe even..."
            n "A girlfriend!"
            n "The teacher interrupts your thoughts."
            n "The teacher introduces the class and has the students go around and introduce themselves, explaing why they chose to take this class."
            n "You learn about each of the students."
            n "A couple students in particular catch your eye"
            
            show girl A
            a "Hi I'm girl A"
            n "Wow"

            show girl B
            b "Hi I'm girl B"            
            n "Wow"
            
            show girl C
            c "Hi I'm girl C"
            n "Wow"

            hide girl C
            n "It's your turn to introduce yourself..."
            n "What should I say?"

            menu:
                "Hello everyone! I hope to get along with everyone :)":
                    $ A = A + 2
                "Suck it":
                    $ B = B + 2
                "I like ART":
                    $ C = C + 2
                "I like Japan":
                    $ D = D + 1

            n "Your teacher goes through the lesson."
            
            n "It's a basic day. Nothing special."

            jump after_class
    
    label day_1:
        $ day = day + 1
        
        n "Wednesday..."
        n "It's the second day of school."
        n "Sigh I am so tired"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_2:
        $ day = day + 1
        
        n "It's Friday."
        n "I spent my entire day off studying SIGH"
        n "Summer sessions are so hard"
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_3:
        n "Its finally the weekend"
        n "I think I'll take a quick nap before studying..."
        $ day = day + 1
        jump day_4

    label day_4:
        $ day = day + 1
        
        n "Monday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_5:
        $ day = day + 1
        
        n "Wednesday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_6:
        $ day = day + 1
        
        n "Friday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_7:
        n "Its finally the weekend"
        n "I think I'll take a quick nap before studying..."
        $ day = day + 1
        jump day_8

    label day_8:
        $ day = day + 1
        
        n "Monday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_9:
        $ day = day + 1
        
        n "Wednesday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_10:
        $ day = day + 1
        
        n "Friday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_11:
        n "Its finally the weekend"
        n "I think I'll take a quick nap before studying..."
        $ day = day + 1
        jump day_12

    label day_12:
        $ day = day + 1
        
        n "Monday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_13:
        $ day = day + 1
        
        n "Wednesday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_14:
        $ day = day + 1
        
        n "Friday."
        n "Sigh"
        n "Whoops did I say that outloud..."
        if 6 <= A <= 10:
            show girl A
            a "hehe"
        else:
            if A > 10:
                show girl A
                a "HEHE"
        if 6 <= B <= 10:
            show girl B
            b "hehe"
        else:
            if B > 10:
                show girl B
                B "HEHE"
        if 6 <= C <= 10:
            show girl C
            c "hehe"
        else:
            if C > 10:
                show girl C
                C "HEHE"
        jump after_class

    label day_15:
        n "Its finally the weekend"
        n "I think I'll take a quick nap before studying..."
        $ day = day + 1
        jump ending_a

    label s_killme:
        n "Kill Me"
        return

    label a_number:
        $ a_number_flag = True
        if A >= 2:
            a "Sure!"
            $ a_number_obtained_flag = 1
            jump gym_main_menu
        else:
            a "Uh, no"
            jump gym_main_menu

    label b_number:
        $ b_number_flag = True
        if B >= 1:
            b "Sure!"
            $ b_number_obtained_flag = 1
            jump library_main_menu
        else:
            b "Uh, no"
            jump library_main_menu

    label c_number:
        $ c_number_flag = True
        if C >= 2:
            c "Sure!"
            $ c_number_obtained_flag = 1
            jump art_main_menu
        else:
            c "Uh, no"
            jump art_main_menu

        # s_5
    label after_class:
        n "Mmm, class was so long..."
        n "There's still some free time before I should head home..."
        n "What should I do?"
        # Setting some variables...
        $ a_number_flag = False 
        $ gym_choice_1_a = False 
        $ gym_choice_1_b = False 
        #$ gym_choice_2_a = False 
        #$ gym_choice_2_b = False 
        # a and b should be remembered
        $ gym_choice_2_c = False
        $ gym_choice_2_d = False
        
        menu:
            "Go to the campus gym.":
                jump gym
            "Go to the library.":
                jump library
            "Go to the art room.":
                jump art
            "Just go back to the dorm.":
                jump end_of_day
        
        label gym:
            scene bg_gym
            n "You go to the gym. A is there. You can talk to A or workout."
            jump gym_main_menu

            label gym_main_menu:
                hide girl A
                menu:
                    "Talk to A" if not gym_choice_1_a:
                        jump gym_1_talk
                    "Workout" if not gym_choice_1_b:
                        jump gym_1_workout
                    "Go Home" if gym_choice_1_a and gym_choice_1_b:
                        jump end_of_day
                
                label gym_1_talk:
                    show girl A
                    $ gym_choice_1_a = True
                    n "You talk with A."
                    if 0 <= A <= 5:
                        a "hi"
                    if 6 <= A <=10:
                        a "hi!"
                    if A >= 10:
                        a "hi!!!"
                    
                    menu:
                        "Ask for her number" if not a_number_flag or a_number_obtained_flag:
                            jump a_number
                        "Small Talk" if not gym_choice_2_a:
                            jump gym_choice_2_a
                        "Ask her about herself" if gym_choice_2_a and not gym_choice_2_b:
                            jump gym_choice_2_b
                        "Ask to work out together" if gym_choice_2_a and gym_choice_2_b and not gym_choice_2_c:
                            jump gym_choice_2_c
                        "Compliment Her":
                            jump gym_choice_2_d
                        "Nevermind...":
                            jump gym_main_menu

                    label gym_choice_2_a:
                        n "you make small talk"
                        $ gym_choice_2_a = True
                        $ A = A + 1
                        jump gym_main_menu

                    label gym_choice_2_b:
                        n "you ask her about herself"
                        $ gym_choice_2_b = True
                        $ A = A + 1
                        jump gym_main_menu

                    label gym_choice_2_c:
                        n "You ask to work out together"
                        $ gym_choice_2_c = True
                        $ A = A + 2
                        jump gym_main_menu

                    label gym_choice_2_d:
                        $ gym_choice_2_d = True 
                        n "You want to compliement her. You notice her beaurty and gym skills"
                        menu:
                            "Compliment appearance":
                                jump s_5_1_1_1_a
                            "Compliment workout":
                                jump s_5_1_1_1_b
                        
                        label s_5_1_1_1_a:
                            n "Pick an appearance compliment"
                            menu: 
                                "Respectful compliment":
                                    if A >= 4:
                                        $A = A + 1
                                        a "Thank you!"
                                    else:
                                        $A = A - 1
                                        a "..."
                                    jump gym_main_menu
                                "Hot damn, your body is fiine":
                                    $A = A - 3
                                    a "..."
                                    jump gym_main_menu
                                "Back":
                                    jump gym_main_menu 

                            label s_5_1_1_1_b:
                            n "Pick an gym compliment"
                            menu: 
                                "__lbs on that machine? You're crazy strong":
                                    $A = A + 2
                                    a "Thank you!"
                                "You're pretty strong for a girl":
                                    $A = A - 4
                                    if 3 <= A:
                                        a "back off"
                                    else:
                                        a "..."
                                    jump gym_main_menu
                                "you're making me look weak out here":
                                    if 2 <= A:
                                        $A = A + 1
                                        a "lol"
                                    else:
                                        a "?"
                                    jump gym_main_menu 
                                "Back":
                                    jump gym_main_menu 
                label gym_1_workout:
                    $ gym_choice_1_b = True 
                    n "You work out, A notices you. You can either focus on work out or wave."
                    menu:
                        "Focus on workout":
                            if A < 4:
                                $ A = A + 1
                                show girl A
                                a "Wow he's working hard"
                            else:
                                if A > 8:
                                    show girl A
                                    $ A = A - 1
                                    a "Is he ignoring me?"
                                else:
                                    show girl A
                                    a "..."
                        "Wave":
                            if A < 4:
                                show girl A
                                $ A = A - 1
                                a "Is he just here to flirt?"
                            else:
                                if A > 4:
                                    show girl A
                                    $ A = A + 1
                                    a "*waves back*"
                                else:
                                    show girl A
                                    a "..."
                    hide girl A
                    n "You finish working out"
                    n "You feel proud of yourself"
                    menu: 
                        "Talk to A":
                            if not gym_choice_1_a:
                                show girl A
                                jump gym_1_talk
                            if gym_choice_1_a:
                                n "You talk to A a little bit before heading home"
                                $ A = A + 1
                            jump end_of_day
                        "Go Home":
                            n "I should get going..."
                            jump end_of_day

        label library:
            scene bg_library
            n "You go to the library. B is there. You can talk to B or study."
            jump library_main_menu

            label library_main_menu:
                hide girl B
                menu:
                    "Talk to B" if not library_choice_1_a:
                        jump library_1_talk
                    "Workout" if not library_choice_1_b:
                        jump library_1_workout
                    "Go Home" if library_choice_1_a and library_choice_1_b:
                        jump end_of_day
                
                label library_1_talk:
                    show girl B
                    $ library_choice_1_a = True
                    n "You talk with B."
                    if 0 <= B <= 5:
                        b "hi"
                    if 6 <= B <=10:
                        b "hi!"
                    if B >= 10:
                        b "hi!!!"
                    
                    menu:
                        "Ask for her number" if not b_number_flag or b_number_obtained_flag:
                            jump b_number
                        "Small Talk" if not library_choice_2_a:
                            jump library_choice_2_a
                        "Ask her about herself" if library_choice_2_a and not library_choice_2_b:
                            jump library_choice_2_b
                        "Ask to study together" if library_choice_2_a and library_choice_2_b and not library_choice_2_c:
                            jump library_choice_2_c
                        "Compliment Her":
                            jump library_choice_2_d
                        "Nevermind...":
                            jump library_main_menu

                    label library_choice_2_a:
                        n "you make small talk"
                        $ library_choice_2_a = True
                        $ B = B + 1
                        jump library_main_menu

                    label library_choice_2_b:
                        n "you ask her about herself"
                        $ library_choice_2_b = True
                        $ B = B + 1
                        jump library_main_menu

                    label library_choice_2_c:
                        n "You ask to study together"
                        $ library_choice_2_c = True
                        $ B = B + 2
                        jump library_main_menu

                    label library_choice_2_d:
                        $ library_choice_2_d = True 
                        n "You want to compliement her. You notice her beauty and intelligence"
                        menu:
                            "Compliment appearance":
                                jump library_choice_compliment_a
                            "Compliment intelligence":
                                jump library_choice_compliment_b
                        
                        label library_choice_compliment_a:
                            n "Pick an appearance compliment"
                            menu: 
                                "Respectful compliment":
                                    if B >= 7:
                                        $B = B + 1
                                        b "Thank you!"
                                    else:
                                        $B = B - 1
                                        b "..."
                                    jump library_main_menu
                                "You're pretty cute for a nerdy girl":
                                    $B = B - 3
                                    b "..."
                                    jump library_main_menu
                                "Back":
                                    jump library_main_menu 

                            label library_choice_compliment_b:
                            n "Pick an intelligence compliment"
                            menu: 
                                "What you said in class earlier really got me thinking":
                                    $B = B + 2
                                    b "Thank you!"
                                "backhanded compliment":
                                    $B = B - 4
                                    if 3 <= B:
                                        b "back off"
                                    else:
                                        b "..."
                                    jump library_main_menu
                                "your notes look so much better than mine":
                                    if 4 <= B:
                                        $B = B + 1
                                        b "lol"
                                    else:
                                        b "?"
                                    jump library_main_menu 
                                "Back":
                                    jump library_main_menu 
                label library_1_workout:
                    $ library_choice_1_b = True 
                    n "You study, B notices you. You can either focus on your studies or wave."
                    menu:
                        "Focus on studies":
                            if B < 4:
                                $ B = B + 1
                                show girl B
                                b "Wow he's working hard"
                            else:
                                if B > 8:
                                    show girl B
                                    $ B = B - 1
                                    b "Is he ignoring me?"
                                else:
                                    show girl B
                                    b "..."
                        "Wave":
                            if B < 4:
                                show girl B
                                $ B = B - 1
                                b "Is he just here to flirt?"
                            else:
                                if B > 4:
                                    show girl B
                                    $ B = B + 1
                                    b "*waves back*"
                                else:
                                    show girl B
                                    b "..."
                    hide girl B
                    n "You finish studying"
                    n "You feel proud of yourself"
                    menu: 
                        "Talk to C":
                            if not library_choice_1_a:
                                show girl B
                                jump library_1_talk
                            if library_choice_1_a:
                                n "You talk to B a little bit before heading home"
                                $ B = B + 1
                            jump end_of_day
                        "Go Home":
                            n "I should get going..."
                            jump end_of_day

        label art:
            scene bg_art
            n "You go to the art room. C is there. You can talk to C or study."
            jump art_main_menu

            label art_main_menu:
                hide girl C
                menu:
                    "Talk to C" if not art_choice_1_a:
                        jump art_1_talk
                    "Workout" if not art_choice_1_b:
                        jump art_1_workout
                    "Go Home" if art_choice_1_a and art_choice_1_b:
                        jump end_of_day
                
                label art_1_talk:
                    show girl C
                    $ art_choice_1_a = True
                    n "You talk with C."
                    if 0 <= C <= 5:
                        c "hi"
                    if 6 <= C <=10:
                        c "hi!"
                    if C >= 10:
                        c "hi!!!"
                    
                    menu:
                        "Ask for her number" if not c_number_flag or c_number_obtained_flag:
                            jump c_number
                        "Small Talk" if not art_choice_2_a:
                            jump art_choice_2_a
                        "Ask her about herself" if art_choice_2_a and not art_choice_2_b:
                            jump art_choice_2_b
                        "Ask for feedback on your art" if art_choice_2_a and art_choice_2_b and not art_choice_2_c:
                            jump art_choice_2_c
                        "Compliment Her":
                            jump art_choice_2_d
                        "Nevermind...":
                            jump art_main_menu

                    label art_choice_2_a:
                        n "you make small talk"
                        $ art_choice_2_a = True
                        $ C = C + 1
                        jump art_main_menu

                    label art_choice_2_b:
                        n "you ask her about herself"
                        $ art_choice_2_b = True
                        $ C = C + 1
                        jump art_main_menu

                    label art_choice_2_c:
                        n "You ask for feedback on your art"
                        $ art_choice_2_c = True
                        $ C = C + 2
                        jump art_main_menu

                    label art_choice_2_d:
                        $ art_choice_2_d = True 
                        n "You want to compliement her. You notice her beauty and intelligence"
                        menu:
                            "Compliment appearance":
                                jump art_choice_compliment_a
                            "Compiment art skills":
                                jump art_choice_compliment_b
                        
                        label art_choice_compliment_a:
                            n "Pick an appearance compliment"
                            menu: 
                                "Respectful compliment":
                                    if C >= 7:
                                        $C = C + 1
                                        c "Thank you!"
                                    else:
                                        $C = C - 1
                                        c "..."
                                    jump art_main_menu
                                "you have such a good body, why don't you wear something that shows it off more":
                                    $C = C - 3
                                    c "..."
                                    jump art_main_menu
                                "Back":
                                    jump art_main_menu 

                            label art_choice_compliment_b:
                            n "Pick an intelligence compliment"
                            menu: 
                                "Wow! Your line art is so clean. I wish mine was that good":
                                    $C = C + 2
                                    c "Thank you!"
                                "backhanded compliment":
                                    $C = C - 4
                                    if 3 <= C:
                                        c "back off"
                                    else:
                                        c "..."
                                    jump art_main_menu
                                "Any tips?":
                                    if 4 <= C:
                                        $C = C + 1
                                        c "lol"
                                    else:
                                        c "?"
                                    jump art_main_menu 
                                "Back":
                                    jump art_main_menu 
                label art_1_workout:
                    $ art_choice_1_b = True 
                    n "You study, C notices you. You can either keep drawing or wave."
                    menu:
                        "Focus on drawing":
                            if C < 4:
                                $ C = C + 1
                                show girl C
                                c "Wow he's working hard"
                            else:
                                if C > 8:
                                    show girl C
                                    $ C = C - 1
                                    c "Is he ignoring me?"
                                else:
                                    show girl C
                                    c "..."
                        "Wave":
                            if C < 4:
                                show girl C
                                $ C = C - 1
                                c "Is he just here to flirt?"
                            else:
                                if C > 4:
                                    show girl C
                                    $ C = C + 1
                                    c "*waves back*"
                                else:
                                    show girl C
                                    c "..."
                    hide girl C
                    n "You finish studying"
                    n "You feel proud of yourself"
                    menu: 
                        "Talk to C":
                            if not art_choice_1_a:
                                show girl C
                                jump art_1_talk
                            if art_choice_1_a:
                                n "You talk to B a little bit before heading home"
                                $ C = C + 1
                            jump end_of_day
                        "Go Home":
                            n "I should get going..."
                            jump end_of_day
                    hide girl C 
                    jump end_of_day


    label end_of_day:
        scene bg_bedroom
        n "At home"
        n "You can:"
        $ text_flag = False 
        $ body_flag = False 
        $ game_flag = False

        label end_of_day_menu:
            menu:
                "Play video games" if not game_flag:
                    jump s_6_1
                "Confide in Body Pillow" if not body_flag:
                    jump s_6_2
                "Text someone" if not text_flag:
                    jump s_6_3
                "Go to Sleep":
                    jump s_6_4

            label s_6_1:
                $ game_flag = True
                n "That was fun"
                jump end_of_day_menu 

            label s_6_2:
                $ body_flag = True
                n "You talk about your day and what kind of impression you think you left."
                if C <= A and B <= A:
                    n "I don't think A likes me very much"
                else:
                    if C <= B and A <= B:
                        n "I don't think B likes me very much"
                    else:
                        if B <= C and A <= C:
                            n "I don't think C likes me very much"
                jump end_of_day_menu 

            label s_6_3:
                $ text_flag = True
                if not a_number_obtained_flag and not b_number_obtained_flag and not c_number_obtained_flag:
                    n "Oh, it doesn't look like you have anyone to talk to"
                    jump end_of_day_menu 
                else:
                    menu:
                        "Text A" if a_number_obtained_flag:
                            jump send_text_a
                        "Text B" if b_number_obtained_flag:
                            jump send_text 
                        "Text C" if c_number_obtained_flag:
                            jump send_text

                label send_text_a:
                    n "What should I say?"

                    menu:
                        "Do you want to go out?" if not event_BA:
                            jump text_go_out_a
                        "Let me know if you want a workout buddy!" if not event_AA:
                            jump text_buddy_a
                        "Send cool video":
                            jump text_video_a
                        "Goodnight!":
                            jump text_night_a
                        "Can you meet me on the library roof?":
                            jump text_roof_a

                    label text_go_out_a:
                        if A >= 6:
                            a "Sure!"
                            $ event_BA = True
                            jump end_of_day_menu
                        else:
                            a "no"
                            jump end_of_day_menu
                    
                    label text_buddy_a:
                        if A >= 4:
                            a "Sure"
                            $ event_AA = True
                        else:
                            a "no"
                            jump end_of_day_menu
                            
                    label text_video_a:
                        n "What should I send?"
                        menu:
                            "Animation test video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Trickshot video":
                                n "She loved it!"
                                $ A = A + 1
                                jump end_of_day_menu
                            "Animated educational video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Cute kitten video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                
                    label text_night_a:
                        if A >= 5:
                            $ A = A + 1
                            a "Aww good night"
                            jump end_of_day_menu
                        else:
                            a "no"
                            jump end_of_day_menu        

                    label text_roof_a:
                        if A >= 7:
                            a "Sure!"
                            jump event_c
                        else:
                            a "no"
                            jump end_of_day_menu

                label send_text_b:
                    n "What should I say?"
                    menu:
                        "Do you want to go out?" if not event_BB:
                            jump text_go_out_b
                        "Let me know if you want a study buddy!" if not event_AB:
                            jump text_buddy_b
                        "Send cool video":
                            jump text_video_b
                        "Goodnight!":
                            jump text_night_b
                        "Can you meet me on the library roof?":
                            jump text_roof_b
                    label text_go_out_b:
                        if B >= 6:
                            b "Sure!"
                            $ event_BB = True
                            jump end_of_day_menu
                        else:
                            b "no"
                            jump end_of_day_menu
                    
                    label text_buddy_b:
                        if B >= 4:
                            b "Sure"
                            $ event_AB = True
                        else:
                            b "no"
                            jump end_of_day_menu
                            
                    label text_video_b:
                        n "What should I send?"
                        menu:
                            "Animation test video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Trickshot video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Animated educational video":
                                n "She loved it!"
                                $ B = B + 1
                                jump end_of_day_menu
                            "Cute kitten video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                
                    label text_night_b:
                        if B >= 5:
                            $ B = B + 1
                            b "Aww good night"
                            jump end_of_day_menu
                        else:
                            b "no"
                            jump end_of_day_menu        

                    label text_roof_b:
                        if B >= 7:
                            b "Sure!"
                            jump event_c
                        else:
                            b "no"
                            jump end_of_day_menu

                label send_text_c:
                    n "What should I say?"
                    menu:
                        "Do you want to go out?" if not event_BC:
                            jump text_go_out_c
                        "Let me know if you want a study buddy!" if not event_AC:
                            jump text_buddy_c
                        "Send cool video":
                            jump text_video_c
                        "Goodnight!":
                            jump text_night_c
                        "Can you meet me on the library roof?":
                            jump text_roof_c
                    label text_go_out_c:
                        if C >= 6:
                            c "Sure!"
                            $ event_BC = True
                            jump end_of_day_menu
                        else:
                            c "no"
                            jump end_of_day_menu
                    
                    label text_buddy_c:
                        if C >= 4:
                            c "Sure"
                            $ event_AC = True
                        else:
                            c "no"
                            jump end_of_day_menu
                            
                    label text_video_c:
                        n "What should I send?"
                        menu:
                            "Animation test video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Trickshot video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                            "Animated educational video":
                                n "She loved it!"
                                $ C = C + 1
                                jump end_of_day_menu
                            "Cute kitten video":
                                n "She wasn't impressed..."
                                jump end_of_day_menu
                
                    label text_night_c:
                        if C >= 5:
                            $ C = C + 1
                            c "Aww good night"
                            jump end_of_day_menu
                        else:
                            c "no"
                            jump end_of_day_menu        

                    label text_roof_c:
                        if C >= 7:
                            c "Sure!"
                            jump event_c
                        else:
                            c "no"
                            jump end_of_day_menu

        label s_6_4:
            n "You sleep. Day ends"
            if day == 0:
                jump day_1
            else:
                if day == 1:
                    jump day_2
                else:
                    if day == 2:
                        jump day_3
                    else:
                        if day == 3:
                            jump day_4
                        else:
                            if day == 4:
                                jump day_5
                            else:
                                if day == 5:
                                    jump day_6
                                else:
                                    if day == 6:
                                        jump day_7
                                    else:
                                        if day == 7:
                                            jump day_8
                                        else:
                                            if day == 8:
                                                jump day_9
                                            else:
                                                if day == 9:
                                                    jump day_10
                                                else:
                                                    if day == 10:
                                                        jump day_11
                                                    else:
                                                        if day == 11:
                                                            jump day_12
                                                        else: 
                                                            if day == 12:
                                                                jump day_13
                                                            else:
                                                                if day == 13:
                                                                    jump day_14
                                                                else: 
                                                                    if day == 14:
                                                                        jump day_15

    label event_a:
        n "It's the day after a school day. You hang out with either A, B, or C at either the gym, library, or art room, respectively"
    
    label event_b:
        n "You have a date! Where should you take girl ___"
    
    label event_c:
        n "Asking ___ to be GF. Before meeting __ on the library roof, I should bring a gift. What should I get from the store?"
    
    label event_d:
        n "Whichever girl you have the most points with shows up to your dorm. If it's a tie, then the order goes B, then C, then A (ex. tie between C and A would result in C showing up). They brought you the study guide since the final is going to be taken at the next class."

    label ending_a:
        n "You end up with girl A."
        n "The End with polaroid of you and A playing video games (the light reflection blocks us from seeing your face)"
   
    label ending_b:
        n "You end up with girl B."
        n "The End with polaroid of you and B playing video games (the light reflection blocks us from seeing your face)"

    label ending_c:
        n "You end up with girl C."
        n "The End with polaroid of you and C playing video games (the light reflection blocks us from seeing your face)"

    label ending_d:
        n "You end up with body pillow."
        n "The End with 3 polaroids: you marrying body pillow, in hospital and baby body pillow is born, saying goodbye to grown up baby body pillow heading to college (the light reflection blocks us from seeing your face)"

    return 