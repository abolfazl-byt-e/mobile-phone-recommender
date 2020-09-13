import requests
from bs4 import BeautifulSoup
import re
import mysql.connector as mysql

cnx = mysql.connect(user="root", password="",host="127.0.0.1", database="digikala")
cursor = cnx.cursor()
query = "insert into mobile (title, memory, ram, network, android) values (%s, %s, %s, %s, %s)"
## 17 page
for i in range(1,18):
    url_page = "https://www.digikala.com/search/category-mobile-phone/?brand[0]=18&brand[1]=1662&brand[2]=82&brand[3]=10&brand[4]=22&brand[5]=26&brand[6]=1&attribute[A202][0]=292&type[0]=201&pageno=%i&sortby=4"%(i)
    print(i)
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
            # print(title)
            spans = detail.find_all("span", attrs={"class":"block"})
            try:
                for i in range(len(spans)):
                    if spans[i].text == "حافظه داخلی":
                        memory2 = spans[i+1].text.strip()
                        memory = re.findall(r"\d+", memory2)[0]
                        # print(memory)
                    if spans[i].text == "مقدار RAM":
                        ram2 = spans[i+1].text.strip()
                        ram = re.findall(r"\d+", ram2)[0]
                        # print(ram)
                    if spans[i].text == "شبکه های ارتباطی":
                        network2 = spans[i+1].text.strip().replace("\n", "").replace(" ", "").replace(",", "")
                        if "5" in network2:
                            network = 5
                        elif "4" in network2:
                            network = 4
                        elif "3" in network2:
                            network = 3
                        else:
                            network = 2
                        # print(network)
                    if spans[i].text == "نسخه سیستم عامل":
                        android2 = spans[i+1].text.strip()
                        android = re.findall(r"\d+", android2)[0]
                        # print(android)
                values = (title, memory, ram, network, android)
                cursor.execute(query, values)
                cnx.commit()
            except:
                continue