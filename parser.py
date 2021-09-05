from os import write
import requests
from bs4 import BeautifulSoup
import csv
import re

URL = 'https://prostoprokat.ru/arenda-auto-klass-kommerc/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 YaBrowser/21.6.4.693 Yowser/2.5 Safari/537.36'}
HOST = 'https://prostoprokat.ru'
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
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item-tale')
    
    for item in items:
        curr_link = HOST + item.find('div', class_='img').find_next('a').get('href')
        html2 = get_html(curr_link)
        soup2 = BeautifulSoup(html2.text, 'html.parser')

        first_img = HOST + item.find('div', class_='img').find_next('a').find_next('img').get('src')
        title = item.find('div', class_='description').find_next('a').get_text(strip = True).replace('AT', '')
        spec = item.find('ul', class_='specifications').find_all('li')
        spec1 = spec[0].find('b').get_text()
        spec2 = spec[1].find('b').get_text()
        if(len(spec)>2):
            spec3 = spec[2].find('b').get_text()
        else:
            spec3 = ''
        if(len(spec)>3):
            spec4 = spec[3].find('b').get_text()
        else:
            spec4 = ''
        price = item.find('div', class_='total').get_text(strip = True).replace('Итого: ', '').replace('<span> за 1 сутки</span>', '').replace('₽', '').replace(' ', '').replace('за1сутки', '')
        brand = soup2.find(somefunc).get('content')
        opt = soup2.find_all('div', class_='option')
        opt1 = opt[0].find('div', class_='price').find_next('div', class_='price').get_text()
        opt2 = opt[1].find('div', class_='price').find_next('div', class_='price').get_text()
        opt3 = opt[2].find('div', class_='price').find_next('div', class_='price').get_text()
        opt4 = opt[3].find('div', class_='price').find_next('div', class_='price').get_text()
        opt5 = opt[4].find('div', class_='price').find_next('div', class_='price').get_text()
        opt6 = opt[5].find('div', class_='price').find_next('div', class_='price').get_text()

        text = soup2.find('div', class_='text').get_text()
        text1 = soup2.find('div', class_='text').find_all('h2')
        text2 = soup2.find('div', class_='text').find_all('p')



        complecion = ''
        complecion = soup2.find('div', class_='equipment')
        if complecion:
            complecion = complecion.find('div', class_='title').find_next('ul').find_all('li')
            #print(len(complecion))
            co1 = complecion[0].get_text()
            co2 = complecion[1].get_text()
            co3 = complecion[2].get_text()
            co4 = complecion[3].get_text()
            if len(complecion) > 4:
                co5 = complecion[4].get_text()
            else:
                co5 = ''
            if len(complecion) > 5:
                co6 = complecion[5].get_text()
            else:
                co6 = ''
            if len(complecion) > 6:
                co7 = complecion[6].get_text()
            else:
                co7 = ''
            if len(complecion) > 7:
                co8 = complecion[7].get_text()
            else:
                co8 = ''
            if len(complecion) > 8:
                co9 = complecion[8].get_text()
            else:
                co9 = ''
            if len(complecion) > 9:
                co10 = complecion[9].get_text()
            else:
                co10 = ''
            if len(complecion) > 10:
                co11 = complecion[10].get_text()
            else:
                co11 = ''
            if len(complecion) > 11:
                co12 = complecion[11].get_text()
            else:
                co12 = ''
            if len(complecion) > 12:
                co13 = complecion[12].get_text()
            else:
                co13 = ''
            if len(complecion) > 13:
                co14 = complecion[13].get_text()
            else:
                co14 = ''
            if len(complecion) > 14:
                co15 = complecion[14].get_text()
            else:
                co15 = ''
            if len(complecion) > 15:
                co16 = complecion[15].get_text()
            else:
                co16 = ''
            if len(complecion) > 16:
                co17 = complecion[16].get_text()
            else:
                co17 = ''
            if len(complecion) > 17:
                co18 = complecion[17].get_text()
            else:
                co18 = ''
            if len(complecion) > 18:
                co19 = complecion[18].get_text()
            else:
                co19 = ''
            if len(complecion) > 19:
                co20 = complecion[19].get_text()
            else:
                co20 = ''
            if len(complecion) > 20:
                co21 = complecion[20].get_text()
            else:
                co21 = ''
            if len(complecion) > 21:
                co22 = complecion[21].get_text()
            else:
                co22 = ''
            if len(complecion) > 22:
                co23 = complecion[22].get_text()
            else:
                co23 = ''
            if len(complecion) > 23:
                co24 = complecion[23].get_text()
            else:
                co24 = ''
            if len(complecion) > 24:
                co25 = complecion[24].get_text()
            else:
                co25 = ''
            if len(complecion) > 25:
                co26 = complecion[25].get_text()
            else:
                co26 = ''
            if len(complecion) > 26:
                co27 = complecion[26].get_text()
            else:
                co27 = ''
            if len(complecion) > 27:
                co28 = complecion[27].get_text()
            else:
                co28 = ''
            if len(complecion) > 28:
                co29 = complecion[28].get_text()
            else:
                co29 = ''

        else:
            complecion = ''
            co1 = ''
            co2 = ''
            co3 = ''
            co4 = ''
            co5 = ''
            co6 = ''
            co7 = ''
            co8 = ''
            co9 = ''
            co10 = ''
            co11 = ''
            co12 = ''
            co13 = ''
            co14 = ''
            co15 = ''
            co16 = ''
            co17 = ''
            co18 = ''
            co19 = ''
            co20 = ''
            co21 = ''
            co22 = ''
            co23 = ''
            co24 = ''
            co25 = ''
            co26 = ''
            co27 = ''
            co28 = ''
            co29 = ''

        cars.append({
            'title': title,
            'first_img': first_img,
            'spec1': spec1,
            'spec2': spec2,
            'spec3': spec3,
            'spec4': spec4,
            'price': price,
            'brand': brand,
            'opt1': opt1,
            'opt2': opt2.replace('+ ', '').replace(' ', '').replace('₽', ''),
            'opt3': opt3.replace('+ ', '').replace(' ', '').replace('₽', ''),
            'opt4': opt4.replace('+ ', '').replace(' ', '').replace('₽', ''),
            'opt5': opt5.replace('+ ', '').replace(' ', '').replace('₽', ''),
            'opt6': opt6.replace('+ ', '').replace(' ₽/км', ''),
            'co1': co1,
            'co2': co2,
            'co3': co3,
            'co4': co4,
            'co5': co5,
            'co6': co6,
            'co7': co7,
            'co8': co8,
            'co9': co9,
            'co10': co10,
            'co11': co11,
            'co12': co12,
            'co13': co13,
            'co14': co14,
            'co15': co15,
            'co16': co16,
            'co17': co17,
            'co18': co18,
            'co19': co19,
            'co20': co20,
            'co21': co21,
            'co22': co22,
            'co23': co23,
            'co24': co24,
            'co25': co25,
            'co26': co26,
            'co27': co27,
            'co28': co28,
            'co29': co29,
            'text': text,
        })
        print(cars)
        spec3 = ''
        spec4 = ''

def save_file(items,path):
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        #writer.writerow(['title', 'first img', 'spec1', 'spec2', 'spec3', 'spec4', 'price', 'brand', 'opt1', 'opt2', 'opt3', 'opt4', 'opt5', 'opt6', 'co1', 'co2', 'co3', 'co4', 'co5', 'co6', 'co7', 'co8', 'co9', 'co10', 'co11', 'co12', 'co13', 'co14', 'co15', 'co16', 'co17', 'co18', 'co19', 'co20', 'co21', 'co22', 'co23', 'co24', 'co25', 'co26', 'co27', 'co28', 'co29', 'text', 'brand'])
        for item in items:
            writer.writerow([item['title'], item['first_img'], item['spec1'], item['spec2'], item['spec3'], item['spec4'], item['price'],  item['brand'], item['opt1'], item['opt2'], item['opt3'], item['opt4'], item['opt5'], item['opt6'], item['co1'], item['co2'], item['co3'], item['co4'], item['co5'], item['co6'], item['co7'], item['co8'], item['co9'], item['co10'], item['co11'], item['co12'], item['co13'], item['co14'], item['co15'], item['co16'], item['co17'], item['co18'], item['co19'], item['co20'], item['co21'], item['co22'], item['co23'], item['co24'], item['co25'], item['co26'], item['co27'], item['co28'], item['co29'], item['text'], 'vip'])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        save_file(cars, 'cars.csv')
        print('Success!')
    else:
        print('Error')

parse()