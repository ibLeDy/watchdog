#!/usr/bin/env python3
import subprocess
import shlex

terminal = shlex.split('alacritty --dimensions 135 64 --position 0 960')
command = shlex.split('--command tmux new-session htop ; split-window nethogs -s')

if __name__ == '__main__':
    subprocess.Popen([*terminal, *command])
