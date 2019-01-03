### NFS服务

- NFS:Network File System 网络文件系统，基于内核的文 件系统。Sun公司开发，通过使用NFS，用户和程序可以像访 问本地文件一样访问远端系统上的文件，基于RPC(Remote Procedure Call Protocol远程过程调用)实现
- RPC采用C/S模式。客户机请求程序调用进程发送一个有进程 参数的调用信息到服务进程，然后等待应答信息。在服务器端 ，进程保持睡眠状态直到调用信息到达为止。当一个调用信息 到达，服务器获得进程参数，计算结果，发送答复信息，然后 等待下一个调用信息，最后，客户端调用进程接收答复信息， 获得进程结果，然后调用执行继续进行。
- NFS优势:节省本地存储空间，将常用的数据如:home目录, 存放在一台NFS服务器上且可以通过网络访问，那么本地终端 将可以减少自身存储空间的使用

#### NFS服务介绍

- 软件包:nfs-utils
- Kernel支持:nfs.ko
- 端口:2049(nfsd), 其它端口由portmap(111)分配
- 配置文件:/etc/exports,/etc/exports.d/*.exports
- CentOS7不支持同一目录同时用nfs和samba共享，因为使用锁机制 不同
- 相关软件包:rpcbind(必须)，tcp_wrappers
- CentOS6开始portmap进程由rpcbind代替
- NFS服务主要进程:
  - rpc.nfsd 最主要的NFS进程，管理客户端是否可登录 
  - rpc.mountd 挂载和卸载NFS文件系统，包括权限管理 
  - rpc.lockd 非必要，管理文件锁，避免同时写出错 
  - rpc.statd 非必要，检查文件一致性，可修复文件
- 日志:/var/lib/nfs/

#### 配置防火墙

- 配置防火墙，开放NFS服务
- 配置NFS使用固定端口
```
vim /etc/sysconfig/nfs
RQUOTAD_PORT=875 
LOCKD_TCPPORT=32803 
LOCKD_UDPPORT=32769 
MOUNTD_PORT=892 
STATD_PORT=662 
STATD_OUTGOING_PORT=2020 
```
- 防火墙除开放上述端口，还需开放TCP和UDP的111和2049 共4个端口





