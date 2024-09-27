---
tags:
  - picoCTF
  - SQL-injection
  - web
  - Medium
---
# Description

>There is a website running at `https://jupiter.challenges.picoctf.org/problem/39720/` ([link](https://jupiter.challenges.picoctf.org/problem/39720/)) or http://jupiter.challenges.picoctf.org:39720. Do you think you can log us in? Try to see if you can login!

# Walk-Through

문제를 풀기위한 사이트로 접속하면 특정 인물들의 정보가 담긴 페이지가 보인다.

좌측 상단에 메뉴버튼을 클릭하면 사이트 내에서 접근할 수 있는 여러 메뉴들이 나타난다. Admin Login 버튼을 누르면 로그인이 가능한 사이트로 이동한다.
```
https://jupiter.challenges.picoctf.org/problem/39720/login.html
```
간단히 시도해볼 수 있는 건 SQL Injection이다. SQL injection의 기본 페이로드를 입력해보자.
```
username : Admin
Password : 1' or '1 --
```
이후 flag를 얻을 수 있다.

# Notes
- username에 Admin을 입력하는 건 Support에서 관리자 ID가 Admin일 것이라 유추했다.
- 사이트 내에서는 힌트를 발견할 수 없다.  robots.txt도 접근이 되지 않는다. 그러므로 시도할 수 있는 방법(SQLi)를 시도한다.