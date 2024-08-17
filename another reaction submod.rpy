# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="Goge",
        name="Another Reaction Submod",
        description="Just another submod that gives Monika more Window Reactions, mainly focused on games",
        version="1.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        "another_reaction_submod_v1_0": "another_reaction_submod_v1_0",
        }
    )

#Mod Itself
init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_persona3reload",
            category=["P3R"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_persona3reload:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Persona!",
            "Let’s Burn our Dreads, shall we [player]?",
            "I am thou, thou art I"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_persona3reload')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_persona4",
            category=["Persona4 GOLDEN"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_persona4:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Persona!",
            "I am thou, thou art I"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_persona4')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_warframe",
            category=["Warframe"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_warframe:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Say hi to Ordis for me",
            "Happy Hunting!",
            "Wake up, [player]"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_warframe')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_eldenring",
            category=["ELDEN RING"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_eldenring:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Rise, [player]"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_eldenring')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_hollowknight",
            category=["Hollow Knight"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_hollowknight:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "No mind to think, No will to break, No voice to cry suffering...",
            "Such an eerie atmosphere..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_hollowknight')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_omori",
            category=["OMORI"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_omori:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Everything is going to be okay",
            "Just know that I’m here if you want to cry, [player]"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_omori')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_balatro",
            category=["Balatro"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_balatro:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "I wish we had something like that in here..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_balatro')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ultrakill",
            category=["ULTRAKILL"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ultrakill:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "So much blood...",
            "Good luck with that P rank!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ultrakill')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fearandhunger",
            category=["Fear & Hunger|Fear & Hunger 2: TERMINA"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fearandhunger:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "I REALLY don’t like this one..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fearandhunger')
    return
