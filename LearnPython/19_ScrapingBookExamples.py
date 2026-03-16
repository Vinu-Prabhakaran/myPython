import bs4
import requests

# Let's scrap https://books.toscrape.com/ to find all books with two star ratings across
# all pages
if __name__ == '__main__':
    book_url_fmt = 'https://books.toscrape.com/catalogue/page-{}.html'
    # request = requests.get(book_url_fmt.format(1))
    # soup = bs4.BeautifulSoup(request.text,'lxml')
    # print(soup)
    # print(soup.select('.product_pod')[0])
    # book = soup.select('.product_pod')[0]
    # print(soup.select('.product_pod')[0].select('a')[1]['title'])
    for i in range (1,51):
        request = requests.get(book_url_fmt.format(i))
        page = bs4.BeautifulSoup(request.text,'lxml')
        print(f'Page {i}')
        for book in page.select('.product_pod'):
            if book.select('.star-rating.Two'):
                print(book.select('a')[1]['title'])
