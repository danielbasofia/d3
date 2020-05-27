
# Copyright (c) 2020 Daniel Valverde

import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook

from typing import List  # noqa: F401

mod = "mod4"
myConfig = "~/.config/qtile/config.py"

keys = [

    # WHATSAPP
    Key([mod, "shift"], "w", lazy.spawn("whatsapp-nativefier")), 

    # CHROME
    Key([mod], "c", lazy.spawn("chromium")),
    
    # VISUAL STUDIO CODE
    Key([mod, "control"], "i", lazy.spawn("code")),

    # TERMINAL
    Key([mod], "Return", lazy.spawn("alacritty")),

    # MENU
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -p 'Run: '"), desc = 'Dmenu Run Launcher'),
    
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "t", lazy.spawn("xterm")),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # SUBIR BAJAR VOLUMEN
    
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"))


]

# GRUPOS

group_names = [ ("WWW", {'layout': 'monadtall'}),
                ("DEV", {'layout': 'monadtall'}),
                ("CHAT",{'layout': 'monadtall'}),
                ("SYS", {'layout': 'monadtall'}),
                ("VID", {'layout': 'monadtall'}),
                ("DOC", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name,kwargs) in enumerate(group_names,1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))


# Tema de Layout
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "e1acff",
                "border_normal": "1D2330"}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
                    font = "Ubuntu",
                    fontsize = 10,
                    sections = ["FIRST", "SECOND"],
                    section_fontsize = 11,
                    bg_color = "141414",
                    active_bg = "90C435",
                    active_fg = "000000",
                    inactive_bg = "384323",
                    inactive_fg = "a0a0a0",
                    padding_y = 5,
                    section_top = 10,
                    panel_width = 320),
    layout.Floating(**layout_theme)
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# PALETA DE COLORES
colors = [["#282a36", "#282a36"],
          ["#434758", "#434758"],
          ["#ffffff", "#ffffff"],
          ["#ff5555", "#ff5555"],
          ["#8d62a9", "#8d62a9"],
          ["#668bd7", "#668bd7"],
          ["#e1acff", "#e1acff"]]

# PROMPT
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font = 'Ubuntu Mono',
    fontsize = 12,
    padding = 2,
    #background = colors[3]
)

extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),
                widget.Sep(
                   linewidth = 0,
                   padding = 6,
                   foreground = colors[2],
                   background = colors[0]
                   ),
                widget.GroupBox(),
                widget.Prompt(
                    prompt = prompt,
                    font = "Ubuntu Mono",
                    padding = 10,
                    foreground = colors[3],
                    background = colors[1]
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 40,
                    foreground = colors[2],
                    background = colors[0]
                    ),
                widget.WindowName(
                    foreground = colors[6],
                    background = colors[0],
                    padding = 0
                    ),
                #widget.TextBox("default config", name="default"),
                widget.Systray(
                    background = colors[0],
                    padding = 5
                    ),
		widget.Sep(
		    linewidth = 0,
		    padding = 10, 
		    foreground = colors[0],
		    background = colors[5]
		),
		widget.Clock(
                    foreground = colors[2],
                    background = colors[5],
                    format='%A, %B %d [ %H:%M ]'
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[0],
                    background = colors[5]
                    ),
                #widget.BatteryIcon(),
                widget.TextBox(
		    foreground = colors[2],
		    background = colors[5],
                    text = "\uf578"
                    ),
                widget.Battery(
		    foreground = colors[2],
		    background = colors[5],
                    format = "{percent:2.0%}"),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[0],
                    background = colors[5]
                    ),
                widget.Volume(
                    foreground = colors[2],
                    background = colors[5],
                    padding = 5
                    ),
                #widget.QuickExit(),
                
            ],
            24,
        ),
    ),
    ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
