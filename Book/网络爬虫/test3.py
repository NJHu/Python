import urllib3

def main():
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://www.baidu.com')
    print(response.data)

if __name__ == '__main__':
    main()