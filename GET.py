from urllib import request, parse


def get_request(url):
    data = [line.strip() for line in request.urlopen(url, data=b'GET').read().decode().split('\n')]
    return data


if __name__ ==