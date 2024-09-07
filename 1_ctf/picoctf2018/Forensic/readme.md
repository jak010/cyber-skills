## PicoCTF2018 :  Forencisc  

---

#### Name :  forensics_Warmup1
- Desciption
    ```
    Can you unzip this file for me and retreive the flag?
    ```
- Walk Throught
  - 1.File Download
    ```
    https://2018shell.picoctf.com/static/d6487f8e2cbbb28b5168b512f0ac0710/flag.zip
    ```
  - 2.unzip
  - 3.open "flag.jpg"
---


#### Name : forensics_Warmup2
- Desciption
    ```
    Hmm for some reason I can't open this PNG? Any ideas?
    ```
- Walk Throught
  - 1.File Download
    ```
    https://2018shell.picoctf.com/static/0fde1a3e09824365348827194db9cdde/flag.png
    ```
  - 2.Open png
  - 3.Read Flag
---

#### Name : Desrouleaux
- Desciption
    ```
    Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with nc 2018shell.picoctf.com 54782. incidents.json
    ```
- Walk Throught
  - There is 3-Question
  ```
  1. What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.

  2.How many unique destination IP addresses were targeted by the source IP address 231.205.245.44?

  3.What is the number of unique destination ips a file is sent, on average? Needs to be correct to 2 decimal places. 
  ```
  - Reference file : most_script.py

---

#### Name : Reading_Between_the_Eyes
- Desciption
    ```
    Stego-Saurus hid a message for you in this image, can you retreive it?
    ```
- Walk Throught
  - Steghide online decoder
    - https://stylesuxx.github.io/steganography/

---

#### Name : Recovering From the Snap
- Desciption
    ```
    There used to be a bunch of animals here, what did Dr. Xernon do to them?
    ```
- Walk Throught
  ```
  Think
    How to "dd" extension file Analysis?
  ```
  -  First Ways
     - foremost
  - Second ways
     - testdisk

---

#### Name : admin panel
- Desciption
    ```
    We captured some traffic logging into the admin panel, can you find the password?
    ```
- Walk Throught
  - FILE URL
    - https://2018shell.picoctf.com/static/ccad03a151a0edac8bd01e665a595b7a/hex_editor.jpg
  - Solve Ways
    - strings data.pcap |grep -oE picoCTF{.*} --color=none

---

#### Name : TrulyAnArtist
- Desciption
    ```
    Can you help us find the flag in this Meta-Material? You can also find the file in /problems/truly-an-artist_3_066d6319e350c1d579e5cf32e326ba02.
    ```
- Walk Throught
  - FILE URL
    - https://2018shell.picoctf.com/static/69b2020b48082fb24714bf93707183e8/2018.png
  - Solve Ways
    - exiftool {FILE_NAME}

---

#### Name : Now You Don't
- Desciption
    ```
    We heard that there is something hidden in this picture. Can you find it?
    ```
- Walk Throught
  - FILE URL
    - https://2018shell.picoctf.com/static/a120d4af95c06068d5f5a08ec14a572d/nowYouDont.png
  - Solve Ways
    - stegsolver.jar {FILE}

---


#### Name : Ext Super Magic
- Desciption
    ```
    We salvaged a ruined Ext SuperMagic II-class mech recently and pulled the filesystem out of the black box. It looks a bit corrupted, but maybe there's something interesting in there. You can also find it in /problems/ext-super-magic_2_5e1f8bfb15060228f577045924e4fca8 on the shell server.
    ```
- Walk Throught
  - 1.ext2/3/4 Byte Recover
  - 2.hex editor -> 1080 -> \x53\xef
  - 3.debugfs -> ls -> flag.jpg
  - picoCTF{ab0CD63BC762514ea2f4fc9eDEC8cb1E}
---