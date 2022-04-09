# django-project
我的第一个项目，充满血泪史。
学了三个月django，发现最累人的不是代码有多复杂，而是入门诸如编辑器，linux，虚拟机，git等“代码工具”的过程。
这些工具对写代码的意义犹如word，PPT对于写作的意义————使用熟练的人能够通过这些工具提高工作效率，而不会的人或者使用不熟练的人则要被这些工具的逻辑和条框反复折腾，而简中网上太多误人子弟的垃圾指南，更是让这种痛苦还要加倍！

# 总结教训    
接下里我会总结每天遇到的问题，以便需要时查看。    

1.如何将代码上传到github？       
> **完成代码**——>**在github上创建远程仓库**——>**在git中使用git clone的方式在本地建立一个与远程仓库同名的文件夹**——>**把代码全部拖到这个文件夹中**——>**cd进入文件夹**——>**使用git add * 命令把文件夹中的代码全部加入上传队列**——>**使用git commit 命令将队列中的代码载入缓存准备推送**——>**使用git push -u origin main将代码推送到github远程仓库**——>**完成**

2.将github上的代码下载到本地后如何正确运行？
> 需要**配置环境**：这个环境就是指代码依赖的所有模块包的集合，即**虚拟环境**，不同的电脑上模块包会有差异，不一定适用于你从别处拿来的代码。所以你需要针对性地增加或修改本机的环境。
常见的方式就是用**pip安装shell提示的缺失包**，**或者修改文件路径**（因为不同系统上对路径的定义有差异，比如window的桌面位置是C:\\users\adminstrator\desktop在linux上是/mnt/c/users/administrtor/desktop）

3.什么是部署?如何部署？
>网络世界可以简化为两台电脑（终端）之间通信。一台电脑请求信息，一台电脑发送信息。请求端叫做客户端（client），发送端叫做服务器（server）。客户端和服务器的联系方式根据信息传输的速度，保真度等性质有TCP和UDP两种。前者由于存在着**请求信息-发送信息-确认收到**的“三次握手”环节，实际上可以对发送的信息做校验，因此传输保真度高，速度稍慢。后者则只有**请求信息-发送信息**的环节，所以传输速度较快，相应地保真度稍低。
>部署就是把个人电脑上的作品发布到公共领域，给更多人访问，即把一个项目从客户端储存到服务器，以便其他客户端在请求这个项目时可以由服务端直接发给他。众所周知，能够支持成百万甚至上亿人访问的服务器必定非常昂贵，所以这个基础设施的建设交给了众多互联网大厂，常见的有阿里云，谷歌云，亚马逊云（AWS）等。**建立本机电脑与云服务器的连接并将项目上传**，这个连接的桥叫做**安全终端模拟软件**,可以理解为古早时期的电话接线员，常见就有Xshell。
