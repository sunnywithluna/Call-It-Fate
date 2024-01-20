
label a_number:
    $ renpy.show(custom_show("maddie", "N"), [])

    $ numberFlagA = True
    n "\'Hey, Maddie, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if A >= A_low:
        $ renpy.show(custom_show("maddie", "F"), [])        
        a "\'Or something?\'"
        n "\'I didn't mean--\'"
        $ renpy.show(custom_show("maddie", "H"), [])
        a "\'Haha, I'm just teasing. I think that's a great idea.\'"
        "We exchange phone numbers."
        $ phoneFlagA = True
        jump talking_to_maddie
    else:
        $ renpy.show(custom_show("maddie", "U"), [])        
        a "\'Or something?\'"
        n "\'I didn't mean--\'"
        $ renpy.show(custom_show("maddie", "A"), [])
        a "\'Listen, I know what you're trying to do. I'm not interested, okay?\'"
        jump talking_to_maddie
        

label b_number:
    $ numberFlagB = True
    n "\'Hey, Anna, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if B >= 1:
        $ renpy.show(custom_show("anna", "H"), [])
        b "\'Good thinking.\'"
        "We exchange phone numbers."
        $ phoneFlagB = 1
        jump talking_to_anna
    else:
        $ renpy.show(custom_show("anna", "A"), [])
        b "\'I won't need help.\'"
        jump talking_to_anna
    return


label c_number:
    $ numberFlagC = True
    n "\'Hey, Erin, we should exchange numbers. You know, in case either of us needs help with a Philosophy assignment or something.\'"
    if C >= 1:
        $ renpy.show(custom_show("erin", "N"), [])
        c "\'Yeah okay! I could probably use the help.\'"
        "We exchange phone numbers."
        $ phoneFlagC = 1
        jump talking_to_erin
    else:
        $ renpy.show(custom_show("erin", "U"), [])
        c "\'Oh, sorry. I don't really give my number out...\'"
        jump talking_to_erin
    return 