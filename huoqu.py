import requests
from bs4 import BeautifulSoup
import html5lib

def save(path,data,encoding):
    with open(path,"w",encoding=encoding) as fp:
        fp.write(data)


url = "https://bj.ke.com/ershoufang/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}


for i in range(1,10):
    url = "https://bj.ke.com/ershoufang/pg{}/".format(i)
    print(url)
    response = requests.get(url=url,headers=headers)
    bs = BeautifulSoup(response.content, "html5lib")
    content = bs.select("#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul > li> div")
    for tag in content:
        title = tag.select("div.title > a")
        position =tag.select("div.address > div.flood > div")
        houseInfo = tag.select("div.address > div.houseInfo")
        followInfo = tag.select(" div.address > div.followInfo")
        totalPrice = tag.select(" div.address > div.priceInfo > div.totalPrice > span")
        unitPrice = tag.select("div.address > div.priceInfo > div.unitPrice > span")

        title = "\n".join([tag.text.strip() for tag in title]).replace("\n", "")
        position = "\n".join([tag.text.strip() for tag in position]).replace(" ","").replace("\n","")
        houseInfo = "\n".join([tag.text.strip() for tag in houseInfo]).replace(" ","").replace("\n","")
        followInfo = "\n".join([tag.text.strip() for tag in followInfo]).replace(" ","").replace("\n","")
        totalPrice = "\n".join([tag.text.strip() for tag in totalPrice])
        unitPrice = "\n".join([tag.text.strip() for tag in unitPrice])
        print(title)
        print(position)
        print(houseInfo)
        print(followInfo)
        print(totalPrice)
        print(unitPrice,"\n")

    content = [tag.text.strip() for tag in content]
    text = "\n".join(content)
    path = "resource/duanzi{}.txt".format(i)
    save(path, text, "utf-8")


# response = requests.get(url=url,headers=headers)

# save("resource/qiubai.html",response.content.decode("utf-8"),"utf-8")

#解析

# print(bs)
#选中content

# for tag in content:
#     title = tag.select("div.title > a")
#     position =tag.select("div.address > div.flood > div")
#     houseInfo = tag.select("div.address > div.houseInfo")
#     followInfo = tag.select(" div.address > div.followInfo")
#     totalPrice = tag.select(" div.address > div.priceInfo > div.totalPrice > span")
#     unitPrice = tag.select("div.address > div.priceInfo > div.unitPrice > span")
#
#     title = "\n".join([tag.text.strip() for tag in title]).replace("\n", "")
#     position = "\n".join([tag.text.strip() for tag in position]).replace(" ","").replace("\n","")
#     houseInfo = "\n".join([tag.text.strip() for tag in houseInfo]).replace(" ","").replace("\n","")
#     followInfo = "\n".join([tag.text.strip() for tag in followInfo]).replace(" ","").replace("\n","")
#     totalPrice = "\n".join([tag.text.strip() for tag in totalPrice])
#     unitPrice = "\n".join([tag.text.strip() for tag in unitPrice])
#     print(title)
#     print(position)
#     print(houseInfo)
#     print(followInfo)
#     print(totalPrice)
#     print(unitPrice,"\n")
