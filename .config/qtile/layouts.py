from libqtile import layout
from libqtile.config import Match
from defaults import colors

# L A Y O U T S

layout_defaults = {
    "margin": 10,
    "border_focus": colors[2],
    "border_normal": colors[0],
    "border_width": 1,
}

layouts = [
    layout.Max(**layout_defaults),
    layout.Columns(**layout_defaults),
    layout.Floating(**layout_defaults),
    # Try more layouts by unleashing below layouts
    #  layout.Stack(num_stacks=2),
    #  layout.Bsp(),
    #  layout.Matrix(	border_focus='#1F1D2E',
    #     border_normal='#1F1D2E',
    #     margin=4,
    #     border_width=0,
    # ),
    layout.MonadTall(**layout_defaults),
    # layout.MonadWide(	border_focus='#1F1D2E',
    #     border_normal='#1F1D2E',
    #     margin=4,
    #     border_width=0,
    # ),
    #  layout.Tile(	border_focus='#1F1D2E',
    #     border_normal='#1F1D2E',
    # ),
    #  layout.RatioTile(),
    #  layout.TreeTab(),
    #  layout.VerticalTile(),
    #  layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_focus="#1F1D2E",
    border_normal="#1F1D2E",
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="file-roller"),  # Zip files
        Match(wm_class="blueman-manager"),  # Bluetooth manager
<<<<<<< Updated upstream
        Match(wm_class="wireguird"), # WireGuard client
=======
        Match(wm_class="flameshot"),  # Screenshot tool

>>>>>>> Stashed changes
    ],
)
