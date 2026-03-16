import bs4
import requests

# Let's scrap https://quotes.toscrape.com
# all pages
if __name__ == '__main__':
    quotes_url_fmt = 'https://quotes.toscrape.com/page/{}/'
    n = 1
    page_n = quotes_url_fmt.format(n)
    request = requests.get(page_n)
    soup = bs4.BeautifulSoup(request.text,'lxml')
    # print(soup.select('.quote'))
    while soup.select('.quote'):
        author_names = set()
        quotes = soup.select('.quote')
        for quote in quotes:
            authors = quote.select('.author')
            for author in authors:
                author_names.add(author.text)
        print(f'Author Names from Page {n} : {author_names}')
        n += 1
        page_n = quotes_url_fmt.format(n)
        request = requests.get(page_n)
        soup = bs4.BeautifulSoup(request.text,'lxml')
