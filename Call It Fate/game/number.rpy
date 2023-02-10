label a_number:
    $renpy.show(custom_show("maddie", "normal"), [])

    $a_number_flag = True
    n "\"Hey, Maddie, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if A >= A_low:
        $renpy.show(custom_show("maddie", "flirty"), [])        
        a "\"Or something?\""
        n "\"I didn't mean--\""
        $renpy.show(custom_show("maddie", "happy"), [])
        a "\"Haha, I'm just teasing. I think that's a great idea.\""
        "We exchange phone numbers."
        $a_number_obtained_flag = True
        jump talking_to_maddie
    else:
        $renpy.show(custom_show("maddie", "uncomf"), [])        
        a "\"Or something?\""
        n "\"I didn't mean--\""
        $renpy.show(custom_show("maddie", "angry"), [])
        a "\"Listen, I know what you're trying to do. I'm not interested, okay?\""
        jump talking_to_maddie
        
label b_number:
    $b_number_flag = True
    n "\"Hey, Anna, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if B >= 1:
        $renpy.show(custom_show("anna", "happy"), [])
        b "\"Good thinking.\""
        "We exchange phone numbers."
        $b_number_obtained_flag = 1
        jump talking_to_anna
    else:
        $renpy.show(custom_show("anna", "angry"), [])
        b "\"I won't need help.\""
        jump talking_to_anna
    return

label c_number:
    $c_number_flag = True
    n "\"Hey, Erin, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\""
    if C >= 1:
        $renpy.show(custom_show("erin", "normal"), [])
        c "\"Yeah okay! I could probably use the help.\""
        "We exchange phone numbers."
        $c_number_obtained_flag = 1
        jump talking_to_erin
    else:
        $renpy.show(custom_show("erin", "uncomf"), [])
        c "\"Oh, sorry. I don't really give my number out...\""
        jump talking_to_erin
    return 