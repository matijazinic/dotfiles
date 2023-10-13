#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

#Custom Aliases
alias pac='sudo pacman'
alias vpnc='ivpn connect -fastest -city'
alias vpnr='ivpn connect -last'
alias vpnd='ivpn disconnect'
alias susp='systemctl suspend'
alias myip='echo $(curl -s https://api.my-ip.io/ip)'
alias officemon="xrandr --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --primary --mode 2560x1600 --pos 0x0 --rate 165.02 --rotate normal --output HDMI-0 --mode 1920x1080 --pos 2560x260 --rate 74.97 --rotate normal"
alias homemon="xrandr --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output HDMI-0 --mode 2560x1440 --pos 0x0 --rotate normal --output DP-4 --primary --mode 2560x1600 --pos 2560x0 --rate 165.02 --rotate normal"
