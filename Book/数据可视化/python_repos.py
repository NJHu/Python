import requests

# https://api.github.com/search/repositories?q=language:python&sort=starts


def main():
    url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
    response = requests.get(url)
    # print(response)
    response_dict = response.json()
    print(response_dict.keys())

if __name__ == '__main__':
    main()
    