> Author: jak010
> Date: 2021.05.28 (Fri)

## Scan
- Result
  ```text
	Nmap scan report for 10.10.143.176
	Host is up (0.31s latency).
	Not shown: 997 filtered ports
	PORT    STATE  SERVICE VERSION
	22/tcp  closed ssh
	80/tcp  closed http
	443/tcp closed https
  ```

## Enumerate

- `Web`
 - `Directory Brute Forcing`
   ```text
    Gobuster v3.1.0
	by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
	===============================================================
	[+] Url:                     http://10.10.143.176
	[+] Method:                  GET
	[+] Threads:                 10
	[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt
	[+] Negative Status codes:   404
	[+] User Agent:              gobuster/3.1.0
	[+] Timeout:                 10s
	===============================================================
	2021/05/28 10:28:26 Starting gobuster in directory enumeration mode
	===============================================================
	/admin                (Status: 301) [Size: 235] [--> http://10.10.143.176/admin/]
	/images               (Status: 301) [Size: 236] [--> http://10.10.143.176/images/]
	/js                   (Status: 301) [Size: 232] [--> http://10.10.143.176/js/]    
	/wp-content           (Status: 301) [Size: 240] [--> http://10.10.143.176/wp-content/]
	/css                  (Status: 301) [Size: 233] [--> http://10.10.143.176/css/]       
	/wp-admin             (Status: 301) [Size: 238] [--> http://10.10.143.176/wp-admin/]  
	/wp-includes          (Status: 301) [Size: 241] [--> http://10.10.143.176/wp-includes/]
	/xmlrpc               (Status: 405) [Size: 42]                                         
	/login                (Status: 302) [Size: 0] [--> http://10.10.143.176/wp-login.php]  
	/blog                 (Status: 301) [Size: 234] [--> http://10.10.143.176/blog/]       
	/feed                 (Status: 301) [Size: 0] [--> http://10.10.143.176/feed/]         
	/rss                  (Status: 301) [Size: 0] [--> http://10.10.143.176/feed/]
   ```
  - `Robots.txt`
    ```text
    User-agent: *
	fsocity.dic
	key-1-of-3.txt
    ```
    - First Key
      - `073403c8a58a1f80d943455fb30724b9`
