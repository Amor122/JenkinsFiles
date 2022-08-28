import requests
from lxml import etree
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get("https://pic.netbian.com/new/")
html = etree.HTML(response.text)
url_base = 'https://pic.netbian.com'
new_url = html.xpath('//*[@id="main"]/div[3]/ul/li[1]/a/img/@src')[0]
pic_url = url_base + new_url
print(pic_url)
