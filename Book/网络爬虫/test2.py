import urllib.parse
import urllib.request


def main():
    data = bytes(urllib.parse.urlencode({'word':'hello'}), encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    html = response.read()
    print(html)

if __name__ == '__main__':
    main()
