# 安捷伦5200/5300/5400数据处理软件开发文档

## 一、开发环境

1、开发语言：Python3.12

2、Package

```shell
altgraph==0.17.4
blinker==1.8.2
certifi==2024.6.2
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
et-xmlfile==1.1.0
Flask==3.0.3
idna==3.7
install==1.3.5
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
numpy==1.26.4
openpyxl==3.1.3
packaging==24.0
pandas==2.2.2
pefile==2023.2.7
pyinstaller==6.8.0
pyinstaller-hooks-contrib==2024.7
PySide6==6.7.1
PySide6_Addons==6.7.1
PySide6_Essentials==6.7.1
python-dateutil==2.9.0.post0
pytz==2024.1
pywin32-ctypes==0.2.2
requests==2.32.3
setuptools==69.5.1
shiboken6==6.7.1
six==1.16.0
tzdata==2024.1
urllib3==2.2.1
Werkzeug==3.0.3
wheel==0.43.0

```

4、文件目录结构

```shell
├─app
│  ├─conf
|  │  └─
│  ├─core
│  │  └─__pycache__
│  ├─lib
│  │  └─__pycache__
│  ├─log
│  ├─resource
│  ├─ui
│  │  └─__pycache__
│  └─__pycache__
├─build
│  ├─DataProcess
│  │  └─localpycs
│  └─startup
│      └─localpycs
└─dist
```

5、返回值

函数返回值分为dict，reg为函数执行状态，0为失败，1为成功；

当函数执行成功，msg返回为成功消息或函数执行结果；

当函数执行失败，msg返回报错信息，并将报错信息记入log文件；

```python
{"reg":1, "msg":"massage"}
```

## 二、变量定义

## 三、判定逻辑

## 其他

```shell
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package
```
