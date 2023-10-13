import os
import subprocess
from libqtile import hook


# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser("~/.config/qtile/autostart_once.sh")])


@hook.subscribe.client_name_updated
def rearrange(window):
    if window.name == "Spotify":
        window.togroup(group_name="8")


# def center_floating_win(window):
#     # wm_name = window.cmd_inspect()["name"]
#     wm_class = window.get_wm_class()[0]
#     if wm_class == "file-roller":
#         window.cmd_set_size_floating(1200, 800)
#         window.cmd_set_position_floating((2560 - 1200) // 2, (1600 - 800) // 2)
