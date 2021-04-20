# Description:

#### Title: Sessions

Find the flag.

http://34.69.61.54:4777

# Solution

The name of the challenge is a hint for analyzing the sessions cookies in your browser. Visit the page in a browser. It asks you for a username and password.

![black-tul1p](/RITSEC-2021/web/Sessions/solve/page.png)

After a look at the source code, you will see the login credentials in a comment. Login using the credentials.

![black-tul1p](/RITSEC-2021/web/Sessions/solve/login.png)

You will now be greeted by this page.

![black-tul1p](/RITSEC-2021/web/Sessions/solve/iroh.png)

Now, take a look at your `cookies` using the `Application` tab in the browser's `Dev Tools` (usually accessed by presing `F12`).

![black-tul1p](/RITSEC-2021/web/Robots/solve/session.png)

You will see a cookie titles `sessiontoken` with a base64 string value `UlN7MG5seV9PbmVfczNzc2lvbl90b2szbn0=`. Decoding this string in CyberChef gives us the flag.

### Flag

`RS{0nly_One_s3ssion_tok3n}`
