# Description:

#### Title: NSNC
#### Challenge Difficulty: Easy

Enjoy some comics, just like the ones on not-snc.com... :cry:

# Solution:

If you look carefully, you will see two parts of a QR code embedded into the image. You can also use `stegsolve` and cycle through the filters (the best one is "Red plane 1") to see it clearly.

![stegsolve](/b01lersCTF-21/misc/nsnc/solve/stegsolve.png)

Then you can use any image editing software to reconstruct the original QR code. As you can see, some of it is obscured by the "technology" text, but using the source image you should be able to guess what the QR code looks like.

![QR](/b01lersCTF-21/misc/nsnc/solve/QR.png)
