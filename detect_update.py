from encodings import utf_8
from bs4 import BeautifulSoup
import requests
import re
import line
# import utf_8

def detect_update():
    url="https://www.statusparty.jp/schedule/tokyo/ginza/13019/"
    res=requests.get(url)
    soup=BeautifulSoup(res.text,"html.parser")
    
    try:
        femail=soup.select(".female")
        new_elem=str(soup.select(".type_only_remaining"))
        print(new_elem)
    except:
        new_elem=""
        
    try:
        with open("old_elem.txt") as f:
            old_elem=f.read()
    except:
        old_elem=""

    if new_elem==old_elem:
        print('更新はありません')
        line.main(f"更新はありません。")
        return True
    
    else:
        with open("old_elem.txt","w") as f:
            f.write(new_elem)
        print('もうすぐ満席です。')
        line.main(f"もうすぐ満席です。リンクを確認してください。\n{url}")
        return False
    
detect_update()
