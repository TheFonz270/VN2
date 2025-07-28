# The script of the game goes in this file.


# The game starts here.

define config.keymap['evidence'] = [ 'e' ]

label start:

    scene bg room
    with fade

    "Welcome to your grimdark court test."

    "You will first collect evidence, then present it during a trial."

    jump investigation_hub

label trial_scene:

    scene bg room
    with dissolve

    "Cleric: I swear I never saw that dagger before in my life!"

    menu:
        "Choose your action"
        "Press for details":
            "Truthbinder: Are you certain? Your hesitation betrays you."
            jump trial_scene

        "Present Evidence":
            call screen evidence_menu
            $ selected = _return

            if selected == bloody_dagger:
                "You slam the Bloody Dagger on the altar!"

                "Truthbinder: Then explain why your fingerprints are on it?!"

                "Cleric: ...No... it can’t be..."

                jump ex_trial_success

            elif selected == sealed_letter:
                "Truthbinder: This letter... explains nothing relevant here."
                "Try something else."
                jump trial_scene

            else:
                "You fumble with irrelevant parchment."
                jump trial_scene

label ex_trial_success:

    "Cleric: ...Fine. I lied. I used the blade in the ritual. But I had no choice!"

    "You’ve proven a contradiction in the Cleric's testimony."

    "Trial complete."

    return
