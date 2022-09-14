from urllib.request import Request, urlopen


def search(what):
    request = Request(
        url='https://mvnrepository.com/search?q=' + what,
        headers={'User-Agent': 'Mozilla/5.0',
                 'Accept': 'text/html',
                 'Accept-Charset': 'utf-8',
                 'Connection': 'keep-alive'}
    )
    url = urlopen(request)
    content = url.read().decode('utf-8')
    url.close()
    return content
