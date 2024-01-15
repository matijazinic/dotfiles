from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from defaults import colors
from widgets import init_widgets
import os

from scripts.rofi import power, search


def remove_excess_letters(text):
    for string in strings_to_exclude:
        text = text.replace(string, "")
    return text


def no_text(text):
    return ""


def center(text):
    return text.center(40)


separator = widget.Sep(
    linewidth=2,
    padding=2,
    size_percent=70,
    background=colors[0],
    foreground=colors[2],
)

strings_to_exclude = [
    " - Chromium",
    " — Mozilla Firefox",
    " - Code - OSS",
    "- Mozilla Thunderbird",
    " - Thunar",
    "- Discord",
]


hostname = os.uname()[1]


def init_main_screen():
    widgets_main = init_widgets()
    if hostname != "matija-legion5pro":
        del widgets_main[38:42]
    return widgets_main


def init_secondary_screen():
    widgets_secondary = init_widgets()
    del widgets_secondary[21:26]
    if hostname != "matija-legion5pro":
        del widgets_secondary[33:38]
    return widgets_secondary


wallpaper_path = "/home/matija/dotfiles/Pictures/wallpapers"

screens = [
    Screen(
        top=bar.Bar(
            init_main_screen(),
            42,
            border_color="#0F1212",
            # background="#00000000",
            border_width=[0, 0, 0, 0],
            # margin = [15,60,6,60],
            # margin=[10, 10, 6, 10],
            margin=[0, 0, 10, 0],
            # margin = 0,
        ),
        wallpaper=f"{wallpaper_path}/nord-arch-frost-logo.png",
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            init_secondary_screen(),
            42,
            border_color="#0F1212",
            # background="#00000000",
            border_width=[0, 0, 0, 0],
            # margin = [15,60,6,60],
            # margin=[10, 10, 6, 10],
            margin=[0, 0, 10, 0],
            # margin = 0,
        ),
        wallpaper=wallpaper_path + "/" + "arch-neon.png",
        wallpaper_mode="fill",
    ),
]
