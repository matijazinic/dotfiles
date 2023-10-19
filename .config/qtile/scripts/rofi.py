# from libqtile import qtile
from libqtile.lazy import lazy


@lazy.function
def search(qtile):
    qtile.cmd_spawn("rofi -show drun")


@lazy.function
def power(qtile):
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/powermenu")
