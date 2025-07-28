default evidence_list = []

init python:
    class Evidence:
        def __init__(self, name, description, image=None):
            self.name = name
            self.description = description
            self.image = image

# Example evidence
init:
    $ bloody_dagger = Evidence("Bloody Dagger", "A ceremonial blade with fresh blood.", "evidence/dagger.png")
    $ sealed_letter = Evidence("Sealed Letter", "Found on the victim, addressed to the Cleric.")

label add_evidence(e):
    if e not in evidence_list:
        $ evidence_list.append(e)
        "You obtained [e.name]."
    return
