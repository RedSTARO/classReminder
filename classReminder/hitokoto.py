import requests
import ast
from debug import *

url = "https://v1.hitokoto.cn?c=d&c=k&c=i"
# TODO: Use "https://v1.hitokoto.cn?c=d&c=k&c=i&encode=json" to get json form; or "https://v1.hitokoto.cn?c=d&c=k&c=i&encode=text" to get pure text.
# Details at "https://developer.hitokoto.cn/sentence/#%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

def hitokoto():

    hitokotoRes = requests.get(url, headers=headers).text
    hitokotoResDict = ast.literal_eval(hitokotoRes)
    # log(hitokotoRes)

    hitokotoSentence = hitokotoResDict["hitokoto"]
    hitokotoFrom = hitokotoResDict["from"]
    hitokotoDict = {"Sentence":hitokotoSentence, "From":hitokotoFrom}

    log(f"Matched hitokotoSentence:{hitokotoSentence}")
    log(f"Matched hitokotoFrom:{hitokotoFrom}")
    log(f"Total hitokoto dict:{hitokotoDict}")
    return hitokotoDict

if __name__ == "__main__":
    hitokoto()
