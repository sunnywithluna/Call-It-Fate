label chapter01:
    scene bg_room with fade
    play music "audio/dorm.mp3"

    "It's the first day of my summer session class, and I'm only now looking at the syllabus."
    "My professor sent it a few weeks back before the spring semester had ended, but now is the first time I'm realizing what three months of work looks like crammed into three weeks."
    "This is going to suck."
    "I'm sitting in my dorm that has the distinct smell only dingy laundry in a poorly room could cause."
    "The place is a mess. The bed isn't made, the trash is overflowing, and the only cared-for items in the room are my GS5 and desktop."
    "Well, no time to clean now. I better get to class."
    jump ch1_day1
    return 

label ch1_day1:
    "What should I do before I go?"
    menu:
        "Get dressed." if not bool_ch1_day1_getdressed:
            jump ch1_day1_getdressed
        "Talk to Neko-Chan." if not bool_ch1_day1_talktonc:
            jump ch1_day1_talktonc
        "Head out." if bool_ch1_day1_getdressed:
            show neko
            nc "\"...\""
            stop music fadeout 1.0
            scene black with longfade

            jump ch1_schoolday1
    return

label ch1_day1_getdressed:

    "What should I wear?"
    $ bool_ch1_day1_getdressed = True

    menu:
        "Sleek hoodie with joggers and white sneakers":
            "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
            $ A = A + 1
        "Short-sleeved button down shirt with cuffed jeans and loafers":
            "I wish I was sophisticated enough to pull off this look."
            $ B = B + 1
        "Bold colorblock shirt tucked into tapered pants and boots":
            "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
            $ C = C + 1
        "Neko-Chan graphic tee with sweatpants and sandals":
            jump ch1_day1
    jump ch1_day1
    return

label ch1_day1_talktonc:
    show neko
    "What should I talk to Neko-Chan about?"
    $ bool_ch1_day1_talktonc = True

    menu: 
        "Confide in Neko-Chan.":
            jump ch1_day1_confidenc
        "Say goodbye to Neko-Chan.": 
            jump ch1_day1_goodbyenc
    return

label ch1_day1_confidenc:
    
    n "\"Hey, Neko-Chan. I'm kind of nervous about this class.\""
    n "\"It seems like a lot of work, and I don't know if I can handle it all.\""
    n "\"This is going to be a rough few weeks, isn't it?\""
    nc "\"...\""
    n "\"The only thing that could make this class even slightly bearable would be meeting a cute girl, but we both know how unlikely that is.\""
    n "\"Not that I'd ever be able to find a girl better than you, Neko-Chan.\""
    n "\"You were drawn with proportions real women need surgery to achieve.\""
    nc "\"...\""
    hide neko

    menu:
        "Get dressed." if not bool_ch1_day1_getdressed:
            "What should I wear?"
            $ bool_ch1_day1_getdressed = True

            menu:
                "Sleek hoodie with joggers and white sneakers":
                    "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
                    $ A = A + 1
                    jump whoops_edit
                "Short-sleeved button down shirt with cuffed jeans and loafers":
                    "I wish I was sophisticated enough to pull off this look."
                    $ B = B + 1
                    jump whoops_edit
                "Bold colorblock shirt tucked into tapered pants and boots":
                    "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
                    $ C = C + 1
                    jump whoops_edit
                "Neko-Chan graphic tee with sweatpants and sandals":
                    jump whoops_edit
        "Say goodbye to Neko-Chan." if bool_ch1_day1_getdressed:
            jump ch1_day1_goodbyenc
        "Head out." if bool_ch1_day1_getdressed:
            show neko
            nc "\"...\""

            stop music fadeout 1.0
            scene black with longfade

            jump ch1_schoolday1
    return

label whoops_edit:
    menu:
        "Say goodbye to Neko-Chan." if bool_ch1_day1_getdressed:
            jump ch1_day1_goodbyenc
        "Head out." if bool_ch1_day1_getdressed:
            show neko
            nc "\"...\""

            stop music fadeout 1.0
            scene black with longfade

            jump ch1_schoolday1

label ch1_day1_goodbyenc:

    if not bool_ch1_day1_getdressed:
        "I should get dressed first..."
        "What should I wear?"
        $ bool_ch1_day1_getdressed = True

        menu:
            "Sleek hoodie with joggers and white sneakers":
                "I bought these when I thought I'd start working out. It's ironic how well these clothes hide my lack of muscle definition."
                $ A = A + 1
                jump whoop2_edit
            "Short-sleeved button down shirt with cuffed jeans and loafers":
                "I wish I was sophisticated enough to pull off this look."
                $ B = B + 1
                jump whoop2_edit
            "Bold colorblock shirt tucked into tapered pants and boots":
                "I've always admired really expressive outfits, but I've never been brave enough to actually wear this before now."
                $ C = C + 1
                jump whoop2_edit
            "Neko-Chan graphic tee with sweatpants and sandals":
                "There's nothing like being comfortable. Now if only I could find my fedora, that would really complete this outfit."
                jump whoop2_edit
    else:
        show neko
        n "\"Well, I better get going. Wish me luck, Neko-Chan!\""
        nc "\"...\""

        stop music fadeout 1.0
        scene black with longfade
        jump ch1_schoolday1
    stop music fadeout 1.0
    hide neko
    return 

label whoop2_edit:
    show neko
    n "\"Well, I better get going. Wish me luck, Neko-Chan!\""
    nc "\"...\""

    stop music fadeout 1.0
    scene black with longfade
    jump ch1_schoolday1