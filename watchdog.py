#!/usr/bin/env python3
import pyautogui
import time

# Open new terminal
pyautogui.hotkey('ctrl', 'alt', 't')
time.sleep(1)

# Create tmux session
pyautogui.write('tmux')
pyautogui.press('enter')

# Move terminal to 2nd monitor and resize it
pyautogui.hotkey('winleft', 'shift', 'left')
pyautogui.hotkey('winleft', 'right')
pyautogui.hotkey('winleft', 'down')
pyautogui.hotkey('winleft', 'down')

# Split tmux horizontally
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('-')

# Open nethogs sorting by sent
pyautogui.write('nethogs -s')
pyautogui.press('enter')

# Select upper half
pyautogui.hotkey('alt', 'up')

# Open htop
pyautogui.write('htop')
pyautogui.press('enter')

# Leave nethogs selected
pyautogui.hotkey('alt', 'down')

# Switch to initial terminal
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

# Quit initial terminal
pyautogui.write('exit')
pyautogui.press('enter')
