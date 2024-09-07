# Cyber Talent
- Link: `https://cybertalents.com/`
   
## Web

---
### Admin has the power
- URL
    - `http://35.193.45.56/adminpower/`
- `Walk Throught`  
      - Check the Source Page  
      - Will Get ID:PASSWORD    
   	  - Login & Get Flag    
  
---

### This is Sparta 
- URL
    - `http://35.193.45.56/sparta/`
- `Walk Throught`  
	  - Check the Source page
	  - JavaScript Read : `http://35.193.45.56/sparta/`
	  ```js
	  function check() {
	    var _0xeb80x2 = document['getElementById']('user')['value'];
	    var _0xeb80x3 = document['getElementById']('pass')['value'];
	    if (_0xeb80x2 == 'Cyber-Talent' && _0xeb80x3 == 'Cyber-Talent') {
	        alert('Congratz \x0A\x0A');
	    } else {
	        alert('wrong Password');
	    }
	  }
	  ```
	  - "Cyber-Talent:Cyber-Talent" Login & Get Flag
	  - FLAG:{J4V4_Scr1Pt_1S_Aw3s0me}
	- Etc
	    - Enum : http://ddecode.com/hexdecoder
---

### I am Legend
- URL : `http://35.193.45.56/iamlegend/`
- Walk Throught
     - Deobfuscator Site : 
          - http://deobfuscatejavascript.com/#
      - Check the Source Page
    - Read JSfuck Code & Deobfuscator Site decode
    ```js
    String.fromCharCode(102, 117, 110, 99, 116, 105, 111, 110, 32, 99, 104, 101, 99, 107, 40, 41, 123, 10, 10, 118, 97, 114, 32, 117, 115, 101, 114, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 117, 115, 101, 114, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 118, 97, 114, 32, 112, 97, 115, 115, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 112, 97, 115, 115, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 10, 105, 102, 40, 117, 115, 101, 114, 61, 61, 34, 67, 121, 98, 101, 114, 34, 32, 38, 38, 32, 112, 97, 115, 115, 61, 61, 32, 34, 84, 97, 108, 101, 110, 116, 34, 41, 123, 97, 108, 101, 114, 116, 40, 34, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 67, 111, 110, 103, 114, 97, 116, 122, 32, 92, 110, 32, 70, 108, 97, 103, 58, 32, 123, 74, 52, 86, 52, 95, 83, 99, 114, 49, 80, 116, 95, 49, 83, 95, 83, 48, 95, 68, 52, 77, 78, 95, 70, 85, 78, 125, 34, 41, 59, 125, 32, 10, 101, 108, 115, 101, 32, 123, 97, 108, 101, 114, 116, 40, 34, 119, 114, 111, 110, 103, 32, 80, 97, 115, 115, 119, 111, 114, 100, 34, 41, 59, 125, 10, 10, 125)
      
    ```
    
    - Web Console paste & will username & password
    - Login & Get Flag: {J4V4_Scr1Pt_1S_S0_D4MN_FUN}
---

### Dark Project

- URL: `http://35.184.249.177/darkp/`
- Walk Throught
	- 사이트를 관찰하다 보면 `index.php?home=` 과 같이 php를 통해 파라미터를 받고 있음, php filter를 생각해 볼 수 있음
	- 다음과 같이 php filter 로 index를 읽고 나오는 결과에 대해 디코딩을 하면 플래그가 나옴
	```
	/darkp/index.php?home=php://filter/convert.base64-encode/resource=index
	```
	- Decode Site: `https://www.base64decode.org/`

---

### Cool Name Effect

- URL: `http://34.77.37.110/cool-effect/`
- Walk Throught
	- 페이지 소스보기를 통해 보면  JS 코드가 보이는데 이 코드를 아래 사이트에서 언팩
		- `https://www.strictly-software.com/unpack-javascript`
    - 이 후 코드를 읽다보면 플래그를 얻을 수 있는 라인이 있는데 다음과 같이 플래그를 출력 가능 
	    ```
	    <script>
			var f = ([]["fill"] + "")[3];
			f += ([false] + undefined)[10];
			f += (NaN + [Infinity])[10];
			f += (NaN + [Infinity])[10];
			f += ( + (211))["to" + String["name"]](31)[1];
			f += ([]["entries"]() + "")[3];
			f += ( + (35))["to" + String["name"]](36);
			//legacyAlert(z.join('') + f)
			console.log(f) // flag print
		</script>
	    ```

---

### Encrypted Database

- URL: `http://34.77.37.110//encrypted-database/`
- Walk Throught
	- 아래 링크에서 페이지 소스 보기를 통해 힌트가 될만한 경로를 찾음 : `/secret-admin`
		- `http://34.77.37.110//encrypted-database/`
	- 위에서 찾은 정보로 접속 시 로그인 페이지가 나오고 다시 페이지 소스보기를 통해 읽어보면 `hidden-database/db.json` 이라는 경로 하나를 찾을 수 있음
		- `http://34.77.37.110/encrypted-database/secret-admin/`
	- 다시 위에서 찾은 `hidden-database/db.json`에 접속하면 `{flag:ab003765f3424bf8e2c8d1d69762d72c }` 가 보임
	- 위에서 얻은 flag를 hash-identifier 를 통해 보면 MD5 형식의 타입임을 알 수 있음
	- 이 후 crackstation 에서 복호화하면 플래그가 나옴

---
### Newsletter

- URL: `http://18.192.3.151/newsletter/`
- Walk Throught
	- 입력창에서 백 틱이나 | 를 막고 있음
	- burpsuite를 이용해 입력 창에 다음과 같이 입력 후 요청하면 명령어가 실행
	```
	test@.|ls||
	```
	- 이 후 응답 결과에서 backup 파일이 나타남
---

### Who am i?
- URL: `http://34.76.107.218/whoami/`
- Walk Throught
	- 페이지 소스보기를 통해 보면 로그인이 가능한 계정 정보를 주고 있음.
	- 프록시를 통해 Authorization 헤더를 보면 base64로 디코딩 되어있음
	- 해당 필드를 admin으로 변경한 뒤 base64로 다시 디코딩 하고 Authorization의 값을 바꿔주면 플래그 획득 가능 

### Searching for the cookie
- URL: `http://34.77.37.110/searching-cookie/`
- Walk Throught
    - 입력창에 `</script><script>alert(document.cookie)</script>` 와 같이 입력 시 플래그가 나타남

### bean
- URL: `https://cybertalents.com/challenges/web/bean`
- Walk Throguht
    - Nginx Directory Traversal을 이용해야하는 문제임
    - 주어지는 환경에서 `gobuster`로 접근가능한 히든 디렉토리 경로를 찾아낸 뒤 `..` 로 접근 가능
    - `Ex` : `/bean/files../`
    - 이후 /etc/home/flag.txt에 플래그 획득 가능

---

## Network

### ARP Storm

- URL: `https://hubchallenges.s3-eu-west-1.amazonaws.com/Forensics/ARP+Storm.pcap`
- Walk Throught
	- pcap 파일은 ARP 프로토콜을 관찰해 복호화면 플래그를 얻을 수 있음
```
import base64
from scapy.all import *

op_chars = []
strings = str()

pcap_data = rdpcap("ARP+Storm.pcap")

for pkg in pcap_data:
	ip_layer =  pkg.getlayer("ARP")
	op_chars.append(ip_layer.op)

for x in op_chars:
	print(chr(x), end="")
	strings += chr(x)

print()

print(base64.b64decode(strings).decode())
```