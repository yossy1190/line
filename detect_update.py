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
    new_elems=soup.select(".type_acceptable")
    new_elem=str(new_elems[1])
    print(new_elem)

    try:
        with open("old_elem.txt") as f:
            old_elem=f.read()
    except:
        old_elem=""

    if new_elem==old_elem:
        print('更新はありません')
        line.main(f"更新はありません。リンクを確認してください。\n{url}")
        return True
    else:
        with open("old_elem.txt","w") as f:
            old_elem=f.write(new_elem)
        print('更新されました')
        line.main(f"もうすぐ満席です。")
        return False
    
detect_update()
