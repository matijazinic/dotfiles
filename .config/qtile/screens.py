from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from colors import colors

strings_to_exclude = [
    " - Chromium",
    " — Mozilla Firefox",
    " - Code - OSS",
    "- Mozilla Thunderbird",
    " - Thunar",
    "- Discord",
]


def search():
    qtile.cmd_spawn("rofi -show drun")


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/powermenu")


def remove_excess_letters(text):
    for string in strings_to_exclude:
        text = text.replace(string, "")
    return text


def no_text(text):
    return ""


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=10,
                    background=colors[7],
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/arch_linux.png",
                    margin=6,
                    background=colors[7],
                    mouse_callbacks={"Button1": search},
                ),
                widget.Spacer(
                    length=10,
                    background=colors[7],
                ),
                # widget.Sep(linewidth=0, padding=2, background=colors[2]),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/6.png",
                # ),
                widget.GroupBox(
                    # font="Ubuntu Bold",
                    font="JetBrains Mono Bold",
                    fontsize=16,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=10,
                    borderwidth=3,
                    active=colors[2],
                    inactive=colors[2],
                    rounded=False,
                    highlight_color=colors[1],
                    highlight_method="line",
                    this_current_screen_border=colors[3],
                    this_screen_border=colors[4],
                    other_current_screen_border=colors[0],
                    other_screen_border=colors[0],
                    foreground=colors[2],
                    background=colors[0],
                ),
                # widget.Sep(linewidth=0, padding=2, background=colors[2]),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Spacer(
                    length=20,
                    background="#00000000",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/layout.png", background=colors[0]
                ),
                widget.CurrentLayout(
                    foreground=colors[2],
                    background=colors[0],
                    fmt="{}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    # mouse_callbacks={"Button1": lazy.next_layout(), "Button3": lazy.prev_layout()}
                ),
                widget.Spacer(
                    length=20,
                    background="#00000000",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/1.png",
                ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/5.png",
                # ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/search.png",
                #     margin=2,
                #     background="#0F1212",
                #     mouse_callbacks={"Button1": search},
                # ),
                # widget.TextBox(
                #     fmt="Search",
                #     background="#0F1212",
                #     font="JetBrains Mono Bold",
                #     fontsize=13,
                #     foreground="#607767",
                #     mouse_callbacks={"Button1": search},
                # ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/4.png",
                # ),
                # widget.WindowName(
                #     background = '#202222',
                #     format = "{name}",
                #     font="JetBrains Mono Bold",
                #     fontsize=13,
                #     foreground='#607767',
                #     empty_group_string = 'Desktop',
                # ),
                # widget.WindowTabs(
                #     background="#202222",
                #     font="JetBrains Mono Bold",
                #     fontsize=14,
                #     foreground="#607767",
                # ),
                widget.TaskList(
                    background="#202222",
                    font="JetBrains Mono Bold",
                    fontsize=14,
                    foreground="#607767",
                    max_title_width=0,  # bilo je 200
                    icon_size=None,
                    padding_y=6,
                    theme_mode="preferred",
                    parse_text=remove_excess_letters
                    # parse_text=no_text
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/3.png",
                ),
                # widget.Net(),
                # Spotify(),
                widget.Systray(
                    background="#0F1212",
                    fontsize=2,
                ),
                widget.TextBox(
                    text=" ",
                    background="#0F1212",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                    background="#202222",
                ),
                widget.Mpris2(
                    background="#202222",
                    foreground="#607767",
                    name="Spotify",
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=["xesam:title", "xesam:artist"],
                    font="JetBrains Mono Bold",
                    max_chars=40,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Drop1.png",
                ),
                widget.CPU(
                    background="#202222",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    format="CPU: {load_percent}% -",
                    # format="CPU: {freq_current}GHz - {load_percent}% -",
                ),
                widget.ThermalSensor(
                    background="#202222",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    tag_sensor="Tctl",
                    threshold=90,
                ),
                # widget.Net(
                #     format=" {up}   {down} ",
                #     background="#202222",
                #     foreground="#607767",
                #     font="JetBrains Mono Bold",
                #     prefix="k",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/note.png",
                    background="#202222",
                    scale=True,
                    margin=8,
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle("notes")
                    },
                ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/Misc/clipboard.png",
                #     background="#202222",
                #     scale=True,
                #     margin=8,
                #     mouse_callbacks={
                #         "Button1": lazy.group["scratchpad"].dropdown_toggle("notes")
                #     },
                # ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/Misc/notification.png",
                #     background="#202222",
                #     scale=True,
                #     margin=8,
                #     mouse_callbacks={
                #         "Button1": lazy.group["scratchpad"].dropdown_toggle("notifications")
                #     },
                # ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                # widget.Net(
                #     format=" {up}   {down} ",
                #     background="#202222",
                #     foreground="#607767",
                #     font="JetBrains Mono Bold",
                #     prefix="k",
                # ),
                # widget.CheckUpdates(
                #     font="JetBrains Mono Bold",
                #     fontsize=13,
                #     background="#202222",
                #     foreground="#607767",
                #     colour_have_updates="#607767",
                #     colour_no_updates="#607767",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2-alt.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/ram.png",
                    background="#202222",
                ),
                widget.Spacer(
                    length=-7,
                    background="#202222",
                ),
                widget.Memory(
                    background="#202222",
                    format="{MemUsed: .0f}{mm}",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle(
                            "task_manager"
                        )
                    },
                ),
                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                # widget.BatteryIcon(
                #     theme_path="~/.config/qtile/Assets/Battery/",
                #     background="#202222",
                #     scale=1,
                # ),
                # widget.Battery(
                #     font="JetBrains Mono Bold",
                #     fontsize=13,
                #     background="#202222",
                #     foreground="#607767",
                #     format="{percent:2.0%}",
                # ),
                # widget.Image(
                #     filename="~/.config/qtile/Assets/2.png",
                # ),
                widget.Spacer(
                    length=4,
                    background="#202222",
                ),
                # widget.Battery(format=' {percent:2.0%}',
                # font="JetBrains Mono ExtraBold",
                # fontsize=12,
                # padding=10,
                # background='#202222',
                # ),
                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                # font="JetBrains Mono Bold",
                # fontsize=12,
                # padding=10,
                # background='#4B4D66',
                # ),
                widget.KeyboardLayout(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    configured_keyboards=["hr", "us"],
                    background="#202222",
                    foreground="#607767",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    theme_path="~/.config/qtile/Assets/Volume/",
                    emoji=True,
                    # fmt="{}",
                    background="#202222",
                    mouse_callbacks={
                        "Button3": lazy.group["scratchpad"].dropdown_toggle("mixer")
                    },
                ),
                widget.Spacer(
                    length=-5,
                    background="#202222",
                ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background="#202222",
                    foreground="#607767",
                    mouse_callbacks={
                        "Button3": lazy.group["scratchpad"].dropdown_toggle("mixer")
                    },
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                    background="#202222",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/clock.png",
                    background="#0F1212",
                    margin_y=6,
                    margin_x=5,
                ),
                widget.Clock(
                    format="%d.%m.%y - %H:%M:%S",
                    background="#0F1212",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    mouse_callbacks={
                        "Button1": lazy.group["scratchpad"].dropdown_toggle("khal")
                    },
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/4-alt.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/poweroff.png",
                    margin=8,
                    background="#202222",
                    mouse_callbacks={"Button1": power},
                ),
                widget.Spacer(
                    length=8,
                    background="#202222",
                ),
            ],
            36,
            border_color="#0F1212",
            background="#00000000",
            border_width=[0, 0, 0, 0],
            # margin = [15,60,6,60],
            margin=[10, 10, 6, 10],
            # margin = 0,
        ),
        wallpaper="/home/matija/Pictures/wallpapers/night-desktop.jpg",
        wallpaper_mode="fill",
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                    background="#0F1212",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/launch_Icon.png",
                    margin=2,
                    background="#0F1212",
                    mouse_callbacks={"Button1": power},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                ),
                widget.GroupBox(
                    fontsize=16,
                    borderwidth=3,
                    highlight_method="block",
                    active="#607767",
                    block_highlight_text_color="#B2BEBC",
                    highlight_color="#D0DAF0",
                    inactive="#0F1212",
                    foreground="#4B427E",
                    background="#202222",
                    this_current_screen_border="#202222",
                    this_screen_border="#202222",
                    other_current_screen_border="#202222",
                    other_screen_border="#202222",
                    urgent_border="#202222",
                    rounded=True,
                    disable_drag=True,
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/1.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/layout.png", background="#202222"
                ),
                widget.CurrentLayout(
                    background="#202222",
                    foreground="#607767",
                    fmt="{}",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    # mouse_callbacks={"Button1": lazy.next_layout(), "Button3": lazy.prev_layout()}
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/search.png",
                    margin=2,
                    background="#0F1212",
                    mouse_callbacks={"Button1": search},
                ),
                widget.TextBox(
                    fmt="Search",
                    background="#0F1212",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground="#607767",
                    mouse_callbacks={"Button1": search},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/4.png",
                ),
                # widget.WindowName(
                #     background = '#202222',
                #     format = "{name}",
                #     font="JetBrains Mono Bold",
                #     fontsize=13,
                #     foreground='#607767',
                #     empty_group_string = 'Desktop',
                # ),
                widget.TaskList(
                    background="#202222",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    foreground="#607767",
                    max_title_width=250,
                    icon_size=20,
                    padding_y=6,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.Mpris2(
                    background="#202222",
                    foreground="#607767",
                    name="Spotify",
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=["xesam:title", "xesam:artist"],
                    font="JetBrains Mono Bold",
                    max_chars=40,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Drop1.png",
                ),
                widget.Net(
                    format=" {up}   {down} ",
                    background="#202222",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    prefix="k",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/ram.png",
                    background="#202222",
                ),
                widget.Spacer(
                    length=-7,
                    background="#202222",
                ),
                widget.Memory(
                    background="#202222",
                    format="{MemUsed: .0f}{mm}",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                # widget.Image(
                # filename='~/.config/qtile/Assets/Drop2.png',
                # ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                widget.BatteryIcon(
                    theme_path="~/.config/qtile/Assets/Battery/",
                    background="#202222",
                    scale=1,
                ),
                widget.Battery(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background="#202222",
                    foreground="#607767",
                    format="{percent:2.0%}",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                # widget.Spacer(
                #     length=4,
                #     background="#202222",
                # ),
                # widget.Battery(format=' {percent:2.0%}',
                # font="JetBrains Mono ExtraBold",
                # fontsize=12,
                # padding=10,
                # background='#202222',
                # ),
                # widget.Memory(format='﬙{MemUsed: .0f}{mm}',
                # font="JetBrains Mono Bold",
                # fontsize=12,
                # padding=10,
                # background='#4B4D66',
                # ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    theme_path="~/.config/qtile/Assets/Volume/",
                    emoji=True,
                    background="#202222",
                ),
                widget.Spacer(
                    length=-5,
                    background="#202222",
                ),
                widget.Volume(
                    font="JetBrains Mono Bold",
                    fontsize=13,
                    background="#202222",
                    foreground="#607767",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                    background="#202222",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/Misc/clock.png",
                    background="#0F1212",
                    margin_y=6,
                    margin_x=5,
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background="#0F1212",
                    foreground="#607767",
                    font="JetBrains Mono Bold",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=18,
                    background="#0F1212",
                ),
            ],
            36,
            border_color="#0F1212",
            border_width=[0, 0, 0, 0],
            # margin = [15,60,6,60],
            margin=[5, 10, 0, 10],
            # margin = 0,
        ),
        wallpaper="/home/matija/Pictures/wallpapers/night-desktop.jpg",
        wallpaper_mode="fill",
    ),
]
