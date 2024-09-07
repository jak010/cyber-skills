# NACTF2020

## INSPECT :50
```
http://inspect.challenges.nactf.com/style.css 에 접속하면 flag 획득

nactf{1nspect1ng_sp13s_4_lyf3}
```

## Missing Image : 75
```
https://hidden.challenges.nactf.com/flag.png 에 접속하면 flag 획득

nactf{h1dd3n_1mag3s}
```


## Forms : 125
```
view-source:https://forms.challenges.nactf.com/ 에 접속한 뒤 javaScipt코드를 읽고
verify 함수가 호출되는 지점을 찾아 request 시 flag 획득

nactf{cl13n75_ar3_3v11}
```

## Calculator : 150
```
https://calculator.challenges.nactf.com/index.php 사용자가 입력하면 문자열을 그대로 출력하는 
걸로 eval() 함수를 사용하는 것을 예측 가능 

[Eval Point]
- 포인트는 eval() 함수가 어떤 언어를 통해 사용되고 있는지를 파악해야됨 
-> 페이지 소스 보기를 통해 form 태그에서 index.php에 submit 하고 있으므로 php 인 것으로 추측가능

[PHP calling variables]
php 에서 '$'을 이용하면 변수에 바인딩 된 값을 불러올 수 있음 그러니 요청 $flag로 플래그 획득 가능

nactf{ev1l_eval}
```

## Cookie Recipe : 150
```
https://cookies.challenges.nactf.com/auth.php

[Point]
- id나 pw에 아무 값이나 입력하면 로그인이 된다
- 로그아웃을 하고 돌아와서 쿠키 값을 보게 되면 로그인 했던 정보들이 쿠키에 저장되있는 걸 확인가능

[Cookie Expiration Age]
- Cookie의 속성 중 Expires에서 값을 "Session"으로 설정하게 되면 Cookie 만료가 사라짐

위를 이용하여 로그인 했던 이름으로 재 로그인시 플래그 획득 가능

nactf{c00kie_m0nst3r_5bxr16o0z}
```

## Login : 175
```
https://login.challenges.nactf.com/

[Point]
- 간단한 sql injection 문제

[Payload]
- admin' or '1' ='1
- # 

nactf{sQllllllll_1m5qpr8x}
```