# HackToBer CTF

## About Site : https://www.ghosttown.xyz/t/week-is-50-complete/35

## Start
```
[Rules1]
- Read Manual 
- flag : flag{pl4y_by_th3_ru13s}

[DEADFACE]
- READ : http://ctf.cyberhacktics.com/intel 
- flag : flag{7}

[DEADFACE]
- READ : http://ctf.cyberhacktics.com/intel 
- flag : flag{mort1cia}

[Let's BEGIN]
- flag : flag{lets_get_started}
```

## LINUX
```
[SSH Credential]
ssh hacktober@env.hacktober.io
PASSWORD : hacktober-Underdog-Truth-Glimpse

[Talking to the dead] : 30 point
: flag1.txt ->  find / -name "flag1.txt" 2>dev/null
: flag{cb07e9d6086d50ee11c0d968f1e5c4bf1c89418c}

30 point
flag2.txt -> find / -name "*flag*" 2>/dev/null
: /home/luciafer/Documents/.flag2.txt
: flag{728ec98bfaa302b2dfc2f716d3de7869f3eadcbf}

100 point
flag3.txt -> find / -name "*flag3*" 2>/dev/null
: /home/spookyboi/Documents/flag3.txt
: flag{445b987b5b80e445c3147314dbfa71acd79c2b67}
--> su spookyboi
--> Password Get "SQL"

300 point
flag4.txt -> find /-name "*flag4*" 2>/dev/null
: find / -perm -4000 2>/dev/null
: /usr/local/bin/ouija /flag4.txt
: flag{4781cbffd13df6622565d45e790b4aac2a4054dc}
```

## Programming
```
[Message in an Array] : 10 point
- USE THIS SITE : https://dotnetfiddle.net/
- flag : flag{Nothing Will Stop DEADFACE}

[Trick or Treat] : 50 point 
- unzip file
- function call it
- flag{2f3ba6b5fb8bb84c33b584f981c2d13d}

[Haunted Mirror] : 125 point
- Reverse tool : ghidra 
- flag is showing
- flag : flag{XQwG1PhUqJ9A&5v}

[Red Rum] : 250 point
- nc env2.hacktober.io 5000
- ...?
- flag{h33eeeres_j0hnny!!!}
```

## Cryptography
```
[Hail Caesar!] : 10 point
- READ : https://www.dcode.fr/caesar-cipher
- Decode Message : TGG KUSJWV QGM
- amount : 1
- flag : flag{BOO SCARED YOU} 

[Down the Wrong Path]  : 10 point
-- Transposition Cipher
-- USE : https://www.dcode.fr/transposition-cipher
-- MESSAGE
RMTLOBBTERSUXT EBOLOOOHWGORTA METSKIUETEFNAC EREPYATNATOETK
--
- flag : flag{spookyboi}

[Cover Your BASES]
- echo "ZmxhZ3tzaG91bGRhX21hZGVfdGhpc19vbmVfaGFyZGVyfQ==" |base64 -d
- flag{shoulda_made_this_one_harder}

```

## OSINT
```
[Creeping1] : 10 point
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{F. Kreuger Financial}

[Creeping2] : 10 point
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{Senior Acquisitions Supervisor}

[Creeping3] : 10 point
- READ : https://www.facebook.com/ali.tevlin.5/about
- flag : flag{06 Jun 1973}
```

## SQL
```
[Past Demons] : 30 point
1. file download 
2. mv *.unzip
3. sqlite3 out.db
4. .tables
5. select * from user;
6. select * from passwd;
: Password Crack : CrackStation
--> flag : 	flag{zxcvbnm}

[Address Book] : 50 point
1. file search keyword "Havron"
--> flag: flag{luc1afer.h4vr0n@shallowgraveu.com}

[Body Count] : 25 point
1. create database hacktober;
2. use hacktober;
3. sourcce *.sql 
4. select * from user;
--> flag : flag{900}

[NULL and Void] : 25 Point
--> flag : flag{middle, show}

[Fall classes] : 100 point
Query : select count(distinct course_id) from term_courses where term_id=2;
--> flag{401}

[CALISOTA] : 75 point
Query: select count(*) from users where state_id=6 or state_id=28;
--> flag{select count(*) from users where state_id=6 or state_id=28;}
```

## Traffic Analysis
```
[Remotely Administrated Evil]
- check it follow tcp tream
- flag{solut.exe}

[Evil CORP'S CHILD]
- wireshar -> export object -> http 
- mv picture4.jpg picture.exe
- md5sum picture.exe
- flag{a95d24937acb3420ee94493db298b295}

[An Evil Christmas CAROL]
- wirshark search "http"
- flag{205.185.125.104}

[Remotely Administrator]
- wireshark filtered "dns"
- flag{solution.myddns.me}

[An Evil Christmas CAROL2]
- wireshark search "dns"
- flag{vlcafxbdjtlvlcduwhga.com}

[Evil Corp's Child 2]
- wireshark endpoint use it
- flag{213.136.94.177}

[Evil Corp's CHILD3]
- wireshark search below
- ip.addr ==37.205.9.252 
- find string "ceti"
- flag{mogadishu}

```