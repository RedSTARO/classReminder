import datetime
import pytz
import sys
import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")
conf = configparser.ConfigParser()
conf.read(configPath)

timeZone = pytz.timezone("Asia/Shanghai")
path = conf.get("path", "log")

def log(str_, level = "info"):
    print(str_)
    whichFun = str(sys._getframe().f_back.f_code.co_filename).split("/")[-1].split("\\")[-1]
    if level = "info":
    	with open(path + "logs_info.log", "a") as logFile:
        	logFile.write(f"[{str(datetime.datetime.now(timeZone).replace(tzinfo=None))}]" + 
                      	f"[{whichFun}] " + 
                      	str(str_) + 
						  "\n")
	elif level = "error":
		with open(path + "logs_error.log", "a") as logFile:
        	logFile.write(f"[{str(datetime.datetime.now(timeZone).replace(tzinfo=None))}]" + 
                      	f"[{whichFun}] " + 
                      	str(str_) + 
						  "\n")
	elif level = "warning":
		with open(path + "logs_warning.log", "a") as logFile:
        	logFile.write(f"[{str(datetime.datetime.now(timeZone).replace(tzinfo=None))}]" + 
                      	f"[{whichFun}] " + 
                      	str(str_) + 
						  "\n")

log(f"Matched config.ini, in path {configPath}")

def pathGeter(fileClass):
    name = conf.get("path", fileClass)
    log(f"Matched {fileClass} path")
    return name


if __name__ == "__main__":
    log("Test LOG Module")
