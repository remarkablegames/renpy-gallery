# Gallery Configuration
# https://www.renpy.org/doc/html/rooms.html


default persistent.unlock_with_password = False


init python:
    g = Gallery()

    # The default displayable used by make_button for a locked button.
    g.locked_button = "lock" # game/images/lock.png

    # A button that contains an image that automatically unlocks.
    g.button("bg_club")
    g.image("bg club")
    g.unlock("bg club")

    # This button has multiple images associated with it. We use unlock_image
    # so we don't have to call both .image and .unlock. We also apply a
    # transform to the first image.
    g.button("bg_school")
    g.unlock_image("bg lecturehall")
    g.transform(fade)
    g.unlock_image("bg uni")

    # A button with an image that is always unlocked.
    g.button("bg_meadow")
    g.image("bg meadow")

    # Eileen
    g.button("eileen_concerned")
    g.unlock_image("eileen concerned")

    g.button("eileen_happy")
    g.unlock_image("eileen happy")

    g.button("eileen_vhappy")
    g.unlock_image("eileen vhappy")

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("lucy")
    g.condition("persistent.unlock_lucy")
    g.image("lucy happy")
    g.image("lucy mad")

    # The final two buttons contain images that show multiple pictures
    # at the same time. This can be used to compose character art onto
    # a background.
    g.button("sylvie_blue")
    g.condition("True")
    g.image("bg uni", "sylvie blue normal")
    g.image("bg uni", "sylvie blue smile")
    g.image("bg uni", "sylvie blue giggle")
    g.image("bg uni", "sylvie blue surprised")

    # This is gated behind a password. Use image (not unlock_image) so the
    # images don't also require having been seen in-game.
    g.button("sylvie_green")
    g.condition("persistent.unlock_with_password")
    g.image("bg lecturehall", "sylvie green normal")
    g.image("bg lecturehall", "sylvie green smile")
    g.image("bg lecturehall", "sylvie green giggle")
    g.image("bg lecturehall", "sylvie green surprised")

    # The transition used when switching images.
    g.transition = dissolve


init python:
    def unlock_gallery_image_with_password():
        entered = renpy.invoke_in_new_context(
            renpy.input,
            "Enter the password to unlock Sylvie Green:",
            mask="*",
            _clear_layers=False,
        )

        if entered == "password":
            persistent.unlock_with_password = True
            renpy.save_persistent()
            renpy.restart_interaction()
        else:
            renpy.notify("Wrong password.")
