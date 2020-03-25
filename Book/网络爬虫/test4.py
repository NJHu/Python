import requests


def main():
    response = requests.get('http://www.baidu.com')
    #print(response.status_code)
    #print(response.url)
    #print(response.headers)
    #print(response.cookies)
    #print(response.text)
    print(response.content)

if __name__ == '__main__':
    main()