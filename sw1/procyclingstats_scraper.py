from tokenize import String

import requests
import pandas as pd
from bs4 import BeautifulSoup

from pprint import pprint

url = "https://www.procyclingstats.com/rankings.php"
myheaders = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}



def main():
    html_page = requests.get(url, headers=myheaders) #With headers pretending that request comes from a real browser
    soup = BeautifulSoup(html_page.content, 'lxml') # lxml is a very fast parser engine from  beautiful soup
    table  = soup.find("table", class_ = "basic")

    # 4. Extract headers
    headers = [th.get_text(strip=True) for th in table.find_all("th")]

    # 5. Extract rows
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all("td")]
        rows.append(cells)

    # 6. Create DataFrame
    df = pd.DataFrame(rows, columns=headers)
    print(df)

if __name__ == '__main__':
    main()