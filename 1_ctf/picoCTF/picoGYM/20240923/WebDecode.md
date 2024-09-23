---
tags:
  - picoCTF
  - web
  - browser_webshell_solvable
---


# Description

Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:54359/) to find the flag

# Walk-Through

문제를 열면 특정 사이트에 접속할 수 있다. 세션이나 쿠키에 어떤 값도 저장되어있지 않아 이로부터 flag를 얻을 수 있어보이진 않는다.

웹 인스펙터를 이용해 사이트 내부를 더 탐색해보면 다음과 코드가 별견된다.
```
...
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9">

```
notify_true의 값이 online hash identifier로 돌려보면 base64로 Encode 되어있다. base64로 Decode 하면 flag를 획득할 수 있다.
```shell
$ echo "cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDJjZGNiNTl9" |base64 -d
```
