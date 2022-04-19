学了三个月django，发现最累人的不是代码有多复杂，而是入门诸如编辑器，linux，虚拟机，git等“代码工具”的过程。
这些工具对写代码的意义犹如word，PPT对于写作的意义。

# 总结教训    
接下里我会总结每天遇到的问题，以便需要时查看。    

1.如何将代码上传到github？       
> **完成代码**——>**在github上创建远程仓库**——>**在git中使用git clone的方式在本地建立一个与远程仓库同名的文件夹**——>**把代码全部拖到这个文件夹中**——>**cd进入文件夹**——>**使用git add * 命令把文件夹中的代码全部加入上传队列**——>**使用git commit 命令将队列中的代码载入缓存准备推送**——>**使用git push -u origin main将代码推送到github远程仓库**——>**完成**

2.将github上的代码下载到本地后如何正确运行？
> 需要**配置环境**：这个环境就是指代码依赖的所有模块包的集合，即**虚拟环境**，不同的电脑上模块包会有差异，不一定适用于你从别处拿来的代码。所以你需要针对性地增加或修改本机的环境。
常见的方式就是用**pip安装shell提示的缺失包**，**或者修改文件路径**（因为不同系统上对路径的定义有差异，比如window的桌面位置是C:\\users\adminstrator\desktop在linux上是/mnt/c/users/administrtor/desktop）

3.入门最难的一步，什么是部署?如何部署？
>网络世界可以简化为两台电脑（终端）之间通信。一台电脑请求信息，一台电脑发送信息。请求端叫做客户端（client），发送端叫做服务器（server）。客户端和服务器的联系方式根据信息传输的速度，保真度等性质有TCP和UDP两种。前者由于存在着**请求信息-发送信息-确认收到**的“三次握手”环节，实际上可以对发送的信息做校验，因此传输保真度高，速度稍慢。后者则只有**请求信息-发送信息**的环节，所以传输速度较快，相应地保真度稍低。
>部署就是把个人电脑上的作品发布到公共领域，给更多人访问，即把一个项目从客户端储存到服务器，以便其他客户端在请求这个项目时可以由服务端直接发给他。众所周知，能够支持成百万甚至上亿人访问的服务器必定非常昂贵，所以这个基础设施的建设交给了众多互联网大厂，常见的有阿里云，谷歌云，亚马逊云（AWS）等。**建立本机电脑与云服务器的连接并将项目上传**，这个连接的桥叫做**安全终端模拟软件**,可以理解为古早时期的电话接线员，常见就有Xshell。
>> Xshell怎么使用？    
>Xshell作为SSH远程服务工具，用来沟通你的电脑和服务器。这个XShell的使用里有一些坑，如果事先不知道，会浪费很久的时间。    
- 首先明确**你的本机Linux系统本身是默认关闭SSH服务的！！** 所以你需要先把它打开。    
打开具体步骤为：sudo apt-get update更新所有安装工具的配置-->sudo apt-get remove openssh-server卸载原有的可能有问题的SSH模块-->sudo apt-get install openssh-server 重装SSH模块-->sudo vim /etc/ssh/sshd_config 进入ssh模块配置-->找到PermitRootLogin，把状态改写成Yes，即允许远程登陆-->sudo /etc/init.d/ssh restart重启SSH服务**将本地linux与远程服务器连接**：创建一个与你远程服务器（云服务器）沟通的窗口，里面填入云服务器的公网IP和自己创建的用户密码然后连接。出现“欢迎”字样后，意味着这个Xshell的窗口已经接管你本机Linux系统，此时你只需在Xshell的窗口操作命令
- 两个缓存服务器，Nginx和Gunicorn：nginx是负责初步接收客户端请求的**web服务器**，如果把云服务器当成人们索取食物的大海，那么web服务器的作用相当于一个小湖，简单的静态资源请求（主要指html，css）它可以自己响应，稍复杂的动态资源（代码逻辑跳转）请求则需要转发给**UWSGI类型的服务器**，常见的就是**Gunicorn**。

4.本次练习中用到了哪些业界会要求的重要规则？    
- RESTful: REST是REpresentational State Transfer表述性状态转移的首字母缩写，这是一种被众多开发人员所遵循的架构风格，符合这种风格的开发就被称为RESTful。它有如下六个特点：
  - **客户端 - 服务器** - 通过将用户接口问题与数据存储问题分开，我们通过简化服务器组件来提高跨多个平台的用户接口的可移植性并提高可伸缩性。    
  - **无状态** - 从客户端到服务器的每个请求都必须包含理解请求所需的所有信息，并且不能利用服务器上任何存储的上下文。因此，会话状态完全保留在客户端上。    
  - **可缓存** - 缓存约束要求将对请求的响应中的数据隐式或显式标记为可缓存或不可缓存。如果响应是可缓存的，则客户端缓存有权重用该响应数据以用于以后的等效请求。    
  - **统一接口** - 通过将通用性的软件工程原理应用于组件接口，简化了整个系统架构，提高了交互的可见性。为了获得统一的接口，需要多个架构约束来指导组件的行为。REST由四个接口约束定义：资源识别; 通过陈述来处理资源; 自我描述性的信息; 并且，超媒体作为应用程序状态的引擎。    
  - **分层系统** - 分层系统风格允许通过约束组件行为来使体系结构由分层层组成，这样每个组件都不能“看到”超出与它们交互的直接层。    
  - **按需编码**（可选） - REST允许通过以小程序或脚本的形式下载和执行代码来扩展客户端功能。通过可复用代码来简化客户端。

# Django的一些语法    
django由MTV模型构成，即Model-Templates-Views。    
-model用来定义app的内容，有自定义和外键（ForeignKey）引用两种，前者从零到一地规定app的标题，作者，内容等属性，后者则是将其他app中**已经定义好的属性**引用过来，这样就不用再重新写了。
-templates主要用来管理前端HTML文件，它提供与用户交互的接口，并调用后端views中相应的函数，然后呈现相应的网页效果。静态文件的存在方式有自定义和CDN两种，前者是自己写，后者是远程引用，即在函数后写上所需文件的下载链接就行。
-views是django中相对复杂的部分，它用来定义增删改查四个逻辑动作，比如网站的登陆，修改资料，发表文章，删除文章等。
