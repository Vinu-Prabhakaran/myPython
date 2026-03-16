import bs4
import requests

def read_example():
    request = requests.get('https://www.example.com')
    print(type(request))
    print(request.text)

    # Grab Title
    soup = bs4.BeautifulSoup(request.text,'lxml')
    print(soup)
    title_text = soup.select('title')[0].getText()
    print(title_text)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    page = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)',headers=headers)

    soup = bs4.BeautifulSoup(page.text,'lxml')
    # print(soup)
    img_tag = soup.select('.mw-file-element')
    print(img_tag[1]['src']) # Source of image
    image = requests.get(f"https:{img_tag[1]['src']}",headers=headers).content ## Image file binary representation
    print(image)
    with open("deep_blue.jpg",'wb') as f:
        f.write(image)
        f.close()
