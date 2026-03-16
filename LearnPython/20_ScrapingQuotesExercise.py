import bs4
import requests

# Let's scrap https://quotes.toscrape.com
# all pages
if __name__ == '__main__':
    quotes_url_fmt = 'https://quotes.toscrape.com/page/{}/'
    page_1 = quotes_url_fmt.format(1)
    request = requests.get(page_1)
    soup = bs4.BeautifulSoup(request.text,'lxml')
    # print(soup.select('.quote')[0])
    # print(soup.select('.quote')[0].select('.author')[0])
    # print(soup.select('.quote')[0].select('.author')[0].getText())

    # **TASK: Get the names of all the authors on the first page.**
    author_names = set()
    quotes = soup.select('.quote')
    # for quote in quotes:
    authors = soup.select('.author')
    for author in authors:
        author_names.add(author.getText())
    print(f'Author Names : {author_names}')
    print('*' * 30)
    # TASK: Create a list of all the quotes on the first page.
    quotes_list = list()
    # for quote in quotes:
    texts = soup.select('.text')
    for text in texts:
        quotes_list.append(text.getText())
    print(f'Quotes from page 1 : {quotes_list}')
    print('*' * 30)
    # print(soup.select('.quote')[0].select('span')[0].getText())

    # TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from
    # the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
    # HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in
    # the top right tags, perhaps check the span.
    # print(soup.select('.col-md-4.tags-box')[0].select('.tag-item')[0].select('a')[0].getText())
    # tags = soup.select('.col-md-4.tags-box')
    # for tag in tags:
    tag_items = soup.select('.tag-item')
    for tag_item in tag_items:
        print(tag_item.select('a')[0].getText())
