label trial_cross_examination:
    "Cleric: I never saw the dagger before!"
    
    menu:
        "Choose your action"
        "Press":
            "You press the Cleric for details."
            jump trial_cross_examination
        "Present Evidence":
            jump present_menu

label present_menu:
    call screen evidence_menu
    $ selected = _return
    if selected == bloody_dagger:
        "You present the Bloody Dagger!"
        "Truthbinder: Then explain why your fingerprints are on it?"
        jump trial_success
    else:
        "This evidence doesn't help here."
        jump trial_cross_examination

label trial_success:
    "Cleric: ...Fine. I lied."
    return
