# Description

### Title: BIRDTHIEF: FYSA

Read the pdf in `\src` for the description.

# Solution

Open the provided packet capture file in Wireshark. After a bit of scrolling you'll find a TCP packet with data segment containing a login username `pilot`, which is interesting. Right click on the TCP packet and select Follow, then select TCP stream.

![black-tul1p](/RITSEC-2021/forensics/BIRDTHIEF-interception/solve/pca.png)

It appears that credentials are being passed over the network. There is a base64 password string that decodes to `ritsec`. There is another base64 string (read from a "droneinfo.log" file) that gives us the flag.  

`D6FQQAHYFFQWAAH7AVADCDQACAGPZURVPUBAMK7WJMRTMMLUCPY7PJWV2FFXVWLRSTTEUXZGOI4YD7IDLWZE74Q5AAAAA===`

### Flag

`RITSEC{Dr0n3_ar3_rea11y_c00l}`
