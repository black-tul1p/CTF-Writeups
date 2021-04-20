# Description

### Title: Robots

Robots are taking over. Find out more.

34.69.61.54:5247

# Solution

The name of the challenge is a hint for looking at the robots.txt file, which is present at the root directory of most websites.

![black-tul1p](/RITSEC-2021/web/Robots/solve/page.png)

Add a `/robots.txt` after the link, and press enter. The robots.txt file contents will be displayed. Going through each entry, you will find an entry titled `flag` with a base64 string `UlN7UjBib3RzX2FyM19iNGR9`.

![black-tul1p](/RITSEC-2021/web/Robots/solve/robots_txt.png)

Decoding this string in CyberChef gives us the flag.

### Flag

`RS{R0bots_ar3_b4d}`
