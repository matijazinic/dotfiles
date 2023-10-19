#!/bin/bash

# Set correct displays
autorandr -c &

# Start GNOME authentication agent
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# Start picom
picom --config ~/.config/picom/picom.conf &

# Set default keyboard layout
setxbmap hr &

# Start lockscreen
xss-lock --transfer-sleep-lock -- ~/.local/share/lock.sh &

# Start SyncThing in background
syncthing &

# Start wanted applets
nm-applet & # Network manager
blueman-applet & # Bluetooth manager
redshift &
clipit &

# Start often used apps
wireguird &
firefox &
alacritty &
spotify &
discord &
thunderbird &

# Set wallpapers
# ~/.fehbg &
