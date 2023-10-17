from libqtile.config import ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from defaults import terminal, editor

# Notes file modification
from datetime import date

current_date = str(date.today())

location = "/home/matija/Sync/'Obsidian Vault'/'Daily Notes/'"
file_name = "notes" + "-" + current_date
file_extension = ".md"

scratchpad_groups = [
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "khal",
                terminal + " -t ikhal -e ikhal",
                x=0.695,
                width=0.3,
                height=0.5,
                opacity=1,
            ),
            DropDown(
                "task_manager",
                terminal + " -t htop -e htop",
                x=0.595,
                width=0.4,
                height=0.6,
                opacity=1,
            ),
            DropDown(
                "notes",
                terminal
                + " -e "
                + editor
                + " "
                + location
                + file_name
                + file_extension,
                x=0.595,
                width=0.4,
                height=0.6,
                opacity=0.8,
            ),
            DropDown(
                "mixer",
                "pavucontrol",
                x=0.695,
                # y=0.1,
                width=0.3,
                height=0.4,
                opacity=0.8,
            ),
            DropDown(
                "colorpick",
                "gpick",
                x=0.4,
                y=0.1,
                width=0.4,
                height=0.6,
                opacity=1,
                on_focus_lost_hide=False,
            ),
            DropDown(
                "notifications",
                terminal + " -t notifications -e notification_history",
                x=0.4,
                y=0.1,
                width=0.4,
                height=0.6,
                opacity=1,
            ),
        ],
    ),
]

scratchpad_keys = [
    Key(
        ["control"],
        "1",
        lazy.group["scratchpad"].dropdown_toggle("notes"),
        desc="Launch notes",
    ),
    Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("colorpick")),
    Key(["control"], "3", lazy.group["scratchpad"].dropdown_toggle("notifications")),
]
