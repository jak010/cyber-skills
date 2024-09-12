
# Reference

## X-forwareded-for

```warp-runnable-command
현재까지 거쳐온 서버의 IP에 대한 정보를 가지고 있음, IP 필터링 우회를 위해 사용할 수도 있는 것으로 보임
Example >>
curl -H "X-Forwarded-For:127.0.0.1" -XGET http://DNS
```

## Cookie

```warp-runnable-command
클라이언트에 저장되는 쿠키의 값을 변조해서 플래그를 얻을 수 있음
Case 1, HackCTF : Cookie
- Cookie Value를 base64 디코딩
- Cookie에 저장된 값을 bypassing (php)
```

# SSRF

```warp-runnable-command
: Server-Side Request Forgery 
: 서버가 사용자 입력을 받아 직접 웹이나 포트에 접근해 데이터를 가져오는 기능에서 발생
Case1, HackCTF : LOL
```