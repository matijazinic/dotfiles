from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from defaults import colors
from scripts.rofi import power, search
from plugins.spotify import Spotify


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


def init_widgets():
    default_widgets = [
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
        separator,
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
            hide_unused=True,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[3],
            this_screen_border=colors[4],
            other_current_screen_border=colors[0],
            other_screen_border=colors[0],
            foreground=colors[2],
            background=colors[0],
            disable_drag=True,
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/chevron_left.png",
            background=colors[0],
            mouse_callbacks={"Button1": lazy.layout.previous()},
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/chevron_right.png",
            background=colors[0],
            mouse_callbacks={"Button1": lazy.layout.next()},
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
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
            length=8,
            background=colors[0],
        ),
        separator,
        # widget.Spacer(
        #     length=4,
        #     background=colors[0],
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/1.png",
        # ),
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
        #     foreground=colors[2],
        #     mouse_callbacks={"Button1": search},
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/4.png",
        # ),
        widget.Spacer(
            length=100,
            background=colors[0],
            # background="#00000000",
        ),
        # widget.WindowName(
        #     background=colors[0],
        #     format="{name}",
        #     font="JetBrains Mono Bold",
        #     fontsize=14,
        #     foreground=colors[2],
        #     empty_group_string="Desktop",
        #     parse_text=center,
        # ),
        # widget.WindowTabs(
        #     background=colors[0],
        #     font="JetBrains Mono",
        #     fontsize=14,
        #     foreground=colors[2],
        #     # max_chars=0,
        # ),
        # widget.Spacer(
        #     length=10,
        #     background=colors[0],
        # ),
        widget.TaskList(
            background=colors[0],
            # background="#00000000",
            font="JetBrains Mono Bold",
            fontsize=14,
            foreground=colors[2],
            max_title_width=0,  # bilo je 200
            icon_size=24,
            padding_y=9,
            theme_mode="preferred",
            theme_path="/usr/share/icons/Papirus-Dark",
            border=colors[2],
            parse_text=remove_excess_letters,
            # parse_text=no_text,
        ),
        widget.Spacer(
            length=100,
            background=colors[0],
            # background="#00000000",
        ),
        separator,
        # widget.Image(
        #     filename="~/.config/qtile/Assets/3.png",
        # ),
        # widget.Net(),
        # Spotify(),
        widget.Spacer(
            length=8,
            background=colors[7],
        ),
        widget.Systray(
            background=colors[7],
            # fontsize=4,
        ),
        widget.Spacer(
            length=12,
            background=colors[7],
        ),
        separator,
        # widget.TextBox(
        #     text=" ",
        #     background="#0F1212",
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/6.png",
        #     background="#202222",
        # ),
        widget.Spacer(
            length=8,
            background=colors[0],
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/spotify.png",
            background=colors[0],
            margin=4,
        ),
        widget.Mpris2(
            background=colors[0],
            foreground=colors[2],
            name="Spotify",
            objname="org.mpris.MediaPlayer2.spotify",
            display_metadata=["xesam:title", "xesam:artist"],
            font="JetBrains Mono Bold",
            max_chars=40,
        ),
        widget.Spacer(
            length=12,
            background=colors[0],
        ),
        separator,
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2.png",
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/Drop1.png",
        # ),
        # widget.CPU(
        #     background="#202222",
        #     foreground="#607767",
        #     font="JetBrains Mono Bold",
        #     format="CPU: {load_percent}% -",
        #     # format="CPU: {freq_current}GHz - {load_percent}% -",
        # ),
        # widget.ThermalSensor(
        #     background="#202222",
        #     foreground="#607767",
        #     font="JetBrains Mono Bold",
        #     tag_sensor="Tctl",
        #     threshold=90,
        # ),
        # widget.Net(
        #     format=" {up}   {down} ",
        #     background="#202222",
        #     foreground="#607767",
        #     font="JetBrains Mono Bold",
        #     prefix="k",
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2.png",
        # ),
        # separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/note.png",
            background=colors[0],
            # scale=True,
            margin=8,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("notes"),
                "Button4": lambda: qtile.cmd_spawn("dunstctl history-pop"),
            },
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        separator,
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
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2-alt.png",
        # ),
        # widget.Spacer(
        #     length=4,
        #     background="#202222",
        # ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/ram.png",
            background=colors[0],
        ),
        widget.Spacer(
            length=-7,
            background=colors[0],
        ),
        widget.Memory(
            background=colors[0],
            format="{MemUsed: .0f}{mm}",
            foreground=colors[2],
            font="JetBrains Mono Bold",
            fontsize=13,
            update_interval=5,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("task_manager")
            },
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        # widget.Image(
        # filename='~/.config/qtile/Assets/Drop2.png',
        # ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2.png",
        # ),
        # widget.Spacer(
        #     length=4,
        #     background=colors[0],
        # ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        widget.BatteryIcon(
            theme_path="~/.config/qtile/Assets/Battery/",
            background=colors[0],
            scale=1.25,
        ),
        widget.Battery(
            font="JetBrains Mono Bold",
            fontsize=13,
            background=colors[0],
            foreground=colors[2],
            format="{percent:2.0%}",
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2.png",
        # ),
        # widget.Spacer(
        #     length=4,
        #     background=colors[0],
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
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        widget.KeyboardLayout(
            font="JetBrains Mono Bold",
            fontsize=13,
            configured_keyboards=["hr", "us"],
            background=colors[0],
            foreground=colors[2],
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/2.png",
        # ),
        # widget.Spacer(
        #     length=4,
        #     background=colors[0],
        # ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        # widget.Volume(
        #     font="JetBrains Mono Bold",
        #     fontsize=13,
        #     theme_path="~/.config/qtile/Assets/Volume/",
        #     emoji=True,
        #     step=5,
        #     # fmt="{}",
        #     background=colors[0],
        #     mouse_callbacks={"Button3": lazy.group["scratchpad"].dropdown_toggle("mixer")},
        # ),
        # widget.Spacer(
        #     length=-10,
        #     background=colors[0],
        # ),
        widget.Volume(
            font="JetBrains Mono Bold",
            fontsize=13,
            step=5,
            background=colors[0],
            foreground=colors[2],
            mouse_callbacks={
                "Button3": lazy.group["scratchpad"].dropdown_toggle("mixer")
            },
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/5.png",
        #     background=colors[0],
        # ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[7],
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/clock.png",
            background=colors[7],
            margin_y=6,
            margin_x=5,
        ),
        widget.Clock(
            format="%d.%m.%y - %H:%M:%S",
            background=colors[7],
            foreground=colors[2],
            font="JetBrains Mono Bold",
            fontsize=13,
            mouse_callbacks={
                "Button1": lazy.group["scratchpad"].dropdown_toggle("khal")
            },
        ),
        # widget.Image(
        #     filename="~/.config/qtile/Assets/4-alt.png",
        # ),
        widget.Spacer(
            length=4,
            background=colors[7],
        ),
        separator,
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/Misc/poweroff.png",
            margin=8,
            background=colors[0],
            mouse_callbacks={"Button1": power},
        ),
        widget.Spacer(
            length=4,
            background=colors[0],
        ),
    ]
    return default_widgets
