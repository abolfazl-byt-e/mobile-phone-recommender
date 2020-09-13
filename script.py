import requests
from bs4 import BeautifulSoup

url_page = "https://www.digikala.com/search/category-mobile-phone/?brand[0]=18&brand[1]=1662&brand[2]=82&brand[3]=10&brand[4]=22&brand[5]=26&brand[6]=1&attribute[A202][0]=292&type[0]=201&pageno=1&sortby=4"
r = requests.get(url_page)
soup = BeautifulSoup(r.content, 'html.parser')
boxes = soup.find_all("div", attrs={"class":"c-product-box"})
for box in boxes:
    url_box = "https://www.digikala.com" + box.a["href"]
    r = requests.get(url_box)
    soup = BeautifulSoup(r.content, "html.parser")
    boxes_mobile = soup.find_all("section", attrs={"class":"c-product__info"})
    for mob in boxes_mobile:
        title = mob.h1
        print(title.text.strip())