# Affinity CTF Lite 2020
- Link: `https://2020.affinityctf.com/challenges`
- Write Up:`https://ctftime.org/event/1146/tasks/`

## Web

---
### soodefault
HTML Entities 문제

- Description
	- 링크로 접속 시 HTML entite가 눈에 띔, 숫자를 보고 문자로 바꿔주면 플래그 나타남

- Referenece  
	- soodefault/solve.py 

---

### Path of Double-Dipping

URL Double Encoding

- Description
	- 특정 경로에 접속하면 플래그가 나타날 것임을 바로 눈치챌 수 있지만 문제는 어떻게 접속할 것인가
	- 일반적인 접속인 경우 접속 못하지만, URL DOUBLE ENCODING 기법을 통해 접속하면 bypassing 됨

- URL Double Encoding site: `https://www.url-encode-decode.com/`

---

### True Content

# Redriect, Proxy, Exposure

- Description
	- 링크로 접속하면 아무것도 뜨지 않는다. DocumentRoot로 접속한 뒤 나타나는 정보를 이용해
	- 플래그를 찾는 것이 목적이다.

- Walk Throught
	1. Burp Suite -> Repeater -> Response -> Source Code Exposure
		: `http://web1.affinityctf.com/redirect.js`
	2. Source Downloads -> redirect.js
	3. function call 'getData(true)'
---


