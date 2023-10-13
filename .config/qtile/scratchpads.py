from libqtile.config import ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from defaults import terminal

scratchpad_groups = [
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "khal",
                terminal + " -t ikhal -e ikhal",
                x=0.695,
                width=0.3,
                height=0.3,
                opacity=1,
            ),
            DropDown(
                "mixer",
                "pavucontrol",
                x=0.3,
                y=0.1,
                width=0.4,
                height=0.6,
                opacity=0.9,
            ),
            DropDown(
                "colorpick", "gpick", x=0.4, y=0.1, width=0.4, height=0.6, opacity=1, on_focus_lost_hide=False
            ),
        ],
    ),
]

scratchpad_keys = [
    Key(
        ["control"],
        "1",
        lazy.group["scratchpad"].dropdown_toggle("mixer"),
        desc="Launch volume mixer scratchpad",
    ),
    Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("colorpick")),
]
