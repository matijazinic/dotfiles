from libqtile.config import Group, Match, ScratchPad, DropDown
from defaults import terminal
from scratchpads import scratchpad_groups

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█


# groups = [Group(f"{i+1}", label="󰏃") for i in range(9)]

groups = [
    Group("1", label="󰏃", matches=[Match(wm_class=["firefox"])]),
    Group("2", label="󰏃", matches=[Match(wm_class=["code-oss"])]),
    Group("3", label="󰏃", layout="columns", matches=[Match(wm_class=["Alacritty"])]),
    Group("4", label="󰏃"),
    Group("5", label="󰏃", matches=[Match(wm_class=["thunderbird"])]),
    Group("6", label="󰏃", matches=[Match(wm_class=["thunar"])]),
    Group("7", label="󰏃"),
    Group(
        "8",
        label="󰏃",
        layout="max",
        matches=[
            Match(wm_class=["Spotify"])
        ],  # There is a chance that spotify won't get automatically moved to correct tag, so we have a hook for that at the bottom of the file
    ),
    Group("9", label="󰏃", 
	layout="columns",
	matches=[Match(wm_class=["discord"])]),
    Group("0", label="󰏃", layout="columns"),
    Group("10", label="󰏃", matches=[Match(wm_class=["RVGL"])]),
    # ScratchPad(
    #     "scratchpad",
    #     [
    #         DropDown(
    #             "khal",
    #             terminal + " -t ikhal -e ikhal",
    #             x=0.695,
    #             width=0.3,
    #             height=0.3,
    #             opacity=1,
    #         ),
    #         DropDown(
    #             "mixer",
    #             "pavucontrol",
    #             x=0.3,
    #             y=0.1,
    #             width=0.4,
    #             height=0.6,
    #             opacity=0.9,
    #         ),
    #         DropDown(
    #             "colorpick", "gpick", x=0.4, y=0.1, width=0.4, height=0.6, opacity=1
    #         ),
    #     ],
    # ),
]

groups.extend(scratchpad_groups)
