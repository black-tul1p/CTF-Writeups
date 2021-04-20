# Solve

Like last time, use `olevba3` to view the VBA scripts embedded in the document. Analyzing the code reveals that the first large code segment of the script is a decoder for the ROT-13 cipher.

Looking at the line `Public Const aqv6tf As String = "EVGFRP{E0GG1ATZ@YP0Q3}"`, we can guess that this is the flag that needs to be deciphered. Using the CyberChef ROT13 decoder, we get the flag.

### Flag

`RITSEC{R0TT1NGM@LC0D3}`

# Note

I initially did not analyze the code and guessed that the flag was encrypted using some kind of substitution cipher (which to me hinted at a ROT-x cipher), since the numbers and parentheses are still readable. So I decoded it using the ROT-13 decoder on CyberChef. I only analyzed the code for the next challenge (BokBot), which turned out to be unsolvable until the script was updated near the end of the CTF.

I have uploaded the updated files in this repo but have not analyzed the BokBot challenge section. From the analysis of the code from the unfixed version, I found that the code calls `C:\windows\system32\mshta.exe` (stored as a string encrypted in ROT-13) with a string as a parameter (most likely an HTML script, given the name of the virus), which was a common method of achieving RCE in older viruses. The unfixed code had the issue of not containing the HTML script, which is why I stopped working on it after that.
