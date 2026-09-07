label start:

    scene bg club

    # Show expressions will automatically unlock gallery images.
    show eileen happy

    e "Welcome to Ren'Py gallery!"

    e concerned "I'm feeling a bit concerned about the gallery implementation."

    e vhappy "But now I'm very happy that it's working!"

    menu:
        "Unlock Lucy gallery":
            $ persistent.unlock_lucy = True
            $ renpy.save_persistent()

            e "Lucy's gallery has been unlocked!"

        "Lock Lucy gallery":
            $ persistent.unlock_lucy = False # persistent._clear()
            $ renpy.save_persistent()

            e "Lucy's gallery has been locked!"

    jump end
