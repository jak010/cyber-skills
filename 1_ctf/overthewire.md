
## Badit

#### Level 00
 - Server : `ssh bandit0@bandit.labs.overthewire.org -p 2220`
 	- password: bandit0
 - `Walk Throught`
 	- ssh 로 원격 서버 접속을 시도할 수 있는지를 보는 문제
 - Next Level: boJ9jbbUNNfktd78OOpsqOltutMc3MY1

#### Level 01 
  - Server : `ssh bandit1@bandit.labs.overthewire.org -p 2220`
 	- password: boJ9jbbUNNfktd78OOpsqOltutMc3MY1
  - `Walk Throught`
 	```sh
 	cat *
 	```
 	- 대시 (-) 파일 읽는 문제
  - Next Level: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9

#### Level 02
  - Server : `ssh bandit2@bandit.labs.overthewire.org -p 2220`
 	- password: CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
  - `Walk Throught`
 	- 파일명에 공백이 들어간 파일을 읽을 수 있는 지 보는 문제
 	- tab을 통해 자동완성으로 읽으면 됨
  - Next Level: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK

#### Level 03
  - Server : `ssh bandit3@bandit.labs.overthewire.org -p 2220`
 	- password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
  - `Walk Throught`
 	```sh
 	$ cat ~/inhere/.hidedn
 	```
  - Next Level: pIwrPrtPN36QITSp3EQaw936yaFoFgAB


#### Level 04
  - Server : `ssh bandit4@bandit.labs.overthewire.org -p 2220`
 	- password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
 - `Walk Throught`
 	```sh
 	$ cd ~/inhere
 	$ file ./*
 	...
 	./-file07: ASCII text
 	...
 	```
 	- 필요한 파일의 종류를 탐색하고 어떤 식으로 찾아낼 수 있는지 보는 문제
 - Next Level: koReBOKuIDDepwhWk7jZC0RTdopnAYKh

#### Level 05
  - Server : `ssh bandit5@bandit.labs.overthewire.org -p 2220`
 	- password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
 - `Walk Throught`
 	```sh
 	$ cd ~/inhere
 	$ find ./* -size 1033c
 	```
 	- 파일의 크기를 이용하여 find를 이용할 수 있는지 보는 문제
 - Next Level: DXjZPULLxYr17uwoI01bNLQbtFemEgo7

#### Level 06
  - Server : `ssh bandit6@bandit.labs.overthewire.org -p 2220`
 	- password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
 - `Walk Throught`
 	```sh
 	$ find / -group "bandit6" 2>/dev/null
 	$ cat /var/lib/dpkg/info/bandit7.password
 	```
 	- 특정 그룹에 소속된 파일을 검색할 수 있는지 보는 문제
 - Next Level: HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

#### Level 07
  - Server : `ssh bandit7@bandit.labs.overthewire.org -p 2220`
 	  - password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
 - `Walk Throught`
 	```sh
 	$ cat data.txt | grep "millionth"
 	```
 	- 파일의 텍스트가 많을 떄 특정 값으로 원하는 내용만 추출할 수 있는지 보는 문제
 - Next Level: cvX2JJa4CFALtqS87jk27qwqGhBM9plV


#### Level 08
  - Server : `ssh bandit8@bandit.labs.overthewire.org -p 2220`
    - password: UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
 - `Walk Throught`
  ```sh
  $ cat data.txt | sort | uniq -c | more
  ```
  - 파일의 내용을 정렬할 수 있는지 보는 문제
 - Next Level: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR


#### Level 09
  - Server : `ssh bandit9@bandit.labs.overthewire.org -p 2220`
    - password: UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
 - `Walk Throught`
  ```sh
  $ strings data.txt | grep =
  ```
 - Next Level: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk


#### Level 10
  - Server : `ssh bandit10@bandit.labs.overthewire.org -p 2220`
    - Password: truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
 - `Walk Throught`
  ```sh
  $ cat data.txt | base64 -d
  ```
 - Next Level: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR

#### Level 11
  - Server : `ssh bandit11@bandit.labs.overthewire.org -p 2220`
    - Password: IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
 - `Walk Throught`
  ```sh
  $ cat data.txt | tr "[A-Za-z]" "[N-ZA-Mn-za-m]"
  ```
    - ROT 13 Decode
 - Next Level: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu


#### Level 12
  - Server : `ssh bandit12@bandit.labs.overthewire.org -p 2220`
    - Password: 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
  - `Walk Throught`
   ```sh
   $ xxd -r data.txt > file.gz 
   ```
    - gzip -d
    - bzip2 -d
    - tar xvf
  - Next Level: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL

#### Level 13
  - Server : `ssh bandit13@bandit.labs.overthewire.org -p 2220`
    - Password: 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
  - `Walk Throught`
   ```sh
   $ chmod 600 sshkey.private
   $ ssh -i sshkey.private ${SERVER}
   ```
  - Next Level: sshkey.private

#### Level 14
  - Server : `ssh bandit14@bandit.labs.overthewire.org -p 2220`
    - SSH Private Key Connection 
    - `cat /etc/bandit_pass/bandit14` : 4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
  - `Walk Throught`
   ```sh
   $ nc 127.0.0.1 30000
   ```
  - Next Level: BfMYroe26WYalil77FoDi9qh59eK5xNr

#### Level 15
  - Server : `ssh bandit15@bandit.labs.overthewire.org -p 2220`
    - `Password`: BfMYroe26WYalil77FoDi9qh59eK5xNr  
  - `Walk Throught`
   ```sh
   $ openssl s_client -connect localhost:30001
   ```
  - Next Level: cluFn7wTiGryunymYOu4RcffSxQluehd


#### Level 16
  - Server : `ssh bandit16@bandit.labs.overthewire.org -p 2220`
    - `Password`: cluFn7wTiGryunymYOu4RcffSxQluehd  
  - `Walk Throught`
   ```sh
   $ nmap localhost -p 31000-32000
   ```
   - Port on 31790
   - `SSL Connec`
      ```sh
      $ ncat --ssl localhost 31790
     ```
  - `Private key`
    ```sh
    $ ssh -i bandit17.pkey bandit17@bandit.labs.overthewire.org -p 2220
    ```

  - Next Level: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn


#### Level 17
 - Server : `ssh bandit16@bandit.labs.overthewire.org -p 2220`
    - `Password`: xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn  
  - `Walk Throught`
   ```sh
   $ diff password.old password.new
   ```
  - Next Level: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

#### Level 18
 - Server : `ssh bandit18@bandit.labs.overthewire.org -p 2220`
    - `Password`: kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd  
  - `Walk Throught`
   ```sh
   $ ssh bandit18@bandit.labs.overthewire.org -p 2220 -t /bin/sh
   ```
  - Next Level: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x

#### Level 19
  - Server : `ssh bandit19@bandit.labs.overthewire.org -p 2220`
    - `Password`: IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x  
  - `Walk Throught`
   ```sh
   $ ./bandit20-do cat /etc/bandit_pass/bandit20
   ```
  - Next Level: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

#### Level 20
  - Server : `ssh bandit20@bandit.labs.overthewire.org -p 2220`
    - `Password`: GbKksEFF4yrVs6il55v6gwY5aVje5f0j  
  - `Walk Throught`
   ```sh
   $ ./bandit20-do cat /etc/bandit_pass/bandit20
   ```
  - Next Level: GbKksEFF4yrVs6il55v6gwY5aVje5f0j

#### Level 21
  - Server : `ssh bandit21@bandit.labs.overthewire.org -p 2220`
    - `Password`: GbKksEFF4yrVs6il55v6gwY5aVje5f0j  
  - `Walk Throught`
   ```sh
   # term 1
   $ nc -l -p 12345
   GbKksEFF4yrVs6il55v6gwY5aVje5f0j

   # term 2
   $ ./suconnect 12345
   ```
  - Next Level: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

#### Level 22
  - Server : `ssh bandit22@bandit.labs.overthewire.org -p 2220`
    - `Password`: gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr  
  - `Walk Throught`
   ```sh
   $ cat /etc/cron.d/cronjob_bandit23
   @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
   * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
   
   $ cat /usr/bin/cronjob_bandit22.sh
   $ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
   $ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
   ```
  - Next Level: jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n



