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
    boxes_mobile = soup.find_all("div", attrs={"class":"c-params"})
    for detail in boxes_mobile:
        title = detail.h2.span.text.strip()
        print(title)
        spans = detail.find_all("span", attrs={"class":"block"})
        for i in range(len(spans)):
            if spans[i].text == "حافظه داخلی":
                memory = spans[i+1].text.strip().strip(" گیگابایت")
                print(memory)
            if spans[i].text == "مقدار RAM":
                ram = spans[i+1].text.strip().strip(" گیگابایت")
                print(ram)