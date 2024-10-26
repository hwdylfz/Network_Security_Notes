### 一、安装和配置Git

#### 1. 安装Git

- 前往[Git官网](https://git-scm.com/)下载适用于Windows的Git安装程序，完成安装后打开**Git Bash**。

#### 2. 配置Git用户名和邮箱

- 在Git Bash中，输入以下命令，设置你的Git用户名和邮箱：

  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  ```

------

### 二、在Windows上配置SSH密钥

#### 1. 生成SSH密钥

- 打开Git Bash，输入以下命令生成SSH密钥：

  ```
  ssh-keygen -t rsa  -C "youremail@example.com"
  ```

- 当系统提示选择保存位置时，直接按**Enter**，使用默认路径`C:\Users\YourUsername\.ssh\id_rsa`。

- 系统还会提示输入密码，可以按Enter留空，或设置一个用于保护SSH密钥的密码。

#### 2. 将SSH密钥添加到GitHub

- 在Git Bash中，查看生成的SSH公钥：

  ```
  cat ~/.ssh/id_rsa.pub
  ```

- 复制输出的内容（从`ssh-rsa`到结尾的整段文本）。

- 登录[GitHub](https://github.com/)，依次进入**Settings > SSH and GPG keys > New SSH key**，在“Key”栏粘贴刚才复制的公钥内容，并为该密钥设置名称（如“Home PC”），点击**Add SSH key**。

#### 3. 测试SSH连接

- 使用以下命令测试SSH连接是否成功：

  ```
  ssh -T git@github.com
  ```

- 如果配置成功，会显示一条类似“Hi yourusername! You've successfully authenticated...”的消息。

------

### 三、在本地创建项目并推送到GitHub

#### 1. 创建本地代码项目文件夹

- 在Windows资源管理器中，创建一个新文件夹（例如，`MyProject`），用于存放你的项目代码。

#### 2. 初始化Git仓库

- 在Git Bash中，进入你的项目文件夹：

  ```
  cd /c/path/to/your/MyProject
  ```

- 将该文件夹初始化为Git仓库：

  ```
  git init
  ```

#### 3. 添加项目文件

- 将项目文件放入`MyProject`文件夹中，或直接在该文件夹中创建代码文件。

#### 4. 添加并提交文件

- 使用以下命令将所有文件添加到Git的暂存区：

  ```
  git add .
  ```

- 提交这些文件到本地仓库：

  ```
  git commit -m "首次提交"
  ```

#### 5. 创建GitHub仓库

- 登录GitHub，创建一个新仓库（例如，`MyProject`），记住仓库的SSH地址，例如`git@github.com:yourusername/MyProject.git`。

#### 6. 将本地仓库连接到GitHub远程仓库

- 在Git Bash中，运行以下命令，将本地仓库与GitHub上的远程仓库关联起来：

  ```shell
  git remote add origin git@github.com:yourusername/MyProject.git
  ```

#### 7. 推送项目到GitHub

- 使用以下命令将本地项目推送到GitHub远程仓库：

  ```shell
  git push -u origin main   (首次推送需要-u)
  ```

------

### 四、在另一台电脑上同步项目

#### 1. 在第二台电脑上克隆项目

- 在公司或第二台电脑上，打开Git Bash并输入以下命令，将项目克隆到本地：

  ```
  git clone git@github.com:yourusername/MyProject.git
  ```

- 这样第二台电脑会获得GitHub仓库中的项目文件。

#### 2. 在两台电脑之间同步

- **在任意电脑上编辑代码**：完成编辑后，运行以下命令将更改上传到GitHub：

  ```shell
  git add .
  git commit -m "注释内容"
  git push origin main
  ```

- **在另一台电脑上同步代码**：在另一台电脑上运行以下命令拉取最新更改：

  ```shell
  git pull origin main
  ```

### 五、可能存在的问题

#### 1. 代理能访问github，但clone项目时，却克隆失败，显示超时

如果你可以通过代理访问GitHub网页，但在Git Bash中克隆项目时遇到超时问题，通常是因为Git在使用SSH或HTTPS协议时没有正确配置代理。以下是在Windows上配置Git代理的步骤：

##### 解决方案：为Git配置代理

###### 1. 使用HTTP代理配置Git

如果你的代理是HTTP代理，使用以下命令设置代理：

```shell
git config --global http.proxy http://username:password@proxy_address:proxy_port
git config --global https.proxy http://username:password@proxy_address:proxy_port
```

- **username**：代理的用户名和密码（如果有的话）；若没有可以省略。
- **proxy_address**：代理服务器的地址。
- **proxy_port**：代理服务器的端口号。

**例如**，如果代理地址是 `192.168.1.100`，端口是 `8080`，没有用户名和密码，则命令如下：

```shell
git config --global http.proxy http://192.168.1.100:8080
git config --global https.proxy http://192.168.1.100:8080
```

###### 2. 配置SSH使用代理（可选）

如果你通过SSH连接GitHub而非HTTPS，Git Bash的SSH部分也需要通过代理连接。为SSH配置代理的方法如下：

- 打开Git Bash，输入以下命令打开或创建SSH配置文件：

  ```shell
  nano ~/.ssh/config
  ```

- 在文件中添加以下内容：

  ```plantext
  Host github.com
    Hostname github.com
    User git
    ProxyCommand /bin/cmd.exe /c "curl -x http://proxy_address:proxy_port %h:%p"
  ```

  - 将`proxy_address`和`proxy_port`替换为你的代理的地址和端口。

- 保存并关闭文件（在`nano`中，按`Ctrl+X`，然后`Y`确认保存，回车退出）。

###### 3. 验证代理配置

- 尝试克隆项目，检查是否成功：

  ```shell
  git clone https://github.com/yourusername/yourrepository.git
  ```

###### 4. 移除代理配置（如果需要）

- 如果需要移除代理设置，可用以下命令：

  ```shell
  git config --global --unset http.proxy
  git config --global --unset https.proxy
  ```

#### 2. failed to restrict file handles

出现该错误，是因为git版本太低了，解决办法：开启git bash并输入

```
git update（git update-git-for-windows）
```

将Git客户端更新到最新即可。

#### 3. fatal ：remote origin already exists

这个错误表示Git仓库已经有一个名为`origin`的远程仓库，通常会在你重复添加远程仓库时出现。可以通过以下方法解决：

###### 方法1：修改现有的`origin`地址

如果你只是想更新现有的`origin`地址，可以用以下命令替换远程仓库地址：

```
git remote set-url origin <新的远程仓库地址>
```

例如，如果你的新远程仓库地址是`git@github.com:yourusername/yourrepository.git`，可以这样设置：

```
git remote set-url origin git@github.com:yourusername/yourrepository.git
```

###### 方法2：删除现有的`origin`并重新添加

如果你想完全重新添加远程仓库，可以先删除现有的`origin`，然后重新添加。

```
git remote remove origin
git remote add origin <新的远程仓库地址>
```

这样会删除原来的`origin`，并添加新的远程仓库。

##### 4. 首次操作需要输入用户名和密码

就按提示输入用户名和密码即可

##### 5.提交项目代码，空文件夹没有被上传

Git不跟踪空文件夹，如果你想在Git中保留空文件夹，可以使用以下方法：

###### 方法1：在空文件夹中添加占位符文件

你可以在空文件夹中添加一个文件（通常命名为`.gitkeep`），这个文件可以是空的，或者可以包含一些简单的注释。然后Git就会跟踪这个文件夹。操作步骤如下：

1. 在空文件夹中创建一个名为`.gitkeep`的文件：

   ```
   touch path/to/your/empty_folder/.gitkeep
   ```

2. 然后，将这个文件添加到暂存区并提交：

   ```
   git add path/to/your/empty_folder/.gitkeep
   git commit -m "添加空文件夹占位符"
   ```

###### 方法2：使用其他占位符文件

除了`.gitkeep`，你也可以使用其他任何文件名（例如`README.md`或`placeholder.txt`），只要它在文件夹中就可以。

通过以上方法，可以在Git中保留空文件夹。每当你想在Git中创建一个空文件夹时，记得在其中添加一个占位符文件。