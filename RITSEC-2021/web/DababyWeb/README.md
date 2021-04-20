# Description:

### Title: Dababy Web

Dababy wanted to share a message, but he seemed to put it too high up...

34.72.118.158:6284

# Solution

The description hints at where the flag file might be. Visit the link on your browser.

![black-tul1p](/RITSEC-2021/web/DababyWeb/solve/index.png)

If we go to the `Dababy's Images` link from the main page, we can see that the URL takes files as a parameter.

![black-tul1p](/RITSEC-2021/web/DababyWeb/solve/page2.png)

If we try to enter `flag.txt`, it won't work but if we enter `../flag.txt` (remember the hint?), we get the flag.

![black-tul1p](/RITSEC-2021/web/Dababy0Web/solve/page2_flag.png)

### Flag

`RS{J3TS0N_M4D3_4N0TH3R_0N3}`
