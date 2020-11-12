import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_all_links(html):
    # print(html)
    links = []
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    tds = soup.find('table', class_='table').find_all('td')
    
    for td in range(1,len(tds), 3):
        a = tds[td].find('a').get('href')
        
        link='http://kenesh.kg'+ a
        links.append(link)
        print(link)

    
     

def main():
    url = "http://www.kenesh.kg/ru/deputy/list/35"
    a = get_all_links(get_html(url))
    all_links = a


if __name__ == "__main__":
    main()