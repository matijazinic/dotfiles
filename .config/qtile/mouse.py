from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from defaults import mod, terminal

mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod], "Button4", lazy.screen.prev_group()),
    Click([mod], "Button5", lazy.screen.next_group()),
]
