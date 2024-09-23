---
tags:
  - picoCTF
  - obfuscation
  - easy
---

# Walk-Through

>Why search for the flag when I can make a bookmarklet to print it for me?Browse [here](http://titan.picoctf.net:65363/), and find the flag!


문제 풀이 instance를 실행하면 web에 접근할 수 있는 링크가 열린다. 이 링크에 접속하면 다음과 같은 javascript  코드가 보인다.
```
javascript:(function() {
var encryptedFlag = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓÒËÉ§©í";
var key = "picoctf";
var decryptedFlag = "";
for (var i = 0; i < encryptedFlag.length; i++) {
	decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
}
alert(decryptedFlag);
})();
    
```
온라인 [javascript 컴파일러 사이트](https://www.programiz.com/javascript/online-compiler/)로 가서 해당 코드를 실행시키면 flag가 보인다.
```
node /tmp/5ckZyt7zr3.js
picoCTF{p@g3_turn3r_6bbf8953}
```
너무 쉽게 풀어서 다른 풀이법도 찾아봤지만 트릭이라고 불리는 특별한 무언가는 없다.
