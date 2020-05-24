#!/usr/bin/env python3
import subprocess
import shlex

CONSOLE = shlex.split('alacritty --dimensions 155 64 --position 0 960')
COMMAND = shlex.split('--command tmux new-session htop ; split-window nethogs -s')

if __name__ == '__main__':
    proc = subprocess.Popen([*CONSOLE, *COMMAND])
