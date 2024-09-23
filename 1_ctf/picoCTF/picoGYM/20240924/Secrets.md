---
tags:
  - picoCTF
  - web
  - Trailing-Slash
  - Medium
Date: 2024-09-24T03:59:00
---

# Description
> We have several pages hidden. Can you find the one with the flag?
> Additional details will be available after launching your challenge instance.

# Walk-Throught

문제 instance를 실행하면 web page로 접속할 수 있는 링크가 하나 열린다. web page에 접속하면 다음 글귀가 보인다.
```
If Security wasn't your job, would you do it as a hobby?
```
문제 풀이에 딱히 단서로 사용할 수 있만한 글귀는 아닌듯 싶다. Inspector로 page롤 들여다보면 하나의 페이지 링크가 노출된다.
```
...
<div class="imgcontainer">
      <img
        src="secret/assets/DX1KYM.jpg"
        alt="https://www.alamy.com/security-safety-word-cloud-concept-image-image67649784.html"
        class="responsive"
      />
      <div class="top-left">
        <h1>If security wasn't your job, would you do it as a hobby?</h1>
      </div>
    </div>
```
"secret/assets/DX1KYM.jpg" 라는 위치가 눈에 띄는데 secret를 가리키는 위치로 이동하자. 
```
http://saturn.picoctf.net:53513/secret/
```
이동 후의 페이지를 inspector로 찾아봐도 flag는 보이지 않는다. 그러나 다음과 같은 위치가 html source에서 눈에 띈다.
```
<link rel="stylesheet" href="hidden/file.css" />
```
secret으로 이동한 위치에서 "hidden" 으로 이동해보자.
```
http://saturn.picoctf.net:53513/secret/hidden/
```
이번엔 UserName과 Password를 입력하는 InputBox가 보인다. 이러나 저러나 html source를 들여다봐야하는 건 마찬가지다.  이번엔 html source에 다음과 같은 링크가 보인다.
```
<link href="superhidden/login.css" rel="stylesheet" />
```
눈에 띄는 건 superhidden이다. 다시 접근해보자.
```
http://saturn.picoctf.net:53513/secret/hidden/superhidden/
```
위 사이트로 접속하면 다음과 같은 글귀가 보인다.
```
Finally, You found me, But can you see me
```
페이지를 마우스로 드래그하면 flag가 보인다.

# Notes

## Trailing Slash

URL을 여러번 대입해보면서 풀었다. 다른 풀이를 읽어보니 이 문제에는 후행 슬래쉬라고 불리는 요소를 알아두면 도움이 된다.

후행 슬래쉬란 경로 끝에 슬래시(/) 를 삽입하는 것으로 다음과 같은 차이가 있다.

1. 후행 슬래쉬를 사용하는 경우 (Ex, `./secret/`)
	- 후행 슬래쉬를 사용하는 경우 서버는 이를 디렉토리로 취급한다. 즉, 후행 슬래쉬가 포함된 경로로 접근면 디렉토리 내의 기본 페이지를 리턴한다. (물론 그렇게 설정이 되어있는 경우이다.)
2. 후행 슬래쉬를 사용하지 않는 경우(Ex, `./secret`)
	- 후행 슬래쉬를 사용하지 않는 경우는 서버는 이를 파일로 취급한다. 즉 해당 파일의 존재 여부에 따라서 서버는 응답을 내려줄 것이다.