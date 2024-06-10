import logging  
import logging.handlers  
import os  
import time  
from logging.handlers import TimedRotatingFileHandler  
  
class DailyRotatingFileHandlerWithRename(TimedRotatingFileHandler):  
    def __init__(self, filename, when='D', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None):  
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)  
  
    def doRollover(self):  
        """Override to rename the old file before rotating."""  
        super().doRollover()  
        if self.backupCount > 0:  
            # Get the file extension (e.g., ".log")  
            _, ext = os.path.splitext(self.baseFilename)  
            # Rename all the old log files  
            for i in range(self.backupCount - 1, 0, -1):  
                sfn = self.rotation_filename("%Y-%m-%d" % time.gmtime())  
                if i == 1:  
                    # Rename the existing baseFilename to the new rotated file  
                    dfn = sfn + ext  
                else:  
                    # Rename the older log file to the next oldest  
                    dfn = self.rotation_filename("%Y-%m-%d" % (time.gmtime() - time.timedelta(days=i))) + ext  
                if os.path.exists(dfn):  
                    os.rename(dfn, dfn + ".1")  
                if os.path.exists(sfn + ext):  
                    os.rename(sfn + ext, dfn)  
  
# 配置logger  
logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)  
  
# 创建自定义的handler  
handler = DailyRotatingFileHandlerWithRename('my_log.log', when='D', interval=1, backupCount=5)  
handler.setLevel(logging.INFO)  
  
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
handler.setFormatter(formatter)  
  
# 给logger添加handler  
logger.addHandler(handler)  
  
# 记录日志  
logger.info('This is a log info')