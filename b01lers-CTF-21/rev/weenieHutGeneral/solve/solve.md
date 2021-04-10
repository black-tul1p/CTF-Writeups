# Solution:


We are given a C binary, which we will need to anaylze. Using `ghidra`, we can disassemble the binary. Here we can see two functions of interest: `tryToRev` and `revvy`


Looking at the decompiled code for `tryToRev`, we can see that there is a call to `revvy`. We can also see that `revvy` makes a call to `srand()` with a specific seed.

Going back to the `tryToRev` function, after the revvy call, there are two calls to `rand()`. Since we know the seed, we can figure out the values returned by those two `rand()` calls.

Next we see that the input is being Bitwise XOR-ed with the the first srand() value and 0x3597b74, and this is being checked against the second srand() value.

All we have to do to get the original input is Bitwise XOR the known values (the srand() values and 0x3597b74), and we will get what we seek!

You can write your own C program check if the answer is right, which is what I did, and you should get the flag: `btcf{1432175799}`
