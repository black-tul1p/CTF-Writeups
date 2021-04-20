# Description

### Title: Dababy Web

Dababy wanted to share a message, but he seemed to put it too high up...

34.72.118.158:6284

# Solution

The description hints at where the flag file might be. Visit the link on your browser. If we go to the `Dababy's Images` link from the main page, we can see that the URL takes files as a parameter (LFI vulnerability). If we try to enter `flag.txt`, it won't work but if we enter `../flag.txt` (remember the hint?), we get the flag.

### Flag

`RS{J3TS0N_M4D3_4N0TH3R_0N3}`
