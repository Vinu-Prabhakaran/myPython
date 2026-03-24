import csv
import re

import pypdf
import requests

# PDFs and Spreadsheets Puzzle Exercise
# Let's test your skills, the files needed for this puzzle exercise
#
# You will need to work with two files for this exercise and solve the following tasks:
#
# Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal
# from top left to bottom right).
# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case
# you can't download from Google Drive) and find the phone number that is in the document.
# Note: There are different ways of formatting a phone number!
if __name__ == '__main__':
    csv_file = open('ExerciseFiles/find_the_link.csv','r',encoding='utf-8')
    csv_data = csv.reader(csv_file)
    csv_lines = list(csv_data)

    print(f'No:of rows in csv : {len(csv_lines)}')
    print(f'No:of columns in csv : {len(csv_lines[0])}')

    # Reading csv to reveal the url - Alternate solution is to use enumerate(csv_lines)
    url=''
    codes = []
    for r in range(0,len(csv_lines)):
        for c in range(0,len(csv_lines[r])):
            if r == c:
                codes.append(csv_lines[r][c])
    # print(codes)
    url = "".join(codes)
    print(f'url is {url}')

    #Download file
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers) ## Image file binary representation
    print(response.headers.get('Content-Type'))
    pdf_data = response.content
    # print(pdf_data)
    #Saving downloaded file
    # with open("ExerciseFiles/downloaded_pdf.pdf",'wb') as f:
    #     f.write(pdf_data)
    #     f.close()

    # Reading provided file since download failed
    pdf_file = open('ExerciseFiles/Find_the_Phone_Number.pdf','rb')
    pdf_reader = pypdf.PdfReader(pdf_file)
    num_pages = pdf_reader.get_num_pages()
    print(f'No:of pages in pdf : {num_pages}')

    for page_no in range (0,num_pages):
        text = pdf_reader.get_page(page_no).extract_text()
        # print(f'Page {page_no} contents : {text}')
        phone_pattern = re.compile(r'(\d{3}).(\d{3}).(\d{4})')
        phone_match_result = re.search(phone_pattern,text)

        if phone_match_result:
            print(f'Phone number {phone_match_result.group()} found on page {page_no+1}')

