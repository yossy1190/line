from encodings import utf_8
from bs4 import BeautifulSoup
import requests
import re
import line
# import utf_8

def detect_update():
    url="https://www.statusparty.jp/schedule/tokyo/ginza/13124/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    
    try:
        femail=soup.select(".female")
        # new_elem=str(soup.select(".type_waiting"))        
        new_elem=str(soup.select(".type_only_remaining"))        
        # print(new_elem)
    except:
        new_elem=""

# [<span class="type_waiting"> キャンセル待ち</span>]
    with open("50PS管理ツール/remain_elem.txt","r",encoding='utf-8') as f:
        remain_elem=f.read()
        # wating_elem=f.read()
    # with open("wating_elem.txt","r") as f:
    #     wating_elem=f.read()
 
    if new_elem==remain_elem:
        line.main(f"testです。\n{url}")
    else:
        line.main(f"女性がもうすぐ満席です。リンクを確認してください。\n{url}")
        return True
        # line.main(f"女性が満席です。リンクを確認してください。\n{url}")
        # return True
    
detect_update()
