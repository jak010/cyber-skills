---
tags:
  - picoCTF
  - obfuscation
  - web
  - Medium
---

# Description
 
>   Can you break into this super secure portal? 
   `https://jupiter.challenges.picoctf.org/problem/60786/` ([link](https://jupiter.challenges.picoctf.org/problem/60786/)) or http://jupiter.challenges.picoctf.org:60786

# Walk-Through

[Description](#Description)에서 제공된 문제 링크에 접속하면 인증을 위한 Password를 입력받는 사이트가 보인다. 페이지 소스보기를 통해 해당 사이트 페이지 코드를 보면 다음과 같은 JavaScript 코드가 보인다.
``` javascript
  var _0x5a46 = ['f49bf}', '_again_e', 'this', 'Password\x20Verified', 'Incorrect\x20password', 'getElementById', 'value', 'substring', 'picoCTF{', 'not_this'];
  (function(_0x4bd822, _0x2bd6f7) {
      var _0xb4bdb3 = function(_0x1d68f6) {
          while (--_0x1d68f6) {
              _0x4bd822['push'](_0x4bd822['shift']());
          }
      };
      _0xb4bdb3(++_0x2bd6f7);
  }(_0x5a46, 0x1b3));
  var _0x4b5b = function(_0x2d8f05, _0x4b81bb) {thty
      _0x2d8f05 = _0x2d8f05 - 0x0;
      var _0x4d74cb = _0x5a46[_0x2d8f05];
      return _0x4d74cb;
  };

  function verify() {
      checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
      split = 0x4;
      if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3')) {
          if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n') {
              if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {
                  if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT') {
                      if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {
                          if (checkpass['substring'](0x6, 0xb) == 'F{not') {
                              if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {
                                  if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7')) {
                                      alert(_0x4b5b('0x8'));
                                  }
                              }
                          }
                      }
                  }
              }
          }
      }
  }
```
코드가 난독화(obfuscation) 되어 있어서 무엇을 검증하는지 알아보기 어렵다. 그러나 `_0x5a46` 로 선언된 변수의 리스트를 보면 Flag를 암시하는 값들이 들어있다.
```
var _0x5a46 = ['f49bf}', '_again_e', 'picoCTF{', 'not_this'];
```
위 변수들을 서순에 따라 재배열하면 다음과 같은 텍스트를 만들어낼 수 있다.
```
picoCTF{not_this_again_ef49bf}
```
위 문자가 이 문제의 flag다.

# Notes
읽을 수 있는 힌트를 보고 직감으로 flag를 만들어냈지만 다른 풀이를 보니 직접 난독화된 소스를 보면서 하나하나 추적해가는 형식으로 접근하는 문제인 듯 하다.