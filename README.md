# 分布式 GPU 信息显示系统

使用 grpc 进行通信的分布式 GPU 信息显示系统，在实验室以 Ubuntu14.04 为主要操作系统的集群上可以顺利运行。

**New:** 和 [原版](https://github.com/WillQvQ/GPUInfoCollector) 相比大大提升了显卡查询的效率和网页信息更新的频率，便于用户实时了解显卡使用情况。

## 项目结构

### reporter

使用[魔改的gpustat](https://github.com/J-Catherine/gpustat) 进行显卡信息收集和发送

安装方法：

```bash
git clone git@github.com:J-Catherine/gpustat.git
cd gpustat
python3 setup.py install
```

使用方法：

```bash
# 具有原有gpustat的全部功能
gpustat
# 新增的发送显卡信息的功能
gpustat -r {{grpc服务器的ip}}
```

### grpc_server

使用 grpc 与 reporter 进行通信，并把数据存到 mongoDB 的数据库中，详见[文档](./grpc_server)。

### server

暂且使用原版留下的 flask 服务器，但实际上已经已经前后端分离，详见[文档](./server)。

### vue 前端

使用 vue.js 编写的[前端](https://github.com/J-Catherine/GPUInfoVue)，与后端分离，只要能连上内网就可以本地启动。用户可以个性化修改前端显示界面。

### controller

用于批量启动GPU 服务器上的reporter，使用方法如下：

```bash
Usage:
    python3 controller.py <file>  [-k|--kill] [-s|--start]

Arguments:
    file                    The csv file with information of servers

Options:
    -s --start              Start reporters on servers
    -k --kill               Kill all reporters on servers
```


## 改进方向

我不清楚大家的具体需求，欢迎提 Issue