# server

使用 flask 编写的服务器后端，用于返回显卡信息数据和静态主页

## API

| url       | methods | 内容                    |
| --------- | ------- | ----------------------- |
| /         | GET     | 返回静态主页            |
| /data/all | GET     | 返回JSON 格式的显卡信息 |

## 使用方法

```bash
# 安装依赖
pip3 install -r requirements
# 运行服务器
python3 app run
# 进入调试模式
python3 app dev
```

### 