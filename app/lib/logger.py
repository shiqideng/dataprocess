import logging
import logging.handlers
import requests


from app.lib import Module


# 配置日志记录器
logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

# 配置 TimedRotatingFileHandler，按照每天切片
file_handler = logging.handlers.TimedRotatingFileHandler('log/log.log', when='midnight', interval=1, backupCount=7, encoding="utf-8")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 配置 SocketHandler，用于将日志上传到服务器 127.0.0.1 的某个端口（假设端口为 9999）
# socket_handler = logging.handlers.SocketHandler('127.0.0.1', 9999)
# socket_handler.setLevel(logging.INFO)  # 设定级别为 INFO 及以上
# logger.addHandler(socket_handler)

# 记录不同级别的日志消息
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

def uploadLogToServer(logFilePath):
    """
    上传日志文件到服务器的函数

    logFilePath: 日志文件路径
    return: dict {"reg": 1, "msg": "上传成功"}
    """
    message = "上传成功"
    logFiles = {'file': open(logFilePath, 'rb')}
    url = Module.getConfig("conf/config.ini", "Server", "uploadLogURL")
    if url["reg"] == 1:
        # 尝试上传，最多重试2次
        for attempt in range(3):  # 尝试次数包括第一次尝试，所以是3
            try:
                with open(logFilePath, 'rb') as file:
                    files = {'file': file}
                    response = requests.post(url["msg"], files=logFiles)
                    
                    # 如果上传成功（HTTP状态码200），则返回成功信息并跳出循环
                    if response.status_code == 200:
                        return {"reg": 1, "msg": message}
                    else:
                        message = f'第{attempt + 1}次尝试上传失败，状态码：{response.status_code}'
            except Exception as e:
                pass
                
            # 如果不是最后一次尝试，则等待一段时间后重试
            if attempt < 2:
                import time
                time.sleep(2)  # 等待2秒后重试
                
        # 所有尝试都失败后，返回失败信息
        return {"reg": 0, "msg": message}