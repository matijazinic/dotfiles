import json
from os.path import expanduser


def show_keys(keys):
    """
    print current keybindings in a pretty way for a rofi/dmenu window.
    """
    key_help = "{:<20} {:<30} {}\n".format("Group", "Keybinds", "Description")
    keys_ignored = (
        "XF86AudioMute",  #
        "XF86AudioLowerVolume",  #
        "XF86AudioRaiseVolume",  #
        "XF86AudioPlay",  #
        "XF86AudioNext",  #
        "XF86AudioPrev",  #
        "XF86AudioStop",
        "XF86MonBrightnessUp",
        "XF86MonBrightnessDown",
    )
    text_replaced = {
        "mod4": "[MOD]",  #
        "control": "[CTRL]",  #
        "mod1": "[ALT]",  #
        "shift": "[SHIFT]",  #
        "Escape": "ESC",  #
    }

    data = {}
    category = {}
    file_path = expanduser("~/.config/qtile/keybinds.json")
    for k in keys:
        if k.key in keys_ignored:
            continue

        mods = ""
        key = ""
        desc = k.desc.title()
        # group = k.group.title()
        group = ""
        allargs = ", ".join(
            [
                value.__name__ if callable(value) else repr(value)
                for value in k.commands[0].args
            ]
            + [
                "%s = %s" % (keyword, repr(value))
                for keyword, value in k.commands[0].kwargs.items()
            ]
        )
        command = k.commands[0].name + " " + allargs
        for m in k.modifiers:
            if m in text_replaced.keys():
                mods += text_replaced[m] + " + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            if k.key in text_replaced.keys():
                key = text_replaced[k.key]
            else:
                key = k.key.title()
        else:
            key = k.key

        key_line = "{:<20} {:<30} {}\n".format(group, mods + key, desc)
        key_help += key_line

        if group not in data:
            data[group] = {}

        category = data[group]
        category[desc] = {}
        category[desc]["keybind"] = mods + key
        category[desc]["command"] = command

    with open(file_path, "w") as json_data:
        json.dump(data, json_data, indent=4)

    return expanduser("~/.config/qtile/scripts/qtile-cheat")
