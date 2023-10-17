# from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Key
from libqtile.lazy import lazy
from groups import groups
from defaults import mod, terminal
from show_keys import show_keys
from scratchpads import scratchpad_keys

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [
    #  D E F A U L T
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Change keyboard layout",
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "c", lazy.window.toggle_floating()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle previous layout"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle next layout"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget",
    ),
    Key(
        [mod],
        "w",
        lazy.spawn("rofi -show window"),
        desc="Show all currently open windows",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("sh -c ~/.config/rofi/scripts/powermenu"),
        desc="powermenu",
    ),
    Key(
        [mod],
        "t",
        lazy.spawn("sh -c ~/.config/rofi/scripts/themes"),
        desc="theme_switcher",
    ),
    # C U S T O M
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+"),
        desc="Volume Up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-"),
        desc="volume down",
    ),
    Key(
        [], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Volume Mute"
    ),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="playerctl"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="playerctl"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="playerctl"),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="brightness UP",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="brightness Down",
    ),
    Key([mod], "e", lazy.spawn("thunar"), desc="file manager"),
    Key([mod], "h", lazy.spawn("roficlip"), desc="clipboard"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),
    # Key(["control"], "1", lazy.group["scratchpad"].dropdown_toggle("mixer")),
    # Key(["control"], "2", lazy.group["scratchpad"].dropdown_toggle("colorpick")),
]

keys.extend(scratchpad_keys)

for i in groups:
    if i.name == "scratchpad":
        continue
    if int(i.name) < 10:
        keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                ),
            ]
        )
    else:
        name = int(i.name)
        key = name - 10
        key = str(key)
        scr = str(name)
        keys.extend(
            [
                Key(
                    [mod, "control"],
                    key,
                    lazy.group[scr].toscreen(),
                    desc="Switch to group {}".format(scr),
                ),
                Key(
                    [mod, "control", "shift"],
                    key,
                    lazy.window.togroup(scr, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(scr),
                ),
            ]
        )


cheater = show_keys(keys)
keys.extend(
    [
        Key([mod], "F1", lazy.spawn(cheater), desc="Print keyboard bindings"),
    ]
)
