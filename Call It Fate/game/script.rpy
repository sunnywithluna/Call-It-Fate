define a = Character('Maddie', who_color = '#104010')
define b = Character('Anna', who_color = '#104010')
define c = Character('Erin', who_color = '#104010')
define nc = Character('Neko-Chan', who_color = '#104010')
define p = Character('Dr. Paige', who_color = '#104010')
define n = Character('Sam', who_color = '#104010') 

# persistent data, gallery and main menu
define persistent.endingAFlag = False
define persistent.endingBFlag = False
define persistent.endingCFlag = False
define persistent.titleScreenCounter = 0

init:
    image neko = Image('emote_neko_11.png')
    image jennifer = Image('emote_jenn_11.PNG')    
    image jennifer2 = Image('emote_jenn_12.PNG')    
    
    #  maddie date outfit
    image maddie_5 A = Image('emote_maddie_51.png')
    image maddie_5 E = Image('emote_maddie_52.png')
    image maddie_5 F = Image('emote_maddie_53.png')
    image maddie_5 H = Image('emote_maddie_54.png')
    image maddie_5 N = Image('emote_maddie_55.png')
    image maddie_5 S = Image('emote_maddie_56.png')
    image maddie_5 U = Image('emote_maddie_57.png')

    #  maddie outfit 1
    image maddie_1 A = Image('emote_maddie_11.png')
    image maddie_1 E = Image('emote_maddie_12.png')
    image maddie_1 F = Image('emote_maddie_13.png')
    image maddie_1 H = Image('emote_maddie_14.png')
    image maddie_1 N = Image('emote_maddie_15.png')
    image maddie_1 S = Image('emote_maddie_16.png')
    image maddie_1 U = Image('emote_maddie_17.png')

    #  maddie outfit 2
    image maddie_2 A = Image('emote_maddie_21.png')
    image maddie_2 E = Image('emote_maddie_22.png')
    image maddie_2 F = Image('emote_maddie_23.png')
    image maddie_2 H = Image('emote_maddie_24.png')
    image maddie_2 N = Image('emote_maddie_25.png')
    image maddie_2 S = Image('emote_maddie_26.png')
    image maddie_2 U = Image('emote_maddie_27.png')

    #  maddie outfit 3
    image maddie_3 A = Image('emote_maddie_31.png')
    image maddie_3 E = Image('emote_maddie_32.png')
    image maddie_3 F = Image('emote_maddie_33.png')
    image maddie_3 H = Image('emote_maddie_34.png')
    image maddie_3 N = Image('emote_maddie_35.png')
    image maddie_3 S = Image('emote_maddie_36.png')
    image maddie_3 U = Image('emote_maddie_37.png')

    #  maddie outfit 4
    image maddie_4 A = Image('emote_maddie_41.png')
    image maddie_4 E = Image('emote_maddie_42.png')
    image maddie_4 F = Image('emote_maddie_43.png')
    image maddie_4 H = Image('emote_maddie_44.png')
    image maddie_4 N = Image('emote_maddie_45.png')
    image maddie_4 S = Image('emote_maddie_46.png')
    image maddie_4 U = Image('emote_maddie_47.png')

    #  anna date outfit
    image anna_5 U = Image('emote_anna_31.png')
    image anna_5 F = Image('emote_anna_32.png')
    image anna_5 N = Image('emote_anna_33.png')
    image anna_5 N2 = Image('emote_anna_34.png')
    image anna_5 H = Image('emote_anna_35.png')
    image anna_5 A = Image('emote_anna_36.png')
    image anna_5 E = Image('emote_anna_37.png')
    image anna_5 E2 = Image('emote_anna_38.png')

    #  anna outfit 1
    image anna_1 U = Image('emote_anna_11.png')
    image anna_1 F = Image('emote_anna_12.png')
    image anna_1 N = Image('emote_anna_13.png')
    image anna_1 N2 = Image('emote_anna_14.png')
    image anna_1 H = Image('emote_anna_15.png')
    image anna_1 A = Image('emote_anna_16.png')
    image anna_1 E = Image('emote_anna_17.png')
    image anna_1 E2 = Image('emote_anna_18.png')

    #  anna outfit 2
    image anna_2 U = Image('emote_anna_21.png')
    image anna_2 F = Image('emote_anna_22.png')
    image anna_2 N = Image('emote_anna_23.png')
    image anna_2 N2 = Image('emote_anna_24.png')
    image anna_2 H = Image('emote_anna_25.png')
    image anna_2 A = Image('emote_anna_26.png')
    image anna_2 E = Image('emote_anna_27.png')
    image anna_2 E2 = Image('emote_anna_28.png')

    #  anna outfit 3
    image anna_3 U = Image('emote_anna_11b.png')
    image anna_3 F = Image('emote_anna_12b.png')
    image anna_3 N = Image('emote_anna_13b.png')
    image anna_3 N2 = Image('emote_anna_14b.png')
    image anna_3 H = Image('emote_anna_15b.png')
    image anna_3 A = Image('emote_anna_16b.png')
    image anna_3 E = Image('emote_anna_17b.png')
    image anna_3 E2 = Image('emote_anna_18b.png')

    #  anna outfit 4
    image anna_4 U = Image('emote_anna_21b.png')
    image anna_4 F = Image('emote_anna_22b.png')
    image anna_4 N = Image('emote_anna_23b.png')
    image anna_4 N2 = Image('emote_anna_24b.png')
    image anna_4 H = Image('emote_anna_25b.png')
    image anna_4 A = Image('emote_anna_26b.png')
    image anna_4 E = Image('emote_anna_27b.png')
    image anna_4 E2 = Image('emote_anna_28b.png')

    #  erin date outfit
    image erin_5 U = Image('emote_erin_51.png')
    image erin_5 N = Image('emote_erin_52.png')
    image erin_5 H = Image('emote_erin_53.png')
    image erin_5 A = Image('emote_erin_54.png')
    image erin_5 S = Image('emote_erin_55.png')
    image erin_5 E = Image('emote_erin_56.png')
    image erin_5 F = Image('emote_erin_57.png')
    image erin_5 W = Image('emote_erin_58.png')

    #  erin outfit 1
    image erin_1 U = Image('emote_erin_11.png')
    image erin_1 N = Image('emote_erin_12.png')
    image erin_1 H = Image('emote_erin_13.png')
    image erin_1 A = Image('emote_erin_14.png')
    image erin_1 S = Image('emote_erin_15.png')
    image erin_1 E = Image('emote_erin_16.png')
    image erin_1 F = Image('emote_erin_17.png')
    image erin_1 W = Image('emote_erin_18.png')

    #  erin outfit 2
    image erin_2 U = Image('emote_erin_21.png')
    image erin_2 N = Image('emote_erin_22.png')
    image erin_2 H = Image('emote_erin_23.png')
    image erin_2 A = Image('emote_erin_24.png')
    image erin_2 S = Image('emote_erin_25.png')
    image erin_2 E = Image('emote_erin_26.png')
    image erin_2 F = Image('emote_erin_27.png')
    image erin_2 W = Image('emote_erin_28.png')

    #  erin outfit 3
    image erin_3 U = Image('emote_erin_31.png')
    image erin_3 N = Image('emote_erin_32.png')
    image erin_3 H = Image('emote_erin_33.png')
    image erin_3 A = Image('emote_erin_34.png')
    image erin_3 S = Image('emote_erin_35.png')
    image erin_3 E = Image('emote_erin_36.png')
    image erin_3 F = Image('emote_erin_37.png')
    image erin_3 W = Image('emote_erin_38.png')

    #  erin outfit 4
    image erin_4 U = Image('emote_erin_41.png')
    image erin_4 N = Image('emote_erin_42.png')
    image erin_4 H = Image('emote_erin_43.png')
    image erin_4 A = Image('emote_erin_44.png')
    image erin_4 S = Image('emote_erin_45.png')
    image erin_4 E = Image('emote_erin_46.png')
    image erin_4 F = Image('emote_erin_47.png')
    image erin_4 W = Image('emote_erin_48.png')

#  Points
default A = 0
default B = 0
default C = 0
default day_counter = 1
default end_of_act_menu1_flag2_counter = 0
default gym_counter = 0
default lib_counter = 0
default art_counter = 0
default workout_counter = 0
default study_counter = 0
default arting_counter = 0
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
default class_score = 0
default end_of_act_menu1_flag1_counter = 0
default temp = 0
# default A_bad = 0
# default A_low = 5
# default A_mid = 10
# default A_mid2 = 15
# default A_mid3 = 20
# default A_high = 25
# default A_high2 = 30
# default A_high3 = 35
default A_bad = 0
default A_low = 6
default A_mid = 11
default A_mid2 = 13
default A_mid3 = 18
default A_high = 20
default A_high2 = 25
default A_high3 = 35
default B_bad = 0
default B_low = 5
default B_mid = 10
default B_mid2 = 15
default B_mid3 = 20
default B_high = 25
default B_high2 = 30
default B_high3 = 35
default C_bad = 0
default C_low = 5
default C_mid = 10
default C_mid2 = 15
default C_mid3 = 20
default C_high = 25
default C_high2 = 30
default C_high3 = 35
default neko_counter = 0
default calendar_days_skipped = 0
# DELETE default love_points = 'K'
# DELETE default love_interest = 'Kim'

default smallTalkFlagA = False
default smallTalkFlagB = False
default smallTalkFlagC = False
default gnSentA = False
default gnSentB = False
default gnSentC = False
default endingAFlag_Attempt = False 
default endingBFlag_Attempt = False
default endingCFlag_Attempt = False
default end_of_act_menu1_flag1 = False
default weekendDateFlag = False
default believe_in_her = False
default special_C_on = False
default special_B_on = False
default dateSentFlagB = False
default hangSentFlagB = False 
default dateSentFlagC = False
default hangSentFlagC = False 
default dateSentFlagA = False
default hangSentFlagA = False 
default videoSentA = False 
default videoSentB = False 
default videoSentC = False 
default eventBHangCompletedFlag = False 
default eventCHangCompletedFlag = False
default eventAHangCompletedFlag = False
default eventADateCompletedFlag = False 
default eventCDateCompletedFlag = False 
default eventBDateCompletedFlag = False 
default gym_compliment = False 
default lib_compliment = False
default art_compliment = False
default act1_scene0_menu1_option1 = False
default act1_scene0_menu1_option2 = False 
default eventAHangFlag = False
default eventBHangFlag = False 
default eventCHangFlag = False
default eventADateFlag = False
default eventBDateFlag = False 
default eventCDateFlag = False
default eventca_trigger = False
default eventcb_trigger = False 
default eventcc_trigger = False
default clean = False
default end_of_act_menu1_flag4 = False 
default end_of_act_menu1_flag3 = False 
default end_of_act_menu1_flag2 = False
default phoneFlagA = False 
default phoneFlagB = False 
default phoneFlagC = False
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
default confessedFlagC = False
default confessedFlagA = False
default confessedFlagB = False
default endingAFlag = False
default endingBFlag = False
default endingCFlag = False
default nekochan = False
default confide_nc = False
default maddie_unlocked = False
default erin_unlocked = False
default anna_unlocked = False
default fluffy = False
default temp_usage = False
default eventAHangToday = False
default eventBHangToday = False 
default eventCHangToday = False

transform trueleft:
    xpos 300   
    ypos 150

transform trueright:
    xpos 1000
    ypos 150

define longfade = Fade(2.0, 1.0, 2.0)

init python:

    def custom_show(person, emotion):
        if day_counter == 1:
            str_out = person + '_1 ' + emotion
            return str_out
        elif day_counter == 2:
            str_out = person + '_2 ' + emotion
            return str_out
        elif day_counter == 3:
            str_out = person + '_3 ' + emotion
            return str_out
        elif day_counter == 4:
            str_out = person + '_4 ' + emotion
            return str_out
        elif day_counter == 10:
            str_out = person + '_5 ' + emotion
            return str_out
        else: 
            str_out = person + '_1 ' + emotion
            return str_out


    def custom_hide(person):
        if day_counter == 1:
            str_out = person + '_1 '
            return str_out
        elif day_counter == 2:
            str_out = person + '_2 '
            return str_out
        elif day_counter == 3:
            str_out = person + '_3 '
            return str_out
        elif day_counter == 4:
            str_out = person + '_4 '
            return str_out
        elif day_counter == 10:
            str_out = person + '_5 '
            return str_out
        else: 
            str_out = person + '_1 '
            return str_out


label splashscreen:

    play music 'audio/end.mp3' fadein 1.0

    scene black
    with Pause(1)

    show intro_0 with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    show intro_1 with dissolve
    with Pause(1)

    show intro_2 with dissolve
    with Pause(1)

    show intro_3 with dissolve
    with Pause(1)

    show intro_4 with dissolve
    with Pause(1)

    scene black with dissolve
    with Pause(1)

    return


label start:
    jump act1_scene0