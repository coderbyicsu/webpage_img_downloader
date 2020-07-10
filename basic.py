import os
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


srouce_url = "https://marroncake.tistory.com/entry/180728-%EC%9D%BC%EC%A7%80%EC%95%84%ED%8A%B8%ED%99%80-%ED%8C%AC%EC%8B%B8%EC%9D%B8%ED%9A%8C-%EB%A7%88%EB%A7%88%EB%AC%B4-%ED%9C%98%EC%9D%B8"

os.makedirs("./img/",exist_ok=True)

playload = {"user-agent":generate_user_agent()}
res = requests.get(srouce_url, headers=playload)

soup = BeautifulSoup(res.content, 'html.parser')


for i, img in enumerate(soup.select(".area_view img")):
    img_path = "./img/第"+str(i+1)+"張圖片.jpg"
    img_res = requests.get(img["src"])
    
    with open(img_path,"wb") as f:
        f.write(img_res.content)
    
    print("第"+str(i+1)+"張圖片")