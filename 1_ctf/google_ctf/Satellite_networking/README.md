# Google CTF for Beginner's Quest

# Satellite_networking

***FILE NAME:768be4f10429f613eb27fa3e3937fe21c7581bdca97d6909e070ab6f7dbf2fbf***
: We get the FILE NAME on site

```
1. How to Access?
- The Command 
: file {FILE NAME}
: unzip {FILE NAME}
: init_sat.log , README.pdf

The pdf Viewer : okular

2. Read to pdf file
: i'm figure it out password on {FILE NAME}
: PASSWORD is : osmium

3. Execute "init_sat"
: Input password "osmium"
: see the link -> https://docs.google.com/documentd/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
: visited link -> VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==
: seem's like base64?
: base64 decode command -> echo {msg} |base64 -d
: Result 
Username: wireshark-rocks
Password: start-sniffing!

: Should be Notice  Read the 'username' and 'password'
: Doing on wirshark the packet observe

: We see the one more informaiton
: username is brewtoot

4. packet observe with tcpdump
: command is
: tcpdump -nn -i eth0 -X
: CTF{4efcc72090af28fd33a2118985541f92e793477f}


```