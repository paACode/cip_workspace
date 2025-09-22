#!/usr/bin/env python3
"""\
scrape finance data of google stock from yahoo.com.
In the 'tr'-tags of the table, find all values of the 'span' - tag.

authors:    Ramón Christen, Andreas Melillo
date:       24.09.2024
"""

import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"
myheaders = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"}

html_page = requests.get(url, headers = myheaders)
soup = BeautifulSoup(html_page.content, 'lxml')

# extract information by tag and class attributes
stock_title_text = soup.find('h1', class_='yf-4vbjci').string
print("Stocktitle:     ", stock_title_text)

#current_price = soup.find("fin-streamer", class_="livePrice yf-1tejb6").string
current_price = soup.find("span", class_="yf-ipw1h0", attrs={"data-testid":"qsp-price"}).string
print("Current price:  ", current_price)

# Extract information with xpath:
from lxml import etree
dom = etree.HTML(str(soup))
#price_time_stp = dom.xpath('/html/body/div[2]/main/section/section/section/article/section[1]/div[2]/div[1]/section/div/section[1]/div[2]/span/text()')
price_time_stp = dom.xpath('/html/body/div[2]/main/section/section/section/section/section[1]/div[2]/div[1]/section/div/section/div[2]/span/span')
print(price_time_stp[0].text)

# get all quote statistics
quote_stat = soup.find("div", attrs={'data-testid': 'quote-statistics'})

# extract all statistic list elements
all_stat = quote_stat.find_all("li")

# extract all statistic values and merge in dictionary list
print(60*'-')
print(*["{:<30}{:>30}".format(*s.stripped_strings) for s in all_stat], sep='\n')
print(60*'-')

