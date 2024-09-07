- URL (picoGYM)
     - `https://play.picoctf.org/practice?page=1`

## General

### Obedian Cat
 - Description
	 ```
	  This file has a flag in plain sight (aka "in-the-clear"). 
	 ```
 - Walk-Throught
   ```sh
   $ cat flag
   ```
 - Flag Is: picoCTF{s4n1ty_v3r1f13d_2aa22101}

### Python Wrangling
  - Description
  ```
  Python scripts are invoked kind of like programs in the Terminal...
  Can you run this Python script using this password to get the flag?
  ```
  - Walk-Throught
    - File (file_name: content)
        - `ende.py`
        - `flag.txt.en`
        - `pw.txt`: 67c6cc9667c6cc9667c6cc9667c6cc96 
    - Solve
    ```sh
    $ python3 ende.py -d flag.txt.en
	  Please enter the password:67c6cc9667c6cc9667c6cc9667c6cc96
	  picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}
    ```

### Wave a flag
  - Description
  ```
  Can you invoke help flags for a tool or binary
  This program has extraordinarily helpful information...
  ```
  - Walk-Throught
     - File: `warm`
     - Solve
	  ```
	  $ warm -h
	  Oh, help? I actually don't do much, but I do have this flag here:
	  picoCTF{b1scu1ts_4nd_gr4vy_30e77291}
	  ```

### Nice NetCat
 - Description
 ```text
 There is a nice program that you can talk to by using this command in a shell:
 $ nc mercury.picoctf.net 35652, but it doesn't speak English...
 ```
 - `Walk-Throught`
 ```python
  with open("nice_netcat", "r" ,encoding="utf8") as file:
    strings = "".join([ chr(int(x)) for x in file.readlines()])
    print(strings)
 ```

### Static ain't always noise
 - Description
 ```text
 Can you look at the data in this binary: static? This BASH script might help!
 ```
 - `Walk-Throught`
 ```sh
 $ ./ltdis.sh static
 $ cat static.ltdis.strings.txt
 ```

### Tab, Tab, Attack
 - Description
 ```text
 Using tabcomplete in the Terminal will add years to your life, esp.
 when dealing with long rambling directory structures and filenames: Addadshashanammu.zip
 ```
 - `Walk-Throught`
 ```sh
 $ apt install tree unzip
 $ tree -L 11 -f
 $ cat ./Addadshashanammu/../fang-of-haynekhtnamet
 ```


## Web Exploitation

### Get aHEAD
 - Description
 ```text
 Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:53554/
 ```
 - `Walk-Throught`
 ```sh
 curl -IHEAD http://mercury.picoctf.net:53554/
 ```

### Cookies
 - Description
 ```text
 Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:6418/x
 ```
 - `Walk-Throught`
    - Edit Cookie {"name":"18"} 

### Insp3ct0r
 - Description
 ```text
 Kishor Balan tipped us off that the following code may need inspection
 : https://jupiter.challenges.picoctf.org/problem/9670/ (link)
 or http://jupiter.challenges.picoctf.org:9670
 ```
 - `Walk-Throught`
    - `First Flag` : https://jupiter.challenges.picoctf.org/problem/9670/
        - `picoCTF{tru3_d3`
    - `Second Flag`: https://jupiter.challenges.picoctf.org/problem/9670/mycss.css
        - `t3ct1ve_0r_ju5t`
    - ` Third Flag`: https://jupiter.challenges.picoctf.org/problem/9670/myjs.js
        - `_lucky?2e7b23e3}`
 - Result
    - picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?2e7b23e3}

### Scavenger Hunt
 - Description
 ```text
 There is some interesting information hidden around this site http://mercury.picoctf.net:27278/. Can you find it?
 ```
 - `Walk-Throught`
    - `view-source:http://mercury.picoctf.net:27278/` : picoCTF{t
    - `http://mercury.picoctf.net:27278/mycss.css` : h4ts_4_l0
    - `http://mercury.picoctf.net:27278/robots.txt`: t_0f_pl4c
    - `ffuf`: 3s_2_lO0k
      ```sh 
      $ ffuf -w Apache.fuzz.txt -u http://mercury.picoctf.net:27278/FUZZ
      ```
    - `http://mercury.picoctf.net:27278/.DS_Store` : _a69684fd}
  - Result : `picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_a69684fd}`

### Where are the robots
- Description
    ```text
      Can you find the robots? https://jupiter.challenges.picoctf.org/problem/56830/ (link) or http://jupiter.challenges.picoctf.org:56830
    ```
- `Walk-Throught`
    - Workflow
      ```text
      https://jupiter.challenges.picoctf.org/problem/56830/robots.txt

      https://jupiter.challenges.picoctf.org/problem/56830/1bb4c.html
      ```
        - Result: `picoCTF{ca1cu1at1ng_Mach1n3s_1bb4c}`

### logon
- Description
    ```text
    The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/44573/ (link) or http://jupiter.challenges.picoctf.org:44573
    ```
- `Walk-Throught`
    - WorkFlow
        ```text
        F12 > Storage > Cookies > admin value `False` -> `True`
        ```
        - Result: `picoCTF{th3_c0nsp1r4cy_l1v3s_0c98aacc}`

### login
- Description
    ```text
    My dog-sitter's brother made this website but I can't get in; can you help?
    
    login.mars.picoctf.net
    ```
- `Walk-Throught`
    - WorkFlow
        - view-source:https://login.mars.picoctf.net/index.js  
          ```js
            const flag = "cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"  
            atob(flag)
          ```
            - Result : `picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`

### dont-user-client-side
- Description
    ```text
    Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/17682/ (link) or http://jupiter.challenges.picoctf.org:17682
    ```
- `Walk-Throught`
    - Work Flow
        ```text
        F12 > Source Code View > flag in JavaScript 
        ```
        - Result : `picoCTF{no_clients_plz_b706c5}`

## Reverse Engineering

### Transformation
- Description
  ```
  I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
  ```
- `Walk-Throught`
    - Online Decode Cyber Chef: `https://gchq.github.io/CyberChef/#recipe=Text_Encoding_Brute_Force('Encode')&input=54Gp5o2v5I2U5Jm744S25b2i5qW0542f5qWu542044y05pGf5r2m5by45byw5pGk5o2k46S35oW9JQ`

## Cryptography

### Mind your Ps And Qs
- Description
  ```
  In RSA, a small e value can be problematic, but what about N? Can you decrypt this? values
  ```
- `Walk-Throught`
  ```python
  from Crypto.Util.number import inverse
  from Crypto.Util.number import long_to_bytes

  c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
  n =769457290801263793712740792519696786147248001937382943813345728685422050738403253
  e =65537

  # n = p*q 
  # Usage: factodb (http://factordb.com/)
  p = 1617549722683965197900599011412144490161
  q = 475693130177488446807040098678772442581573
  phi = (p-1) * (q-1)

  d = inverse(e, phi)
  m = pow(c,d,n)

  print(long_to_bytes(m))
  ```
  - `Reference`: `https://www.youtube.com/watch?v=o4K5G7W8CbE`


