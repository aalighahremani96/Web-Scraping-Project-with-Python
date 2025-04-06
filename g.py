import requests


url="https://pub.modares.ac.ir/bookstore.php?slc_lang=fa&sid=1&slct_pg_id=63"
r= requests.get(url)
r.encoding = 'utf-8'
w=r.text


from bs4 import BeautifulSoup

soup=BeautifulSoup(w)
print("******************************************************************************************")
a= soup.select("title")

print(f"title of website is: {a} ")
print("******************************************************************************************")


b=soup.select(".price")
print("prices are shown below from the class of: 'price' ")

for i in b:
    print(i.text)
print("pic links are below**********************************************************************")
images = soup.find_all('img')

if not images:
    print("No pics found")
else:
    for i, img in enumerate(images, 1):
        img_url = img.get('src')
        if img_url: 
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('/'):
                img_url = 'https://pub.modares.ac.ir' + img_url
            elif not img_url.startswith(('http', 'https')):
                img_url = url + '/' + img_url
            
            print(f"{i}. {img_url}")
