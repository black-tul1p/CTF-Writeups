# Solution:

if you click on any of the animal names, you will see the url query change to the format: `?animal=<animal_name>`.

Trying a filename like `/etc/passwd` prints the contents of the file upto certain character limit. Trying `loremipsum.py` shows us most of the source code, and from this we know that the code prints the opened file up to 200 characters. Trying `flag` prints the standard lorem ipsum text, and the flag is most likely at the end of this file, which we cannot read completely (yet!). Trying a random word like `bruh` in the query pulls up a Werkzeug debug page. We can also see that this is a flask app, with a filename `loremipsum.py`. We can also see that there is a python console but it's locked behind a pin :(

Time to figure out the pin... Looking up "Werkzeug debug pin exploit" brings up a site: https://book.hacktricks.xyz/pentesting/pentesting-web/werkzeug

Reading up on the exploit, we find out that we can generate the pin on our end with the right information! For this we need too look at the following structs mentioned on the site:

```
probably_public_bits = [
    username,
    modname,
    getattr(app, '__name__', getattr(app.__class__, '__name__')),
    getattr(mod, '__file__', None),
]

private_bits = [
    str(uuid.getnode()),
    get_machine_id(),
]
```

From this, we see that we will need:
- `username` (we can see this on the debug screen, it is loremipsum)
- `modname` (this is flask.app)
- `getattr(app, '__name__', getattr (app .__ class__, '__name__'))` (this is Flask)
- `getattr(mod, '__file__', None)` (this is the absolute path to the flask app, which we can see on the debug screen)
- `uuid.getnode()` (we can get this by reading `/sys/class/net/eth0/address`)
- `get_machine_id()` (we can get this by reading and concatenating `/proc/sys/kernel/random/boot_id` and `/proc/self/cgroup`)

Entering those values in the provided script gives us a pin! Enter the pin into the prompt and you will gain access to the python terminal and will be able to execute arbitrary commands. To read the flag, we need to enter the following command:

`>>> with open('/home/loremipsum/flag', 'r') as f: print(f.read())`

[console](/b01lersCTF-21/web/LoremIpsum/solve/flag.png)

Then we will be able to the read the entire file and at the end, we will find the flag: `b0ctf{Fl4sK_d3buG_is_InseCure}`
