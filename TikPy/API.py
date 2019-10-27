from newspaper import Article
from bs4 import BeautifulSoup
import requests
import json
import os
import time

def get_jsoned(url):
    """

    :param url:
    :return: json file containing the matadata
    """
    art = Article(url)
    art.download()
    art.parse()
    soup = BeautifulSoup(art.html)
    for div in soup.findAll('script'):
        if "window.__INIT_PROPS__" in div.text:
            text = div.text[24:]
            text = text.replace('\n', '')
            return json.loads(text)

def get_user_info(name, from_video):
    """
    :param name of user:
    :return: user Data  
    """
    jsoned = ''
    if from_video:
        start_index = name.find('/video/')
        print(name[:start_index])
        jsoned = get_jsoned(name[:start_index])
    else:
        jsoned = get_jsoned(name)
    try:
        return jsoned['/@:uniqueId']['userData']
    except Exception as E:
        return {}


def get_user_videos(name):
    url = 'https://www.tiktok.com/@' + name
    jsoned = get_jsoned(url)
    return jsoned['/@:uniqueId']['itemList']


def get_trending_hashtags():
    url = 'https://www.tiktok.com/trending'
    jsoned = get_jsoned(url)
    return jsoned['/trending']['challengeList']


def get_trending_posts():
    url = 'https://www.tiktok.com/trending'
    jsoned = get_jsoned(url)
    return jsoned['/trending']['itemList']


def get_video_info(url):
    jsoned = get_jsoned(url)
    try:
        temp = jsoned['/@:uniqueId/video/:id']['videoData']
        temp['url'] = url
        return temp
    except Exception as identifier:
        print(identifier)
        return {}


def get_hash_recommend_list(name):
    url = 'https://www.tiktok.com/tag/' + name
    jsoned = get_jsoned(url)
    return jsoned['/tag/:name']['recommendList']


def get_hash_videos(name):
    url = 'https://www.tiktok.com/tag/' + name
    jsoned = get_jsoned(url)
    return jsoned['/tag/:name']['itemList']


def get_videos_from_music(music_id, name):
    url = 'https://www.tiktok.com/music/'+name.replace(' ', '-') + music_id
    jsoned = get_jsoned(url)
    return jsoned['/music/*-:id']['itemList']


def get_music_recommend_list(music_id, name):
    url = 'https://www.tiktok.com/music' + name.replace(' ', '-') + music_id
    jsoned = get_jsoned(url)
    return jsoned['/music/*-:id']['recommendList']


def download_video(url, post_name=None):
    r = requests.get(url, stream=True)
    if post_name:
        with open(post_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                else:
                    return None
    else:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                return chunk
            else:
                return None


