import pandas as pd
import datetime


def detectEncoding(filePath):
    encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin1']
    error_msg = "Unknown encoding"
    
    try:
        for encoding in encodings:
            try:
                df = pd.read_csv(filePath, encoding=encoding)
                return df
            except UnicodeDecodeError:
                pass
        raise UnicodeDecodeError(error_msg)
    except UnicodeDecodeError as e:
        if str(e) != error_msg:
            print(e)
        return None
    

def logFormat(Type, message):
    if Type == "DEBUG":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffff00;'> [Waring] </span>" + message
    elif Type == "INFO":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#00aa00;'> [INFO] </span>" + message
    elif Type == "WARRING":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffaa00;'> [Waring] </span>" + message
    elif Type == "ERROR":
        return  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#aa00ff;'> [Error] </span>" + message
    elif Type == "FATAL":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ff0000;'> [FATAL] </span>" + message