# Computer Monitoring Automation

When i start the computer i always open a new terminal in my 2nd monitor occupying the right half of the screen.
Then i will open a new [tmux](https://github.com/tmux/tmux) session and split the
panel horizontally.

```bash
------------------------
|          |..........||
|          |..........||
|          |----------||
|          |..........||
|          |..........||
------------------------
```

I always have [nethogs](https://github.com/raboof/nethogs) in the
lower part and [htop](https://github.com/hishamhm/htop) in the upper part.

This scripts automates this actions using [PyAutoGUI](https://github.com/asweigart/pyautogui)

1. Open a new terminal
2. Create tmux session
3. Move terminal to the right monitor
4. Resize terminal
5. Split tmux horizontally
6. Open nethogs in lower half
7. Open htop in upper half
8. Close initial terminal
