from PIL import Image

if __name__ == '__main__':
    db_img = Image.open('deep_blue.jpg')
    # Displays the file in image viewer
    # db_img.show()
    print(db_img.filename)
    print(db_img.size)
    print(db_img.format_description)
    db_img.crop((10,10,100,150)).show()
