# Description:

### Title: 1597

... as in https://xkcd.com/1597/

http://git.ritsec.club:7000/1597.git/

# Solution:

The XKCD comic in the description talks about git branches, so we have to look at the branches in this repo. Clone the repo and view the branches using `git branch`. Restore the `flag.txt` file and read the file.

```
git checkout origin/\!flag
cat flag.txt
```
(The previously empty flag.txt now contains the flag)

### Flag

`RS{git_is_just_a_tre3_with_lots_of_branches}``
