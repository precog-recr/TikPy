#%%
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
    return soup

#%%
for i in range(1000):
    get_jsoned('https://tubehi.com/babyariel/tiktok-profile/209793')