## 前言

在[ctf](https://so.csdn.net/so/search?q=ctf&spm=1001.2101.3001.7020)比赛中，misc方向是必考的一个方向，其中，图片隐写也是最常见的题目类型，在本篇文章中，将教授以下内容

```plain
1.各种图片文件的头数据以及判断是什么类型的图片
2.png图片隐写
3.jpg图片隐写
4.gif图片隐写
5.bmp图片隐写
6.从图片中提取文件
7.lsb隐写
8.盲水印
9.exif隐写
10.图片宽高修改
……
```

题目以及本文所使用的所有工具项目地址，环境也配置好了，一键安装即可：

```plain
https://github.com/baimao-box/Misc_Picture_Steganography
```

![img](assets/1701657495022-58c3047c-da70-4200-8590-6afe49b3d6b4.png)

安装完后，可以直接在终端输入脚本名称即可运行

![img](assets/1701657495026-5b0c0d19-fcc1-4b7f-a16b-3068febbe63c.png)我不喜欢一开始就在文章前面抛出一大堆生涩的原理，我个人喜欢遇到什么就讲什么，这样也方便理解，各位可以点击右边目录自动跳转到需要的部分

## 什么是计算机文件

文件由一大堆10101110……的二进制码组成，现代大多数电脑的操作系统中，文件是数据的容器，格式主要它的内容定义

## PNG隐写

### 判断图片类型

我们将图片拖入[winhex](https://so.csdn.net/so/search?q=winhex&spm=1001.2101.3001.7020)里，就能看见文件的十六进制码

![img](assets/1701657495096-40250fe4-d52d-478b-a033-a028f80f98d9.png)

文件通过特殊的格式，能让操作系统知道这是一个什么类型的文件

PNG图像格式文件由一个8字节的PNG文件标识域和3个以上的后续数据块如:IHDR、IDAT、IEND等组成

```plain
89 50 4E 47 0D 0A 1A 0A
89：用于检测传输系统是否支持8位的字符编码，用以减少将文本文件被错误的识别成PNG文件的机会，反之亦然
50 4E 47：PNG每个字母对应的ASCII，让用户可以使用文本编辑器查看时，识别出是PNG文件
0D 0A：DOS风格的换行符，用于DOS-Unix数据的换行符转换
1A：在DOS命令行下，用于阻止文件显示的文件结束符
0A：Unix风格的换行符，用于Unix-DOS换行符的转换
```

#### 判断文件格式

![img](assets/1701657495034-4d0cee30-dffb-4e24-8925-251c90e253f1.png)

这是一个exe程序，我们将它拖入winhex里查看

![img](assets/1701657496006-0209e476-8eb0-4301-900d-40961756d51e.png)

可以看到，这个文件头标识为

```plain
89 50 4E 47 0D 0A 1A 0A
```

标准的png图片格式，我们将后缀改为png

![img](assets/1701657496409-c5263fcc-edf1-416d-8c34-315ecead0875.png)

扫码就能获得flag

#### 倒转文件byte

![img](assets/1701657496650-b3c6c332-7075-4994-9ad0-f86877121803.png)

这是一个后缀为jpg的图片，我们用winhex打开这个图片看看

![img](assets/1701657497185-7992e3c6-fc6c-4330-bb10-fa8561c63b74.png)

在最下面，可以看到一个倒过来的PNG和IHDR标识，说明这个png的图片格式都倒过来了，我们需要写一个小脚本来让他复原

```plain
a = open('flag.jpg','rb')  #读取flag.jpg图片的byte数据
b = open('png.png','wb')  #新建一个名为png.png的图片，写入byte数据
b = b.write(a.read()[::-1])  #将flag.jpg图片的byte数据，倒着写入png.png图片里
```

运行脚本，就能得到flag

![img](assets/1701657497129-690c798d-2518-445a-9d67-bd3f6c2aa4d0.png)

![img](assets/1701657497436-aed69bb2-81b8-4158-8269-a440c57f2a6c.png)

![img](assets/1701657498323-8f15f990-d6aa-4d34-8d8a-f83607ec8013.png)

#### 添加文件头数据

![img](assets/1701657498331-d722a678-a56a-4fe7-9bf5-459126c16017.png)

这个图片无法打开，我们拖入winhex里看看

![img](assets/1701657498941-e98d62e0-3161-4b63-9bb0-578ee40a11fc.png)

文件头部只有

```plain
0D 0A 1A 0A
```

而png文件头部为

```plain
89 50 4E 47 0D 0A 1A 0A
```

我们需要写入89 50 4E 47，ctrl+n新建一个文件

![img](assets/1701657499339-e680e9f5-b243-4c5e-ac8d-bd5ef436b86a.png)

随意设置一个大小，然后ctrl+a全选数据，然后ctrl+c复制后粘贴到新文件里

![img](assets/1701657499314-8674d9ee-b4cb-42d8-a8a5-0f35c44aba4b.png)

点击第一个值，写入89 50 4E 47

![img](assets/1701657500089-15edc571-04a0-4278-8a20-ed59e7d77181.png)

然后ctrl+s保存为png格式的文件

![img](assets/1701657501920-8f37a2c7-b42b-4cba-ae62-4fe3df20d6b7.png)

![img](assets/1701657503011-6b718bf1-0e17-45cf-b7fe-cfc64805b332.png)

现在图片就显示正常了

### 图片宽高以及CRC爆破

PNG文件中，每个数据块都由四个部分组成，如下:

```plain
长度(Length)：指定数据块中数据区域的长度，长度不可超过(2^31-1)个字节
数据块类型码(Chunk Type Code)：数据块类型码由ASCII字母(A-Z和a-z)组成的"数据块符号"
数据块数据(Chunk Data)：存储数据块类型码指定的数据
循环冗余检测(CRC)：存储用来检测是否文件传输有误的循环冗余码
```

![img](assets/1701657503472-f1974edf-e992-4573-b154-5ef2c464f306.png)

#### 图片高度修改

![img](assets/1701657503569-df813462-d969-42b2-94b3-36aab4d8621f.png)这是一个png图片，但是感觉高度不太对，我们把图片拖入winhex里

![img](assets/1701657504242-ec389c92-ea11-48d6-9c2e-fdacd8c91c73.png)

修改图片高度的值

![img](assets/1701657504765-be594ca8-41a6-4446-8e67-1cc8830ac161.png)

ctrl+s保存后查看图片

![img](assets/1701657505063-fa3efd98-578b-47e0-8cc9-ada5508cbd79.png)

出现了flag

#### 图片宽度和CRC值爆破

目前手上没这种类型的题，可以去看看落雪wink师傅的文章，因为csdn不让我添加太多外链，所以手动去掉链接中的字符即可

```plain
ht去掉字符tps://blog.csdn.net/weixin_44145452/article/details/109612189
```

## 从图片中提取文件

通过cmd的copy命令，可以将文件隐藏在图片里，我们需要从图片中提取文件，这也是ctf经常考的点

![img](assets/1701657505376-6fd29a11-15e2-4852-96e0-681fe867a0e2.png)

这是一张正常的jpg图片，但是在最下面可以看到一个文件

![img](assets/1701657506304-d8dd748d-6580-4c7b-a358-65477d23a8b4.png)

说明有其他文件在这个图片里，我们需要提取出来

### 通过binwalk提取图片中的文件

binwalk扫描图片内是否存在其他文件

```plain
binwalk dog.jpg
```

![img](assets/1701657506434-f4c40599-6045-4084-ab28-4db685089051.png)

可以看到，这个图片里有一个名为hidden_text.txt的文件，现在我们提取这个文件

```plain
binwalk -e dog.jpg --run-as=root
```

![img](assets/1701657507664-bf28df06-6229-42be-9263-67a8e99483b0.png)

他会自动生成一个文件夹，将提取出来的文件放入这个文件夹里

### 通过foremost提取图片中的文件

我常用的提取工具是foremost，因为他比binwalk更精确一些

```plain
foremost dog.jpg -o dog  //-o：指定输出的文件夹
```

在文件夹里有一个名为audit.txt的文件，这个文件里可以查看一些图片的信息

![img](assets/1701657507843-b68574ed-91ea-46bf-8467-da7a61dfa3a3.png)

![img](assets/1701657507839-ef095034-9074-468c-80c7-a9aa487a543f.png)

## JPG[图片隐写](https://so.csdn.net/so/search?q=图片隐写&spm=1001.2101.3001.7020)

### jpg图片格式

jpg图片的头数据为

```plain
FF D8 FF
```

![img](assets/1701657508411-6389ea42-eab1-4767-b02e-13fdaf6251a8.png)

### jpg图片高度修改

这是一个jpg图片，但是在最下面，可以看到flag的一些信息

![img](assets/1701657509353-9f30d070-4fa8-48fe-9122-0ac038c90316.png)

我们将图片拖入winhex里

![img](assets/1701657509425-0bee66a1-2813-4ba2-844b-98f689d4ad17.png)

我们修改高度，然后ctrl+s保存

![img](assets/1701657509883-e14b5e53-f5df-4d36-9872-c69e9cb99f04.png)

![img](assets/1701657510470-91c583a0-a0c4-4b0f-b7ee-729ed11e037b.png)

就能看见flag了

## EXIF信息

在我们拍摄图片时，exif可以记录数码照片的属性信息和拍摄数据

右击图片，点击熟悉，选择详细信息，这里面可以看到图片拍摄的一些值，有时候还能找到经纬度

![img](assets/1701657510276-f86f9dff-7b36-493a-a517-6ec92ae59b47.png)

在kali里，我们可以用exiftool工具来查看更详细的exif数据

```plain
exiftool cat.jpg
```

![img](assets/1701657511643-8ece26df-eeed-44e0-8430-5a8b79fe08f9.png)

在这里可以看到一串base64编码，我们解密看看

![img](assets/1701657511600-25f28273-aba0-402e-8418-5a52dbbba6a7.png)

得到flag

在做osint类题目时，需要留意图片的exif信息里有没有经纬度，在做不出来题的时候，可以看看图片的exif信息

## BMP图片隐写

### BMP图片格式

BMP 文件格式能够存储单色和彩色的二维数字图像，具有各种颜色深度，并且可以选择使用数据压缩、alpha 通道和颜色配置文件

bmp的头文件数据为

```plain
42 4D
```

![img](assets/1701657511679-a6eaa2b5-f326-430c-9bac-93f3d0f14c34.png)

头数据后四位是图片大小

![img](assets/1701657512856-790f2287-548b-498b-83c2-07f61cfa4f53.png)
由于个人计算机都是以小端序，所以数据要从右往左写

```plain
0x002c268e == 2893454(Byte) == 2.75M
```

![img](assets/1701657512747-9cebb903-1c9d-4c34-afb4-b2aa9029895c.png)

### BMP图片高度修改

![img](assets/1701657513294-a8294d80-26ee-4d14-a6d0-69bc075f3b66.png)

这是一个没有后缀名的文件，我们用winhex打开这个文件

![img](assets/1701657513629-e5c4f44e-7f40-4af3-a0ee-d0f94f2249e0.png)

文件头为42 4D，这是一个bmp文件，我们将后缀名改成bmp

![img](assets/1701657514775-8558b30a-3bd7-46fe-a972-9005289e7632.png)

用ps打开这个图片，可以看到一个假的flag，并且高度也有些不对

这是维基百科对bmp图片结构的解释

```plain
https://en.wikipedia.org/wiki/BMP_file_format
```

![img](assets/1701657514303-0c91258e-af1d-499e-86a5-e0d85748b4cd.png)

![img](assets/1701657514510-6ef98bd3-9249-4dcd-8d99-c6ce63e8580f.png)

我们将32 01 修改为 32 04，再拖进ps里就能看见flag了

![img](assets/1701657516570-354bd2f5-3096-494d-9b92-7c0dde149792.png)

## GIF图片隐写

gif图片是动图，它是由一帧一帧的图片拼接而成

### GIF图片格式

gif头文件数据为

```plain
47 49 46 38 39 61
```

![img](assets/1701657516537-b82dedd2-df16-49be-a8be-a273d46f060b.png)

### GIF帧分离再拼接

![img](assets/1701657516379-d3f69cb1-80e9-49ac-a819-f0a35fdf26fb.png)

这是一个很细的gif图片，我们需要分离它的每一帧后再拼接

```plain
convert glance.gif flag.png   #一帧一帧分割图片
```

![img](assets/1701657517781-1a39d048-ed3d-4f58-93ef-f63f9b0c3093.png)

分离出了很多图片，现在我们要把他们拼成一张图片

```plain
montage flag*.png -tile x1 -geometry +0+0 flag.png     #合并图片
```

![img](assets/1701657518011-2e596eb7-74da-4cf0-b85a-c875dd5843bc.png)

得到flag

### GIF图像格式和特征

有些GIF图片每一帧都可能存在规律，这也是常考的点

![img](assets/1701657517980-38667692-675f-45c6-8e0b-07ae7c8503cd.png)

发现打不开这个gif图片，我们把它拖到winhex里看看

![img](assets/1701657518738-770dc2e9-9bc5-4fd4-83a5-0e885e1a3e4e.png)

发现文件头数据不见了，我们ctrl+n新建一个文档，然后输入gif的头数据

```plain
47 49 46 38 39 61
```

![img](assets/1701657518699-1b226231-c2f2-4118-b191-24bbb395ac50.png)

回到第一个图片数据，ctrl+a全选，然后复制粘贴到新文件里

![img](assets/1701657519882-c7b3c790-2ba1-49d9-adb0-0f790d8841fb.png)

ctrl+s保存

![img](assets/1701657519791-8ca7f6a6-6970-4644-866a-047d2cf3550d.png)

![img](assets/1701657519802-74414519-b2ba-4a1e-abc3-3cc65602ea44.png)

现在就能正常读取gif图片了，但是并没有显示flag，而且图片也不是动图，我们猜测它的每一帧都有规律

现在用identify工具来识别规律

```plain
identify -format "%T" flag.gif
```

![img](assets/1701657521054-9bfda7d3-bb66-4562-8697-d851a509f958.png)

我们将这些值复制出来，新建一个文本文档，将开头的四个6删除过，ctrl+h替换数字

![img](assets/1701657521051-64a4bf19-51c3-41b6-bf95-47a75619e3ff.png)

将10全部替换为1，将20全部替换为0

![img](assets/1701657522165-f68c081b-3100-45d9-9bf2-3e49c083fdfd.png)

把这些二进制值复制下来，去这个网站对应位置粘贴上去

```plain
https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html
```

![img](assets/1701657522172-dd9f2203-0ec9-4cc3-863c-5fe9fe94e12b.png)

得到flag

### GIF每一帧查看

如果想查看gif图片的每一帧，则可以使用Stegsolve工具

![img](assets/1701657522165-0b75c07b-a481-45a0-8bbd-6a2a6382bcb9.png)

选择要查看的图片导入

![img](assets/1701657522575-6860389d-4c16-4704-862c-cf61015b0bb6.png)

选择frame browser即可查看每一帧

或者用pr也行

## 盲水印

盲水印是一种肉眼不可见的水印方式，可以保持图片美观的同时，保护版权，隐藏式的水印是以数字数据的方式加入音频、图片或影片中，但在一般的状况下无法被看见

这里就用官方图片做演示

![img](assets/1701657523224-5b9034cd-5b97-4fea-8db1-d718efd80022.png)

这里有两张一模一样的图片，现在我们查看水印

```plain
bwm decode hui.png hui_with_wm.png flag.png
```

![img](assets/1701657523233-7bb8c929-f849-4471-8d06-a10e906f0889.png)

![img](assets/1701657523498-06aec67d-5d64-4236-a554-9ae1e6eaacea.png)

![img](assets/1701657523474-697e2e7f-745e-44a1-83bd-993d6dc88e27.png)

## LSB隐写

lsb隐写题在ctf中也经常考到，LSB即为最低有效位，我们知道，图片中的图像像素一般是由RGB三原色（红绿蓝）组成，每一种颜色占用8位，取值范围为0x00~0xFF，即有256种颜色，一共包含了256的3次方的颜色，即16777216种颜色。而人类的眼睛可以区分约1000万种不同的颜色，这就意味着人类的眼睛无法区分余下的颜色大约有6777216种。

![img](assets/1701657524366-c0201868-d348-48bc-a41b-a9cee2cac620.png)

LSB隐写就是修改RGB颜色分量的最低二进制位也就是最低有效位（LSB），而人类的眼睛不会注意到这前后的变化，每个像数可以携带3比特的信息。

![img](assets/1701657524403-e12317d1-a9a1-4712-ae17-61975f6d5948.png)

上图我们可以看到，十进制的235表示的是绿色，我们修改了在二进制中的最低位，但是颜色看起来依旧没有变化。我们就可以修改最低位中的信息，实现信息的隐写

这里就需要用到Stegsolve工具了

![img](assets/1701657524994-c53f5dbe-1e30-41d0-9ba3-08c9719bd873.png)

这是一个正常的png图片，但是用binwalk工具发现了这个图片里还隐藏了一张图片

```plain
binwalk final.png 
```

![img](assets/1701657524377-a51372bf-860f-4e17-be4e-92eded436f9c.png)

我们用foremost工具提取图片

```plain
foremost final.png -o flag
```

![img](assets/1701657525212-2a2bb245-4346-409a-b7ee-0a709e36bff8.png)

提取出来的图片名叫00003745.png

![img](assets/1701657525213-a4892a7e-5559-4e47-8dba-a104b3502a36.png)

然后用Stegsolve打开这个图片

![img](assets/1701657525833-ea0fe548-c4f8-4488-8795-ea579c4859fc.png)

![img](assets/1701657525852-25fe3435-e39b-41ee-b517-19684398e264.png)

选择data extract

![img](assets/1701657526942-c73e140e-a69b-4a49-ac03-50a8ad0a60f5.png)

设置red位和lsb模式后，点击preview

![img](assets/1701657526353-bf94d1f5-a0bf-4a6d-87bb-72e2d5b71379.png)

往上查看就能看见flag

![img](assets/1701657526953-12c2656a-92ac-405b-a48d-57367b221803.png)

有些题需要一个一个试，或者使用一开始的图标查看图片有没有什么特殊的变化，然后对应左上角的模式去data extract里查看

![img](assets/1701657526976-972683d8-1477-46cb-8f90-1be0c2a0b819.png)

### 提取图像中的隐藏数据

有些题目是利用LSB的特性来往里面隐藏一些字符串

![img](assets/1701657527932-ffd21466-2a13-4e85-b8c3-c5820425dfc9.png)

这是一张正常的png图片，我们把它拖入winhex里查看

![img](assets/1701657527670-25f9f682-4240-4b33-8952-a0b0de8c226f.png)

在最下面发现了隐藏的图片和一串字符串7his_1s_p4s5w0rd，猜测是lsb隐写解密的key值

现在使用foremost提取图片

```plain
foremost FindHideMsg.png -o test
```

![img](assets/1701657528069-580bee62-aebe-4046-8cdd-0562ab5cbdae.png)

![img](assets/1701657528077-86342cc1-399a-4b7d-aee3-729529944e91.png)

![img](assets/1701657531090-b4c5624a-ed86-4fca-98cb-fea16a3a2111.png)

图片提示我们是lsb隐写，现在我们就需要用到刚刚的key值去解密信息

```plain
lsb extract secret.png flag.txt  7his_1s_p4s5w0rd
//extract：提取，后面为需要提取信息的图片和输出的文件名，以及key值
```

![img](assets/1701657529604-76dc3989-e3fa-46c0-9162-058faac7d92b.png)

## 查看文件里的字符串

有些题目往图片里添加一些字符串，列如上一道题目，我们可以使用strings工具来查看文件里的字符串

![img](assets/1701657529596-c0cdbc1f-6df9-448a-a16d-23ce94ed13ce.png)

这是一张正常的jpg图片，现在我们提取文件里的字符串

```plain
strings hex.jpg
```

![img](assets/1701657529627-a76386db-4bc9-4758-98e4-8a2909949edc.png)

## 总结

很多题目都是考了不同或者多方向的知识点，总之，学得越多越好