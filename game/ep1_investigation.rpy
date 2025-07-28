label investigation_hub:
    scene map
    menu:
        "Where to investigate?"
        "Gallowswood Chapel":
            jump chapel
        "Mortuary":
            jump mortuary
        "Back to Town Square":
            jump town_square
        "gallowswood":
            jump gallowswood_entry

label chapel:
    scene chapel
    "You enter a shadowy room with blood on the walls."

    "Something glints beneath a pile of rags."

    $ bloody_dagger = Evidence("Bloody Dagger", "A ceremonial blade with fresh blood.", "evidence/dagger.png")
    $ sealed_letter = Evidence("Sealed Letter", "Found on the victim, addressed to the Cleric.")
    
    call add_evidence(bloody_dagger)
    call add_evidence(sealed_letter)

    "You now have two pieces of evidence."

    "Press 'E' at any time to open your evidence menu."

    "Proceeding to trial..."

    jump trial_scene

label mortuary:
    scene mortuary
    "Hmm... Not much here..."
    jump investigation_hub

label town_square:
    scene townSquare
    "Hmm... Not much here..."
    jump investigation_hub

label examine_gallowswood:
    hide screen location_menu
    "You examine the twisted trees and the blood-soaked noose."
    call add_evidence(bloody_dagger)
    jump gallowswood_entry

label talk_gallowswood:
    hide screen location_menu
    "You speak with the nervous cleric pacing near the altar."
    jump gallowswood_entry

label move_from_gallowswood:
    hide screen location_menu
    menu:
        "Where will you go?"
        "Town Square":
            jump town_square
        "Stay here":
            jump gallowswood_entry

label gallowswood_entry:
    scene bg gallowswood
    "You arrive at the desolate Gallowswood."

    show screen location_menu("Gallowswood",
        examine_callback="examine_gallowswood",
        talk_callback="talk_gallowswood",
        move_callback="move_from_gallowswood"
    )

    # Keep player here until they choose to move
    $ renpy.pause(hard=True)
