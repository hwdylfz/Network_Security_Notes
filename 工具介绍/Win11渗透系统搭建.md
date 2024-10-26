## 0x00 前言

**https://github.com/arch3rPro/Pentest-Windows  跟着里面选择需要的软件进行安装**

**下一步任务：**

**1、maye启动器**

**4、继续对比物理机工具、win11_pentestsuite_toolkit工具，继续添加完善**



  经过多次更换电脑，重配渗透环境的苦恼之后，下定决心制作一个渗透环境虚拟机（网上也有别人制作的渗透集成环境，但是一个是风格我并不喜欢，另一个，诸多的集成环境都不乏有为了集成而集成的嫌疑，实在是感到没必要。因此，出于刚需以及个性化需求，在此开始制作一个个性化的渗透工作机器镜像，方便迁移）。

## 0x01 系统镜像

```
Windows11_22H2_22621.1992不忘初心精简版镜像  来源：https://www.ghxi.com/win1122h2xnj.html  已激活
```

## 0x02 常规工具（Normal_tools）

```
0.maye启动器
1.bandzip  解压软件
2.Everything  全局搜索
3.WiseCare365 系统优化工具绿色修改版 v6.5.1_Pro（果核剥壳）
4.Clash       vpn管理
5.office2019  已激活
6.python_path
  包含python2、python36、python38(ciphey解密)、python39(其他主力工具包)
7.Java_path
  包含java1.8、java9、java11
```



## 0x03 渗透工具（Sec_tools）

### 1、Web_Tools

|                  Get_Information                   |      Comprehensive_Tools      |                        App_Databases                         |   Cloud_Tools   |    Dictionary    |  Proxy_Tunnel   |     Web_Shell_Manager     |
| :------------------------------------------------: | :---------------------------: | :----------------------------------------------------------: | :-------------: | :--------------: | :-------------: | :-----------------------: |
| Fofa_viewer、mitan(密探，信息收集资产测绘集成工具) |         afrog(扫描器)         |                             JWT                              | oss命令执行.exe | fuzzDicts-master | Proxifier汉化版 |         antSword          |
|                 Ehole3.0(指纹识别)                 | dddd(扫描器)、GUI_Tools工具包 | Jenkins、nacos、Rocket-MQ、redis、shiro、spring、s2、thinkphp、tomcat、weblogic、php |                 |     SaiDict      |                 |         Bbhinder          |
|     GitHack、Githacker、dumpall、ds_store_exp      |       burpsuite_2024.09       |                        MDUT、navicat                         |                 |       sql        |                 |         Godzilla          |
|              御剑、dirsearch、dirmap               |  DudeSuite(扫描器，Poc更新)   |                            sqlmap                            |                 |      upload      |                 |          TianXie          |
|                        nmap                        |        TscanPlus(无影)        |       OA利用工具(apt-tools、the_lostword、IWanaGetAll)       |                 |      待丰富      |                 | Webshell_Generate-1.2.jar |
|                    子域名挖掘机                    |           AuxTools            |              SSTI(fenjing、sstimap、tplmap-0.5)              |                 |                  |                 |                           |

### 2、Intranet_tools

| Get_Information | Comprehensive_Tools |       Proxy_Tunnel       |   Privilege_Escalation    | privilege_Maintenance | Trace_erasure |
| :-------------: | :-----------------: | :----------------------: | :-----------------------: | :-------------------: | :-----------: |
|   mimipenguin   |     Metasploit      |          netcat          | linux-exploit-suggester-2 |                       |               |
|                 |    afrog(扫描器)    |           frp            |  linux-exploit-suggester  |                       |               |
|                 |  CS4.4+CS_Plugins   |     icmpsh+icmpsh_32     | Windows-Exploit-Suggester |                       |               |
|                 |        fscan        | pingtunnel_windows_amd64 |          LinEnum          |                       |               |
|                 |    impacket套件     |        proxifier         |                           |                       |               |
|                 |        Ladon        |         stowaway         |                           |                       |               |

### 3、Misc_Tools

```
1.ToolsFx-1.17.0-jdk8-all-platform    编解码
2.ciphey   智能解码  python38启动
```



### 4、EXP_POC

```
1.windows-kernel-exploits
2.linux-kernel-exploits
```



### 5、AntiAntiVirus





