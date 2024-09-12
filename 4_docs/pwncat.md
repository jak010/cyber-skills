> Author: jak010
> Date: 2021.05.29
> Handle with Pwncat Summary

## pwncat repository
  - `https://github.com/calebstewart/pwncat`

## Reverse Shell
  - Command
    ```sh
    $ pwncal 0.0.0.0:4444 
    ```

## Modules
  - `pwncat`에서 제공해주는 모듈을 사용하기 위해서는 `CTRL + D` 키를 입력 후 아래와 같은 쉘이 떨어지면 사용가능
    ```sh
    (local) pwncat$
    ```
  - Enumeration
    ```sh
     (local) pwncat$ run enumerate.gather
    ```
  - Automated Privilege Escalation
    ```sh
    (local) pwncat$ run escalate.auto exec user=root shell=/bin/bash
    ```