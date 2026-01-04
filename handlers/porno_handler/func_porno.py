import csv

import json

from datetime import datetime

import requests

from bs4 import BeautifulSoup


class UserGetVideo:
    d: dict = {}
    lst: list = []

    @classmethod
    def get_content_count(cls, name_v: str, content: list):
        '''Метод для записи категории видео в словарь'''
        cls.lst.append(name_v)
        cls.d[name_v] = {'count': 0, 'content': content}

    @classmethod
    def set_count(cls, name_v: str, znak: str):
        '''Метод для пролистывания видео'''
        if znak == '+':
            cls.d[name_v]['count'] += 1
        else:
            cls.d[name_v]['count'] -= 1


def get_set_video(znak: str) -> tuple:
    '''Функция для получения контента'''
    for date in UserGetVideo.lst:
        if UserGetVideo.d.get(date):
            UserGetVideo.set_count(date, znak)
            content = UserGetVideo.d[date]['content']
            count = UserGetVideo.d[date]['count']
    photo = content[count][0]
    text = content[count][1]
    url = content[count][2]
    return photo, text, url


def get_video(name):
    '''Функция для получения списка видео из файла'''
    lst = []
    with open(fr'D:\script\remaster_bot\porno_files\{name}.csv') as f:
        file = csv.reader(f, delimiter=',')
        for lst_video in file:
            lst.append(lst_video)
    return lst


def get_content(bs):
    '''Функция для парсера видео из сайта'''
    lst = []
    video_content = bs.find('div', {'id': 'video-content'}).find('ul', class_='videos_ul')

    for content in video_content.find_all('li', class_='video_block trailer'):
        image = content.find('div', class_='tumba').find('img').get('src')
        text = content.find('div', class_='tumba').find('img').get('alt')
        url_porn = content.find('a', class_='image').get('href')
        lst.append([image, text, url_porn])

    return lst


def get_file(contents, name):
    '''Функция для записи видео в файл'''
    with open(fr'D:\script\remaster_bot\porno_files\{name}.csv', 'w', newline='') as f:
        w = csv.writer(f, delimiter=',')
        for content in contents:
            w.writerow(content)


def get_url(user_url):
    '''Функция для поиска категории'''
    head = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://x.porno365.directory/' + user_url
    req = requests.get(url, headers=head)
    bs = BeautifulSoup(req.text, 'lxml')
    if user_url == '':
        user_url = 'classic'
    get_file(get_content(bs), user_url)


def proverka_date():
    '''Фунция для проверки даты для обновления видео'''
    now_date: datetime = datetime.now()
    now_date_month = now_date.month
    now_date_day = now_date.day

    with open(fr'D:\script\remaster_bot\porno_files\date.txt', 'r') as f:
        f = json.load(f)
        date = f['date']
        month = int(date[0])
        day = int(date[1])

    if (month * day) > now_date_month * now_date_day:
        with open(fr'D:\script\remaster_bot\porno_files\date.txt', 'w') as new_f:
            json.dump({'date': (now_date_month, now_date_day)}, new_f)
        return True
    
    return False