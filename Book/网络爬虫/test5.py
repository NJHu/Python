from bs4 import BeautifulSoup
import requests

def main():
    response = requests.get('http://www.baidu.com')
    html_doc = response.content
    soup = BeautifulSoup(html_doc, features='html.parser', from_encoding='utf8')
    print(soup.prettify())


if __name__ == '__main__':
    main()