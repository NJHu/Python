import urllib.request

def main():
    response = urllib.request.urlopen('http://www.baidu.com')
    html = response.read()
    print(html)

if __name__ == '__main__':
    main()