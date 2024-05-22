import requests
from bs4 import BeautifulSoup

'''
url = 'https://www.jumia.com.tn/catalog/?q=smartphone'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html')

print(soup)

oba = soup.find('div', class_="-paxs row _no-g _4cl-3cm-shs")

print('888888888888888888888888888888888\n',oba)
'''



# soup = BeautifulSoup(scrapped_html, 'html.parser')

# div = soup.find('div')

#print('\n' ,div)

# data = [oba.text.strip() for oba in div ]

#data2 = [for ]



url = 'https://www.jumia.com.tn/catalog/?q=smartphone'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html')

#print(soup)

#zeb = soup.find('h3', class_="name")
div = soup.find('article', class_="prd _fb col c-prd")
for item in div:
        oba = item.find('h3', class_="name")
        #print('888888888888888888888888888888888\n', zeb)

# Find the next 'div' after the current 'div'
div2 = soup.find('button', class_="btn _prim _md -mls -fsh0")

#for element in div2.find_all('h3', class_="name"):
 #       oba = soup.find('h3', class_="name")
  #      print('888888888888888888888888888888888\n', oba)
# Now you can do the same thing with the next 'div'
#for element in next_div.find_all('article'):
 #   oba = soup.find('h3', class_="name")
  #  print('888888888888888888888888888888888\n', oba)



'''for element in div.find_all('article'):
    art = element.find_all(['article'])
    #art = cols = [art.get_text(strip=True) for art in art]
    data.append(art)'''
#print('888',data)
# Open the file in write mode ('w')
'''
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write each pair of words to the file
    for i in range(0, len(data), 2):
        # Group every two words together into a list
        row = data[i:i+2]
        writer.writerow(row)

import pandas as pd

#df = pd.DataFrame(data)
df = pd.read_csv('data.csv', encoding='ISO-8859-1')



print(df)
'''
import pandas as pd
import threading


brands = []
price = []

def scrape_page(page):
    print('Scraping page:', page)
    url = 'https://www.jumia.com.tn/mlp-telephone-tablette/smartphones/?page=' + str(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    div = soup.find_all('article', {'class': 'prd _fb col c-prd'})
    for item in div:
        oba = item.find('h3', class_="name")
        if oba is not None:
            brand = oba.text.split()[0]
            brands.append(brand)
        
        oba1 = item.find('div', class_="prc")
        if oba1 is not None:
            prix = oba1.text
            price.append(prix)
        print(brand, prix)

num_threads = 5

threads = []
for page in range(1, 16):
    thread = threading.Thread(target=scrape_page, args=(page,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Scraping complete.")

df1 = pd.DataFrame(brands, columns=['Brand'])


df5 = pd.DataFrame(price, columns=['Price'])
df = pd.concat([df1, df5], axis=1)
df.to_csv('scrap/data.csv', index=False)


#df1.to_csv('scrap/data1.csv', index=False)




