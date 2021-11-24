from os import write
import requests
from bs4 import BeautifulSoup
import csv
import re

URL = 'https://XXXXXXXXX.ru/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5 Safari/537.36'}
HOST = 'https://XXXXXXXXX.ru'
cars = []

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def somefunc(tag):
    if tag.has_attr('itemprop'):
        if tag.get('itemprop') == 'brand':
            return True
        else:
            return False
    else:
        return False

def get_content(html):
        html2 = get_html('https://prostoprokat.ru/arenda/prokat-hyundai-solaris-2/')
        soup2 = BeautifulSoup(html2.text, 'html.parser')
        images = soup2.find_all('img', class_='slider-detail-item-img')
        #print(len(images))
        title = soup2.find('div', class_='order').find('div', class_='name').get_text(strip = True).replace('AT', '')
        print(images[1])
        img1 = HOST + images[0].get('data-lazy')
        img2 = HOST + images[1].get('data-lazy')
        if len(images)>2:
            img3 = HOST + images[2].get('data-lazy')
        else:
            img3 = ''
        if len(images)>3:
            img4 = HOST + images[3].get('data-lazy')
        else:
            img4 = ''
        if len(images)>4:
            img5 = HOST + images[4].get('data-lazy')
        else:
            img5 = ''
        if len(images)>5:
            img6 = HOST + images[5].get('data-lazy')
        else:
            img6 = ''
        if len(images)>6:
            img7 = HOST + images[6].get('data-lazy')
        else:
            img7 = ''
        if len(images)>7:
            img8 = HOST + images[7].get('data-lazy')
        else:
            img8 = ''
        if len(images)>8:
            img9 = HOST + images[8].get('data-lazy')
        else:
            img9 = ''
        if len(images)>9:
            img10 = HOST + images[9].get('data-lazy')
        else:
            img10 = ''
        if len(images)>10:
            img11 = HOST + images[10].get('data-lazy')
        else:
            img11 = ''
        if len(images)>11:
            img12 = HOST + images[11].get('data-lazy')
        else:
            img12 = ''
        if len(images)>12:
            img13 = HOST + images[12].get('data-lazy')
        else:
            img13 = ''
        if len(images)>13:
            img14 = HOST + images[13].get('data-lazy')
        else:
            img14 = ''

        cars.append({
            'title': title,
            'img1': img1,
            'img2': img2,
            'img3': img3,
            'img4': img4,
            'img5': img5,
            'img6': img6,
            'img7': img7,
            'img8': img8,
            'img9': img9,
            'img10': img10,
            'img11': img11,
            'img12': img12,
            'img13': img13,
            'img14': img14,
        })
        print(cars)

def save_file(items,path):
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        #writer.writerow(['title', 'img', 'num' ])
        for item in items:
            writer.writerow([item['title'], item['img1'], 1])
            writer.writerow([item['title'], item['img2'], 2])
            writer.writerow([item['title'], item['img3'], 3])
            if item['img4']:
                writer.writerow([item['title'], item['img4'], 4])
            if item['img5']:
                writer.writerow([item['title'], item['img5'], 5])
            if item['img6']:
                writer.writerow([item['title'], item['img6'], 6])
            if item['img7']:
                writer.writerow([item['title'], item['img7'], 7])
            if item['img8']:
                writer.writerow([item['title'], item['img8'], 8])
            if item['img9']:
                writer.writerow([item['title'], item['img9'], 9])
            if item['img10']:
                writer.writerow([item['title'], item['img10'], 10])
            if item['img11']:
                writer.writerow([item['title'], item['img11'], 11])
            if item['img12']:
                writer.writerow([item['title'], item['img12'], 12])
            if item['img13']:
                writer.writerow([item['title'], item['img13'], 13])
            if item['img14']:
                writer.writerow([item['title'], item['img14'], 14])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        save_file(cars, 'cars.csv')
        print('Success!')
    else:
        print('Error')

parse()
