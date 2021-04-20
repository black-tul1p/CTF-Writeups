# Description:

### Title: Parcel

That's a lot of magick

# Solution:

Extract the given archive containing a file named `Parcel`. Analyzing the file using the command `file Parcel` shows us that it's a collection of emails with a bunch of base64 encoded PNGs. Decoding the PNGs using https://base64.guru/converter/decode/image gives us a puzzle of sorts, with several pieces of the flag.

![black-tul1p](/RITSEC-2021/forensics/Parcel/solve/8.png)
![black-tul1p](/RITSEC-2021/forensics/Parcel/solve/3.png)

Rearranging the PNGs with `Photoshop` (or GIMP), gives us the flag.

![black-tul1p](/RITSEC-2021/forensics/Parcel/solve/flag.png)

### Flag

`RS{help_m3_Im_doing_a_puzzl3}`
