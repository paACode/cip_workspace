from tokenize import String

import requests
from bs4 import BeautifulSoup

from pprint import pprint

url = "https://www.imdb.com/chart/top/"
myheaders = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}



def main():
    print("I am a Demo example  for Movie scraping ")
    response = requests.get("https://httpbin.org/user-agent") #
    print(f"The standard Python Default Agent:{response.text}") # This is normally blocked

    html_page = requests.get(url, headers=myheaders) #With headers pretending that request comes from a real browser

    soup = BeautifulSoup(html_page.content, 'lxml') # lxml is a very fast parser engine from  beautiful soup
    tmp_movies = soup.find_all(class_="ipc-title__text ipc-title__text--reduced")
    movies = list()
    for movie in tmp_movies:
        movies.append(movie.get_text(strip =True))

    pprint(movies)

if __name__ == '__main__':
    main()