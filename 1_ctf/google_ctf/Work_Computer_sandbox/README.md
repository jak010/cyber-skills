# Google CTF for Beginner's Quest

# Work Computer Sandbox

```
1. How to Access ?
- nc readme.ctfcompetition.com 1337


2. The Goal is read flag file
- Goal File : README.flag , ORME.flag
- useful command path is "/usr/bin"
- file read command 'iconv', 'shuf' then Do it "iconv README.flag"

- How to Read File ORME.flag?
- Key is The "setpriv" Command (path is :/usr/bin)
- use command this
- setpriv busybox chmod 777 ORME.flag
- Got it!

```