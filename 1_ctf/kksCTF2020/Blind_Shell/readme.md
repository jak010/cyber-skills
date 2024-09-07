# Blind Shell
```
https://open.kksctf.ru/tasks/5126ef4e-b7a9-4f4a-8d65-b64d24be1c61
```

## Walk Throught
```
[obtain infor]
1. ls | wc -l | grep 1 -> Failed!
2. ls | wc -l | grep 2 -> Failed!
3. ls | wc -l | grep 3 -> Success!


[Guessing FILE]
$ ls | grep ^flag.txt


```