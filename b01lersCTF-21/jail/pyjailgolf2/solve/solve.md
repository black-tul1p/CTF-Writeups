# Solution:

Now have to find a way to print the flag using a command that is less than 9 characters long. While not the originally intended solution, we can use `help()` again for this. First we call `help()` and then enter `pyjailgolf2` (since it shows up as a module; verify using `modules` command to see a list of modules). Then we enter `flag` and we get:

```
>>> flag
Help on module pyjailgolf2:

NAME
    pyjailgolf2

DATA
    flag = 'pctf{Un1c0d3_i5_sw34t}'
    line = 'flag'

FILE
    c:\users\divay\downloads\ctf-writeups\b01lersctf-21\jail\pyjailgolf2\src\pyjailgolf2.py
```

This gives us the flag: `pctf{Un1c0d3_i5_sw34t}`

From the flag, we can see that this was not an intended solution, so the creator of the challenge made `pyjailgolf3` as a third challenge to address this.
