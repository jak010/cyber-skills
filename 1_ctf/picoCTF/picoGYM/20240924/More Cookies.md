---
tags:
  - picoCTF
  - web
  - cookie
  - CBC-Bit-Flip-Attack
Date: 2024-09-24T17:00:00
---
# Description
> I forgot Cookies can Be modified Client-side, so now I decided to encrypt them!


# Approach

문제 제목에 "Cookie"가 드러나 있기에 Cookie와 관련된 문제라고 유추했다. 문제 사이트에 접속하면 Cookie에 다음과 같은 값이 보인다.
```
eGZsVDZLTDlrckZaZnZZNnJ4Z3Z3QkJ3TEdyQ2IwbTNVR0lEYldiNXdOMFB2V1dGSTRjL0lZUmhSUXBYSEx6SW5KWFBsV3RIUXQyY3V2elh4M0lZZkwvdTlPRXkzV2ZKaDViY2NOZGdjclFUL2svZDFYTEo4VWt0OEl1QjVUbVQ=
```
이를 base64로 디코딩하면 다음과 같은 값이 다온다.
```
a4yJAptmftKXgnCJybEe9wWnKFMWzHG7Ja9QPpiYBJjHgYcoToai9NK04ju+h6BqK5/f9CYkki+hZ8VR38r1yeK9dobc23d8
```
문제 사이트에서는 Admin으로 로그인하면 flag가 보일것이라고 한다. 어떤 암호문을 base64로 디코딩이 가능하다는 사실을보고 "어떤 평문을 base64로 인코딩" 하는 Brute-Force를 하면 될 것이라는 지레짐작은 했지만 "어떻게?" 라는 생각만 떠오를 뿐 실질적인 풀이 방법은 떠오르지 않았다.

다른 풀이를 참고하니 CBC 암호와 Bit Flip Attack이란 것을 알게되었고 이 문제를 통해 개념을 익히고 실습을 해봤다.


##  CBC Mode?
그렇다면 CBC가 무엇이길래 CBC Bit Flipping Attack 같은게 가능할까? 다음은 CBC 모드에 관련된 몇 가지 사실을 나열한 것이다.

- CBC(Cipher Blck Chaning) 모드는 블록 암호화 방식 중 하나로 각 블록을 암호화 할 때 이전 암호문 블록의 결과를 활용하여 암호문의 의존성을 높이는 방식이다.
	- CBC 모드에서 첫 번쨰 평문 블록을 암호화 할 떄는 이전 블록이 존재하지 않는다. 이 떄는 "초기화 벡터(IV)"를 사용하여 첫번째 평문 블록과 XOR 연산을 수행한다.
	- CBC 모드는 각 평문 블록을 암호화기전에 이전 블록의 암호문을 XOR 연산한다.
	- 이 과정을 반복하면서 전체 평문을 암호화한다.
- CBC 모드는 보통 DES, AES 같은 블록 암호화 알고리즘과 함깨 사용된다. 

##  Bit Flipping Attack ?

한국어로 설명된 자료가 별로 없어서 Chatgpt를 이용했다. CBC Bit Flling Attack에 대해서 Chatgpt는 다음과 같이 설명한다. 

> CBC 비트 플리핑  공격은 **암호화 방식 중 하나인 CBC (Cipher Block Chaining) 모드를 이용한 공격**으로, 특히 **패딩 오라클 공격과** 관련이 깊습니다. 이 공격의 기본 목표는 암호문을 수정하여 해독된 평문에 원하는 변경을 유도하는 것입니다.

간단한 정리하자면 "암호문을 수정하여 평문에 원하는 변경을 가한다"라는 골자인듯 싶다. 비트 플리핑에 대한 추가 설명에 대해서는 ChatGpt는 다음과 같이 알려준다.

> CBC 모드는 각 블록을 XOR 연산으로 처리하므로, 암호문 블록에서 특정 비트를 조작하면 해당 평문 블록이 복호화될때 그 부분이 변경됩니다. 공격자는 이를 이용해 평문을 조작할 수 있습니다.



# Walk-Throught
다시 문제로 돌아와보자. 문제 풀이에 사용할 수 있는 개념인 CBC와 CBC Bit Flipping  Attack을 알게 되었다. 그런데 이 개념을 알았다고해서 발견한 암호문이 CBC 모드를 이용해서 암호화가 되었단 걸 어떻게 알 수 있을까?

아마 불가능할 듯 싶다. 다른 풀이에서는 문제 설명에 CBC를 암시하는 글자가 숨겨져 있다고 한다. Description에 인용해놓은 문장은 More Cookies에 대한 문제 설명이다. 

>I forgot Cookies can Be modified Client-side, so now I decided to encrypt them!

자세히 보면 알파벳 C와 B가 대문자로만 되어있다. 개인적으로는 이 부분을 보면서 뭔가 억지 아닌가라는 생각이 든다.

어쨌든 계속 풀이를 이어나가보자. CBC-Bit-Flipping 공격을 가하기 위해선 스크립트를 작성해야한다.
```python
import base64    
import requests  
  
cipher_text = "MG5RT3QzcGZkZWhCNnJUcVR6QXlNN2ZvYkxsS3RFcjk4Q1V4clpvQjBrT3hBMlB0K2hEU2NhV0QyeVlZY28rVzZ4eXFGa3k3emFmTENjU3c2MGF2dGNaSC8vMkdWMXNVSHZ0d3U2U1BoSGltaG5WT0kxbFBVdDVSMmh0K3lyNUo="    
  
def bit_flip(position, bit, data):  
	raw_text = base64.b64decode(data)  
	  
	ord_list = list(raw_text)  	  
	ord_list[position] = ord(chr(bit_list[position] ^ bit))
	  
	c = ''.join([chr(x) for x in bit_list])  	
	return base64.b64encode(c.encode()).decode()  
  
  
if __name__ == '__main__':  
	for x in range(128):  
		for y in range(128):  
			random_base64 = bit_flip(x, y, data=cipher_text)  
			cookies = {'auth_name': random_base64}  
			r = requests.get('http://mercury.picoctf.net:25992/', cookies=cookies)  
			if "picoCTF{" in r.text:  
				print(r.text)  
				break
```

"cipher_text"는 문제 사이트에 접속했을 때 얻을 수 있는 base64로 encoding 되어있는 문자열이다. 이를 기준으로 bit_flip 함수에서 base64로 다시 decoding하여 list로 변환해준다. 
```
raw_text = base64.b64decode(data)
```
base64로 data를 deocding 하면 리스트의 각 인덱스별 문자에 맞는 ord가 들어가있다.
```
ord_list = list(raw_text)
```
이제 list의 각 인덱스를 이동해가면서 xor 연산을 가해주자.
```
ord_list[position] = ord(chr(bit_list[position] ^ bit))
```
이제 나머지는 이를 다시 base64로 인코딩하여 flag를 획득할 때 까지 서버에 계속 요청을 보내는 작업이다.