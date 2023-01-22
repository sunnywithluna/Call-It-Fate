define a = Character("Maddie", who_color = "#104010")
define b = Character("Anna", who_color = "#104010")
define c = Character("Erin", who_color = "#104010")
define nc = Character("Neko-Chan", who_color = "#104010")
define p = Character("Dr. Paige", who_color = "#104010")
define n = Character("Sam", who_color = "#104010") 

#persistent data, gallery and main menu
define persistent.a_ending_success2 = False
define persistent.b_ending_success2 = False
define persistent.c_ending_success2 = False
define persistent.score = 0

init:
    image neko = Image("nekochan.png")
    image jennifer = Image("jennifer.PNG")    
    # maddie date outfit
    image maddie_5 uncomf = Image("maddie_date_uncomf.png")
    image maddie_5 flirty = Image("maddie_date_flirty.png")
    image maddie_5 normal = Image("maddie_date_normal.png")
    image maddie_5 happy = Image("maddie_date_happy.png")
    image maddie_5 angry = Image("maddie_date_angry.png")
    image maddie_5 sad = Image("maddie_date_sad.png")
    image maddie_5 embarrassed = Image("maddie_date_embarrassed.png")

    # maddie outfit 1
    image maddie_1 uncomf = Image("maddie_1_uncomf.png")
    image maddie_1 flirty = Image("maddie_1_flirty.png")
    image maddie_1 normal = Image("maddie_1_normal.png")
    image maddie_1 happy = Image("maddie_1_happy.png")
    image maddie_1 angry = Image("maddie_1_angry.png")
    image maddie_1 sad = Image("maddie_1_sad.png")
    image maddie_1 embarrassed = Image("maddie_1_embarrassed.png")

    # maddie outfit 2
    image maddie_2 uncomf = Image("maddie_2_uncomf.png")
    image maddie_2 flirty = Image("maddie_2_flirty.png")
    image maddie_2 normal = Image("maddie_2_normal.png")
    image maddie_2 happy = Image("maddie_2_happy.png")
    image maddie_2 angry = Image("maddie_2_angry.png")
    image maddie_2 sad = Image("maddie_2_sad.png")
    image maddie_2 embarrassed = Image("maddie_2_embarrassed.png")

    # maddie outfit 3
    image maddie_3 uncomf = Image("maddie_3_uncomf.png")
    image maddie_3 flirty = Image("maddie_3_flirty.png")
    image maddie_3 normal = Image("maddie_3_normal.png")
    image maddie_3 happy = Image("maddie_3_happy.png")
    image maddie_3 angry = Image("maddie_3_angry.png")
    image maddie_3 sad = Image("maddie_3_sad.png")
    image maddie_3 embarrassed = Image("maddie_3_embarrassed.png")

    # maddie outfit 4
    image maddie_4 uncomf = Image("maddie_4_uncomf.png")
    image maddie_4 flirty = Image("maddie_4_flirty.png")
    image maddie_4 normal = Image("maddie_4_normal.png")
    image maddie_4 happy = Image("maddie_4_happy.png")
    image maddie_4 angry = Image("maddie_4_angry.png")
    image maddie_4 sad = Image("maddie_4_sad.png")
    image maddie_4 embarrassed = Image("maddie_4_embarrassed.png")

    # anna date outfit
    image anna_5 uncomf = Image("anna (33).png")
    image anna_5 flirty = Image("anna (34).png")
    image anna_5 normal = Image("anna (35).png")
    image anna_5 happy = Image("anna (36).png")
    image anna_5 angry = Image("anna (37).png")
    image anna_5 sad = Image("anna (38).png")
    image anna_5 embarrassed = Image("anna (39).png")
    image anna_5 embarrassed2 = Image("anna (40).png")

    # anna outfit 1
    image anna_4 uncomf = Image("anna (25).png")
    image anna_4 flirty = Image("anna (26).png")
    image anna_4 normal = Image("anna (27).png")
    image anna_4 happy = Image("anna (28).png")
    image anna_4 angry = Image("anna (29).png")
    image anna_4 sad = Image("anna (30).png")
    image anna_4 embarrassed = Image("anna (31).png")
    image anna_4 embarrassed2 = Image("anna (32).png")

    # anna outfit 2
    image anna_3 uncomf = Image("anna (17).png")
    image anna_3 flirty = Image("anna (18).png")
    image anna_3 normal = Image("anna (19).png")
    image anna_3 happy = Image("anna (20).png")
    image anna_3 angry = Image("anna (21).png")
    image anna_3 sad = Image("anna (22).png")
    image anna_3 embarrassed = Image("anna (23).png")
    image anna_3 embarrassed2 = Image("anna (24).png")

    # anna outfit 3
    image anna_1 uncomf = Image("anna (9).png") #wrong
    image anna_1 flirty = Image("anna (10).png") 
    image anna_1 normal = Image("anna (11).png") #wrong
    image anna_1 happy = Image("anna (12).png")
    image anna_1 angry = Image("anna (13).png")
    image anna_1 sad = Image("anna (14).png")
    image anna_1 embarrassed = Image("anna (15).png")
    image anna_1 embarrassed2 = Image("anna (16).png")

    # anna outfit 4
    image anna_2 uncomf = Image("anna (1).png")
    image anna_2 flirty = Image("anna (2).png")
    image anna_2 normal = Image("anna (3).png")
    image anna_2 happy = Image("anna (4).png")
    image anna_2 angry = Image("anna (5).png")
    image anna_2 sad = Image("anna (6).png")
    image anna_2 embarrassed = Image("anna (7).png")
    image anna_2 embarrassed2 = Image("anna (8).png")

    # erin date outfit
    image erin_5 uncomf = Image("erin (9).png")
    image erin_5 flirty = Image("erin (10).png")
    image erin_5 normal = Image("erin (11).png")
    image erin_5 happy = Image("erin (12).png")
    image erin_5 angry = Image("erin (13)png")
    image erin_5 sad = Image("erin (14).png")
    image erin_5 embarrassed = Image("erin (15).png")
    image erin_5 surprised = Image("erin (16).png")

    # erin outfit 1
    image erin_1 uncomf = Image("erin (1).png")
    image erin_1 flirty = Image("erin (7).png")
    image erin_1 normal = Image("erin (2).png")
    image erin_1 happy = Image("erin (3).png")
    image erin_1 angry = Image("erin (4).png")
    image erin_1 sad = Image("erin (5).png")
    image erin_1 embarrassed = Image("erin (6).png")
    image erin_1 surprised = Image("erin (8).png")

    # erin outfit 2
    image erin_2 uncomf = Image("erin (26).png")
    image erin_2 flirty = Image("erin (27).png")
    image erin_2 normal = Image("erin (28).png")
    image erin_2 happy = Image("erin (29).png")
    image erin_2 angry = Image("erin (30).png")
    image erin_2 sad = Image("erin (31).png")
    image erin_2 embarrassed = Image("erin (32).png")
    image erin_2 surprised = Image("erin (33).png")

    # erin outfit 3
    image erin_3 uncomf = Image("erin (18).png")
    image erin_3 flirty = Image("erin (19).png")
    image erin_3 normal = Image("erin (20).png")
    image erin_3 happy = Image("erin (21).png")
    image erin_3 angry = Image("erin (22).png")
    image erin_3 sad = Image("erin (23).png")
    image erin_3 embarrassed = Image("erin (24).png")
    image erin_3 surprised = Image("erin (25).png")

    # erin outfit 3
    image erin_4 uncomf = Image("erin (34).png")
    image erin_4 flirty = Image("erin (35).png")
    image erin_4 normal = Image("erin (36).png")
    image erin_4 happy = Image("erin (37).png")
    image erin_4 angry = Image("erin (38).png")
    image erin_4 sad = Image("erin (39).png")
    image erin_4 embarrassed = Image("erin (40).png")
    image erin_4 surprised = Image("erin (41).png")    



# Points
default A = 0
default B = 0
default C = 0
default day = 0
default game_counter = 0
default gym_counter = 0
default lib_counter = 0
default art_counter = 0
default workout_counter = 0
default study_counter = 0
default arting_counter = 0
default avideo_counter = 0
default mvideo_counter = 0
default evideo_counter = 0
default i = 0
default j = 0
default k = 0
default ii = 0
default jj = 0
default kk = 0
default iii = 0
default jjj = 0
default kkk = 0
default special_A = 5
default special_B = 5
default special_C = 5
default grade = 0
default course_counter = 0
default temp = 0
default A_bad = 0
default A_low = 5
default A_mid = 10
default A_mid2 = 15
default A_mid3 = 20
default A_high = 25
default A_high2 = 30
default A_high3 = 35

default small_a_sent = False
default small_a_sent2 = False
default gn_a_sent2 = False
default gn_b_sent2 = False
default gn_c_sent2 = False
default a_ending = False 
default b_ending = False
default c_ending = False
default course_flag = False
default date_this_weekend = False
default believe_in_her = False
default special_C_on = False
default special_B_on = False
default date_b_sent = False
default hang_b_sent = False 
default date_c_sent = False
default hang_c_sent = False 
default date_a_sent = False
default hang_a_sent = False 
default video_a_sent = False 
default video_b_sent = False 
default video_c_sent = False 
default gn_b_sent = False 
default like_b_sent = False
default gn_a_sent = False 
default like_a_sent = False
default gn_c_sent = False 
default like_c_sent = False
default anna_hang_over = False 
default erin_hang_over = False
default maddie_hang_over = False
default maddie_date_over = False 
default erin_date_over = False 
default anna_date_over = False 
default gym_compliment = False 
default lib_compliment = False
default art_compliment = False
default bool_ch1_day1_getdressed = False
default bool_ch1_day1_talktonc = False 
default date = False
default eventaa_trigger = False
default eventab_trigger = False 
default eventac_trigger = False
default eventba_trigger = False
default eventbb_trigger = False 
default eventbc_trigger = False
default eventca_trigger = False
default eventcb_trigger = False 
default eventcc_trigger = False
default clean = False
default text_flag = False 
default body_flag = False 
default game_flag = False
default a_number_obtained_flag = False 
default b_number_obtained_flag = False 
default c_number_obtained_flag = False
default gym_choice_1_a = False 
default gym_choice_1_b = False 
default gym_choice_2_a = False 
default gym_choice_2_b = False 
default gym_choice_2_c = False 
default library_choice_1_a = False 
default library_choice_1_b = False 
default library_choice_2_a = False 
default library_choice_2_b = False 
default library_choice_2_c = False 
default art_choice_1_a = False 
default art_choice_1_b = False 
default art_choice_2_a = False 
default art_choice_2_b = False 
default art_choice_2_c = False 
default maddie_gift = False 
default anna_gift = False 
default erin_gift = False 
default art_comp = False
default lib_comp = False
default gym_comp = False
default erin = False
default anna = False
default maddie = False
default erin_confessed = False
default maddie_confessed = False
default anna_confessed = False
default a_ending_success = False
default b_ending_success = False
default c_ending_success = False
default d_ending_success = False

transform trueleft:
    xpos 300   
    ypos 150

transform trueright:
    xpos 1000
    ypos 150

init python:

    longfade = Fade(2.0, 1.0, 2.0)


    def custom_show(person, emotion):
        if day == 0:
            str_out = person + "_1 " + emotion
            return str_out
        else:
            if day == 1:
                str_out = person + "_2 " + emotion
                return str_out
            else:
                if day == 3:
                    str_out = person + "_3 " + emotion
                    return str_out
                else:
                    if day == 4:
                        str_out = person + "_4 " + emotion
                        return str_out
                    else: 
                        if day == 10:
                            str_out = person + "_5 " + emotion
                            return str_out
                        else: 
                            str_out = person + "_1 " + emotion
                            return str_out


    def custom_hide(person):
        if day == 0:
            str_out = person + "_1 " 
            return str_out
        else:
            if day == 1:
                str_out = person + "_2 " 
                return str_out
            else:
                if day == 3:
                    str_out = person + "_3 " 
                    return str_out
                else:
                    if day == 4:
                        str_out = person + "_4 "
                        return str_out
                    else: 
                        if day == 10:
                            str_out = person + "_5 " 
                            return str_out
                        else:
                            str_out = person + "_1 " 
                            return str_out


label start:
    jump chapter01