# 安捷伦5200/5300/5400数据处理软件开发文档

## 一、更新日志

v0.1.0(beta)

- 新增
  - 新增图片重命名模块
  - lims上传结果表格数据从字符串改为整数
- 优化
  - 优化运算速度

v0.0.2(beta)

- 新增
  - 导出数据时同时导出原始计算结果和lims上传结果
  - lims上传结果表格最后3列清空内容
- 优化
  - 优化无明显目的峰摩尔浓度判定规则（<500pmol/L）
  - 优化导出成功提示窗口结果描述

v0.0.1(beta)

- 初始版本

## 二、开发环境

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

函数返回值为字典格式

当函数执行成功，则返回：
```python
{"reg": 1, "msg": "massage"}
# message为成功消息或执行结果
```
当函数执行失败，则返回：
```python
{"reg": 0, "msg": "massage"}
# message为报错信息
```

## 三、判定逻辑
使用5400的Smear Analysis表作为参考，Smear区间需提起在ProSize Analysis软件中存为配置文件，结果分析时直接导入

可按照各SmearPeak的质量浓度或摩尔浓度的占比作为判定依据（根据实验情况自由调整）

## 四、其他

### 1、安装package

```shell
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package
```

### 2、打包

```shell
pyinstaller -w .\app\startup.py -i .\app\resource\logo.ico -n DataProcess
```
